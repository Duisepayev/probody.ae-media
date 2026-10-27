# All 30 carousels: slides + captions. Generates specs/cNN.json
import json, os
S = os.path.dirname(os.path.abspath(__file__))
TAGS = "#DubaiMassage #MassageDubai #DubaiLife #MensWellness #ProbodyAE"
SPORT_TAGS = "#SportsMassageDubai #DubaiFitness #DubaiGym #MassageDubai #ProbodyAE"
CTA_TEXT = "Search by map across Dubai, filter by area and price, check verified profiles and message the therapist directly. Free for guests."

C = []
def add(slug, cover, s2, s3, s4, s5, s6, cta, caption, tags=TAGS):
    C.append(dict(slug=slug, cover=cover, slides=[s2, s3, s4, s5, s6], cta=cta, caption=caption, tags=tags))

def L(kicker, title, items, note=None):
    d = {"type": "text", "kicker": kicker, "title": title, "list": items}
    if note: d["note"] = note
    return d
def T(kicker, title, text, chips=None):
    d = {"type": "text", "kicker": kicker, "title": title, "text": text}
    if chips: d["chips"] = chips
    return d
def P(photo, kicker, title, text, chips=None):
    d = T(kicker, title, text, chips); d["photo"] = "../photos/" + photo + ".png"; return d
def CV(photo, tag, title, sub, pos="center 30%"):
    return {"type": "cover", "photo": "../photos/" + photo + ".png", "pos": pos, "tag": tag, "title": title, "sub": sub}
def CTA(title, search, share):
    return {"type": "cta", "title": title, "text": CTA_TEXT, "search": search, "share": share}

# 01
add("desk-neck",
 CV("desk-neck", "Desk life in Dubai", "Your neck is <em>paying</em> for your career", "Why it's stiff by 6 pm, and what actually helps."),
 L("Sound familiar?", "The office guy's checklist", ["Neck locks up when you check the blind spot", "Shoulders creep up to your ears by lunch", "Dull headache after back-to-back calls", "You wake up already tight"], "Two or more? Keep swiping."),
 T("What's going on", "Your head is heavy. Your neck holds it all day.", ["Every time you lean toward the screen, the muscles at the back of your neck and upper shoulders work harder.", "<b>Hours of that, every day,</b> and they stay tight even after you close the laptop."]),
 L("Quick fixes", "3 things to do at your desk today", [["Raise your screen to eye level", "A laptop stand or a stack of books works"], ["Shoulder rolls every hour", "Up, back, down. Five slow reps"], ["Chin tucks", "Pull your chin straight back, hold 5 sec, repeat 10x"]]),
 P("p-shoulders", "When stretching isn't enough", "Let a pro reach what you can't", ["If the tension keeps coming back, a massage therapist works on the deep neck, upper back and between the shoulder blades."], ["Deep tissue", "Classic", "Sports"]),
 L("Book it right", "Get the most out of your session", [["Start with 60 minutes", "Enough time for neck, shoulders and back"], ["Say where it hurts", "And how firm you like the pressure"], ["Go after work", "Not right before a big meeting"]]),
 CTA("Find a massage near your office", ["Deep tissue", "Business Bay"], "Send this to a colleague who needs it"),
 "Stiff neck by 6 pm is not a personality trait. It's hours of leaning toward a screen.\n\nSwipe for 3 desk fixes you can start today, and what to do when stretching isn't enough. Save it for tomorrow morning.")

# 02
add("leg-day",
 CV("cov-gym", "Gym & recovery", "You train hard. Do you <em>recover</em> hard?", "Still sore three days after leg day? Read this."),
 T("First, the good news", "Soreness after training is normal", ["That heavy, stiff feeling a day or two after a hard session has a name: <b>DOMS</b>, delayed onset muscle soreness.", "It's part of training. Walking like a robot all week is not."]),
 L("Red flags", "Signs you're under-recovering", ["Legs still heavy at the next session", "Hips feel locked, squat depth drops", "Lower back starts doing the work", "You dread the gym instead of wanting it"], "Sound like you? Swipe."),
 L("The recovery stack", "What actually moves the needle", [["Sleep", "The one thing you can't out-train"], ["Water and protein", "Every day, not only on training days"], ["Easy movement next day", "A walk or 10 minutes of mobility"], ["Sports massage", "When the legs need more than a foam roller"]]),
 P("sports-massage", "Why sports massage", "Work on the muscles you actually loaded", ["A sports massage therapist focuses on quads, hamstrings, glutes and calves, the muscles leg day hits hardest."], ["Sports", "Deep tissue", "Stretching"]),
 L("Timing", "When to book it", [["The day after a hard session", "Not right before heavy lifting or a race"], ["Tell the therapist what you trained", "So they know where to focus"], ["Make it a routine", "Not only when something hurts"]]),
 CTA("Find a sports massage near your gym", ["Sports massage", "JLT"], "Tag your gym partner"),
 "Training is only half the work. The other half happens after you leave the gym.\n\nSwipe for the signs you're under-recovering and the recovery stack that actually helps. Tag the friend who skips it.", SPORT_TAGS)

# 03
add("5-signs",
 CV("cov-signs", "Body check", "5 signs your body is <em>asking</em> for a massage", "Most men wait until it hurts. Don't."),
 L("Signs 1–3", "Your body is already talking", [["You crack your neck all day", "And it never really releases"], ["Your shoulders feel like armour", "Hard to the touch, high and tight"], ["You turn your whole body to look back", "Instead of just your head"]]),
 L("Signs 4–5", "And it's getting louder", [["You sleep but wake up stiff", "Mornings feel older than you are"], ["Stress sits in your body", "Jaw clenched, fists tight, short breath"]], "Ticked two or more? Swipe."),
 T("Why it matters", "Tension rarely fixes itself", ["When you ignore it for weeks, you start moving around it: shorter steps, rounded shoulders, stiff turns.", "<b>The sooner you deal with it,</b> the easier it is to undo."]),
 P("p-studio", "The simple fix", "One hour that resets the week", ["A classic or deep tissue massage helps you notice where you hold tension, and let it go."], ["Classic", "Deep tissue", "Relax"]),
 L("Before you book", "Make the first session count", [["Pick one goal", "Relax, recover, or work on a problem area"], ["Choose the type", "Classic for relaxing, deep tissue for tight spots"], ["Book the time you'll keep", "Evening slots are easier after work"]]),
 CTA("Find a massage near you tonight", ["Classic massage", "Dubai Marina"], "Save this and check yourself next week"),
 "Your body doesn't send emails. It sends stiff necks, tight shoulders and bad mornings.\n\nSwipe through the 5 signs and be honest about how many you ticked. Save this and check again next week.")

