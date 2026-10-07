"""Static site generator for Zenvora Digital (performance marketing agency). Run: python build.py"""
import os
import glob

OUT = os.path.dirname(os.path.abspath(__file__))
BRAND = "Zenvora Digital"

SERVICES = [
    dict(slug="google-ads", icon="🔍", name="Google Ads Management",
         short="Show up when customers are searching and turn high-intent clicks into leads and sales.",
         intro="People who search on Google already want what you sell. We build and manage Search, Performance Max, Shopping, Display and YouTube campaigns that put your offer in front of them at the right moment and the right cost.",
         points=["Account audits and conversion tracking setup", "Search, Shopping and Performance Max campaigns", "Keyword research and negative keyword control", "Ad copy testing and ad extensions", "Smart bidding and budget optimisation", "Weekly reporting with clear next steps"],
         tech=["Google Ads", "Google Analytics 4", "Tag Manager", "Merchant Center", "YouTube Ads", "Looker Studio"],
         kpis=["Cost per lead", "Conversion rate", "ROAS", "Impression share", "Quality Score", "Cost per acquisition"],
         faq=[("How fast can my Google Ads campaigns go live?", "After the audit and tracking setup, most campaigns launch within 5 to 10 working days. We start with a focused test budget and scale what works."),
              ("Do I own my Google Ads account?", "Yes. The account is always in your name. We are given access to manage it, and you can see everything at any time."),
              ("How do you decide the keywords to bid on?", "We start from your services and customer questions, then expand with search term data. Irrelevant searches are blocked early with negative keywords to protect your budget.")]),
    dict(slug="meta-ads", icon="📣", name="Meta Ads (Facebook & Instagram)",
         short="Reach the right audience on Facebook and Instagram with creative that stops the scroll.",
         intro="Meta's platforms let you reach people before they start searching. We plan the audiences, produce the creative and run the campaigns that generate leads, enquiries and sales across Facebook and Instagram.",
         points=["Audience research, lookalikes and retargeting", "Lead form and conversion campaigns", "Ad creative, video and copy testing", "Pixel and Conversions API setup", "Instagram Stories, Reels and feed placements", "Creative refresh cycles to fight ad fatigue"],
         tech=["Meta Ads Manager", "Meta Pixel", "Conversions API", "Instagram Ads", "Canva", "CapCut"],
         kpis=["Cost per lead", "Click-through rate", "Frequency", "Cost per purchase", "ROAS", "Lead quality score"],
         faq=[("Should I advertise on Meta or Google first?", "Google captures people who are already searching. Meta creates demand and reaches people earlier. Many businesses use both, and we can recommend the order based on your offer and budget."),
              ("Do you create the ad creative as well?", "Yes. We write the copy and produce static, carousel and short video ads, and we test several versions to find what performs."),
              ("Why do my Meta ads stop working after a while?", "Audiences get tired of seeing the same ad. We watch frequency and performance and refresh creative on a regular schedule.")]),
    dict(slug="ppc-management", icon="🎯", name="PPC Campaign Management",
         short="Full-funnel pay-per-click strategy across search, social and display, managed for profit.",
         intro="PPC works best when every channel has a clear job. We plan, launch and optimise paid campaigns across platforms, keep a close eye on your budget and report on the numbers that actually matter to your business.",
         points=["Multi-channel PPC strategy and budgeting", "Search, social, display and remarketing", "A/B testing of ads, audiences and offers", "Bid and budget optimisation", "Competitor and market analysis", "Transparent dashboards and monthly strategy calls"],
         tech=["Google Ads", "Meta Ads", "LinkedIn Ads", "TikTok Ads", "Microsoft Ads", "Looker Studio"],
         kpis=["Return on ad spend", "Cost per acquisition", "Click-through rate", "Conversion rate", "Customer lifetime value", "Wasted spend"],
         faq=[("What ad budget do I need?", "It depends on your market and goal. We work backwards from your target cost per lead or sale and the volume you want, then recommend a budget and a test plan."),
              ("How soon will I see results?", "You will see data in the first couple of weeks. Most accounts need a few weeks of learning and a couple of months of optimisation to reach stable results. We never guarantee specific numbers."),
              ("How do you report performance?", "You get a live dashboard, a weekly summary and a monthly call where we explain what changed, what we learned and what we will do next.")]),
    dict(slug="lead-generation", icon="🧲", name="Lead Generation",
         short="A steady flow of qualified enquiries, booked calls and appointments for your sales team.",
         intro="More leads only help if they are the right leads. We build complete lead generation systems, from the ad and the landing page to the form, follow-up and tracking, so your team spends time on people who are ready to buy.",
         points=["Lead funnels built around a clear offer", "Lead forms, landing pages and call tracking", "Lead qualification questions and scoring", "CRM and email or WhatsApp follow-up automation", "Cost per qualified lead tracking", "Feedback loop with your sales team to improve quality"],
         tech=["Google Ads", "Meta Lead Ads", "HubSpot", "Zapier", "WhatsApp Business", "CallRail", "Google Sheets"],
         kpis=["Cost per lead", "Cost per qualified lead", "Lead-to-sale rate", "Speed to first contact", "Booked calls", "Pipeline value"],
         faq=[("How do you make sure leads are good quality?", "We add qualifying questions to forms, target carefully and ask your sales team for feedback on every batch. We then optimise for qualified leads, not just the cheapest ones."),
              ("Can leads go straight into my CRM?", "Yes. We connect your ads and forms to your CRM, email or WhatsApp so every lead is captured and followed up quickly."),
              ("What industries do you generate leads for?", "We work with local service businesses, real estate, education, healthcare, finance and B2B companies, among others.")]),
    dict(slug="landing-pages-cro", icon="🚀", name="Landing Pages & CRO",
         short="High-converting landing pages and tests that make every ad click work harder.",
         intro="Great ads can still lose money on a weak page. We design fast, focused landing pages and run conversion rate optimisation so more of your paid traffic turns into leads and customers.",
         points=["Landing pages designed for a single goal", "Fast loading, mobile-first layouts", "Persuasive copy and clear calls to action", "A/B testing of headlines, offers and forms", "Heatmaps and session recordings analysis", "Tracking and thank-you page setup"],
         tech=["Webflow", "WordPress", "Next.js", "Hotjar", "VWO", "Figma"],
         kpis=["Conversion rate", "Bounce rate", "Page speed", "Form completion rate", "Cost per lead", "Revenue per visitor"],
         faq=[("Why do I need a separate landing page for ads?", "A page built for one offer and one action converts better than a general website page, which gives visitors many other things to do."),
              ("How long does a landing page take?", "A new landing page typically takes 1 to 2 weeks including copy, design, build and tracking."),
              ("Do you test the pages after launch?", "Yes. We run structured A/B tests and use behaviour data to keep improving the conversion rate.")]),
]

