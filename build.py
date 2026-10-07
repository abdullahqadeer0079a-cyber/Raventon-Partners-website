"""Static site generator for Zenvora Digital. Run: python build.py"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
BRAND = "Zenvora Digital"

SERVICES = [
    dict(slug="web-development", icon="💻", name="Web Development",
         short="Fast, secure and scalable websites and web apps built around your business goals.",
         intro="From brand websites to complex web platforms, we build products that load fast, rank well and convert visitors into customers.",
         points=["Custom websites and landing pages", "Web apps and dashboards", "E-commerce and CMS integration", "API and third-party integrations", "Performance, SEO and security hardening", "Ongoing maintenance and support"],
         tech=["React", "Next.js", "Node.js", "Laravel", "WordPress", "PostgreSQL", "Tailwind"],
         faq=[("How long does a website take?", "A typical business website takes 3 to 6 weeks. Larger web apps are scoped in phases so you see working software early."),
              ("Will my site be mobile friendly?", "Yes. Every site we build is responsive and tested on real phones, tablets and desktops."),
              ("Do you provide support after launch?", "Yes. We offer monthly maintenance plans covering updates, backups, monitoring and small improvements.")]),
    dict(slug="mobile-app-development", icon="📱", name="Mobile App Development",
         short="Native-quality iOS and Android apps that people enjoy using every day.",
         intro="We design, build and launch mobile apps for iOS and Android, from first prototype to App Store and Google Play release.",
         points=["Cross-platform apps with Flutter and React Native", "Native iOS and Android development", "Backend, push notifications and payments", "App Store and Play Store publishing", "App performance and crash monitoring", "Updates, new features and long-term support"],
         tech=["Flutter", "React Native", "Swift", "Kotlin", "Firebase", "REST", "GraphQL"],
         faq=[("Should I build native or cross-platform?", "Most products ship faster and cheaper with a single cross-platform codebase. We recommend native only when you need deep hardware features."),
              ("Can you take over an existing app?", "Yes. We audit the code first, then fix, refactor or extend it based on what we find."),
              ("Do you handle store submission?", "We handle the full submission process, including screenshots, listings and review feedback.")]),
    dict(slug="ui-ux-design", icon="🎨", name="UI/UX Design",
         short="Research-led interface design that is simple to use and a pleasure to look at.",
         intro="Great products start with understanding users. Our designers turn research and ideas into clear, beautiful and usable interfaces.",
         points=["User research and journey mapping", "Wireframes and clickable prototypes", "High-fidelity UI design", "Design systems and component libraries", "Usability testing and iteration", "Developer-ready handoff in Figma"],
         tech=["Figma", "FigJam", "Maze", "Lottie", "Storybook", "Adobe CC"],
         faq=[("What do I receive at the end?", "You get full Figma files, a design system, interactive prototypes and a handoff guide for developers."),
              ("Can you redesign my existing product?", "Yes. We review analytics and user feedback, then improve the experience step by step or all at once."),
              ("Do you test designs with users?", "Yes. We run quick usability sessions on prototypes before any development starts.")]),
]

POSTS = [
    dict(slug="why-fast-websites-win", t="t1", e="⚡", title="Why Fast Websites Win More Customers", date="September 18, 2026", cat="Web Development",
         desc="Speed is a feature. Here is how load time affects bounce rate, rankings and revenue.",
         body=["Visitors decide within seconds whether a site is worth their time. Every extra second of load time increases bounce rate and lowers conversions.",
               "Start with the basics: compress images, serve modern formats, lazy-load below-the-fold content and ship less JavaScript. These four changes alone fix most slow sites.",
               "Next, measure. Use real-user data, not just lab tests, and track Core Web Vitals over time. Performance is not a one-off task; it needs a budget and an owner."]),
    dict(slug="flutter-vs-native", t="t2", e="📲", title="Flutter vs Native: Which Should You Choose?", date="August 30, 2026", cat="Mobile Apps",
         desc="A practical comparison of cross-platform and native development for your next app.",
         body=["Cross-platform frameworks like Flutter let one team ship to iOS and Android from a single codebase. That usually means lower cost and faster releases.",
               "Native development still wins when you need the newest platform APIs, heavy graphics or tight hardware integration.",
               "For most startups and business apps, cross-platform is the right default. Choose native when a specific requirement forces your hand."]),
    dict(slug="ux-mistakes-to-avoid", t="t3", e="✏️", title="7 UX Mistakes That Quietly Kill Conversions", date="August 12, 2026", cat="UI/UX Design",
         desc="Small usability problems add up. Learn the common ones and how to fix them.",
         body=["Unclear navigation, long forms, low-contrast text and hidden pricing are among the most common conversion killers we see in audits.",
               "Fixing them rarely needs a full redesign. Simplify the main journey, remove steps that do not help the user and make the next action obvious.",
               "Always validate changes with real users. Five short usability sessions will reveal most of the serious problems."]),
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
<link rel="stylesheet" href="assets/style.css"><link rel="stylesheet" href="assets/extras.css"><link rel="stylesheet" href="assets/extras2.css"><link rel="stylesheet" href="assets/extras3.css"><link rel="stylesheet" href="assets/extras4.css"><link rel="stylesheet" href="assets/extras5.css"><link rel="stylesheet" href="assets/extras6.css">
</head><body>
<div class="progress"></div>
<header class="nav"><div class="wrap">
<a href="index.html" class="logo"><i>Z</i>Zenvora</a>
<button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
<nav class="menu">{links}<a href="contact.html" class="btn btn-primary">Get a Quote</a></nav>
</div></header>
"""