# 04
add("which-massage",
 CV("cov-choose", "Massage 101", "Deep tissue, sports or classic: <em>which one</em> is yours?", "Stop guessing. Pick the right one in 30 seconds."),
 T("Classic (Swedish)", "For switching off", ["Long, flowing strokes and medium pressure.", "<b>Pick it if:</b> you're stressed, it's your first massage, or you simply want to relax."], ["Medium pressure", "Relaxing"]),
 T("Deep tissue", "For stubborn tight spots", ["Slow, firm work on the deeper layers of muscle, often neck, back and shoulders.", "<b>Pick it if:</b> desk job, long drives, the same knot that keeps coming back."], ["Firm pressure", "Focused"]),
 T("Sports", "For people who train", ["Targets the muscles you load: legs, hips, back, shoulders. Often mixed with stretching.", "<b>Pick it if:</b> gym, running, padel, football, golf."], ["Firm", "Stretching", "Recovery"]),
 P("p-thai", "Bonus", "Thai massage: stretching without the effort", ["Done on a mat, fully clothed. The therapist moves you through stretches you'd never do alone."], ["Clothed", "Stretching", "Mobility"]),
 L("Still not sure?", "Quick decision guide", [["Stressed and tired", "Classic"], ["Stiff from the desk or car", "Deep tissue"], ["Sore from training", "Sports"], ["Feel stiff all over", "Thai"]]),
 CTA("Filter by massage type in one tap", ["Any type", "Downtown Dubai"], "Save this for your next booking"),
 "Most men book 'a massage' and hope for the best. Choosing the right type changes the whole experience.\n\nSwipe for a 30-second guide: classic, deep tissue, sports and Thai. Save it for your next booking.")

# 05
add("first-massage",
 CV("cov-first", "First timer", "First massage? The <em>men's guide</em>", "What happens, what to wear, what to say."),
 L("Before", "The night before and on the day", [["Pick the type and duration", "60 minutes classic is a safe start"], ["Shower before you go", "Simple courtesy, you'll feel better too"], ["Arrive 10 minutes early", "Rushing in stressed wastes half the session"]]),
 T("What to wear", "Comfort and privacy come first", ["The therapist leaves the room while you change and you're covered with a towel the whole time. Only the area being worked on is uncovered.", "<b>For Thai massage</b> you stay fully clothed in loose clothes."]),
 L("During", "Things nobody tells you", [["Talk or stay quiet, both are fine", "Most men just switch off"], ["Speak up about pressure", "\"Firmer\" or \"lighter\" is all it takes"], ["Mention any injuries", "Before you start, not halfway"]]),
 P("p-shoulders", "Remember", "It's a professional service", ["A good therapist is focused on your muscles and your comfort. Choose verified profiles and read the program description before you book."], ["Verified", "Clear programs", "Fixed prices"]),
 L("After", "Make it last", [["Drink water", "And take it easy for the evening"], ["Notice how you feel next day", "That tells you what to book next time"], ["Book the next one", "Results come from regular sessions"]]),
 CTA("Find your first therapist", ["Classic massage", "Jumeirah"], "Send this to a friend who's never tried it"),
 "Never had a massage because you don't know what to expect? Totally normal.\n\nSwipe for the no-awkwardness guide: before, during and after. Send it to the friend who keeps saying 'one day'.")

# 06
add("driving-back",
 CV("cov-drive", "Commute pain", "The Sheikh Zayed Road <em>back</em>", "An hour in the car each way? Your back keeps the score."),
 L("Sound familiar?", "The driver's checklist", ["Lower back aches when you get out of the car", "Right hip feels tight", "Neck stiff from checking mirrors", "Shoulders up near your ears in traffic"], "Two or more? Swipe."),
 T("What's going on", "Sitting still, but working hard", ["In the car your hips stay bent, your lower back rounds and your shoulders hold the wheel.", "<b>Same position, every day,</b> and those muscles forget how to relax."]),
 L("Fix it in the car", "3 small changes", [["Seat closer and more upright", "Knees slightly lower than hips"], ["Support your lower back", "A small cushion or rolled towel"], ["Hands at 9 and 3, shoulders down", "Check at every red light"]]),
 P("p-lowback", "When it doesn't go away", "Hand it to a professional", ["Deep tissue work on the lower back, hips and glutes helps undo hours of sitting behind the wheel."], ["Deep tissue", "Back & hips"]),
 L("Book it right", "Fit it into your week", [["Go on a lighter traffic day", "Don't add stress to a 2-hour commute"], ["Ask for back, hips and glutes", "The whole chain, not only the sore spot"], ["Pick a place near home", "Then go straight to bed"]]),
 CTA("Find a massage near home", ["Deep tissue", "Al Barsha"], "Send this to someone who lives on SZR"),
 "If you spend an hour or more in Dubai traffic every day, your lower back feels it.\n\nSwipe for 3 small fixes for the car and what to do when the ache doesn't go away. Share it with someone who commutes every day.")