POSTS = [
    dict(slug="google-ads-vs-meta-ads", t="t1", e="⚖️", title="Google Ads vs Meta Ads: Where Should You Spend First?", date="September 22, 2026", cat="PPC Strategy",
         desc="Search and social solve different problems. Here is how to choose the right starting point for your budget.",
         body=["Google Ads and Meta Ads are both powerful, but they work in very different ways. Google captures demand: people type what they need and your ad appears. Meta creates demand: your ad reaches people who were not searching yet but fit your ideal customer.",
               "If your customers already search for what you sell, such as an emergency plumber or an accountant, start with Google Search. Intent is high and leads tend to be ready to talk. If your product is visual, new or impulse-driven, Meta is often the better starting point.",
               "Most growing businesses end up using both. Meta introduces your brand and fills the top of the funnel, while Google captures people who are ready to act, and retargeting brings back those who did not convert the first time.",
               "Whichever you choose, set up conversion tracking first. Without clean data, neither platform can optimise toward the results you actually want."]),
    dict(slug="lower-cost-per-lead", t="t2", e="📉", title="7 Ways to Lower Your Cost Per Lead", date="September 5, 2026", cat="Lead Generation",
         desc="Practical changes that reduce wasted spend and improve lead quality without cutting your budget.",
         body=["A high cost per lead usually comes from a handful of fixable problems. Start by looking at where the money is going before you change anything.",
               "First, tighten your targeting: add negative keywords on Google and exclude poor audiences on Meta. Second, test your offer, because a clearer promise often beats a clever ad. Third, improve the landing page: faster loading, shorter forms and one clear action.",
               "Fourth, test new creative regularly. Fifth, use conversion-based bidding once you have enough data. Sixth, follow up quickly, since leads contacted within minutes are far more likely to respond. Seventh, track cost per qualified lead, not just cost per lead.",
               "Make one change at a time and give each test enough data to be meaningful. Small, steady improvements compound quickly."]),
    dict(slug="landing-page-checklist", t="t3", e="✅", title="The Landing Page Checklist for Higher Conversions", date="August 18, 2026", cat="Conversion Optimisation",
         desc="Before you send more traffic, make sure your landing page is doing its job.",
         body=["Sending paid traffic to a weak page is the fastest way to waste ad spend. Before you scale a campaign, check the basics on your landing page.",
               "The headline should match the ad and state the main benefit in plain words. The offer should be clear and the main button should be visible without scrolling. Keep forms as short as you can while still qualifying the lead.",
               "Add proof near the call to action: reviews, logos or short case results. Make sure the page loads quickly on mobile, since most ad clicks come from phones. Finally, confirm your tracking fires correctly on the thank-you page.",
               "Once the basics are right, run A/B tests on one element at a time, such as the headline or the form, and let the data guide your next change."]),
]

NAV = [("index.html", "Home"), ("about.html", "About Us"), ("services.html", "Services"), ("blog.html", "Blog"), ("contact.html", "Contact")]


