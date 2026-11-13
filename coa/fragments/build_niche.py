#!/usr/bin/env python3
"""Builds the three audience landing pages (dentists, medspas, coaches) as GHL Custom HTML fragments."""
import html, pathlib

OUT = pathlib.Path(__file__).parent
IMG = "https://wilk1990.github.io/spl-free-session/coa/img/"

NICHES = {
"dentists": dict(
  work_h='Proof we can film', work_sub='This is what our crew and cameras have made for other businesses. Your practice gets the same treatment: real people, real rooms, shot like a film.',
  title="Meta video ads for LA dental practices",
  fonts="family=Manrope:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@1,9..144,500",
  sans='"Manrope"', serif='"Fraunces"',
  css="""--bg:#ffffff;--soft:#eef6f7;--ink:#0d2530;--muted:#4c626b;--line:#d7e6ea;--accent:#0b6e8a;--accent-2:#0b6e8a;--accent-ink:#ffffff;--hl:#0b6e8a;
  --hero-bg:linear-gradient(180deg,#f3f9fa 0%,#ffffff 100%);--hero-ink:#0d2530;--hero-sub:#40575f;--pill-bg:#ffffff;--pill-line:#cfe3e8;--pill-ink:#0d2530;--chip-bg:#ffffff;--chip-line:#d7e6ea;--chip-ink:#2b434c;--frame-shadow:0 30px 80px rgba(13,37,48,.18);--radius:14px;--btn-radius:999px;--logo-filter:none;--foot-bg:#0d2530;--card-bg:#ffffff""",
  logo="logo-lockup-720.png", logo_w=1485, logo_h=360, hero_dark=False,
  eyebrow="For LA dental practices doing $50K+ a month",
  h1='Fill your chairs with implant consults. <span class="serif">Not $59 cleanings.</span>',
  sub="We film your doctor and your practice with cinema cameras and run it as Meta ads that book the cases you actually want. Watch the 4 minute video first.",
  pains_h="Why most dental ads bring you the wrong patients",
  pains=[
    ("The coupon trap","A $59 new patient special brings in a $59 patient. She books the cleaning, takes the free x ray and you never see her again."),
    ("Stock smiles","Every practice in your zip code runs the same model with perfect teeth. Nobody chooses a dentist they have never seen."),
    ("Reports, not consults","Your agency sends reach and clicks. Your front desk can't schedule a click. You still don't know which ad booked which case."),
  ],
  steps_h="How we fill your schedule with cases",
  steps=[
    ("We pick the cases","Implants, full arch, Invisalign, veneers. We build the ads around the treatments that pay for your chair time."),
    ("We film at your practice","Your doctor explains the procedure. Your team. Your real operatory. Shot on cinema cameras in one day, cut into Reels and feed ads."),
    ("We build the booking page","Every click lands on a page made for that treatment, not your homepage. Patients pick a consult time right there."),
    ("We run it and track it","Meta ads to locals around your practice. Every booked consult shows up next to the ad that booked it."),
  ],
  ideas_h="The kind of ads we would film for you",
  ideas_sub="Before your call we write 3 of these for your practice. You keep them either way.",
  ideas=[
    ("“What does an implant feel like the day after?”","Your doctor answers the one question every implant patient googles at 11pm. Calm, honest, 40 seconds."),
    ("“I hid my smile for 9 years”","A real patient story, shot like a short film. The before is told, not shown, so it stays inside Meta's rules."),
    ("“Meet the team before you meet the chair”","A walk through your practice from the front desk to the operatory. Nervous patients book when they know the room."),
  ],
  about="I'm Dennis. I run City of Angels Advertising from Encino. We are a small team that films, edits and runs the ads ourselves. You talk to me, not an account manager.",
  apply_h="Book your call by November 20 and lock in $5,000 a month",
  faq=[
    ("We already have an agency for Google. Is this different?","Yes. Google catches people who already search for a dentist. Meta reaches the people who need an implant and haven't started looking yet. Video is how they get to know you before they call."),
    ("Do you need our doctor on camera?","It works best when the doctor is in it, even for 20 minutes. We do the rest with your team and your rooms. We direct everything, nobody needs to be a natural."),
    ("Are before and after photos allowed?","Meta limits them, so we don't build ads around them. We tell the story with the doctor and the patient instead. That also keeps your ads from getting rejected."),
    ("What does it cost?","$5,000 a month for management if you book your call by November 20. Your ad budget goes straight to Meta, we recommend at least $3,000 a month."),
  ],
  small="Your answers are only used to prepare your call. We never sell or share your data.",
),
"medspas": dict(
  work_h='Proof we can film', work_sub='This is what our crew and cameras have made for other brands. Your spa gets the same look: your injectors, your rooms, shot like a film.',
  title="Meta video ads for LA med spas",
  fonts="family=Jost:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500",
  sans='"Jost"', serif='"Cormorant Garamond"',
  css="""--bg:#fbf7f3;--soft:#f3e9e1;--ink:#2b1f1b;--muted:#6f5d55;--line:#e8d9cd;--accent:#a8705a;--accent-2:#c79a84;--accent-ink:#ffffff;--hl:#a8705a;
  --hero-bg:radial-gradient(1200px 500px at 50% 0%,#f6e7dc 0%,#fbf7f3 70%);--hero-ink:#2b1f1b;--hero-sub:#5e4d46;--pill-bg:#fffaf6;--pill-line:#e3cfc0;--pill-ink:#2b1f1b;--chip-bg:#fffaf6;--chip-line:#e8d9cd;--chip-ink:#5e4d46;--frame-shadow:0 30px 80px rgba(80,45,30,.18);--radius:4px;--btn-radius:2px;--logo-filter:none;--foot-bg:#2b1f1b;--card-bg:#fffaf6""",
  logo="logo-lockup-720.png", logo_w=1485, logo_h=360, hero_dark=False,
  eyebrow="For Los Angeles med spas doing $50K+ a month",
  h1='Book clients who buy the package. <span class="serif">Not the $9 a unit special.</span>',
  sub="We film your injectors and your spa with cinema cameras and run it as Meta ads that book high value consults. Watch the 4 minute video first.",
  pains_h="Why discount ads keep your calendar full and your margins thin",
  pains=[
    ("Coupon clients","Discount tox brings people who chase the next discount. They come once, never rebook and never buy the membership."),
    ("No shows and ghosts","$20 leads look great in a report. Then 4 out of 10 show up and your front desk spends the week chasing the rest."),
    ("Everyone looks the same","Fifty med spas within ten miles post the same lips, the same lasers and the same stock model. Trust goes to the one people can see."),
  ],
  steps_h="How we bring you clients who stay",
  steps=[
    ("We sharpen the offer","Memberships, laser packages, body contouring, full face treatments. We sell what keeps clients coming back, not a one time discount."),
    ("We film at your spa","Your injectors, your rooms, your vibe. Shot on cinema cameras in one day, cut into Reels, Stories and feed ads."),
    ("We build the booking page","Every click lands on a page made for that treatment. Clients pick a consult time right there, no phone tag."),
    ("We run it and track it","Meta ads to women and men around your spa. Every booked consult shows up next to the ad that booked it."),
  ],
  ideas_h="The kind of ads we would film for you",
  ideas_sub="Before your call we write 3 of these for your spa. They are yours, even if we never work together.",
  ideas=[
    ("“What a natural result actually looks like”","Your lead injector explains her approach while she works. Soft light, real client, no filters. Trust in 30 seconds."),
    ("“Why I stopped buying tox on sale”","A member tells why she pays more at your spa. Sells the membership without saying the word discount."),
    ("“Your first visit, start to finish”","From the front door to the treatment room. First timers book when they know exactly what happens."),
  ],
  about="I'm Dennis. I run City of Angels Advertising from Encino. We are a small team that films, edits and runs the ads ourselves. You talk to me, not an account manager.",
  apply_h="Book your call by November 20 and lock in $5,000 a month",
  faq=[
    ("Meta keeps rejecting our ads. Will that happen here?","We build every ad around Meta's rules for aesthetics from the start. No banned before and after photos, no body shaming hooks. Your injector and your clients carry the story."),
    ("Do our injectors need to be on camera?","It works best when they are. We direct everything and only need them for an hour or two between appointments."),
    ("We do promos every month. Do we have to stop?","No. We just stop leading with them. The ads sell the experience and the result, the promo can still close the deal on the consult."),
    ("What does it cost?","$5,000 a month for management if you book your call by November 20. Your ad budget goes straight to Meta, we recommend at least $3,000 a month."),
  ],
  small="Your answers are only used to prepare your call. We never sell or share your data.",
),
"coaches": dict(
  work_h='Proof we can film', work_sub='This is what our crew and cameras have made for creators and brands. You get the same eye for story, filmed wherever you are.',
  price="$3,000", price_what="the full remote package",
  video_note='<span class="note" style="opacity:1;font-weight:600">The video talks about our LA offer. For coaches anywhere in the US we film remotely, and it is $3,000 a month.</span>',
  cta_note="Five quick questions, then you pick a time. Your ads go live within 14 days of your filming session or your first month's fee is waived.",
  title="Video ads for coaches and consultants anywhere in the US",
  fonts="family=Space+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@1",
  sans='"Space Grotesk"', serif='"Instrument Serif"',
  css="""--bg:#ffffff;--soft:#f2f2ee;--ink:#0c0c0c;--muted:#585852;--line:#e3e3dc;--accent:#e4ff3a;--accent-2:#e4ff3a;--accent-ink:#0c0c0c;--hl:#0c0c0c;
  --hero-bg:#0c0c0c;--hero-ink:#ffffff;--hero-sub:#c9c9c0;--pill-bg:rgba(228,255,58,.08);--pill-line:rgba(228,255,58,.35);--pill-ink:#f2f2ea;--chip-bg:rgba(255,255,255,.06);--chip-line:rgba(255,255,255,.16);--chip-ink:#e2e2da;--frame-shadow:0 30px 90px rgba(0,0,0,.6);--radius:6px;--btn-radius:6px;--logo-filter:none;--foot-bg:#0c0c0c;--card-bg:#ffffff""",
  logo="logo-lockup-720.png", logo_w=1485, logo_h=360, hero_dark=True,
  eyebrow="For coaches and consultants doing $50K+ a month, anywhere in the US",
  h1='Nobody books a call with a coach they forgot. <span class="serif">We make you hard to forget.</span>',
  sub="We direct you on camera from LA, cut it like a film and run it as Meta ads that fill your calendar with qualified sales calls. No flights, no film crew in your living room. Watch the 4 minute video first.",
  pains_h="Why your ads get likes and no booked calls",
  pains=[
    ("You look like everyone","Selfie video, captions, a whiteboard. Your feed is full of people who say the same thing. Nobody remembers who said it first."),
    ("Leads that never book","A free PDF brings 300 emails and 2 calls. Cheap leads feel like progress until you count the sales."),
    ("Calls with the wrong people","Your calendar fills with tire kickers who can't afford the program. You spend your best hours saying no."),
  ],
  steps_h="How we fill your calendar with buyers",
  steps=[
    ("We sharpen the offer","One program, one promise, one price range. Ads that filter out the people who can't buy before they book."),
    ("We direct you remotely","We write the scripts and send you a simple setup list for light and sound. Then we direct you live over Zoom while you film on your iPhone. One session gives us a library of ads."),
    ("We edit and build the page","Our editors cut it like a film, with captions and hooks. Every click lands on a video page with a short application, so only qualified people book."),
    ("We run it and track it","Meta ads to the people who fit your buyer, anywhere in the US. Every booked call shows up next to the ad that booked it."),
  ],
  ideas_h="The kind of ads we would make with you",
  ideas_sub="Before your call we write 3 of these for your program. You keep them either way.",
  ideas=[
    ("“The advice I'd pay $10K to unlearn”","A contrarian take from your field, cut like a short documentary. Polarizes the wrong people out, pulls the right ones in."),
    ("“What actually happens on a call with me”","You walk through your sales call. Buyers book when the call stops being a mystery."),
    ("“Client story, told by the client”","A real result, recorded with the person who got it. Proof that does the selling for you."),
  ],
  about="I'm Dennis. I run City of Angels Advertising from Encino. We built my wife's coaching business with our own ads before we ever sold this to anyone. You talk to me, not an account manager.",
  apply_h="Book your call by November 20 and lock in $3,000 a month",
  faq=[
    ("I'm not in LA. Does this work for me?","Yes. That is the whole point. We direct you over Zoom, you film at home or in your office, and we handle editing, ads, funnel and tracking from LA."),
    ("Will it look cheap if I film on my phone?","No. A current iPhone with good light and a clip on mic is plenty. The difference is direction and editing, and that is our job. We tell you exactly where to sit, what to say and how to say it."),
    ("I hate being on camera.","Most of our clients said the same. We ask questions and let you talk. Nobody reads a script word for word."),
    ("What does it cost?","$3,000 a month for everything if you book your call by November 20. Your ad budget goes straight to Meta, we recommend at least $3,000 a month."),
  ],
  small="Your answers are only used to prepare your call. We never sell or share your data.",
),
}