# 07
add("cant-switch-off",
 CV("cov-night", "Stress & sleep", "Can't <em>switch off</em> at night?", "Your mind stops when your body does."),
 L("Sound familiar?", "The 1 am checklist", ["Scrolling in bed long after you meant to sleep", "Replaying today's meetings", "Jaw clenched, shoulders tight", "Tired all day, wide awake at night"]),
 T("What's going on", "Your body is still at work", ["After a long, intense day the body can stay in 'on' mode: fast breathing, tight muscles, racing thoughts.", "<b>You can't think your way out of it.</b> You have to help the body slow down."]),
 L("Tonight's routine", "A 30-minute wind-down", [["Screens off 30 min before bed", "Or at least the work apps"], ["Warm shower", "Then cooler bedroom"], ["Slow breathing", "In 4 sec, out 6 sec, five minutes"]]),
 P("p-studio", "Once a week", "A full hour of switching off", ["A relaxing evening massage is one of the simplest ways to give your body a clear 'day is over' signal."], ["Relax", "Classic", "Aroma"]),
 L("Book it right", "Make it an evening ritual", [["Book late afternoon or evening", "Then go home, not back to the laptop"], ["Ask for slower, medium pressure", "Relax, not deep work"], ["Leave the phone in the bag", "The whole hour is yours"]]),
 CTA("Book an evening massage nearby", ["Relax massage", "Business Bay"], "Save this for your next bad night"),
 "Lying in bed at 1 am replaying the day? Your mind won't stop until your body does.\n\nSwipe for a 30-minute wind-down routine and how to turn one evening a week into a proper reset.")

# 08
add("myths",
 CV("cov-myths", "Myth busting", "4 myths that stop men from <em>booking</em> a massage", "Which one have you heard?"),
 T("Myth #1", "\"It's just pampering\"", ["For most men a massage is maintenance, like the gym or the barber.", "<b>Reality:</b> it's one of the simplest ways to deal with tight muscles from desk work, driving and training."]),
 T("Myth #2", "\"No pain, no gain\"", ["Pressure should be firm when you need it, not unbearable.", "<b>Reality:</b> if you're holding your breath and tensing up, it's too much. Say so."]),
 T("Myth #3", "\"I'll go when something hurts\"", ["By the time it hurts, the tension has usually been building for weeks.", "<b>Reality:</b> regular sessions are easier and usually more pleasant than fixing a problem later."]),
 P("p-sports-legs", "Myth #4", "\"Massage is for spas, not for guys like me\"", ["Athletes, drivers, office workers and fathers who carry kids all day book massages. It's a professional service for anyone with a body that works hard."]),
 L("The truth", "What massage actually is", [["Maintenance", "Not a luxury"], ["Professional", "Verified therapists, clear programs"], ["For you", "Desk, gym, car or all three"]]),
 CTA("Try it this week", ["Any type", "Near you"], "Send this to the friend who still believes #3"),
 "'It's just pampering.' 'No pain, no gain.' 'I'll go when it hurts.'\n\nSwipe through the 4 myths that keep men away from massage, and what's actually true. Send it to the friend who still believes #3.")

# 09
add("padel-shoulder",
 CV("cov-padel", "Padel & racket sports", "Padel shoulder is <em>real</em>", "Love the game? Look after the arm that plays it."),
 L("Sound familiar?", "After a few sets", ["Front of the shoulder aches on overheads", "Forearm and elbow feel tight", "Lower back stiff from all the twisting", "Calves tight after quick sprints"]),
 T("What's going on", "Short, sharp, one-sided", ["Padel is fast bursts, twists and overheads, mostly on one side of the body.", "<b>Play several times a week</b> and the same muscles never fully recover."]),
 L("Before and after", "Your court routine", [["Warm up 5–10 minutes", "Arm circles, band work, light rallies"], ["Cool down", "Stretch shoulders, forearms and calves"], ["Rest days matter", "Back-to-back evenings add up"]]),
 P("p-shoulders", "Recovery", "Sports massage for players", ["A therapist can work on shoulders, forearms, back and calves, the exact chain padel loads."], ["Sports", "Shoulders", "Forearms"]),
 L("Book it right", "Plan around your games", [["The day after a heavy session", "Not right before a tournament"], ["Tell them your dominant arm", "And where it bothers you"], ["Pain that doesn't settle?", "See a doctor or physio first"]]),
 CTA("Find a sports massage near your club", ["Sports massage", "Al Quoz"], "Tag your padel partner"),
 "Padel nights are the best nights. Until your shoulder starts complaining.\n\nSwipe for a simple court routine and how to recover between games. Tag your padel partner.", SPORT_TAGS)

# 10
add("long-haul",
 CV("cov-flight", "Travel recovery", "Just <em>landed</em> in Dubai after a long-haul flight?", "Stiff back, heavy legs, foggy head. Here's the reset."),
 L("Sound familiar?", "After 7+ hours in a seat", ["Lower back stiff when you stand up", "Legs and ankles feel heavy", "Neck sore from sleeping upright", "Body clock completely off"]),
 T("What's going on", "Hours without moving", ["Long flights mean sitting still in a cramped position, dry air and broken sleep.", "<b>Your body needs to move</b> and loosen up before it feels normal again."]),
 L("The landing plan", "First 24 hours", [["Walk as soon as you land", "Stairs, not escalators"], ["Water, lots of it", "Cabin air is dry"], ["Daylight in the morning", "Helps your body clock adjust"]]),
 P("p-sports-legs", "The reset", "A massage after you land", ["A classic or sports massage helps a stiff back and heavy legs feel human again, especially after a business trip."], ["Classic", "Sports", "Legs & back"]),
 L("Book it right", "Make it easy", [["Book it the evening you land", "Or the next morning"], ["Ask for back and legs", "Where flights hit hardest"], ["Medium pressure", "Your body is tired, not injured"]]),
 CTA("Find a massage near your hotel or home", ["Classic massage", "DIFC"], "Save this for your next trip"),
 "Flew in from London, Mumbai or Almaty and feel like you've been folded in half?\n\nSwipe for a simple landing plan and how to reset your body after a long-haul flight. Save it for your next trip.")