def head(title, desc, active, depth=""):
    links = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {BRAND}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0b1020">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css"><link rel="stylesheet" href="assets/extras.css"><link rel="stylesheet" href="assets/extras2.css"><link rel="stylesheet" href="assets/extras3.css"><link rel="stylesheet" href="assets/extras4.css"><link rel="stylesheet" href="assets/extras5.css"><link rel="stylesheet" href="assets/extras6.css"><link rel="stylesheet" href="assets/extras9.css">
</head><body>
<div class="progress"></div>
<header class="nav"><div class="wrap">
<a href="index.html" class="logo"><i>Z</i>Zenvora</a>
<button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
<nav class="menu">{links}<a href="contact.html" class="btn btn-primary">Free Audit</a></nav>
</div></header>
"""


def foot():
    svc = "".join(f'<li><a href="services-{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f"""
<footer><div class="wrap">
<div class="fgrid">
<div><a href="index.html" class="logo"><i>Z</i>Zenvora</a>
<p>A performance marketing agency specialising in Google Ads, Meta Ads, PPC and lead generation for ambitious businesses.</p>
<div class="soc"><a href="#" aria-label="LinkedIn">in</a><a href="#" aria-label="Facebook">f</a><a href="#" aria-label="Instagram">ig</a><a href="#" aria-label="X">x</a></div></div>
<div><h4>Company</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About Us</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h4>Services</h4><ul>{svc}</ul></div>
<div><h4>Get in touch</h4><ul><li>hello@zenvora.example</li><li>+1 (555) 014-2290</li><li>221 Market Street, Suite 400<br>Austin, TX 78701</li></ul></div>
</div>
<div class="copy"><span>© 2026 {BRAND}. All rights reserved.</span><span><a href="privacy-policy.html">Privacy Policy</a> &nbsp;·&nbsp; <a href="terms-conditions.html">Terms &amp; Conditions</a></span></div>
</div></footer>
<button class="top" aria-label="Back to top">↑</button>
<script src="assets/main.js"></script><script src="assets/extras.js"></script><script src="assets/extras4.js"></script><script src="assets/extras5.js"></script><script src="assets/extras6.js"></script><script type="module" src="assets/extras8.js"></script>
</body></html>"""


def page_hero(title, sub, crumb):
    return f"""<div class="page-hero"><div class="wrap rv">
<div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
<h1>{title}</h1><p>{sub}</p></div></div>"""


def cta():
    return """<section><div class="wrap"><div class="cta rv">
<h2>Ready to get more leads?</h2>
<p>Get a free audit of your ad account and a clear plan to lower your cost per lead. We reply within one business day.</p>
<a href="contact.html" class="btn">Get Your Free Audit →</a></div></div></section>"""


def svc_cards():
    return "".join(f"""<div class="svc rv"><div class="ico">{s['icon']}</div><h3>{s['name']}</h3><p>{s['short']}</p>
<a class="more" href="services-{s['slug']}.html">Learn more →</a></div>""" for s in SERVICES)


def post_cards(posts):
    return "".join(f"""<article class="post rv"><div class="thumb {p['t']}">{p['e']}</div><div class="body">
