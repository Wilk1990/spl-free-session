#!/usr/bin/env python3
"""Builds the three audience landing pages (dentists, medspas, coaches) as GHL Custom HTML fragments.

Structure follows the framework "Regelwerk fuer High-Ticket Call Funnels auf kaltem Meta-Traffic":
1 hero (callout, outcome headline, one line, video with runtime, CTA) · 2 proof · 3 problem ·
4 three steps · 5 the call (what you get, who it is for, capacity) · 6 embedded application + P.S.
No retainer price, no deadline, no dollar value on the call, no promised number of consults.
"""
import html, pathlib

OUT = pathlib.Path(__file__).parent
IMG = "https://wilk1990.github.io/spl-free-session/coa/img/"

def card(wid, thumb, dur, label, tag, name, results, text):
    res = "".join(f"<li>{html.escape(r)}</li>" for r in results)
    return (f'<div class="wcard"><button type="button" class="film" data-w="{wid}" aria-label="Play {html.escape(label)}">'
            f'<img src="https://embed-ssl.wistia.com/deliveries/{thumb}.jpg?image_crop_resized=960x540" alt="" loading="lazy" decoding="async">'
            f'<span class="pl" aria-hidden="true"></span><span class="du">{dur}</span></button>'
            f'<span class="wtag">{html.escape(tag)}</span><h3>{html.escape(name)}</h3><ul class="res">{res}</ul><p>{html.escape(text)}</p></div>')

TANDLER = card("629ti7yiya", "880d520f3c9cf0f87b49e63a31e4ea44", "0:44", "Tandler", "Recruiting ads", "Tandler",
    ["60 applicants in 2 months", "6 open positions filled in under 4 weeks", "All 4 apprentice spots filled within 4 weeks"],
    "A manufacturer with 200+ employees needed people. We filmed the ads and ran them.")
OPBROS = card("m4gq0ahvgu", "55c2be7b6011f92209c79b7adbbdc411d90f0f3d", "0:27", "OP Bros", "Cinematic trailer", "OP Bros",
    ["Picked for our cinematic look"],
    "Two operating room nurses who turned hospital humor into a channel with over 1 billion views. They chose our cinematic style for the trailer of one of their formats.")
HAWART = card("vp09z32ku0", "38fd724ae4270ad7ca6c0ac5d192bda5e3136a28", "4:19", "HAWART", "Film, Reels and ads", "HAWART",
    ["12 hires from 37 applicants"],
    "A manufacturer with three locations. One film, Reels and the ads that ran them.")

LA_STEPS = lambda place, people: [
    (f"We film at your {place}", f"{people}, your rooms. One shoot day with cinema cameras. We direct everything."),
    ("We run the ads and build the booking page", "Meta ads to people near you. Every click lands on a page where they pick a consult time."),
    ("You meet people who are ready", "Every lead answers a few questions before they book. You see which ad booked which consult."),
]

def call_items(biz):
    return [
        (f"3 video ad ideas written for your {biz}.", "The hook, the angle and what we would film. You get them before we talk."),
        ("We walk through them together.", "You see how each idea turns into an ad that books the right people."),
        ("A straight answer.", "If we are not the right fit, we tell you on the call."),
    ]