# 11
add("screen-headache",
 CV("cov-headache", "Desk life", "That <em>4 pm headache</em> after a day on screens", "It may start in your neck and shoulders."),
 L("Sound familiar?", "The afternoon pattern", ["Dull ache at the back of the head", "Tight band across the forehead", "Eyes tired, shoulders tense", "Coffee doesn't really help"]),
 T("What's going on", "Neck, shoulders, screen", ["Tension headaches are often linked to tight muscles in the neck and shoulders, plus long hours focusing on a screen.", "<b>Frequent or severe headaches?</b> Check with a doctor first."]),
 L("Today", "3 desk habits", [["20-20-20", "Every 20 min, look 20 feet away for 20 sec"], ["Drop your shoulders", "Set an hourly reminder"], ["Water before coffee", "Dehydration makes it worse"]]),
 P("p-neck", "Neck and shoulders", "Release the tension at the source", ["A massage focused on neck, shoulders and the base of the skull helps many people with that tight, heavy feeling."], ["Neck & shoulders", "Classic", "Deep tissue"]),
 L("Book it right", "What to ask for", [["Neck, shoulders and upper back", "30 or 60 minutes"], ["Gentle on the neck", "Firm on the shoulders"], ["Go when it starts building", "Not only on the worst day"]]),
 CTA("Find a neck & shoulder massage", ["Neck & shoulders", "Dubai Internet City"], "Send this to your screen-buddy"),
 "Every day at 4 pm, the same headache? For many desk workers it starts in a tight neck and shoulders.\n\nSwipe for 3 desk habits and when a neck & shoulder massage helps. Frequent or severe headaches are a reason to see a doctor first.")

# 12
add("lower-back",
 CV("cov-lowback", "Lower back", "Lower back <em>tight</em> after a long day sitting?", "You're not old. You're sitting too much."),
 L("Sound familiar?", "End of the day", ["Stiff when you stand up from the chair", "Need to 'crack' your back", "Hard to bend for your shoes in the morning", "Hips feel tight"]),
 T("What's going on", "Hips bent all day", ["When you sit for hours, the hip flexors stay short and the glutes switch off.", "<b>Your lower back</b> ends up doing work it shouldn't."]),
 L("Do this tonight", "3 stretches, 5 minutes", [["Kneeling hip flexor stretch", "30 sec each side"], ["Knees to chest", "Lying on your back, 30 sec"], ["Figure-4 glute stretch", "30 sec each side"]]),
 P("p-lowback", "Deeper work", "When stretching doesn't release it", ["Deep tissue massage on the lower back, glutes and hips works on the muscles stretching can't fully reach."], ["Deep tissue", "Back & hips"]),
 L("Book it right", "Get real results", [["Ask for back AND hips", "The problem rarely sits in one spot"], ["Firm but bearable", "You should still breathe easily"], ["Sharp or radiating pain?", "See a doctor first"]]),
 CTA("Find deep tissue massage nearby", ["Deep tissue", "Dubai Hills"], "Send this to someone who sits all day"),
 "Stiff lower back by evening? Usually it's not age, it's hours of sitting.\n\nSwipe for a 5-minute stretch routine and when deep tissue massage makes sense.")

# 13
add("runners-calves",
 CV("cov-run", "Runners", "Runners: your <em>calves</em> are talking", "Listen before they start shouting."),
 L("Sound familiar?", "After your weekly kilometres", ["Calves rock hard after runs", "Feet sore in the morning", "Tight hamstrings, short stride", "Shins grumble on harder sessions"]),
 T("What's going on", "Thousands of small impacts", ["Every run means thousands of landings. Calves, feet and hamstrings absorb most of it.", "<b>Add more distance quickly</b> and they never fully recover between runs."]),
 L("The runner's checklist", "Simple, every week", [["Increase distance gradually", "Small steps, not big jumps"], ["Calf raises and stretching", "After every run"], ["Good shoes, replaced on time", "Old foam doesn't protect"]]),
 P("p-sports-legs", "Recovery", "Sports massage for runners", ["Many runners use sports massage on calves, hamstrings and feet to feel looser between sessions and before race day."], ["Sports", "Legs", "Feet"]),
 L("Book it right", "Timing for runners", [["Easy day or rest day", "Not right before a hard session"], ["Not the day before a race", "Book a few days earlier"], ["Sharp pain?", "Get it checked first"]]),
 CTA("Find a sports massage near your running route", ["Sports massage", "Al Barsha"], "Tag your running club"),
 "Running Kite Beach or Al Qudra every week? Your calves and feet do most of the work.\n\nSwipe for a simple runner's checklist and how to time your sports massage. Tag your running crew.", SPORT_TAGS)

# 14
add("thai-massage",
 CV("p-thai", "Massage guide", "Thai massage: <em>stretching</em> without the effort", "For men who feel stiff from head to toe."),
 T("What it is", "Assisted stretching on a mat", ["Thai massage is done on a mat, fully clothed. The therapist uses hands, forearms and body weight to move you through stretches.", "<b>No oil, no table,</b> lots of movement."]),
 L("Is it for you?", "Pick Thai if", ["You can't touch your toes", "Hips feel locked", "You hate stretching on your own", "You want energy, not sleep"]),
 L("What to expect", "The session", [["Wear loose clothes", "Or the clothes provided"], ["Expect movement", "Pulls, presses and long stretches"], ["Breathe out into each stretch", "And tell them if it's too much"]]),
 P("p-studio", "Thai vs classic", "Feels very different", ["Classic is calm and flowing on a table. Thai is active and stretchy on a mat. Many men leave Thai feeling taller and lighter."], ["Thai", "Clothed", "Mobility"]),
 L("Book it right", "First Thai session", [["90 minutes if you can", "Thai needs time"], ["Eat light before", "You'll be moved around a lot"], ["Mention old injuries", "Knees, back, shoulders"]]),
 CTA("Find Thai massage in Dubai", ["Thai massage", "Al Karama"], "Send this to your stiffest friend"),
 "Thai massage is the closest thing to someone doing your stretching for you.\n\nSwipe to see what it is, who it's for and what to expect in your first session.")