<div class="meta">{p['date']} · {p['cat']}</div><h3>{p['title']}</h3><p>{p['desc']}</p>
<a class="more" href="blog-{p['slug']}.html">Read article →</a></div></article>""" for p in posts)


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)


# remove pages from the previous version of the site
for old in glob.glob(os.path.join(OUT, "services-*.html")) + glob.glob(os.path.join(OUT, "blog-*.html")):
    os.remove(old)

MARQ = "".join(f"<span>{x}</span>" for x in ["Google Ads", "Meta Ads", "Instagram", "Facebook", "YouTube", "Google Analytics", "Tag Manager", "LinkedIn Ads", "TikTok Ads", "HubSpot", "Zapier", "Looker Studio"])

# sample case studies: replace with real client results before publishing
WORKS = [("🏠", "Lumio Realty", "Real estate · Meta Lead Ads", "Lower cost per lead and more booked viewings", "linear-gradient(135deg,#5b4bff,#8f7bff)"),
         ("🛒", "Orbitly Store", "E-commerce · Google Shopping", "Stronger ROAS from Shopping and remarketing", "linear-gradient(135deg,#00a8b8,#37e0cf)"),
         ("🦷", "Kestrel Dental", "Healthcare · Google Search", "More appointment requests from local search", "linear-gradient(135deg,#ff6b9a,#ffa36b)")]
WORKS_HTML = "".join(f'<div class="work rv zoom" style="background:{g}"><div class="big">{i}</div><small>{c}</small><h3>{n}</h3><small>{r}</small></div>' for i, n, c, r, g in WORKS)

HOME_FAQ = [("How much should I spend on ads?", "It depends on your market and what a lead or sale is worth. We work backwards from your target cost per lead and the volume you want, then recommend a budget and a clear test plan."),
            ("Should I use Google Ads or Meta Ads?", "Google Ads reaches people who are already searching for what you sell. Meta Ads reaches people earlier, based on interests and behaviour. Many businesses use both, and we will recommend the right starting point after a short audit."),
            ("How soon will I see results?", "You will see data within the first couple of weeks. Stable, optimised results usually take a couple of months. We do not promise specific numbers, but we do promise honest reporting."),
            ("Who owns the ad accounts?", "You do. Your ad accounts, pixels and data stay in your name and we are given access to manage them."),
            ("How do you report performance?", "You get a live dashboard, a weekly summary and a monthly strategy call covering results, learnings and next steps.")]
FAQ_HTML = "".join(f"<details class='rv'><summary>{q}</summary><p>{a}</p></details>" for q, a in HOME_FAQ)

# ---------- HOME ----------
home = head("Google Ads, Meta Ads, PPC & Lead Generation", "Zenvora Digital is a performance marketing agency specialising in Google Ads, Meta Ads, PPC and lead generation.", "index.html") + f"""
<section class="hero"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><canvas id="particles"></canvas><div class="wrap hero-grid">
<div><span class="eyebrow">Performance marketing agency</span>
<h1>We turn ad spend into <span class="grad-text typed" data-words='["qualified leads","booked calls","new customers","real growth"]'>qualified leads</span></h1>
<p class="lead">Google Ads, Meta Ads, PPC and lead generation, managed by specialists who focus on one thing: more of the right customers at a lower cost.</p>
<div class="hero-btns"><a href="contact.html" class="btn btn-primary">Get Free Ad Audit →</a><a href="services.html" class="btn btn-ghost">Our Services</a></div></div>
<div class="hero-visual">
<div class="stage" id="stage">
<div class="layer swatch" data-depth="20"><div class="in"><i style="background:#4285f4"></i><i style="background:#ea4335"></i><i style="background:#fbbc05"></i><i style="background:#34a853"></i><i style="background:#0866ff"></i></div></div>
<div class="layer dashw" data-depth="12"><div class="in">
<div class="dh"><i></i><i></i><i></i><span>Campaign performance</span></div>
<div class="kpis"><div><small>Leads this month</small><b>1,284</b></div><div><small>Cost per lead</small><b class="up">−31%</b></div></div>
<svg class="chart" viewBox="0 0 300 100" preserveAspectRatio="none"><defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#5b4bff"/><stop offset="1" stop-color="#00c2d1"/></linearGradient><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00c2d1" stop-opacity=".35"/><stop offset="1" stop-color="#00c2d1" stop-opacity="0"/></linearGradient></defs>
<path class="area" d="M0 80 C30 70 50 40 80 50 S130 75 160 45 S220 20 250 30 S290 10 300 8 L300 100 L0 100Z" fill="url(#ar)"/>
<path class="line" d="M0 80 C30 70 50 40 80 50 S130 75 160 45 S220 20 250 30 S290 10 300 8" fill="none" stroke="url(#lg)" stroke-width="3" stroke-linecap="round"/></svg>
<div class="bars"><i style="--h:45%;--d:1"></i><i style="--h:70%;--d:2"></i><i style="--h:55%;--d:3"></i><i style="--h:90%;--d:4"></i><i style="--h:65%;--d:5"></i><i style="--h:100%;--d:6"></i><i style="--h:80%;--d:7"></i></div>
</div></div>
<div class="layer phoneh" data-depth="28"><div class="in"><div class="pscreen">
<div class="ph"><i></i><span>New leads</span></div>
<div class="row" style="--c:#4285f4"><u></u><s></s></div><div class="row" style="--c:#0866ff"><u></u><s></s></div><div class="row" style="--c:#34a853"><u></u><s></s></div><div class="row" style="--c:#ffb020"><u></u><s></s></div>
<div class="pbtn"></div></div></div></div>
<div class="layer toast tst1" data-depth="42"><div class="in"><em>🎯</em><div><b>New lead</b><small>From Meta Lead Ads</small></div></div></div>
<div class="layer toast tst2" data-depth="36"><div class="in"><em>📈</em><div><b>ROAS is up</b><small>Google Ads campaign</small></div></div></div>
</div>
</div></div></section>

<div class="logos"><div class="wrap"><small style="font-weight:600;color:var(--muted);letter-spacing:.08em;text-transform:uppercase;font-size:.78rem">Expertise across the platforms that drive growth</small>
<div class="marq"><div class="track">{MARQ}{MARQ}</div></div></div></div>

<section><div class="wrap split">
<div class="art rv"><div class="mini m1">🎯 Lead-focused</div><div class="badge"><b>8+</b>Years running paid ads</div><div class="mini m2">📊 Data-driven</div></div>
<div class="rv"><span class="eyebrow">About us</span><h2>Paid advertising built around your return</h2>
<p>Zenvora Digital is a team of paid media specialists, creatives and analysts. We plan, launch and optimise Google Ads and Meta Ads campaigns, and we judge our work by one measure: the leads and sales it brings you.</p>
<ul class="checks"><li>Specialists in search, social and lead generation</li><li>Transparent reporting you can check any time</li><li>You own your ad accounts and your data</li></ul>
<br><a href="about.html" class="btn btn-dark">More about us →</a></div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">What we do</span><h2>Services built to generate leads</h2><p>Everything you need to find, win and keep customers through paid advertising.</p></div>
<div class="grid g3">{svc_cards()}</div></div></section>