NICHES = {
"dentists": dict(
  title="Meta video ads for LA dental practices", biz="practice",
  fonts="family=Manrope:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@1,9..144,500",
  sans='"Manrope"', serif='"Fraunces"',
  css="""--bg:#ffffff;--soft:#eef6f7;--ink:#0d2530;--muted:#4c626b;--line:#d7e6ea;--accent:#0b6e8a;--accent-2:#0b6e8a;--accent-ink:#ffffff;--hl:#0b6e8a;
  --hero-bg:linear-gradient(180deg,#f3f9fa 0%,#ffffff 100%);--hero-ink:#0d2530;--hero-sub:#40575f;--frame-shadow:0 30px 80px rgba(13,37,48,.18);--radius:14px;--btn-radius:999px;--foot-bg:#0d2530;--card-bg:#ffffff""",
  hero_dark=False,
  eyebrow="For LA dental practices doing $50K+ a month",
  h1='Fill your chairs with implant consults from cinematic video ads. <span class="serif">Without the $59 new patient special.</span>',
  sub="Watch the 4 minute video. Then claim 3 video ad ideas written for your practice.",
  cta_note="Five quick questions, then you pick a time.",
  work_h="What our work did for other businesses",
  work_sub="Different industries, same approach. Real people, real rooms, shot like a film.",
  cards=[TANDLER, OPBROS, HAWART],
  pains_h="Why most dental ads bring you the wrong patients",
  pains="A $59 new patient special brings in a $59 patient. She takes the cleaning and you never see her again. Every practice in your zip code runs the same stock smile. Nobody picks an implant dentist they have never seen.",
  steps_h="How it works in 3 steps",
  steps=LA_STEPS("practice", "Your doctor, your team"),
  guarantee="Your ads go live within 14 days of the shoot day or your first month's fee is waived.",
  who="dental practices in the LA area",
),
"medspas": dict(
  title="Meta video ads for LA med spas", biz="spa",
  fonts="family=Jost:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500",
  sans='"Jost"', serif='"Cormorant Garamond"',
  css="""--bg:#fbf7f3;--soft:#f3e9e1;--ink:#2b1f1b;--muted:#6f5d55;--line:#e8d9cd;--accent:#a8705a;--accent-2:#c79a84;--accent-ink:#ffffff;--hl:#a8705a;
  --hero-bg:radial-gradient(1200px 500px at 50% 0%,#f6e7dc 0%,#fbf7f3 70%);--hero-ink:#2b1f1b;--hero-sub:#5e4d46;--frame-shadow:0 30px 80px rgba(80,45,30,.18);--radius:4px;--btn-radius:2px;--foot-bg:#2b1f1b;--card-bg:#fffaf6""",
  hero_dark=False,
  eyebrow="For Los Angeles med spas doing $50K+ a month",
  h1='Book high value consults with cinematic video ads. <span class="serif">Without another discount special.</span>',
  sub="Watch the 4 minute video. Then claim 3 video ad ideas written for your spa.",
  cta_note="Five quick questions, then you pick a time.",
  work_h="What our work did for other businesses",
  work_sub="Different industries, same approach. Real people, real rooms, shot like a film.",
  cards=[TANDLER, OPBROS, HAWART],
  pains_h="Why discount ads keep your margins thin",
  pains="Discount tox brings people who chase the next discount. They come once and never buy the package. Fifty med spas near you post the same lips and the same stock model. People book the spa they can see and trust.",
  steps_h="How it works in 3 steps",
  steps=LA_STEPS("spa", "Your injectors"),
  guarantee="Your ads go live within 14 days of the shoot day or your first month's fee is waived.",
  who="med spas in the LA area",
),
"coaches": dict(
  title="Video ads for coaches and consultants anywhere in the US", biz="program",
  fonts="family=Space+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@1",
  sans='"Space Grotesk"', serif='"Instrument Serif"',
  css="""--bg:#ffffff;--soft:#f2f2ee;--ink:#0c0c0c;--muted:#585852;--line:#e3e3dc;--accent:#e4ff3a;--accent-2:#e4ff3a;--accent-ink:#0c0c0c;--hl:#0c0c0c;
  --hero-bg:#0c0c0c;--hero-ink:#ffffff;--hero-sub:#c9c9c0;--frame-shadow:0 30px 90px rgba(0,0,0,.6);--radius:6px;--btn-radius:6px;--foot-bg:#0c0c0c;--card-bg:#ffffff""",
  hero_dark=True,
  eyebrow="For coaches and consultants doing $50K+ a month, anywhere in the US",
  h1='Fill your calendar with qualified sales calls from video ads. <span class="serif">Without flying in a film crew.</span>',
  sub="Watch the 4 minute video. Then claim 3 video ad ideas written for your program.",
  cta_note="Five quick questions, then you pick a time. The video talks about our LA offer. For coaches anywhere in the US we film remotely.",
  work_h="What our cameras did for others",
  work_sub="Different industries, same eye for story.",
  cards=[OPBROS, TANDLER],
  pains_h="Why your ads get likes and no booked calls",
  pains="Selfie video, captions, a whiteboard. Your feed is full of coaches who say the same thing. A free PDF brings emails, not buyers. Your calendar fills with people who can't afford the program.",
  steps_h="How it works in 3 steps",
  steps=[
    ("We direct you over Zoom", "We write the scripts. You film on your iPhone at home while we direct you live. One session gives us a library of ads."),
    ("We edit, run the ads and build the page", "Our editors cut it like a film. Meta ads send the right people to a video page with a short application."),
    ("You take calls with qualified people", "Everyone answers a few questions before they book. You see which ad booked which call."),
  ],
  guarantee="Your ads go live within 14 days of your filming session or your first month's fee is waived.",
  who="coaches and consultants anywhere in the US",
),
}