# 15
add("text-neck",
 CV("cov-phone", "Phone posture", "Text neck: what your <em>phone</em> does to you", "Check your posture right now. Yes, now."),
 L("Quick test", "Are you doing it now?", ["Chin pushed forward", "Shoulders rounded", "Head tilted down at the screen", "Phone held at chest height or lower"], "Most of us tick all four."),
 T("What's going on", "Your head tilts, your neck pays", ["When you look down at your phone, the muscles at the back of your neck work much harder to hold your head.", "<b>Do that for hours a day</b> and they stay tight."]),
 L("Easy fixes", "Starting today", [["Lift the phone to eye level", "Not your head down to the phone"], ["Chin tucks", "10 reps, a few times a day"], ["Screen-time limits", "Your neck will thank you"]]),
 P("p-neck", "Undo the damage", "Release neck and upper back", ["A neck, shoulder and upper back massage releases the muscles that hold your head up all day."], ["Neck & shoulders", "Classic"]),
 L("Book it right", "Ask for", [["Neck, shoulders, upper back", "The whole chain"], ["Gentle on the neck", "Firmer on the shoulders"], ["Some stretching at the end", "Ask for it"]]),
 CTA("Find a neck massage nearby", ["Neck & shoulders", "JBR"], "Send this to someone looking down at their phone"),
 "Look at how you're holding your phone right now. Chin forward, head down, shoulders rounded?\n\nSwipe for what 'text neck' does and 3 easy fixes. Then send this to someone who's looking down at their phone.")

# 16
add("how-often",
 CV("cov-calendar", "Massage 101", "How often should you <em>really</em> get a massage?", "There's no single answer. Here's how to choose yours."),
 T("Start here", "It depends on your week", ["How often depends on how hard you use your body, your budget and your goal.", "<b>Here's a simple way to think about it.</b> Adjust to how you feel."]),
 L("Office worker", "Desk + screens", [["Every 3–4 weeks", "To keep neck and back tension in check"], ["Classic or deep tissue", "60 minutes"]]),
 L("Gym regular", "Training 3+ times a week", [["Every 2–4 weeks", "Around your heaviest training days"], ["Sports or deep tissue", "60–90 minutes"]]),
 P("p-shoulders", "Desk + gym + kids", "Doing it all?", ["If you sit all day and train hard in the evenings, your body is working two shifts. Book a regular slot and keep it."], ["Sports", "Deep tissue"]),
 L("The rule", "Listen to your body", [["Feel great for weeks?", "Space sessions out"], ["Tight again in days?", "Book more often or longer"], ["Consistency beats intensity", "Regular is better than rare and painful"]]),
 CTA("Save a favourite therapist", ["Your therapist", "Saved ★"], "Save this to plan your month"),
 "Once a year? Once a week? There's no single answer, but there is a simple way to choose.\n\nSwipe for a rough guide for desk workers, gym regulars and those doing both. Save it and plan your month.")

# 17
add("before-after-gym",
 CV("cov-gym2", "Training", "Massage before or <em>after</em> the gym?", "Timing changes everything."),
 T("Before training", "Short and light, or not at all", ["A deep massage right before heavy lifting can leave muscles feeling loose and slow.", "<b>If you want something before,</b> keep it short and light."]),
 T("After training", "The sweet spot", ["The day after a hard session is often ideal: muscles are recovering and you're not about to load them again.", "<b>Same-day?</b> Keep the pressure lighter."]),
 L("Rules of thumb", "Easy timing guide", [["Heavy leg day", "Massage next day"], ["Competition or race", "Book a few days before, not the day before"], ["Rest day", "Perfect for deep work"]]),
 P("p-sports-legs", "Sports massage", "Built around your training", ["A sports therapist adjusts pressure and focus to where you are in your training week."], ["Sports", "Recovery"]),
 L("Tell your therapist", "3 things to mention", [["What you trained and when", "So they focus on the right muscles"], ["What's coming up", "Heavy session, game or race"], ["Any old injury", "Before you start"]]),
 CTA("Find a sports massage near your gym", ["Sports massage", "Dubai Marina"], "Tag the friend who trains with you"),
 "Massage before training or after? Most men get the timing wrong.\n\nSwipe for a simple timing guide and what to tell your therapist. Tag your training partner.", SPORT_TAGS)

# 18
add("burnout",
 CV("cov-burnout", "High-pressure jobs", "Burnout doesn't <em>announce</em> itself", "It sneaks in. Here's what to look for."),
 L("Early signs", "Check yourself", ["Tired even after a full night's sleep", "Short temper with people you like", "Weekends feel like recovery, not life", "Body always tense, jaw always tight"]),
 T("What's going on", "Always on, never off", ["Long hours, constant messages, pressure to perform. The body stays in high alert mode.", "<b>Ignore it long enough</b> and everything starts feeling heavier."]),
 L("Reset habits", "Small, but they work", [["A hard stop to the workday", "Same time, most days"], ["Move every day", "A walk counts"], ["Protect your sleep", "Like you protect your calendar"]]),
 P("p-studio", "Your hour off", "A massage as a weekly reset", ["An hour with your phone off and someone working the tension out of your body. Many men use it as their weekly reset."], ["Relax", "Classic", "Hot stone"]),
 L("Make it stick", "Put it in the calendar", [["Same day, same time", "Treat it like a meeting"], ["Close to home or office", "No extra stress getting there"], ["Signs getting worse?", "Talk to a professional"]]),
 CTA("Book your weekly reset", ["Relax massage", "Downtown Dubai"], "Send this to a friend who's running on empty"),
 "Burnout rarely arrives in one day. It shows up as bad sleep, short temper and a body that never relaxes.\n\nSwipe for the early signs and the small habits that help. If things feel heavy for weeks, talk to a professional.")