<section class="stats"><div class="wrap grid g4">
<div><b data-count="250" data-suffix="+">0</b><span>Campaigns launched</span></div>
<div><b data-count="120" data-suffix="+">0</b><span>Brands served</span></div>
<div><b data-count="40" data-suffix="%">0</b><span>Avg. lower cost per lead</span></div>
<div><b data-count="95" data-suffix="%">0</b><span>Client retention</span></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">How we work</span><h2>A simple, proven process</h2><p>Clear steps from the first audit to scaling what works, with reporting at every stage.</p></div>
<div class="grid g4">
<div class="step rv"><div class="n">01</div><h3>Audit &amp; strategy</h3><p>We review your accounts, set up tracking and agree goals, audiences and budget.</p></div>
<div class="step rv"><div class="n">02</div><h3>Launch &amp; test</h3><p>We launch focused campaigns and test ads, audiences and offers against each other.</p></div>
<div class="step rv"><div class="n">03</div><h3>Optimise</h3><p>We cut waste, improve lead quality and shift budget to what performs.</p></div>
<div class="step rv"><div class="n">04</div><h3>Scale &amp; report</h3><p>We scale winning campaigns and share clear reports and next steps.</p></div></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our work</span><h2>Sample campaign results</h2><p>The kinds of campaigns we plan and run for our clients across different industries.</p></div>
<div class="grid g3">{WORKS_HTML}</div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Testimonials</span><h2>What our clients say</h2></div>
<div class="grid g3">
<div class="quote rv"><div class="stars">★★★★★</div><p>"Our cost per lead dropped within two months and the leads we get now are actually ready to talk. Reporting is clear and honest."</p><div class="who"><i>SM</i><div><b>Sarah Mitchell</b><small>Marketing Director, Lumio</small></div></div></div>
<div class="quote rv"><div class="stars">★★★★★</div><p>"They fixed our tracking, rebuilt our campaigns and finally showed us which ads bring sales. We now know where every dollar goes."</p><div class="who"><i>DK</i><div><b>Daniel Kim</b><small>Founder, Orbitly</small></div></div></div>
<div class="quote rv"><div class="stars">★★★★★</div><p>"Our appointment bookings from Google and Instagram have become steady and predictable. The team responds quickly and always has a plan."</p><div class="who"><i>AR</i><div><b>Ana Rodriguez</b><small>Practice Manager, Kestrel</small></div></div></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">From the blog</span><h2>Latest insights</h2></div>
<div class="grid g3">{post_cards(POSTS)}</div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">FAQ</span><h2>Questions we often hear</h2></div>
<div class="faqs">{FAQ_HTML}</div></div></section>
{cta()}
""" + foot()
write("index.html", home)

# ---------- ABOUT ----------
about = head("About Us", "Learn about Zenvora Digital, our mission, values and team.", "about.html") + page_hero("About Us", "We are a performance marketing agency on a mission to turn ad budgets into measurable growth.", "About Us") + f"""
<section><div class="wrap split">
<div class="rv"><span class="eyebrow">Our story</span><h2>Built by marketers, driven by results</h2>
<p>Zenvora started in 2018 when a small group of paid media specialists got tired of agencies that reported clicks instead of customers. We set out to build an agency that is accountable for leads and sales.</p>
<p>Today we manage Google Ads, Meta Ads and lead generation campaigns for businesses across 12 countries. We stay close to the numbers, test constantly and share what we learn with our clients.</p>
<ul class="checks"><li>Founded in 2018, remote-first team</li><li>250+ campaigns launched</li><li>Specialists in search, social and lead generation</li></ul></div>
<div class="art rv"><div class="mini m1">🌍 12 countries</div><div class="badge"><b>25</b>Marketing specialists</div><div class="mini m2">⭐ 4.9 client rating</div></div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="grid g2">
<div class="svc rv"><div class="ico">🎯</div><h3>Our mission</h3><p>To help businesses grow through paid advertising that is transparent, accountable and tied to real revenue.</p></div>
<div class="svc rv"><div class="ico">🔭</div><h3>Our vision</h3><p>To be the most trusted performance marketing partner for ambitious companies, known for honest reporting and lasting results.</p></div></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our values</span><h2>What guides us</h2></div>
<div class="grid g4">
<div class="step rv"><div class="n">01</div><h3>Results first</h3><p>We measure ourselves by leads, sales and return, not vanity metrics.</p></div>
<div class="step rv"><div class="n">02</div><h3>Honesty</h3><p>Clear numbers, plain language and no hidden fees or surprises.</p></div>
<div class="step rv"><div class="n">03</div><h3>Testing</h3><p>We test ads, audiences and offers constantly and let the data decide.</p></div>
<div class="step rv"><div class="n">04</div><h3>Partnership</h3><p>We work as an extension of your team and share what we learn.</p></div></div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our journey</span><h2>How we got here</h2></div>
<div class="timeline">
<div class="tl rv left"><b>2018</b><h3>Zenvora is founded</h3><p>We start by managing Google Ads for local service businesses.</p></div>
<div class="tl rv left"><b>2020</b><h3>Paid social team launches</h3><p>We add Meta Ads specialists and creative production for Facebook and Instagram.</p></div>
<div class="tl rv left"><b>2022</b><h3>Lead generation systems</h3><p>We build funnels with landing pages, CRM integrations and follow-up automation.</p></div>
<div class="tl rv left"><b>2024</b><h3>Serving 12 countries</h3><p>The team grows to 25 specialists working across many industries.</p></div>
<div class="tl rv left"><b>2026</b><h3>250+ campaigns launched</h3><p>Today we partner with brands on long-term, full-funnel paid growth.</p></div>
</div></div></section>