PROOF = (
 '<section class="proof" id="proof">\n<div class="wrap center">\n<h2>We tested it on my wife first</h2>\n'
 '<p class="lead">My wife Elena runs a coaching business. We built every ad, every video, every funnel and the tracking ourselves, with our own money.</p>\n'
 '<div class="stats"><div class="stat"><b>$1.3M+</b><span>collected since 2024, from our own ads, videos and funnels</span></div>'
 '<div class="stat"><b>$45K to $65K</b><span>per VIP coaching client</span></div>'
 '<div class="stat"><b>$131K</b><span>in 30 days, from the small products alone</span></div></div>\n'
 f'<div class="shot"><picture><source type="image/webp" srcset="{IMG}proof-ablefy-alltime.webp"><img src="{IMG}proof-ablefy-alltime.jpg" width="1600" height="820" alt="Payment dashboard: 569,674 euros received, 1,793 payments, all time" loading="lazy" decoding="async"></picture></div>\n'
 '<p class="cap">Screenshot from our live account, October 2026, German interface. The checkout dashboard only shows the smaller automated products in euros (about $1.08 per euro). VIP coaching paid by invoice is not included. Our results are not a promise of yours. They depend on your offer, your market and your sales calls.</p>\n'
 '</div>\n</section>\n\n'
)

TEMPLATE = open(OUT / "niche.template.html", encoding="utf-8").read()

def steps(items):
    return "\n".join(f'<li><span class="n">{i+1:02d}</span><div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></li>' for i,(t,d) in enumerate(items))

def items(rows):
    return "\n".join(f"<li><b>{html.escape(a)}</b> {html.escape(b)}</li>" for a, b in rows)

for slug, n in NICHES.items():
    biz = n["biz"]
    rep = {
      "{{SLUG}}": slug, "{{TITLE}}": html.escape(n["title"]), "{{FONTS}}": n["fonts"], "{{SANS}}": n["sans"], "{{SERIF}}": n["serif"], "{{VARS}}": n["css"],
      "{{LOGO}}": IMG + "logo-lockup-720.png", "{{LOGO_W}}": "1485", "{{LOGO_H}}": "360",
      "{{HERO_CLASS}}": "dark" if n["hero_dark"] else "light",
      "{{EYEBROW}}": html.escape(n["eyebrow"]), "{{H1}}": n["h1"], "{{SUB}}": html.escape(n["sub"]), "{{CTA_NOTE}}": html.escape(n["cta_note"]),
      "{{PROOF}}": PROOF if slug == "coaches" else "",
      "{{WORK_H}}": html.escape(n["work_h"]), "{{WORK_SUB}}": html.escape(n["work_sub"]), "{{CARDS}}": "\n".join(n["cards"]), "{{WCOLS}}": str(len(n["cards"])),
      "{{PAINS_H}}": html.escape(n["pains_h"]), "{{PAINS}}": html.escape(n["pains"]),
      "{{STEPS_H}}": html.escape(n["steps_h"]), "{{STEPS}}": steps(n["steps"]), "{{GUARANTEE}}": html.escape(n["guarantee"]),
      "{{CALL_H}}": "Your free Ad Strategy Session",
      "{{CALL_SUB}}": "30 minutes on video with Dennis. You leave with something you can use, even if we never work together.",
      "{{CALL_ITEMS}}": items(call_items(biz)),
      "{{CALL_FIT}}": f"<b>Who this is for:</b> {html.escape(n['who'])} doing $50K+ a month, with a separate budget for ads. If that is not you yet, this call will not help you. <b>We take two calls a day</b> because we write your 3 ideas before each one.",
      "{{PS}}": f"<b>P.S.</b> You get 3 video ad ideas written for your {biz} before we talk. They are yours to keep either way. We only take two calls a day, so pick your time now.",
    }
    page = TEMPLATE
    for k, v in rep.items():
        page = page.replace(k, v)
    assert "{{" not in page.replace("{{{", ""), slug
    for bad in ("November", "$5,000", "$3,000", "—", "–"):
        assert bad not in page, (slug, bad)
    (OUT / f"{slug}.fragment.html").write_text(page, encoding="utf-8")
    print("wrote", slug, len(page))