# 19
add("ac-stiffness",
 CV("cov-ac", "Dubai life", "AC all day, <em>stiff</em> all day?", "Cold office, cold car, cold mall. Your muscles notice."),
 L("Sound familiar?", "The Dubai pattern", ["Office AC blasting on your neck", "Car AC straight at your shoulders", "Stiff in the morning, tight by evening", "You only feel loose in the heat outside"]),
 T("What's going on", "Cold muscles tighten up", ["Many people notice they tense up and feel stiffer when they sit in cold air for hours, especially around the neck and shoulders.", "<b>Move between heat and cold</b> all day and you rarely fully relax."]),
 L("Simple fixes", "Easy wins", [["Point the vents away", "Not directly on your neck"], ["Keep a light layer at work", "Shoulders covered"], ["Warm shower in the evening", "Loosens you up before bed"]]),
 P("p-hotstone", "Warm it up", "Hot stone massage", ["Heated stones on the back and shoulders plus massage. A good pick when you feel cold, tight and tired."], ["Hot stone", "Relax", "Back"]),
 L("Book it right", "Ask for", [["Hot stone or warm oil", "60–90 minutes"], ["Focus on neck and shoulders", "Where the AC hits"], ["Go in the evening", "Then straight home"]]),
 CTA("Find hot stone massage in Dubai", ["Hot stone", "Jumeirah"], "Send this to the guy under the AC vent"),
 "In Dubai we go from 40°C outside to 20°C inside dozens of times a day. Many people notice their neck and shoulders tighten up.\n\nSwipe for easy fixes and why hot stone massage is a good pick when you feel cold and stiff.")

# 20
add("pick-therapist",
 CV("cov-choose2", "Smart booking", "How to <em>pick</em> the right massage therapist", "A 5-point checklist before you book."),
 L("Checklist 1–3", "Before you message anyone", [["Verified profile", "Look for the Verified badge on pro-body.ae"], ["Clear programs", "Massage types, durations, what's included"], ["Clear prices", "No surprises when you arrive"]]),
 L("Checklist 4–5", "Then check", [["Location that works", "Near home, office or gym, use the map"], ["Massage type matches your goal", "Relax, recover, or work on a problem"]]),
 T("Red flags", "Skip the profile if", ["No clear description of services or prices, vague promises, or anything that doesn't look like a professional massage service.", "<b>Professional service only.</b> That's the standard on pro-body.ae."]),
 P("p-shoulders", "Ask before booking", "Message them directly", ["On pro-body.ae you contact the salon or therapist directly. Ask about the type, duration and availability before you go."], ["Direct contact", "WhatsApp", "Call"]),
 L("Save time", "Use the filters", [["Filter by area", "Dubai districts"], ["Filter by type and price", "Only what you need"], ["Save favourites", "Book again in one tap"]]),
 CTA("Find a verified therapist", ["Verified ✓", "Your area"], "Save this checklist"),
 "Booking a massage shouldn't feel like a gamble.\n\nSwipe for a 5-point checklist: verified profile, clear programs, clear prices, location and the right massage type. Save it for your next booking.")

# 21
add("etiquette",
 CV("cov-etiquette", "Massage etiquette", "Massage etiquette <em>for men</em>", "The unwritten rules, written down."),
 L("Do", "Good habits", [["Shower before", "Basic respect"], ["Arrive on time", "Late means a shorter session"], ["Speak up about pressure", "Therapists want feedback"], ["Mention injuries and allergies", "Before you start"]]),
 L("Don't", "Avoid these", [["Don't take calls", "Phone on silent"], ["Don't 'tough it out'", "Too painful? Say so"], ["Don't come straight after a big meal", "Wait an hour or two"]]),
 T("Common question", "Talk or stay quiet?", ["Both are completely fine. Many men chat at the start and go quiet once they relax.", "<b>The therapist will follow your lead.</b>"]),
 P("p-shoulders", "Remember", "It's a professional service", ["You stay covered with a towel. Only the area being worked on is uncovered. Pick verified profiles and clear programs."], ["Professional", "Verified"]),
 L("Tipping", "Is it expected?", [["Check the salon's policy", "It varies"], ["Appreciated, not required", "If you had a great session"], ["Best tip of all?", "Book again"]]),
 CTA("Find a professional therapist", ["Any type", "Dubai"], "Send this to a first-timer"),
 "Talk or stay quiet? What to wear? Tip or not?\n\nSwipe for the unwritten rules of massage etiquette for men, written down. Send it to a friend who's booking his first one.")

# 22
add("feet",
 CV("cov-feet", "On your feet all day", "Long day on your <em>feet</em>?", "Malls, site visits, trade shows. Your feet carry all of it."),
 L("Sound familiar?", "End of the day", ["Feet throb when you take your shoes off", "Heels sore in the morning", "Calves tight", "Lower back tired"]),
 T("What's going on", "Small muscles, big job", ["Your feet carry your full weight with every step. Formal shoes and hard floors make it harder.", "<b>Tired feet</b> often pull calves and back along with them."]),
 L("Tonight", "Feet first", [["Roll your foot on a ball", "2 minutes each side"], ["Calf stretch on a step", "30 sec each side"], ["Better shoes for long days", "Your back will notice"]]),
 P("p-feet", "Foot reflexology", "An hour for the part that works hardest", ["Foot reflexology and foot massage work through the sole, heel and ankle. Many men are surprised how relaxing it is."], ["Reflexology", "Foot massage"]),
 L("Book it right", "Ask for", [["Feet and calves together", "45–60 minutes"], ["Firm on the soles", "Lighter on the ankles"], ["Combine with back massage", "If you can"]]),
 CTA("Find foot reflexology nearby", ["Foot reflexology", "Deira"], "Send this to someone who walks all day"),
 "Trade show, site visit or a long day at the mall? Your feet carried you through all of it.\n\nSwipe for 2-minute foot fixes and why foot reflexology is worth trying.")