<section class="stats"><div class="wrap grid g4">
<div><b data-count="250" data-suffix="+">0</b><span>Campaigns launched</span></div>
<div><b data-count="120" data-suffix="+">0</b><span>Brands served</span></div>
<div><b data-count="25" data-suffix="">0</b><span>Specialists on the team</span></div>
<div><b data-count="8" data-suffix="+">0</b><span>Years in business</span></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Leadership</span><h2>Meet the team</h2></div>
<div class="grid g3">
<div class="quote rv"><div class="who"><i>JH</i><div><b>James Harlow</b><small>Founder &amp; CEO</small></div></div><p style="margin-top:18px">Paid media strategist who leads the agency and works directly with our biggest accounts.</p></div>
<div class="quote rv"><div class="who"><i>PN</i><div><b>Priya Nair</b><small>Head of Paid Social</small></div></div><p style="margin-top:18px">Leads Meta Ads strategy and creative testing across Facebook and Instagram.</p></div>
<div class="quote rv"><div class="who"><i>OB</i><div><b>Omar Bashir</b><small>Head of Search &amp; Analytics</small></div></div><p style="margin-top:18px">Oversees Google Ads, tracking and reporting so every decision is backed by data.</p></div></div></div></section>
{cta()}
""" + foot()
write("about.html", about)

# ---------- SERVICES ----------
VISUALS = {
    "google-ads": '<div class="mock serp"><div class="sbar"><span>🔍</span> emergency plumber near me</div><div class="ad"><small><b>Ad</b> · example-plumbing.com</small><h5>24/7 Emergency Plumber – Fast Response</h5><p>Call now for a free quote. Licensed and insured.</p></div><div class="res"></div><div class="res short"></div></div>',
    "meta-ads": '<div class="mock phone"><div class="notch"></div><div class="ps"><div class="av"></div><div class="l1"></div><div class="l2"></div><div class="card adimg"></div><div class="cta-pill"></div><div class="nav"><i></i><i></i><i></i><i></i></div></div></div>',
    "ppc-management": '<div class="mock browser"><div class="bt"><i></i><i></i><i></i><span>ads.zenvora.io</span></div><div class="bb"><div class="kp"><div><small>Clicks</small><b>12.4K</b></div><div><small>CPA</small><b>$18</b></div><div><small>ROAS</small><b>4.8x</b></div></div><div class="minibars"><i style="--h:40%"></i><i style="--h:62%"></i><i style="--h:50%"></i><i style="--h:80%"></i><i style="--h:70%"></i><i style="--h:100%"></i></div></div></div>',
    "lead-generation": '<div class="mock funnel"><div class="fu f1">Ad clicks</div><div class="fu f2">Leads</div><div class="fu f3">Qualified</div><div class="fu f4">Customers</div></div>',
    "landing-pages-cro": '<div class="mock browser"><div class="bt"><i></i><i></i><i></i><span>offer.yoursite.com</span></div><div class="bb"><div class="l1"></div><div class="l2"></div><div class="cols"><div></div><div></div><div></div></div><div class="l3"></div></div></div>',
}

rows = ""
for i, s in enumerate(SERVICES):
    pts = "".join(f"<li>{p}</li>" for p in s["points"][:4])
    tags = "".join(f"<span>{t}</span>" for t in s["tech"][:5])
    flip = " flip" if i % 2 else ""
    rows += f"""<div class="srow{flip}">
