// Render carousel slides (1080x1350 JPEG) from a JSON spec.
// usage: node render.js spec.json outDir
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FONTS = path.resolve(__dirname, '../fonts');
const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const outDir = path.resolve(process.argv[3]);
fs.mkdirSync(outDir, { recursive: true });

const img = (p) => 'data:image/' + (p.endsWith('.png') ? 'png' : 'jpeg') + ';base64,' + fs.readFileSync(path.resolve(path.dirname(process.argv[2]), p)).toString('base64');

const css = `
@font-face{font-family:MA;src:url(file://${FONTS}/MontserratAlternates-Bold.ttf);font-weight:700}
@font-face{font-family:MA;src:url(file://${FONTS}/MontserratAlternates-ExtraBold.ttf);font-weight:800}
@font-face{font-family:MA;src:url(file://${FONTS}/MontserratAlternates-SemiBold.ttf);font-weight:600}
@font-face{font-family:MA;src:url(file://${FONTS}/MontserratAlternates-Medium.ttf);font-weight:500}
@font-face{font-family:M;src:url(file://${FONTS}/Montserrat.ttf);font-weight:100 900}
*{margin:0;padding:0;box-sizing:border-box}
:root{--y:#FFC83A;--ink:#0C0C0E;--soft:#9A9AA2}
body{width:1080px;height:1350px;overflow:hidden;font-family:M;color:#fff;background:var(--ink)}
.s{position:relative;width:1080px;height:1350px;overflow:hidden}
.grain{position:absolute;inset:0;opacity:.07;pointer-events:none;mix-blend-mode:overlay;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.top{position:absolute;top:64px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;z-index:5}
.cover .top{text-shadow:0 2px 12px rgba(0,0,0,.6)}.cover .count{color:#fff}
.logo{font-family:MA;font-weight:800;font-size:30px;letter-spacing:.5px}
.logo i{font-style:normal;color:var(--y)}
.count{font-family:MA;font-weight:600;font-size:24px;color:var(--soft);letter-spacing:2px}
.tag{display:inline-block;font-family:MA;font-weight:700;font-size:22px;letter-spacing:3px;text-transform:uppercase;color:var(--ink);background:var(--y);padding:12px 22px;border-radius:999px}
em{font-style:normal;color:var(--y)}
.bar{position:absolute;left:80px;right:80px;bottom:64px;display:flex;gap:10px;z-index:5}
.bar span{flex:1;height:5px;border-radius:5px;background:rgba(255,255,255,.18)}
.bar span.on{background:var(--y)}
/* cover */
.cover .ph{position:absolute;inset:0;background-size:cover;background-position:center}
.cover .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,12,14,.55) 0%,rgba(12,12,14,0) 22%,rgba(12,12,14,0) 38%,rgba(12,12,14,.88) 66%,rgba(12,12,14,.98) 100%)}
.cover .txt{position:absolute;left:80px;right:80px;bottom:150px;z-index:4}
.cover h1{font-family:MA;font-weight:800;font-size:96px;line-height:1.02;letter-spacing:-2px;margin:30px 0 26px}
.cover p{font-size:34px;font-weight:500;line-height:1.35;color:#E6E6EA}
.swipe{position:absolute;right:80px;bottom:98px;z-index:5;font-family:MA;font-weight:700;font-size:24px;color:var(--y);letter-spacing:2px}
/* text */
.text{background:radial-gradient(900px 700px at 100% 0%,rgba(255,200,58,.13),transparent 60%),radial-gradient(700px 600px at 0% 100%,rgba(255,255,255,.05),transparent 60%),var(--ink)}
.text .num{position:absolute;right:40px;bottom:70px;font-family:MA;font-weight:800;font-size:420px;line-height:1;color:transparent;-webkit-text-stroke:2px rgba(255,200,58,.14)}
.body{position:absolute;left:80px;right:80px;top:150px;bottom:150px;z-index:4;display:flex;flex-direction:column;justify-content:center}
.kicker{font-family:MA;font-weight:700;font-size:28px;letter-spacing:3px;text-transform:uppercase;color:var(--y);margin-bottom:28px}
.body h2{font-family:MA;font-weight:800;font-size:80px;line-height:1.06;letter-spacing:-1.5px;margin-bottom:40px}
.body p{font-size:40px;line-height:1.45;color:#D4D4DA;font-weight:450;margin-bottom:26px}
.body p b{color:#fff;font-weight:700}
ul.l{list-style:none;margin-top:10px}
ul.l li{position:relative;font-size:41px;line-height:1.3;font-weight:600;color:#EDEDF0;padding:30px 0 30px 84px;border-top:1px solid rgba(255,255,255,.1)}
ul.l li:last-child{border-bottom:1px solid rgba(255,255,255,.1)}
ul.l li:before{content:attr(data-i);position:absolute;left:0;top:30px;width:56px;height:56px;border-radius:14px;background:rgba(255,200,58,.14);color:var(--y);font-family:MA;font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center}
ul.l li small{display:block;font-size:31px;color:var(--soft);font-weight:450;margin-top:6px}
.chips{display:flex;flex-wrap:wrap;gap:14px;margin-top:18px}
.chips span{font-family:MA;font-weight:600;font-size:26px;padding:14px 24px;border-radius:999px;border:2px solid rgba(255,200,58,.5);color:var(--y)}
.note{position:absolute;left:80px;right:80px;bottom:110px;font-size:30px;font-weight:600;color:var(--y);line-height:1.4}
/* split photo */
.split .ph{position:absolute;left:0;right:0;top:0;height:640px;background-size:cover;background-position:center 30%}
.split .ph:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,12,14,.35) 0%,rgba(12,12,14,0) 30%,rgba(12,12,14,0) 60%,var(--ink) 100%)}
.split .body{top:600px;bottom:130px;justify-content:flex-start}
.split .body h2{font-size:70px;margin-bottom:28px}
/* cta */
.cta{background:var(--y);color:var(--ink)}
.cta .logo i{color:var(--ink)}
.cta .count{color:rgba(12,12,14,.5)}
.cta .body{top:140px;bottom:200px}
.cta .kicker{color:var(--ink);opacity:.6}
.cta h2{font-size:86px;color:var(--ink)}
.cta p{color:#2A2A2E;font-size:38px}
.card{margin-top:46px;background:var(--ink);border-radius:36px;padding:34px;color:#fff;box-shadow:0 30px 60px rgba(0,0,0,.18)}
.search{display:flex;align-items:center;gap:20px;background:#1C1C20;border-radius:22px;padding:26px 28px;font-size:32px;font-weight:600}
.search .dot{width:22px;height:22px;border-radius:50%;border:4px solid var(--y)}
.search .sep{color:#55555C}
.pills{display:flex;gap:12px;margin-top:22px;flex-wrap:wrap}
.pills span{font-size:24px;font-weight:600;padding:12px 20px;border-radius:999px;background:#1C1C20;color:#C9C9CF}
.pills span.v{color:var(--ink);background:var(--y)}
.btn{margin-top:22px;text-align:center;font-family:MA;font-weight:800;font-size:32px;background:var(--y);color:var(--ink);border-radius:20px;padding:26px}
.foot{position:absolute;left:80px;right:80px;bottom:110px;display:flex;justify-content:space-between;align-items:flex-end;font-family:MA;font-weight:700;font-size:28px}
.foot .share{font-family:M;font-weight:600;font-size:26px;opacity:.7;text-align:right;max-width:520px;line-height:1.35}
.cta .bar span{background:rgba(12,12,14,.18)}
.cta .bar span.on{background:var(--ink)}
`;