# 23
add("friday-reset",
 CV("cov-weekend", "Weekend", "The <em>Friday reset</em>", "End the week properly, start the weekend fresh."),
 L("Sound familiar?", "Friday evening", ["Body tired, mind still at work", "Saturday spent recovering", "Sunday dread starts early", "No real rest all weekend"]),
 T("The idea", "Close the week on purpose", ["Instead of collapsing on the sofa, give yourself a clear end to the week.", "<b>One routine, every Friday.</b> Simple enough to keep."]),
 L("The routine", "Friday, 5–9 pm", [["Hard stop at work", "Phone on do-not-disturb"], ["Move", "Gym, padel or a walk"], ["Massage", "60 minutes, nothing to think about"], ["Early dinner, early night", "Saturday starts fresh"]]),
 P("p-studio", "The anchor", "Make the massage the fixed point", ["Book the same slot every week or every other week. It's easier to keep a routine when it's already in the calendar."], ["Relax", "Classic", "Sports"]),
 L("Book it right", "Make it easy", [["Book a few days ahead", "Friday evenings fill up"], ["Near home", "No traffic afterwards"], ["Pick a favourite therapist", "Save the profile"]]),
 CTA("Book your Friday reset", ["Any type", "Friday evening"], "Send this to your weekend crew"),
 "Most weekends start with recovering from the week. What if you closed the week on purpose instead?\n\nSwipe for a simple Friday routine with one fixed anchor: an hour of massage.")

# 24
add("lunch-break",
 CV("cov-lunch", "Office hack", "A 60-minute <em>lunch break</em> that pays off", "Instead of scrolling at your desk."),
 L("Sound familiar?", "Your usual lunch", ["Eating at the desk", "Scrolling the phone", "Back to work just as tense", "The 3 pm slump hits hard"]),
 T("The idea", "Use the hour for your body", ["A 30–45 minute massage near the office fits into a long lunch break.", "<b>Back at your desk</b> looser, with your head clear."]),
 L("How to do it", "Plan it once", [["Find a place within 10 minutes", "Use the map near your office"], ["Book 30–45 minutes", "Neck, shoulders and back"], ["Grab a light lunch after", "Not a heavy one before"]]),
 P("p-neck", "What to ask for", "Short and focused", ["Neck, shoulders and upper back: where desk work hits hardest. Medium pressure so you're not sleepy after."], ["Neck & shoulders", "30–45 min"]),
 L("Make it a habit", "Once a week", [["Same day every week", "Block it in your calendar"], ["Bring a colleague", "Easier to stick to"], ["Save the place", "Book again in seconds"]]),
 CTA("Find a massage near your office", ["Neck & shoulders", "DIFC"], "Send this to your lunch buddy"),
 "Your lunch break is 60 minutes. You probably spend it at your desk, scrolling.\n\nSwipe to see how to turn it into a quick neck and shoulder reset near the office. Send it to your lunch buddy.")

# 25
add("3-questions",
 CV("cov-questions", "Smart booking", "3 questions to ask <em>before</em> you book", "Avoid paying for the wrong session."),
 T("Question 1", "\"What massage do you recommend for my problem?\"", ["Describe what you feel: stiff neck, sore legs, stress. A good therapist will suggest the type and duration.", "<b>If they can't answer clearly,</b> keep looking."]),
 T("Question 2", "\"What's included in the price?\"", ["Duration, type, any extras like hot stones or stretching.", "<b>Clear price, clear program,</b> no surprises."]),
 T("Question 3", "\"Do you have time today or this week?\"", ["Availability matters. Book the slot you'll actually keep.", "<b>Evening and weekend slots</b> fill up fastest."]),
 P("p-shoulders", "Where to ask", "Message the therapist directly", ["Every profile on pro-body.ae has direct contact. Ask your 3 questions before you go."], ["WhatsApp", "Call", "Direct"]),
 L("Bonus", "Tell them too", [["Any injuries or conditions", "Before you start"], ["Pressure you like", "Light, medium or firm"], ["Your goal", "Relax, recover or fix a problem"]]),
 CTA("Find a therapist and ask directly", ["Your question", "Direct contact"], "Save this before your next booking"),
 "Three quick questions save you from paying for the wrong massage.\n\nSwipe to see what to ask and what to tell your therapist before you book.")

# 26
add("gym-mistakes",
 CV("cov-gym3", "Gym", "5 recovery <em>mistakes</em> gym guys make", "Be honest: how many do you make?"),
 L("Mistakes 1–3", "Recognise any?", [["Training the same muscles daily", "Muscles grow when they rest"], ["Skipping warm-up", "Straight to the heavy weights"], ["Sleeping 5 hours", "And expecting progress"]]),
 L("Mistakes 4–5", "The big ones", [["Ignoring small aches", "Until they become injuries"], ["Never doing any recovery work", "No stretching, no mobility, no massage"]]),
 T("Why it matters", "Recovery is training", ["Progress happens when your body recovers from the work you did.", "<b>Skip recovery</b> and you train tired, plateau and get hurt more."]),
 P("p-sports-legs", "Recovery tool", "Sports massage", ["Many gym regulars add a sports massage every few weeks to stay loose and catch tight spots early."], ["Sports", "Deep tissue"]),
 L("Fix it", "Your new routine", [["Plan rest days", "Write them in your program"], ["10 minutes of mobility", "After every session"], ["Massage every 2–4 weeks", "Around heavy blocks"]]),
 CTA("Find a sports massage near your gym", ["Sports massage", "Business Bay"], "Tag the guy who never rests"),
 "Training hard but stuck? It might not be the program. It might be the recovery.\n\nSwipe for the 5 most common recovery mistakes and how to fix them. Tag the guy who never takes a rest day.", SPORT_TAGS)