<div class="stext rv {'right' if i % 2 else 'left'}"><div class="snum">{i + 1:02d}</div><h2>{s['name']}</h2><p class="sint">{s['intro']}</p>
<ul class="checks">{pts}</ul><div class="tags">{tags}</div>
<a href="services-{s['slug']}.html" class="btn btn-dark" style="margin-top:26px">Explore {s['name'].split(' (')[0]} →</a></div>
<div class="svis rv zoom">{VISUALS[s['slug']]}</div></div>"""

INDUSTRIES = [("🏠", "Real Estate"), ("🛍️", "E-commerce"), ("🦷", "Healthcare & Dental"), ("🎓", "Education"), ("🔧", "Home Services"), ("💳", "Finance & Insurance"), ("💻", "SaaS & B2B"), ("✈️", "Travel & Hospitality")]
ind = "".join(f'<div class="ind rv"><span>{e}</span><b>{n}</b></div>' for e, n in INDUSTRIES)

services = head("Our Services", "Google Ads, Meta Ads, PPC management, lead generation and landing page optimisation.", "services.html") + page_hero("Our Services", "Google Ads, Meta Ads, PPC and lead generation, managed by specialists who focus on your return.", "Services") + f"""
<section class="sv-intro"><div class="wrap"><div class="intro-grid">
<div class="rv"><span class="eyebrow">What we do</span><h2>One partner for paid growth</h2></div>
<div class="rv"><p>We help businesses find customers through paid advertising. Our team covers strategy, tracking, creative, campaign management and the landing pages that turn clicks into leads, so every part of the funnel works together.</p>
<div class="mini-stats"><div><b data-count="250" data-suffix="+">0</b><span>Campaigns</span></div><div><b data-count="12" data-suffix="">0</b><span>Countries</span></div><div><b data-count="95" data-suffix="%">0</b><span>Retention</span></div></div></div>
</div></div></section>

<section class="sv-rows"><div class="wrap">{rows}</div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our approach</span><h2>From audit to scale</h2><p>The same clear process on every account, so you always know what happens next.</p></div>
<div class="flow">
<div class="fl rv"><div class="fn">1</div><h3>Audit</h3><p>Review accounts, tracking, offers and competitors.</p></div>
<div class="fl rv"><div class="fn">2</div><h3>Strategy</h3><p>Set goals, target cost per lead, audiences and budget.</p></div>
<div class="fl rv"><div class="fn">3</div><h3>Launch</h3><p>Build campaigns, creative and landing pages, then go live.</p></div>
<div class="fl rv"><div class="fn">4</div><h3>Optimise</h3><p>Test, cut waste and improve lead quality every week.</p></div>
<div class="fl rv"><div class="fn">5</div><h3>Scale</h3><p>Increase budget on what works and report on results.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Industries</span><h2>Experience across sectors</h2><p>We bring lessons from many industries to every new account.</p></div>
<div class="ind-grid">{ind}</div></div></section>

<section class="sv-why"><div class="wrap split">
<div class="rv"><span class="eyebrow">Why Zenvora</span><h2>Built on trust and clear numbers</h2>
<p>Our clients stay with us because they always know what their money is doing.</p>
<ul class="checks"><li>Specialists in Google, Meta and lead generation</li><li>You own your ad accounts and data</li><li>Conversion tracking set up before spend scales</li><li>Weekly updates and a monthly strategy call</li><li>Focus on cost per qualified lead, not vanity metrics</li></ul></div>
<div class="why-cards rv">
<div class="wc"><b>24h</b><span>Average response time</span></div>
<div class="wc"><b>Weekly</b><span>Performance updates</span></div>
<div class="wc"><b>100%</b><span>Account ownership is yours</span></div>
<div class="wc"><b>Monthly</b><span>Strategy calls</span></div>
</div></div></section>
{cta()}
""" + foot()
write("services.html", services)

for s in SERVICES:
    others = "".join(f'<li><a href="services-{o["slug"]}.html" class="{"on" if o is s else ""}">{o["icon"]} {o["name"]}</a></li>' for o in SERVICES)
    pts = "".join(f"<li>{p}</li>" for p in s["points"])
    tags = "".join(f"<span>{t}</span>" for t in s["tech"])
    kpis = "".join(f"<span>{k}</span>" for k in s["kpis"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faq"])
    html = head(s["name"], s["short"], "services.html") + page_hero(s["name"], s["short"], f'<a href="services.html">Services</a> / {s["name"]}') + f"""
<section><div class="wrap detail">
<div class="rv"><h2>Overview</h2><p>{s['intro']}</p>
<h2>What's included</h2><ul class="checks">{pts}</ul>
<h2>How it works</h2><div class="grid g2" style="margin-bottom:10px">
<div class="step"><div class="n">01</div><h3>Audit &amp; setup</h3><p>Goals, tracking and a clear plan.</p></div>
<div class="step"><div class="n">02</div><h3>Launch &amp; test</h3><p>Focused campaigns with structured tests.</p></div>
<div class="step"><div class="n">03</div><h3>Optimise</h3><p>Cut waste and improve lead quality.</p></div>
<div class="step"><div class="n">04</div><h3>Scale &amp; report</h3><p>Grow what works and share the results.</p></div></div>
<h2>Frequently asked questions</h2>{faq}</div>
<aside class="side">
<div class="box"><h4>All services</h4><ul>{others}</ul></div>
<div class="box"><h4>Platforms &amp; tools</h4><div class="tags">{tags}</div></div>
<div class="box"><h4>KPIs we track</h4><div class="tags">{kpis}</div></div>
<div class="box"><h4>Want better results?</h4><p style="margin-bottom:16px;color:var(--muted)">Get a free audit of your ad account.</p><a href="contact.html" class="btn btn-primary">Get Free Audit →</a></div>
</aside></div></section>
""" + foot()
    write(f"services-{s['slug']}.html", html)

# ---------- BLOG ----------
blog = head("Blog", "Insights on Google Ads, Meta Ads, PPC and lead generation.", "blog.html") + page_hero("Our Blog", "Practical articles on paid advertising and lead generation.", "Blog") + f"""
<section><div class="wrap"><div class="grid g3">{post_cards(POSTS)}</div></div></section>
""" + foot()
write("blog.html", blog)

for p in POSTS:
    body = "".join(f"<p>{x}</p>" for x in p["body"])
    html = head(p["title"], p["desc"], "blog.html") + page_hero(p["title"], f"{p['date']} · {p['cat']}", '<a href="blog.html">Blog</a> / Article') + f"""
