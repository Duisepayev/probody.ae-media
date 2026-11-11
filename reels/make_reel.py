#!/usr/bin/env python3
"""Build a 9:16 Reel (1080x1920 MP4, silent audio track) from 4:5 carousel slides.
Usage: make_reel.py OUT.mp4 "Hook text on top" slide1.jpg slide2.jpg ..."""
import subprocess, sys, tempfile, os, textwrap
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
out, hook, slides = sys.argv[1], sys.argv[2], sys.argv[3:]
FONT = ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf', 58)
D, X = 3.2, 0.5  # seconds per slide, crossfade
tmp = tempfile.mkdtemp()
frames = []
for i, s in enumerate(slides):
    im = Image.open(s).convert('RGB').resize((1080, 1350))
    bg = im.resize((1536, 1920)).crop((228, 0, 1308, 1920)).filter(ImageFilter.GaussianBlur(45))
    bg = ImageEnhance.Brightness(bg).enhance(0.45)
    bg.paste(im, (0, 300))
    d = ImageDraw.Draw(bg)
    lines = textwrap.wrap(hook, 30)[:2]
    y = 150 - len(lines) * 36
    for ln in lines:
        w = d.textlength(ln, font=FONT)
        d.text(((1080 - w) / 2, y), ln, font=FONT, fill=(255, 255, 255))
        y += 74
    f = os.path.join(tmp, f'{i:02d}.png'); bg.save(f); frames.append(f)
durs = [D + (1.0 if i == 0 else 0) + (1.5 if i == len(frames) - 1 else 0) for i in range(len(frames))]
inp, fil = [], []
for i, f in enumerate(frames):
    inp += ['-loop', '1', '-t', f'{durs[i]}', '-i', f]
    fil.append(f'[{i}:v]fps=30,format=yuv420p,setsar=1[v{i}]')
prev, off = 'v0', 0.0
for i in range(1, len(frames)):
    off += durs[i - 1] - X
    fil.append(f'[{prev}][v{i}]xfade=transition=slideleft:duration={X}:offset={off:.2f}[x{i}]')
    prev = f'x{i}'
total = sum(durs) - X * (len(frames) - 1)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inp,
    '-f', 'lavfi', '-t', f'{total:.2f}', '-i', 'anullsrc=r=44100:cl=stereo',
    '-filter_complex', ';'.join(fil), '-map', f'[{prev}]', '-map', f'{len(frames)}:a',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', out], check=True)
print(out, f'{total:.1f}s')