# 27
add("gift",
 CV("cov-gift", "Gift idea", "A gift for the man who <em>has everything</em>", "Dad, brother, best friend, boss."),
 L("The problem", "Gift ideas you've used", ["Another perfume", "Another watch strap", "Another gadget he won't use", "Another voucher he'll forget"]),
 T("The idea", "Give him an hour off", ["Most men won't book a massage for themselves. They'll happily go if someone books it for them.", "<b>It's practical, personal</b> and he'll actually use it."]),
 L("Match it to him", "Which massage?", [["Office dad", "Deep tissue for neck and back"], ["Gym brother", "Sports massage"], ["Stressed boss", "Relax or hot stone"], ["Friend who can't sit still", "Thai massage"]]),
 P("p-hotstone", "Make it special", "Go together", ["Many salons offer sessions for two at the same time. Book one for him and one for you."], ["For two", "Hot stone", "Relax"]),
 L("How to do it", "3 steps", [["Choose a salon near him", "Use the map"], ["Message the salon", "Ask about gift options"], ["Tell him the date", "So he can't cancel"]]),
 CTA("Find the perfect massage gift", ["Gift idea", "Near him"], "Send this to someone looking for a gift"),
 "Stuck on what to get the man who already has everything?\n\nSwipe for a gift he'll actually use, and how to match the massage to the man. Send this to someone who's still looking for a gift.")

# 28
add("maintenance",
 CV("cov-barber", "Self-maintenance", "The grown man's <em>monthly</em> maintenance list", "You service your car. Service yourself."),
 L("Monthly", "Your list", [["Barber", "Every 2–4 weeks"], ["Gym or sport", "Most weeks"], ["Massage", "Every 2–4 weeks"], ["Phone-free evening", "At least once a week"]]),
 L("Yearly", "Don't forget", [["Dentist", "Check-ups and cleaning"], ["Doctor's check-up", "Blood test, blood pressure"], ["Eye test", "Especially if you live on screens"]]),
 T("Why a massage is on it", "Maintenance, not luxury", ["Your body works every day: desk, car, gym, kids. Regular massage keeps the small stuff small.", "<b>It's the service</b> most men skip and later wish they hadn't."]),
 P("p-shoulders", "Keep it simple", "Same therapist, regular slot", ["Find one therapist you like and book a regular slot. They learn your body and where you hold tension."], ["Regular", "Same therapist"]),
 L("Make it automatic", "Set it and forget it", [["Calendar reminder", "Every 3 weeks"], ["Save your favourite", "Rebook in seconds"], ["Pair it with the barber", "Same day, same area"]]),
 CTA("Add massage to your routine", ["Your favourite", "Saved ★"], "Save this list"),
 "You service your car on schedule. Do you do the same for yourself?\n\nSwipe for the grown man's maintenance list, monthly and yearly. Save it.")

# 29
add("golf",
 CV("cov-golf", "Golf", "Golf swing feeling <em>stiff</em>?", "Rotation starts in your hips, not your arms."),
 L("Sound familiar?", "After a round", ["Lower back tight on one side", "Hips don't rotate like they used to", "Shoulders and forearms stiff", "Wrists sore after the range"]),
 T("What's going on", "One-sided rotation, again and again", ["The golf swing twists your body the same way hundreds of times.", "<b>Tight hips and upper back</b> make the lower back take more of the load."]),
 L("Before your tee time", "5-minute warm-up", [["Hip circles and lunges", "Open the hips"], ["Thoracic rotations", "Club across the shoulders"], ["Easy swings first", "Short irons before the driver"]]),
 P("p-thai", "Mobility", "Massage plus stretching", ["Sports or Thai massage helps work on hips, back and shoulders, and gets you moving more freely."], ["Sports", "Thai", "Mobility"]),
 L("Book it right", "Around your rounds", [["The day after a round", "Or a few days before a competition"], ["Ask for hips, back and shoulders", "The rotation chain"], ["Back pain that lingers?", "See a doctor or physio"]]),
 CTA("Find a sports massage near your club", ["Sports massage", "Emirates Hills"], "Tag your golf partner"),
 "If your swing feels tight, the problem is often in your hips and upper back.\n\nSwipe for a 5-minute warm-up before your tee time and how to recover after a round. Tag your golf partner.", SPORT_TAGS)

# 30
add("find-in-60",
 CV("cov-phone2", "How it works", "Find a massage near you in <em>60 seconds</em>", "No calls around, no guessing."),
 L("Step 1", "Open pro-body.ae", [["Link in our bio", "No app to download"], ["Free for guests", "Always"]]),
 L("Step 2", "Search your way", [["Map", "See salons and therapists around you"], ["Filters", "Area, massage type, price"], ["Catalog", "Browse all of Dubai"]]),
 L("Step 3", "Check the profile", [["Verified badge", "Profile checked by our team"], ["Programs and prices", "What you get and what it costs"], ["Photos and location", "Know where you're going"]]),
 P("p-studio", "Step 4", "Message directly", ["Contact the salon or therapist straight from the profile. Ask your questions, agree on a time, done."], ["Direct contact", "No middleman"]),
 L("Pro tips", "Save time next time", [["Save favourites", "Rebook in one tap"], ["Compare profiles", "Side by side"], ["Watch for promotions", "Special offers from salons"]]),
 CTA("Try it now", ["Any massage", "Near me"], "Send this to a friend in Dubai"),
 "Finding a good massage in Dubai shouldn't take an evening of calls.\n\nSwipe for how to find, compare and contact a therapist on pro-body.ae in about a minute.")

if __name__ == "__main__":
    os.makedirs(S + "/specs", exist_ok=True)
    for i, c in enumerate(C, 1):
        cid = f"c{i:02d}-{c['slug']}"
        spec = {"id": cid, "slides": [c["cover"]] + c["slides"] + [c["cta"]]}
        json.dump(spec, open(f"{S}/specs/c{i:02d}.json", "w"), indent=1)
    caps = []
    for i, c in enumerate(C, 1):
        caps.append({"n": i, "slug": c["slug"], "caption": c["caption"] + "\n\n👉 Find a therapist on pro-body.ae (link in bio)\n\n" + c["tags"]})
    json.dump(caps, open(S + "/captions.json", "w"), indent=1, ensure_ascii=False)
    print(len(C), "carousels")
    photos = sorted({s["photo"] for c in C for s in [c["cover"]] + c["slides"] if "photo" in s})
    print(photos)