PROOF = '<section class="proof" id="proof">\n<div class="wrap center">\n<h2>We tested it on my wife first</h2>\n<p class="lead">My wife Elena runs a coaching business. We built every ad, every video, every funnel and the tracking ourselves, with our own money. Started in 2024. Over $1.3M in revenue since.</p>\n<div class="stats"><div class="stat"><b>$1.3M+</b><span>collected since 2024, from our own ads, videos and funnels</span></div><div class="stat"><b>$45K to $65K</b><span>per VIP coaching client</span></div><div class="stat"><b>$131K</b><span>in the last 30 days, from the small products alone</span></div></div>\n<div class="pgrid">\n<div class="shot full"><picture><source type="image/webp" srcset="https://wilk1990.github.io/spl-free-session/coa/img/proof-ablefy-alltime.webp"><img src="https://wilk1990.github.io/spl-free-session/coa/img/proof-ablefy-alltime.jpg" width="1600" height="820" alt="Payment dashboard: 569,674 euros received, 1,793 payments, all time" loading="lazy" decoding="async"></picture></div>\n<div class="shot"><picture><source type="image/webp" srcset="https://wilk1990.github.io/spl-free-session/coa/img/proof-ablefy-365.webp"><img src="https://wilk1990.github.io/spl-free-session/coa/img/proof-ablefy-365.jpg" width="1600" height="875" alt="Payment dashboard, last 365 days: 435,562 euros, up 332 percent" loading="lazy" decoding="async"></picture></div>\n<div class="shot"><picture><source type="image/webp" srcset="https://wilk1990.github.io/spl-free-session/coa/img/proof-ablefy-30.webp"><img src="https://wilk1990.github.io/spl-free-session/coa/img/proof-ablefy-30.jpg" width="1600" height="840" alt="Payment dashboard, last 30 days: 121,444 euros, up 390 percent" loading="lazy" decoding="async"></picture></div>\n<div class="shot"><picture><source type="image/webp" srcset="https://wilk1990.github.io/spl-free-session/coa/img/proof-youtube-channel.webp"><img src="https://wilk1990.github.io/spl-free-session/coa/img/proof-youtube-channel.jpg" width="1600" height="781" alt="YouTube channel I AM ALL with 6,390 subscribers and 179 videos" loading="lazy" decoding="async"></picture></div>\n<div class="shot"><picture><source type="image/webp" srcset="https://wilk1990.github.io/spl-free-session/coa/img/proof-youtube-memberships.webp"><img src="https://wilk1990.github.io/spl-free-session/coa/img/proof-youtube-memberships.jpg" width="1600" height="1030" alt="YouTube Studio: 8,317 dollars in channel membership revenue in 30 days" loading="lazy" decoding="async"></picture></div>\n</div>\n<p class="cap">Screenshots from our live accounts, October 2026, German interface. The checkout dashboards only show the smaller automated products in euros (about $1.08 per euro). VIP coaching paid by invoice is not included. Our results are not a promise of yours. They depend on your offer, your market and your sales calls.</p>\n</div>\n</section>\n\n'