def foot():
    svc = "".join(f'<li><a href="services-{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f"""
<footer><div class="wrap">
<div class="fgrid">
<div><a href="index.html" class="logo"><i>Z</i>Zenvora</a>
<p>We design and build websites, mobile apps and digital products that help ambitious companies grow.</p>
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
<h2>Ready to build something great?</h2>
<p>Tell us about your idea and we will get back within one business day with a clear plan and estimate.</p>
<a href="contact.html" class="btn">Start Your Project →</a></div></div></section>"""


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


MARQ = "".join(f"<span>{x}</span>" for x in ["NORTHWIND", "Lumio", "BRIGHTLY", "Orbitly", "Kestrel", "React", "Flutter", "Node.js", "Figma", "Next.js", "Firebase", "Laravel"])

WORKS = [("🛒", "Lumio Store", "E-commerce web platform", "linear-gradient(135deg,#5b4bff,#8f7bff)"),
         ("🏃", "Orbitly Fit", "Fitness mobile app (iOS & Android)", "linear-gradient(135deg,#00a8b8,#37e0cf)"),
         ("📊", "Kestrel Analytics", "SaaS dashboard & UX redesign", "linear-gradient(135deg,#ff6b9a,#ffa36b)")]
WORKS_HTML = "".join(f'<div class="work rv zoom" style="background:{g}"><div class="big">{i}</div><small>{c}</small><h3>{n}</h3></div>' for i, n, c, g in WORKS)

HOME_FAQ = [("What services does Zenvora offer?", "We focus on three things: web development, mobile app development and UI/UX design. Each can be bought separately or as one package."),
            ("How much does a project cost?", "It depends on scope. After a short discovery call we send a fixed, itemised quote so you know the cost before any work starts."),
            ("How long will my project take?", "Websites usually take 3 to 6 weeks and mobile apps 8 to 14 weeks. We share a timeline with milestones at kickoff."),
            ("Do you work with clients outside your country?", "Yes. We are remote-first and work with clients in 12 countries, with overlap hours that suit your time zone."),
            ("What happens after launch?", "We offer maintenance and support plans covering updates, monitoring, backups and new features.")]
FAQ_HTML = "".join(f"<details class='rv'><summary>{q}</summary><p>{a}</p></details>" for q, a in HOME_FAQ)

# ---------- HOME ----------
home = head("Websites, Mobile Apps & UI/UX Design", "Zenvora Digital builds web, mobile and design solutions for growing businesses.", "index.html") + f"""
<section class="hero"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><canvas id="particles"></canvas><div class="wrap hero-grid">
<div><span class="eyebrow">Digital product studio</span>
<h1>We craft <span class="grad-text typed" data-words='["websites","mobile apps","brand experiences","digital products"]'>websites</span> people love</h1>
<p class="lead">Web development, mobile apps and UI/UX design under one roof. We turn ideas into fast, beautiful and reliable software.</p>
<div class="hero-btns"><a href="contact.html" class="btn btn-primary">Get Free Consultation →</a><a href="services.html" class="btn btn-ghost">Our Services</a></div></div>
<div class="hero-visual">
<div class="stage" id="stage">
<div class="layer swatch" data-depth="20"><div class="in"><i style="background:#5b4bff"></i><i style="background:#00c2d1"></i><i style="background:#ff6b9a"></i><i style="background:#fff"></i></div></div>
<div class="layer dashw" data-depth="12"><div class="in">
<div class="dh"><i></i><i></i><i></i><span>Growth dashboard</span></div>
<div class="kpis"><div><small>Visitors</small><b>24.8K</b></div><div><small>Conversion</small><b class="up">+38%</b></div></div>
<svg class="chart" viewBox="0 0 300 100" preserveAspectRatio="none"><defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#5b4bff"/><stop offset="1" stop-color="#00c2d1"/></linearGradient><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00c2d1" stop-opacity=".35"/><stop offset="1" stop-color="#00c2d1" stop-opacity="0"/></linearGradient></defs>
<path class="area" d="M0 80 C30 70 50 40 80 50 S130 75 160 45 S220 20 250 30 S290 10 300 8 L300 100 L0 100Z" fill="url(#ar)"/>
<path class="line" d="M0 80 C30 70 50 40 80 50 S130 75 160 45 S220 20 250 30 S290 10 300 8" fill="none" stroke="url(#lg)" stroke-width="3" stroke-linecap="round"/></svg>
<div class="bars"><i style="--h:45%;--d:1"></i><i style="--h:70%;--d:2"></i><i style="--h:55%;--d:3"></i><i style="--h:90%;--d:4"></i><i style="--h:65%;--d:5"></i><i style="--h:100%;--d:6"></i><i style="--h:80%;--d:7"></i></div>
</div></div>
<div class="layer phoneh" data-depth="28"><div class="in"><div class="pscreen">
<div class="ph"><i></i><span>My App</span></div>
<div class="row" style="--c:#5b4bff"><u></u><s></s></div><div class="row" style="--c:#00c2d1"><u></u><s></s></div><div class="row" style="--c:#ff6b9a"><u></u><s></s></div><div class="row" style="--c:#ffb020"><u></u><s></s></div>
<div class="pbtn"></div></div></div></div>
<div class="layer toast tst1" data-depth="42"><div class="in"><em>🚀</em><div><b>Project launched</b><small>Web app is live</small></div></div></div>
<div class="layer toast tst2" data-depth="36"><div class="in"><em>✓</em><div><b>App approved</b><small>Now on the App Store</small></div></div></div>
</div>
</div></div></section>

<div class="logos"><div class="wrap"><small style="font-weight:600;color:var(--muted);letter-spacing:.08em;text-transform:uppercase;font-size:.78rem">Trusted by growing teams &amp; powered by modern technology</small>
<div class="marq"><div class="track">{MARQ}{MARQ}</div></div></div></div>

<section><div class="wrap split">
<div class="art rv"><div class="mini m1">🚀 Fast delivery</div><div class="badge"><b>8+</b>Years of experience</div><div class="mini m2">✅ Quality first</div></div>
<div class="rv"><span class="eyebrow">About us</span><h2>A team that cares about your results</h2>
<p>Zenvora Digital is a team of designers, engineers and strategists. We work as an extension of your company and measure success by the outcomes we deliver for you.</p>
<ul class="checks"><li>Senior team, no handoffs to juniors</li><li>Transparent pricing and weekly progress updates</li><li>Built for speed, security and scale</li></ul>
<br><a href="about.html" class="btn btn-dark">More about us →</a></div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">What we do</span><h2>Services built for growth</h2><p>Everything you need to launch and scale a digital product, delivered by one focused team.</p></div>
<div class="grid g3">{svc_cards()}</div></div></section>

<section class="stats"><div class="wrap grid g4">
<div><b data-count="150" data-suffix="+">0</b><span>Projects completed</span></div>
<div><b data-count="80" data-suffix="+">0</b><span>Happy clients</span></div>
<div><b data-count="12" data-suffix="">0</b><span>Countries served</span></div>
<div><b data-count="98" data-suffix="%">0</b><span>Client retention</span></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">How we work</span><h2>A simple, proven process</h2><p>Clear steps and constant communication from the first call to launch day and beyond.</p></div>
<div class="grid g4">
<div class="step rv"><div class="n">01</div><h3>Discover</h3><p>We learn your goals, users and constraints, then define scope and success metrics.</p></div>
<div class="step rv"><div class="n">02</div><h3>Design</h3><p>Wireframes and prototypes let you see and test the product before we build it.</p></div>
<div class="step rv"><div class="n">03</div><h3>Develop</h3><p>We build in short sprints with regular demos so there are never surprises.</p></div>
<div class="step rv"><div class="n">04</div><h3>Deliver</h3><p>We launch, monitor and keep improving based on real user data.</p></div></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our work</span><h2>Recent projects</h2><p>A few examples of products we have designed and built with our clients.</p></div>
<div class="grid g3">{WORKS_HTML}</div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Testimonials</span><h2>What our clients say</h2></div>
<div class="grid g3">
<div class="quote rv"><div class="stars">★★★★★</div><p>"Zenvora rebuilt our website in five weeks. Load time dropped by 60% and enquiries doubled within the quarter."</p><div class="who"><i>SM</i><div><b>Sarah Mitchell</b><small>Marketing Director, Lumio</small></div></div></div>
<div class="quote rv"><div class="stars">★★★★★</div><p>"Our mobile app launched on both stores with great reviews. The team was responsive and very professional."</p><div class="who"><i>DK</i><div><b>Daniel Kim</b><small>Founder, Orbitly</small></div></div></div>
<div class="quote rv"><div class="stars">★★★★★</div><p>"The new design made our product so much easier to use. Support tickets fell sharply after the redesign."</p><div class="who"><i>AR</i><div><b>Ana Rodriguez</b><small>Product Lead, Kestrel</small></div></div></div>
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
about = head("About Us", "Learn about Zenvora Digital, our mission, values and team.", "about.html") + page_hero("About Us", "We are a product studio on a mission to make great digital experiences accessible to every business.", "About Us") + f"""
<section><div class="wrap split">
<div class="rv"><span class="eyebrow">Our story</span><h2>Built by makers, driven by results</h2>
<p>Zenvora started in 2018 with two developers and a designer who wanted to build better software for small businesses. Today we are a team of 25 working with clients across 12 countries.</p>
<p>We believe good digital products are the result of clear thinking, honest communication and attention to detail. That is how we work with every client, large or small.</p>
<ul class="checks"><li>Founded in 2018, remote-first team</li><li>150+ projects delivered worldwide</li><li>Certified, experienced professionals</li></ul></div>
<div class="art rv"><div class="mini m1">🌍 12 countries</div><div class="badge"><b>25</b>Team members</div><div class="mini m2">⭐ 4.9 rating</div></div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="grid g2">
<div class="svc rv"><div class="ico">🎯</div><h3>Our mission</h3><p>To help businesses grow through thoughtfully designed, well-engineered digital products that deliver measurable value.</p></div>
<div class="svc rv"><div class="ico">🔭</div><h3>Our vision</h3><p>To be the most trusted digital partner for ambitious companies, known for quality, honesty and long-term relationships.</p></div></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our values</span><h2>What guides us</h2></div>
<div class="grid g4">
<div class="step rv"><div class="n">01</div><h3>Quality</h3><p>We sweat the details so your product feels polished.</p></div>
<div class="step rv"><div class="n">02</div><h3>Honesty</h3><p>Clear timelines, fair prices and no hidden surprises.</p></div>
<div class="step rv"><div class="n">03</div><h3>Partnership</h3><p>Your goals are our goals. We succeed when you do.</p></div>
<div class="step rv"><div class="n">04</div><h3>Innovation</h3><p>We keep learning and use the right tools for the job.</p></div></div></div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our journey</span><h2>How we got here</h2></div>
<div class="timeline">
<div class="tl rv left"><b>2018</b><h3>Zenvora is founded</h3><p>Two developers and a designer start building websites for local businesses.</p></div>
<div class="tl rv left"><b>2020</b><h3>Mobile app team launches</h3><p>We add Flutter and native engineers and ship our first apps to both stores.</p></div>
<div class="tl rv left"><b>2022</b><h3>Dedicated UI/UX studio</h3><p>A research and design practice joins the team, with a full design system offering.</p></div>
<div class="tl rv left"><b>2024</b><h3>Serving 12 countries</h3><p>We grow to 25 people and pass 100 delivered projects.</p></div>
<div class="tl rv left"><b>2026</b><h3>150+ products shipped</h3><p>Today we partner with startups and established companies on long-term growth.</p></div>
</div></div></section>

<section class="stats"><div class="wrap grid g4">
<div><b data-count="150" data-suffix="+">0</b><span>Projects completed</span></div>
<div><b data-count="80" data-suffix="+">0</b><span>Happy clients</span></div>
<div><b data-count="25" data-suffix="">0</b><span>Experts on the team</span></div>
<div><b data-count="8" data-suffix="+">0</b><span>Years in business</span></div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Leadership</span><h2>Meet the team</h2></div>
<div class="grid g3">
<div class="quote rv"><div class="who"><i>JH</i><div><b>James Harlow</b><small>Founder &amp; CEO</small></div></div><p style="margin-top:18px">Full-stack engineer and product thinker who leads strategy and client relationships.</p></div>
<div class="quote rv"><div class="who"><i>PN</i><div><b>Priya Nair</b><small>Head of Design</small></div></div><p style="margin-top:18px">Leads UI/UX with a focus on research, accessibility and delightful details.</p></div>
<div class="quote rv"><div class="who"><i>OB</i><div><b>Omar Bashir</b><small>Head of Engineering</small></div></div><p style="margin-top:18px">Oversees web and mobile engineering, architecture and code quality.</p></div></div></div></section>
{cta()}
""" + foot()
write("about.html", about)

# ---------- SERVICES ----------
VISUALS = {
    "web-development": '<div class="mock browser"><div class="bt"><i></i><i></i><i></i><span>zenvora.dev/app</span></div><div class="bb"><div class="l1"></div><div class="l2"></div><div class="cols"><div></div><div></div><div></div></div><div class="l3"></div></div></div>',
    "mobile-app-development": '<div class="mock phone"><div class="notch"></div><div class="ps"><div class="av"></div><div class="l1"></div><div class="l2"></div><div class="card"></div><div class="card"></div><div class="nav"><i></i><i></i><i></i><i></i></div></div></div>',
    "ui-ux-design": '<div class="mock design"><div class="sw"><i style="background:#5b4bff"></i><i style="background:#00c2d1"></i><i style="background:#ff6b9a"></i><i style="background:#0b1020"></i></div><div class="frame"><div class="fr1"></div><div class="fr2"></div><div class="fr3"></div><span class="cursor">➤</span></div></div>',
}
NUM = {"web-development": "01", "mobile-app-development": "02", "ui-ux-design": "03"}

rows = ""
for i, s in enumerate(SERVICES):
    pts = "".join(f"<li>{p}</li>" for p in s["points"][:4])
    tags = "".join(f"<span>{t}</span>" for t in s["tech"][:5])
    flip = " flip" if i % 2 else ""
    rows += f"""<div class="srow{flip}">
<div class="stext rv {'right' if i % 2 else 'left'}"><div class="snum">{NUM[s['slug']]}</div><h2>{s['name']}</h2><p class="sint">{s['intro']}</p>
<ul class="checks">{pts}</ul><div class="tags">{tags}</div>
<a href="services-{s['slug']}.html" class="btn btn-dark" style="margin-top:26px">Explore {s['name']} →</a></div>
<div class="svis rv zoom">{VISUALS[s['slug']]}</div></div>"""

INDUSTRIES = [("🛍️", "Retail & E-commerce"), ("🏥", "Healthcare"), ("🎓", "Education"), ("💳", "Fintech"), ("🏠", "Real Estate"), ("🚚", "Logistics"), ("🍽️", "Food & Hospitality"), ("🚀", "Startups & SaaS")]
ind = "".join(f'<div class="ind rv"><span>{e}</span><b>{n}</b></div>' for e, n in INDUSTRIES)

services = head("Our Services", "Web development, mobile app development and UI/UX design services.", "services.html") + page_hero("Our Services", "Strategy, design and engineering for web and mobile products, delivered by one focused team.", "Services") + f"""
<section class="sv-intro"><div class="wrap"><div class="intro-grid">
<div class="rv"><span class="eyebrow">What we do</span><h2>One partner for design, web and mobile</h2></div>
<div class="rv"><p>We help companies plan, design and ship digital products. Because design and engineering sit in the same team, handoffs are smooth, decisions are quick and the finished product feels consistent from first screen to last.</p>
<div class="mini-stats"><div><b data-count="150" data-suffix="+">0</b><span>Projects</span></div><div><b data-count="12" data-suffix="">0</b><span>Countries</span></div><div><b data-count="98" data-suffix="%">0</b><span>Retention</span></div></div></div>
</div></div></section>

<section class="sv-rows"><div class="wrap">{rows}</div></section>

<section class="bg-soft"><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Our approach</span><h2>From first call to launch day</h2><p>The same clear process on every project, so you always know what happens next.</p></div>
<div class="flow">
<div class="fl rv"><div class="fn">1</div><h3>Discover</h3><p>Workshops to define goals, users, scope and success metrics.</p></div>
<div class="fl rv"><div class="fn">2</div><h3>Design</h3><p>Wireframes and prototypes validated with real users.</p></div>
<div class="fl rv"><div class="fn">3</div><h3>Build</h3><p>Agile sprints, code reviews and a demo every week.</p></div>
<div class="fl rv"><div class="fn">4</div><h3>Launch</h3><p>Testing, deployment and a smooth release plan.</p></div>
<div class="fl rv"><div class="fn">5</div><h3>Grow</h3><p>Monitoring, support and data-led improvements.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head center rv"><span class="eyebrow">Industries</span><h2>Experience across sectors</h2><p>We bring lessons from many industries to every new project.</p></div>
<div class="ind-grid">{ind}</div></div></section>

<section class="sv-why"><div class="wrap split">
<div class="rv"><span class="eyebrow">Why Zenvora</span><h2>Built on trust and clear communication</h2>
<p>Our clients stay with us because we are easy to work with and we deliver what we promise.</p>
<ul class="checks"><li>Senior designers and engineers on every project</li><li>Fixed scope, itemised quotes, no hidden costs</li><li>Weekly demos and a shared project board</li><li>Secure, tested and documented code</li><li>Post-launch support and maintenance</li></ul></div>
<div class="why-cards rv">
<div class="wc"><b>24h</b><span>Average response time</span></div>
<div class="wc"><b>3–6 wks</b><span>Typical website delivery</span></div>
<div class="wc"><b>100%</b><span>Code ownership is yours</span></div>
<div class="wc"><b>30 days</b><span>Free post-launch fixes</span></div>
</div></div></section>
{cta()}
""" + foot()
write("services.html", services)

for s in SERVICES:
    others = "".join(f'<li><a href="services-{o["slug"]}.html" class="{"on" if o is s else ""}">{o["icon"]} {o["name"]}</a></li>' for o in SERVICES)
    pts = "".join(f"<li>{p}</li>" for p in s["points"])
    tags = "".join(f"<span>{t}</span>" for t in s["tech"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in s["faq"])
    html = head(s["name"], s["short"], "services.html") + page_hero(s["name"], s["short"], f'<a href="services.html">Services</a> / {s["name"]}') + f"""
<section><div class="wrap detail">
<div class="rv"><h2>Overview</h2><p>{s['intro']}</p>
<h2>What's included</h2><ul class="checks">{pts}</ul>
<h2>Our process</h2><div class="grid g2" style="margin-bottom:10px">
<div class="step"><div class="n">01</div><h3>Discovery</h3><p>Goals, users, scope and timeline.</p></div>
<div class="step"><div class="n">02</div><h3>Plan &amp; design</h3><p>Prototypes you can click through.</p></div>
<div class="step"><div class="n">03</div><h3>Build &amp; test</h3><p>Short sprints and regular demos.</p></div>
<div class="step"><div class="n">04</div><h3>Launch &amp; grow</h3><p>Release, monitor and improve.</p></div></div>
<h2>Frequently asked questions</h2>{faq}</div>
<aside class="side">
<div class="box"><h4>All services</h4><ul>{others}</ul></div>
<div class="box"><h4>Technologies</h4><div class="tags">{tags}</div></div>
<div class="box"><h4>Have a project in mind?</h4><p style="margin-bottom:16px;color:var(--muted)">Get a free consultation and quote.</p><a href="contact.html" class="btn btn-primary">Contact Us →</a></div>
</aside></div></section>
""" + foot()
    write(f"services-{s['slug']}.html", html)

# ---------- BLOG ----------
blog = head("Blog", "Insights on web development, mobile apps and design.", "blog.html") + page_hero("Our Blog", "Practical articles on building and growing digital products.", "Blog") + f"""
<section><div class="wrap"><div class="grid g3">{post_cards(POSTS)}</div></div></section>
""" + foot()
write("blog.html", blog)

for p in POSTS:
    body = "".join(f"<p>{x}</p>" for x in p["body"])
    html = head(p["title"], p["desc"], "blog.html") + page_hero(p["title"], f"{p['date']} · {p['cat']}", f'<a href="blog.html">Blog</a> / Article') + f"""
<section><div class="wrap legal rv"><div class="thumb {p['t']}" style="border-radius:20px;height:260px;margin-bottom:30px">{p['e']}</div>
{body}<br><a href="blog.html" class="btn btn-dark">← Back to blog</a></div></section>
""" + foot()
    write(f"blog-{p['slug']}.html", html)

# ---------- CONTACT ----------
opts = "".join(f"<option>{s['name']}</option>" for s in SERVICES) + "<option>Other</option>"
contact = head("Contact Us", "Get in touch with Zenvora Digital for a free consultation.", "contact.html") + page_hero("Contact Us", "Tell us about your project. We reply within one business day.", "Contact") + f"""
<section><div class="wrap contact">
<div class="info rv">
<div class="it"><div class="ico">📍</div><div><b>Visit us</b><span>221 Market Street, Suite 400, Austin, TX 78701</span></div></div>
<div class="it"><div class="ico">✉️</div><div><b>Email</b><span>hello@zenvora.example</span></div></div>
<div class="it"><div class="ico">📞</div><div><b>Phone</b><span>+1 (555) 014-2290</span></div></div>
<div class="it"><div class="ico">🕘</div><div><b>Working hours</b><span>Mon – Fri, 9:00 AM – 6:00 PM</span></div></div></div>
<form class="f rv" id="contactForm">
<div class="two"><label>Full name<input required placeholder="John Doe"></label><label>Email<input type="email" required placeholder="you@company.com"></label></div>
<div class="two"><label>Phone<input placeholder="+1 555 000 0000"></label><label>Service<select>{opts}</select></label></div>
<label>Message<textarea required placeholder="Tell us about your project..."></textarea></label>
<div class="ok" id="formOk">Thank you! Your message has been received. We will contact you shortly.</div>
<button class="btn btn-primary" type="submit">Send Message →</button></form></div></section>
""" + foot()
write("contact.html", contact)

# ---------- LEGAL ----------
def legal(name, file, sections):
    body = "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in sections)
    write(file, head(name, f"{name} for {BRAND}.", "") + page_hero(name, "Last updated: October 1, 2026", name) + f'<section><div class="wrap legal">{body}</div></section>' + foot())

legal("Privacy Policy", "privacy-policy.html", [
    ("Information we collect", "We collect information you give us directly, such as your name, email and project details when you contact us, plus basic usage data such as pages visited."),
    ("How we use it", "We use your information to respond to enquiries, deliver our services, improve our website and send updates you have asked for."),
    ("Sharing and security", "We do not sell personal data. We share it only with trusted providers who help us operate, and we use reasonable measures to protect it."),
    ("Your rights", "You may request access to, correction of or deletion of your personal data at any time by emailing hello@zenvora.example."),
])
legal("Terms & Conditions", "terms-conditions.html", [
    ("Use of this website", "By using this website you agree to these terms. Content is provided for general information and may change without notice."),
    ("Services", "Project scope, timelines and fees are defined in a written agreement or proposal signed by both parties."),
    ("Intellectual property", "Unless agreed otherwise, ownership of final deliverables transfers to the client on full payment. Our pre-existing tools and materials remain ours."),
    ("Liability", "To the extent permitted by law, we are not liable for indirect or consequential losses arising from use of this website."),
])

# ---------- 404 ----------
write("404.html", head("Page Not Found", "Page not found.", "") + """
<div class="nf"><div><h1>404</h1><h2 style="color:#fff">Page not found</h2><p>The page you are looking for does not exist or has moved.</p>
<a href="index.html" class="btn btn-primary">Back to Home</a></div></div>
""" + foot())

print("Built", len(os.listdir(OUT)), "items in", OUT)