function chrome(i, n, light) {
  const bars = Array.from({ length: n }, (_, k) => `<span class="${k <= i ? 'on' : ''}"></span>`).join('');
  return `<div class="top"><div class="logo">PRO<i>-</i>BODY<i>.</i>AE</div><div class="count">${String(i + 1).padStart(2, '0')} / ${String(n).padStart(2, '0')}</div></div><div class="bar">${bars}</div><div class="grain"></div>`;
}
const list = (items) => `<ul class="l">${items.map((t, k) => {
  const [a, b] = Array.isArray(t) ? t : [t];
  return `<li data-i="${k + 1}">${a}${b ? `<small>${b}</small>` : ''}</li>`;
}).join('')}</ul>`;

function slide(s, i, n) {
  const c = chrome(i, n);
  if (s.type === 'cover') return `<div class="s cover"><div class="ph" style="background-image:url(${img(s.photo)});background-position:${s.pos || 'center'}"></div><div class="shade"></div>${c}
    <div class="txt"><span class="tag">${s.tag}</span><h1>${s.title}</h1><p>${s.sub}</p></div><div class="swipe">SWIPE →</div></div>`;
  if (s.type === 'cta') return `<div class="s cta">${c}<div class="body"><div class="kicker">${s.kicker || 'Your next step'}</div><h2>${s.title}</h2><p>${s.text}</p>
    <div class="card"><div class="search"><div class="dot"></div>${s.search[0]}<span class="sep">·</span>${s.search[1]}</div>
    <div class="pills"><span class="v">✓ Verified</span><span>Map</span><span>Price</span><span>Area</span><span>Direct contact</span></div>
    <div class="btn">pro-body.ae</div></div></div>
    <div class="foot"><div>Link in bio ↗</div><div class="share">${s.share}</div></div></div>`;
  const cls = s.photo ? 'split' : 'text';
  return `<div class="s ${cls}">${s.photo ? `<div class="ph" style="background-image:url(${img(s.photo)});background-position:${s.pos || 'center 30%'}"></div>` : `<div class="num">${String(i + 1).padStart(2, '0')}</div>`}${c}
    <div class="body">${s.kicker ? `<div class="kicker">${s.kicker}</div>` : ''}<h2>${s.title}</h2>${(s.text || []).map((p) => `<p>${p}</p>`).join('')}${s.list ? list(s.list) : ''}${s.chips ? `<div class="chips">${s.chips.map((x) => `<span>${x}</span>`).join('')}</div>` : ''}</div>
    ${s.note ? `<div class="note">${s.note}</div>` : ''}</div>`;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const n = spec.slides.length;
  for (let i = 0; i < n; i++) {
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${slide(spec.slides[i], i, n)}</body></html>`;
    const f = path.join(outDir, `${spec.id}-${String(i + 1).padStart(2, '0')}.html`);
    fs.writeFileSync(f, html);
    await page.goto('file://' + f);
    await page.evaluate(() => document.fonts.ready);
    const ov = await page.evaluate(() => { const b = document.querySelector('.body,.txt'); if (!b) return 0; let m = 0; b.querySelectorAll('*').forEach(e => { m = Math.max(m, e.getBoundingClientRect().bottom); }); const t = document.querySelector('.top').getBoundingClientRect().bottom; const f = b.getBoundingClientRect().top; return (m > 1245 || f < t) ? Math.round(m) : 0; });
    if (ov) console.log('OVERFLOW', spec.id, i + 1, ov);
    await page.screenshot({ path: f.replace('.html', '.jpg'), type: 'jpeg', quality: 90 });
    fs.unlinkSync(f);
  }
  await browser.close();
})();