TEMPLATE = open(OUT / "niche.template.html", encoding="utf-8").read()

def cards(items, cls):
    return "\n".join(f'<div class="{cls}"><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>' for t, d in items)

def steps(items):
    return "\n".join(f'<li><span class="n">{i+1:02d}</span><div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></li>' for i,(t,d) in enumerate(items))

def ideas(items):
    return "\n".join(f'<div class="idea"><span class="tag">Idea {i+1}</span><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div>' for i,(t,d) in enumerate(items))

def faq(items):
    return "\n".join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q,a in items)

for slug, n in NICHES.items():
    page = TEMPLATE
    rep = {
      "{{SLUG}}": slug, "{{FONTS}}": n["fonts"], "{{SANS}}": n["sans"], "{{SERIF}}": n["serif"], "{{VARS}}": n["css"],
      "{{LOGO}}": IMG + n["logo"], "{{LOGO_W}}": str(n["logo_w"]), "{{LOGO_H}}": str(n["logo_h"]),
      "{{HERO_CLASS}}": "dark" if n["hero_dark"] else "light",
      "{{EYEBROW}}": html.escape(n["eyebrow"]), "{{H1}}": n["h1"], "{{SUB}}": html.escape(n["sub"]),
      "{{PAINS_H}}": html.escape(n["pains_h"]), "{{PAINS}}": cards(n["pains"], "pain"),
      "{{STEPS_H}}": html.escape(n["steps_h"]), "{{STEPS}}": steps(n["steps"]),
      "{{IDEAS_H}}": html.escape(n["ideas_h"]), "{{IDEAS_SUB}}": html.escape(n["ideas_sub"]), "{{IDEAS}}": ideas(n["ideas"]),
      "{{ABOUT}}": html.escape(n["about"]), "{{APPLY_H}}": html.escape(n["apply_h"]), "{{FAQ}}": faq(n["faq"]),
      "{{SMALL}}": html.escape(n["small"]), "{{WORK_H}}": html.escape(n["work_h"]), "{{WORK_SUB}}": html.escape(n["work_sub"]), "{{IMG}}": IMG, "{{PRICE}}": n.get("price","$5,000"), "{{PRICE_WHAT}}": n.get("price_what","our management"), "{{VIDEO_NOTE}}": n.get("video_note",""), "{{CTA_NOTE}}": n.get("cta_note","Five quick questions, then you pick a time. Your ads go live within 14 days of the shoot day or your first month's fee is waived."), "{{PROOF}}": PROOF if slug=="coaches" else "", "{{TITLE}}": html.escape(n["title"]),
    }
    for k, v in rep.items():
        page = page.replace(k, v)
    assert "{{" not in page, slug
    (OUT / f"{slug}.fragment.html").write_text(page, encoding="utf-8")
    print("wrote", slug, len(page))