<section><div class="wrap legal rv"><div class="thumb {p['t']}" style="border-radius:20px;height:260px;margin-bottom:30px">{p['e']}</div>
{body}<br><a href="blog.html" class="btn btn-dark">← Back to blog</a></div></section>
""" + foot()
    write(f"blog-{p['slug']}.html", html)

# ---------- CONTACT ----------
opts = "".join(f"<option>{s['name']}</option>" for s in SERVICES) + "<option>Not sure yet</option>"
contact = head("Contact Us", "Get a free ad account audit from Zenvora Digital.", "contact.html") + page_hero("Get Your Free Audit", "Tell us about your business and goals. We reply within one business day.", "Contact") + f"""
<section><div class="wrap contact">
<div class="info rv">
<div class="it"><div class="ico">📍</div><div><b>Visit us</b><span>221 Market Street, Suite 400, Austin, TX 78701</span></div></div>
<div class="it"><div class="ico">✉️</div><div><b>Email</b><span>hello@zenvora.example</span></div></div>
<div class="it"><div class="ico">📞</div><div><b>Phone</b><span>+1 (555) 014-2290</span></div></div>
<div class="it"><div class="ico">🕘</div><div><b>Working hours</b><span>Mon – Fri, 9:00 AM – 6:00 PM</span></div></div></div>
<form class="f rv" id="contactForm">
<div class="two"><label>Full name<input required placeholder="John Doe"></label><label>Email<input type="email" required placeholder="you@company.com"></label></div>
<div class="two"><label>Phone<input placeholder="+1 555 000 0000"></label><label>Service<select>{opts}</select></label></div>
<div class="two"><label>Website<input placeholder="https://yourwebsite.com"></label><label>Monthly ad budget<select><option>Under $1,000</option><option>$1,000 – $5,000</option><option>$5,000 – $20,000</option><option>$20,000+</option><option>Not sure yet</option></select></label></div>
<label>Your goals<textarea required placeholder="Tell us what you want to achieve with paid ads..."></textarea></label>
<div class="ok" id="formOk">Thank you! Your request has been received. We will contact you shortly.</div>
<button class="btn btn-primary" type="submit">Request Free Audit →</button></form></div></section>
""" + foot()
write("contact.html", contact)

# ---------- LEGAL ----------
def legal(name, file, sections):
    body = "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in sections)
    write(file, head(name, f"{name} for {BRAND}.", "") + page_hero(name, "Last updated: October 1, 2026", name) + f'<section><div class="wrap legal">{body}</div></section>' + foot())

legal("Privacy Policy", "privacy-policy.html", [
    ("Information we collect", "We collect information you give us directly, such as your name, email, website and business details when you contact us, plus basic usage data such as pages visited."),
    ("Cookies and tracking", "Our website may use cookies and analytics tools to understand how visitors use it. You can control cookies through your browser settings."),
    ("How we use it", "We use your information to respond to enquiries, deliver our services, improve our website and send updates you have asked for."),
    ("Sharing and security", "We do not sell personal data. We share it only with trusted providers who help us operate, and we use reasonable measures to protect it."),
    ("Your rights", "You may request access to, correction of or deletion of your personal data at any time by emailing hello@zenvora.example."),
])
legal("Terms & Conditions", "terms-conditions.html", [
    ("Use of this website", "By using this website you agree to these terms. Content is provided for general information and may change without notice."),
    ("Services", "Scope, management fees and reporting are defined in a written agreement or proposal signed by both parties."),
    ("Ad spend and accounts", "Ad spend is paid directly to advertising platforms such as Google and Meta, and is separate from our management fees. Ad accounts remain the property of the client."),
    ("No guaranteed results", "Advertising performance depends on many factors outside our control. We work to improve results but do not guarantee specific outcomes."),
    ("Liability", "To the extent permitted by law, we are not liable for indirect or consequential losses arising from use of this website."),
])

# ---------- 404 ----------
write("404.html", head("Page Not Found", "Page not found.", "") + """
<div class="nf"><div><h1>404</h1><h2 style="color:#fff">Page not found</h2><p>The page you are looking for does not exist or has moved.</p>
<a href="index.html" class="btn btn-primary">Back to Home</a></div></div>
""" + foot())

print("Built", len(os.listdir(OUT)), "items in", OUT)
