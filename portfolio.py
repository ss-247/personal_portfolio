import streamlit as st

st.set_page_config(
    page_title="Satish Surjoo | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# GLOBAL CSS + FONT IMPORTS
# ─────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Creepster&family=Bangers&family=Comic+Neue:wght@400;700&display=swap" rel="stylesheet">

<style>
/* RESET & BASE */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0a !important;
}
[data-testid="stAppViewContainer"] > .main {
    background: #0a0a0a !important;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
[data-testid="stHeader"] { background: transparent !important; }

/* HIDE STREAMLIT CHROME */
#MainMenu, footer, header { visibility: hidden; }

/* ── SELECTOR BAR ── */
.selector-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    padding: 32px 24px 20px;
    flex-wrap: wrap;
}
.sel-btn {
    cursor: pointer;
    border: 2px solid currentColor;
    padding: 10px 26px;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-radius: 2px;
    transition: all 0.25s ease;
    background: transparent;
    text-decoration: none;
    display: inline-block;
}
.sel-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.4); }

/* TECH button */
.btn-tech { color: #00f5d4; border-color: #00f5d4; }
.btn-tech.active { background: #00f5d4; color: #0a0a0a; box-shadow: 0 0 20px #00f5d4aa; }

/* CONCRETE button */
.btn-concrete { color: #f5a623; border-color: #f5a623; }
.btn-concrete.active { background: #f5a623; color: #0a0a0a; box-shadow: 0 0 20px #f5a623aa; }

/* FUNNY button */
.btn-funny { color: #ff6b6b; border-color: #ff6b6b; }
.btn-funny.active { background: #ff6b6b; color: #fff; box-shadow: 0 0 20px #ff6b6baa; }

/* HALLOWEEN button */
.btn-halloween { color: #bf5cf3; border-color: #bf5cf3; }
.btn-halloween.active { background: #bf5cf3; color: #fff; box-shadow: 0 0 20px #bf5cf3aa; }

/* ── HERO STRIP ── */
.hero-strip {
    text-align: center;
    padding: 0 24px 40px;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(52px, 10vw, 120px);
    line-height: 0.9;
    letter-spacing: -3px;
}
.hero-tagline {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 16px;
    opacity: 0.6;
}

/* ── GRID LAYOUT ── */
.cv-grid {
    display: grid;
    grid-template-columns: 1fr 340px;
    gap: 2px;
    padding: 0 24px 60px;
    max-width: 1200px;
    margin: 0 auto;
}
@media (max-width: 768px) {
    .cv-grid { grid-template-columns: 1fr; }
}

.cv-main, .cv-sidebar {
    padding: 40px;
}

/* ── SECTION LABELS ── */
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 20px;
    padding-bottom: 8px;
    opacity: 0.5;
    border-bottom: 1px solid currentColor;
}

/* ── JOB BLOCK ── */
.job-block {
    margin-bottom: 32px;
    padding-left: 20px;
    border-left: 2px solid currentColor;
}
.job-year {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    opacity: 0.5;
    margin-bottom: 4px;
}
.job-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 18px;
    margin-bottom: 4px;
}
.job-company {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    opacity: 0.7;
    margin-bottom: 10px;
}
.job-desc {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    line-height: 1.8;
    opacity: 0.8;
}
.job-desc ul { padding-left: 16px; }
.job-desc li { margin-bottom: 4px; }

/* ── SKILL PILL ── */
.skill-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 24px;
}
.skill-pill {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    padding: 6px 14px;
    border: 1px solid currentColor;
    border-radius: 2px;
    opacity: 0.8;
    letter-spacing: 1px;
}

/* ── CONTACT LINE ── */
.contact-line {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    line-height: 2.2;
    opacity: 0.75;
}
.contact-line a { color: inherit; text-decoration: none; }
.contact-line a:hover { text-decoration: underline; }

/* ── STAT BLOCK ── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 2px;
    margin-bottom: 40px;
}
.stat-box {
    padding: 24px 16px;
    text-align: center;
}
.stat-num {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 42px;
    line-height: 1;
}
.stat-lbl {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0.5;
    margin-top: 6px;
}

/* ── PROJECT CARD ── */
.proj-card {
    padding: 16px 20px;
    margin-bottom: 8px;
    border-left: 3px solid currentColor;
}
.proj-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 15px;
}
.proj-desc {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    opacity: 0.65;
    margin-top: 4px;
    line-height: 1.6;
}

/* ── TICKER ── */
.ticker-wrap {
    overflow: hidden;
    white-space: nowrap;
    padding: 12px 0;
    margin-bottom: 2px;
}
.ticker-inner {
    display: inline-block;
    animation: ticker 20s linear infinite;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    letter-spacing: 3px;
    opacity: 0.35;
}
@keyframes ticker {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}

/* ── PROFILE BIO ── */
.profile-bio {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    line-height: 2;
    margin-bottom: 32px;
    opacity: 0.85;
}

/* ── WEBSITES BAR ── */
.sites-bar {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 20px;
}
.site-link {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    padding: 8px 18px;
    border: 1px solid currentColor;
    text-decoration: none;
    letter-spacing: 1px;
    transition: all 0.2s;
    border-radius: 2px;
}
.site-link:hover { transform: translateY(-2px); }

/* ══════════════════════════════════
   THEME: TECH  (#0a0a0a + cyan)
═══════════════════════════════════ */
.theme-tech {
    --accent: #00f5d4;
    --accent2: #0066ff;
    --bg: #0a0a0a;
    --bg2: #111;
    --bg3: #161616;
    --text: #e8e8e8;
    color: var(--text);
}
.theme-tech .hero-name { color: #fff; }
.theme-tech .hero-name span { color: var(--accent); }
.theme-tech .cv-main { background: var(--bg2); color: var(--text); }
.theme-tech .cv-sidebar { background: var(--bg3); color: var(--text); }
.theme-tech .job-block { border-color: var(--accent); }
.theme-tech .section-label { color: var(--accent); border-color: var(--accent); opacity:1; font-size:11px; }
.theme-tech .stat-box:nth-child(1) { background: #00f5d408; }
.theme-tech .stat-box:nth-child(2) { background: #0066ff08; }
.theme-tech .stat-box:nth-child(3) { background: #00f5d408; }
.theme-tech .stat-num { color: var(--accent); }
.theme-tech .skill-pill { border-color: var(--accent); color: var(--accent); }
.theme-tech .proj-card { background: #fff04; border-color: var(--accent2); }
.theme-tech .ticker-inner { color: var(--accent); }
.theme-tech .site-link { color: var(--accent); border-color: var(--accent); }
.theme-tech .site-link:hover { background: var(--accent); color: #0a0a0a; }

/* glow pulse on name */
.theme-tech .hero-name {
    animation: glow-pulse 3s ease-in-out infinite alternate;
}
@keyframes glow-pulse {
    from { text-shadow: 0 0 40px #00f5d422; }
    to   { text-shadow: 0 0 80px #00f5d466, 0 0 120px #0066ff33; }
}

/* scan-line overlay */
.theme-tech::before {
    content: '';
    position: fixed; top:0; left:0; right:0; bottom:0;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,245,212,0.015) 2px, rgba(0,245,212,0.015) 4px);
    pointer-events: none;
    z-index: 9999;
}

/* ══════════════════════════════════
   THEME: CONCRETE  (industrial)
═══════════════════════════════════ */
.theme-concrete {
    --accent: #f5a623;
    --accent2: #e8e0d5;
    --bg: #1a1610;
    --bg2: #221d14;
    --bg3: #2a2418;
    --text: #e8e0d5;
    color: var(--text);
    background: var(--bg) !important;
}
.theme-concrete .hero-name { color: var(--accent2); }
.theme-concrete .hero-name span { color: var(--accent); }
.theme-concrete .cv-main { background: var(--bg2); color: var(--text); }
.theme-concrete .cv-sidebar { background: var(--bg3); color: var(--text); }
.theme-concrete .job-block { border-color: var(--accent); }
.theme-concrete .section-label { color: var(--accent); border-color: var(--accent); opacity:1; }
.theme-concrete .stat-num { color: var(--accent); }
.theme-concrete .skill-pill { border-color: var(--accent); color: var(--accent); }
.theme-concrete .proj-card { border-color: var(--accent); background: rgba(245,166,35,0.05); }
.theme-concrete .ticker-inner { color: var(--accent); }
.theme-concrete .site-link { color: var(--accent); border-color: var(--accent); }
.theme-concrete .site-link:hover { background: var(--accent); color: #1a1610; }
.theme-concrete .hero-name {
    text-shadow: 3px 3px 0 #f5a62344, 6px 6px 0 #f5a62322;
}

/* ══════════════════════════════════
   THEME: FUNNY  (chaotic pop)
═══════════════════════════════════ */
.theme-funny {
    --accent: #ff6b6b;
    --accent2: #ffd93d;
    --accent3: #6bcb77;
    --bg: #fff8f0;
    --bg2: #fff;
    --bg3: #fff8f0;
    --text: #1a1a2e;
    color: var(--text);
    background: var(--bg) !important;
    font-family: 'Comic Neue', cursive;
}
.theme-funny .hero-name {
    font-family: 'Bangers', cursive;
    color: var(--accent);
    letter-spacing: 2px;
    animation: wobble 1s ease-in-out infinite alternate;
    text-shadow: 4px 4px 0 var(--accent2), 8px 8px 0 var(--accent3);
}
@keyframes wobble {
    from { transform: rotate(-1deg); }
    to { transform: rotate(1deg); }
}
.theme-funny .hero-tagline { color: var(--accent3); opacity: 1; font-family: 'Comic Neue', cursive; font-weight:700; }
.theme-funny .cv-main { background: var(--bg2); color: var(--text); border: 3px dashed var(--accent); border-radius: 12px; }
.theme-funny .cv-sidebar { background: var(--bg3); color: var(--text); border: 3px dashed var(--accent2); border-radius: 12px; }
.theme-funny .job-block { border-color: var(--accent2); }
.theme-funny .section-label { color: var(--accent); border-color: var(--accent); opacity:1; font-family: 'Bangers'; font-size: 16px; letter-spacing: 3px; }
.theme-funny .stat-num { color: var(--accent); font-family: 'Bangers'; }
.theme-funny .stat-box:nth-child(1) { background: #ff6b6b22; border-radius: 8px; }
.theme-funny .stat-box:nth-child(2) { background: #ffd93d22; border-radius: 8px; }
.theme-funny .stat-box:nth-child(3) { background: #6bcb7722; border-radius: 8px; }
.theme-funny .skill-pill { border-color: var(--accent2); color: var(--accent); background: #ffd93d22; border-radius: 20px; }
.theme-funny .proj-card { background: #6bcb7715; border-color: var(--accent3); border-radius: 8px; }
.theme-funny .ticker-inner { color: var(--accent); opacity: 0.7; }
.theme-funny .site-link { color: var(--accent); border-color: var(--accent); border-radius: 20px; font-family: 'Comic Neue'; font-weight: 700; }
.theme-funny .site-link:hover { background: var(--accent); color: #fff; }
.theme-funny .profile-bio { font-family: 'Comic Neue', cursive; font-size: 14px; }
.theme-funny .job-title { font-family: 'Bangers'; font-size: 22px; letter-spacing: 1px; }
.theme-funny .job-desc { font-family: 'Comic Neue'; }
.theme-funny .cv-grid { color: var(--text); }
.theme-funny .hero-strip { background: linear-gradient(135deg, #fff0f0, #fffff0, #f0fff0); border-radius: 16px; margin: 0 24px 24px; padding: 40px; }

/* ══════════════════════════════════
   THEME: HALLOWEEN  (spooky)
═══════════════════════════════════ */
.theme-halloween {
    --accent: #ff6b00;
    --accent2: #bf5cf3;
    --accent3: #1aff8c;
    --bg: #080410;
    --bg2: #0d0820;
    --bg3: #110b28;
    --text: #e8d5ff;
    color: var(--text);
    background: var(--bg) !important;
}
.theme-halloween .hero-name {
    font-family: 'Creepster', cursive;
    color: var(--accent);
    letter-spacing: 4px;
    animation: flicker 2s step-end infinite;
    text-shadow: 0 0 20px var(--accent), 0 0 60px #ff6b0066;
}
@keyframes flicker {
    0%, 92%, 94%, 96%, 100% { opacity: 1; }
    93%, 95% { opacity: 0.4; }
}
.theme-halloween .hero-tagline { color: var(--accent2); opacity: 1; font-family: 'Creepster'; font-size: 16px; letter-spacing: 6px; }
.theme-halloween .cv-main { background: var(--bg2); color: var(--text); border: 1px solid #ff6b0033; }
.theme-halloween .cv-sidebar { background: var(--bg3); color: var(--text); border: 1px solid #bf5cf333; }
.theme-halloween .job-block { border-color: var(--accent); }
.theme-halloween .section-label { color: var(--accent2); border-color: var(--accent2); opacity:1; font-family: 'Creepster'; font-size: 16px; letter-spacing: 4px; }
.theme-halloween .stat-num { color: var(--accent); font-family: 'Creepster'; font-size: 52px; }
.theme-halloween .stat-box { background: rgba(255,107,0,0.08); border: 1px solid rgba(255,107,0,0.2); }
.theme-halloween .skill-pill { border-color: var(--accent2); color: var(--accent2); background: rgba(191,92,243,0.1); }
.theme-halloween .proj-card { background: rgba(26,255,140,0.05); border-color: var(--accent3); }
.theme-halloween .ticker-inner { color: var(--accent); }
.theme-halloween .site-link { color: var(--accent); border-color: var(--accent); }
.theme-halloween .site-link:hover { background: var(--accent); color: #080410; }
.theme-halloween .job-title { font-family: 'Creepster'; font-size: 22px; color: var(--accent); letter-spacing: 2px; }
.theme-halloween .hero-strip {
    background: radial-gradient(ellipse at 50% 0%, #ff6b0015 0%, transparent 70%);
}
/* spider web corners */
.theme-halloween .cv-main::before {
    content: '🕸️';
    position: absolute;
    top: 8px; left: 8px;
    font-size: 40px;
    opacity: 0.3;
}
.theme-halloween .cv-main { position: relative; }

/* floating bats */
.bats {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.bat {
    position: absolute;
    font-size: 20px;
    animation: fly linear infinite;
    opacity: 0.15;
}
.bat:nth-child(1) { top: 10%; animation-duration: 8s; animation-delay: 0s; }
.bat:nth-child(2) { top: 30%; animation-duration: 12s; animation-delay: 3s; }
.bat:nth-child(3) { top: 60%; animation-duration: 10s; animation-delay: 6s; }
.bat:nth-child(4) { top: 80%; animation-duration: 9s; animation-delay: 1s; }
@keyframes fly {
    from { transform: translateX(-5vw) scaleX(1); }
    49% { transform: translateX(105vw) scaleX(1); }
    50% { transform: translateX(105vw) scaleX(-1); }
    to { transform: translateX(-5vw) scaleX(-1); }
}

/* ─── Streamlit column gap fix ─── */
[data-testid="column"] { padding: 0 !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* ensure all text colors propagate */
.theme-tech *, .theme-concrete *, .theme-halloween * { color: inherit; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "cv_mode" not in st.session_state:
    st.session_state.cv_mode = "tech"

# ─────────────────────────────────────────────
# SELECTOR BUTTONS  (using streamlit columns)
# ─────────────────────────────────────────────
def sel_bar():
    cols = st.columns([1,1,1,1,1,1])
    labels = [
        ("⚡ Tech / QA / Dev", "tech"),
        ("🏗️ Concrete Pro",    "concrete"),
        ("😂 Funny CV",        "funny"),
        ("🎃 Halloween",       "halloween"),
    ]
    for i, (label, mode) in enumerate(labels):
        with cols[i+1]:
            if st.button(label, key=f"btn_{mode}", use_container_width=True):
                st.session_state.cv_mode = mode

sel_bar()

mode = st.session_state.cv_mode

# ─────────────────────────────────────────────
# THEME WRAPPER
# ─────────────────────────────────────────────
theme_class = {
    "tech":      "theme-tech",
    "concrete":  "theme-concrete",
    "funny":     "theme-funny",
    "halloween": "theme-halloween",
}[mode]

st.markdown(f'<div class="{theme_class}" id="cv-root">', unsafe_allow_html=True)

# Halloween floating bats
if mode == "halloween":
    st.markdown("""
    <div class="bats">
        <div class="bat">🦇</div>
        <div class="bat">🦇</div>
        <div class="bat">🦇</div>
        <div class="bat">🦇</div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA PER MODE
# ─────────────────────────────────────────────

configs = {

"tech": {
    "name_html": 'SATISH <span>SURJOO</span>',
    "tagline": "DEVELOPER · QA ENGINEER · PROJECT MANAGER",
    "ticker": "PYTHON · GIT · GITHUB · EXCEL · VBA · SQL · QA · AGILE · SCRUM · TESTING · CI/CD · PROCESS AUTOMATION · " * 3,
    "bio": """Experienced iGaming QA Tester and Project Manager in regulated slots & casino environments.
Focused on text accuracy, compliance, and cross-team coordination.
Proficient in Git/GitHub for managing updates and iterations.
Builder of bespoke tools that make teams move faster and smarter.""",
    "stats": [("13+", "Years Exp"), ("100+", "Bugs Squashed"), ("∞", "Git Commits")],
    "jobs": [
        ("2025",        "Software Dev",          "Alpine Cement",        ["Built custom software consolidating multi-format supplier reports into a single live dashboard.", "Automated data pipelines saving hours of manual reconciliation weekly."]),
        ("2021–2024",   "QA Tester & PM",        "Easy Games (iGaming)", ["Owned full QA lifecycle for regulated slot & casino game releases.", "Managed stakeholder communication, compliance sign-off, and release coordination.", "Implemented Git-based review workflow for content change tracking."]),
        ("2017–2018",   "Plant Supervisor",      "On-Time Readymix",     ["Supervised plant operations and maintained production schedules."]),
        ("2006–2015",   "Supervisor / Batcher",  "Lafarge Readymix",     ["Batching, sales & orders, scheduling logistics for large concrete volumes."]),
    ],
    "skills": ["Project Management","Software Testing","Git / GitHub","Python","SQL","VBA","Microsoft Excel (Advanced)","Data Analysis","Agile / Scrum","Process Automation"],
    "tools":  ["Python","Git / GitHub","Microsoft 365","Excel / VBA","SQL","Streamlit","GitHub Actions"],
    "projects": [
        ("Cement Tracker", "Live multi-supplier stock dashboard built in Python + Excel automation"),
        ("Punters Challenge", "Sports prediction web app with leaderboard logic"),
        ("Moses Mabhida Stadium", "QA / PM coordination on major infrastructure project"),
        ("Ixopo Dam", "Plant supervision & logistics for major civil concrete works"),
    ],
    "education": [("2019","Hyperion Dev","Software Engineering Bootcamp"),("2016","Upskillist","Microsoft Excel Advanced"),("2001","Phoenix Technical Secondary","Matric")],
    "contact": {"📞":"0827882373","✉️":"surjoo@icloud.com","📍":"Durban, South Africa","🐙":"github.com/ss-247"},
    "sites": [("🌐 Old Portfolio","https://satishsurjoo.co.za"),("⚡ Streamlit App","https://streamlit.io")],
},

"concrete": {
    "name_html": 'SATISH <span>SURJOO</span>',
    "tagline": "RMC PLANT SUPERVISOR · BATCHER · SCHEDULER",
    "ticker": "BATCHMAN · AS400 · LAFARGE · READY-MIX · CONCRETE · PLANT OPS · SCHEDULING · LOGISTICS · STOCK CONTROL · " * 3,
    "bio": """Ready-Mix Concrete professional with 13 years across batching, supervision, sales & order management.
Specialized in accurate mix production, compliance with quality/safety standards,
inventory & stock control, job scheduling, and truck fleet coordination.
Built custom Excel tools for production planning, job tracking & truck scheduling — reducing downtime and errors.""",
    "stats": [("13", "Years in RMC"), ("1000s", "m³ Batched"), ("2", "Major Projects")],
    "jobs": [
        ("2017–2018",   "Plant Supervisor",         "On-Time Readymix",  ["Full plant operations supervision.","Ensured consistent quality and on-time dispatch."]),
        ("2006–2015",   "Supervisor / Batcher / Sales", "Lafarge Readymix", ["High-volume batching on Batchman & AS400 systems.","Sales & orders processing for commercial clients.","Scheduling logistics for truck fleet dispatch.","Custom Excel tools for stock management & planning."]),
        ("2025",        "Software Tools Dev",        "Alpine Cement",     ["Built bespoke reporting dashboard consolidating supplier data.","Replaced manual stock-take sheets with automated Excel workflows."]),
    ],
    "skills": ["Plant Supervision","Concrete Batching","Batchman","AS400","Job Scheduling","Truck Dispatch","Stock Management","Excel Automation","Sales & Orders","Quality Control"],
    "tools":  ["Batchman","AS400","Microsoft Excel","VBA","Teams","Python (custom tools)"],
    "projects": [
        ("Moses Mabhida Stadium", "Concrete supply & logistics for iconic Durban landmark"),
        ("Ixopo Dam",             "High-volume readymix production for civil dam project"),
        ("Stock Tracker (Excel)", "Custom VBA tool for daily stock reconciliation"),
        ("Truck Scheduler",       "Excel-based dispatch board for fleet of delivery trucks"),
    ],
    "education": [("2019","Hyperion Dev","Software Engineering Bootcamp"),("2016","Upskillist","MS Excel Advanced"),("2001","Phoenix Technical Secondary","Matric")],
    "contact": {"📞":"0827882373","✉️":"surjoo@icloud.com","📍":"Durban, South Africa","🐙":"github.com/ss-247"},
    "sites": [("🌐 Old Portfolio","https://satishsurjoo.co.za"),("⚡ Streamlit App","https://streamlit.io")],
},

"funny": {
    "name_html": '🤪 SATISH SURJOO 🤪',
    "tagline": "PROFESSIONAL BUG WHISPERER · CONCRETE WHISPERER · EXCEL WIZARD 🧙",
    "ticker": "☕ COFFEE → CODE → TEST → BUG → PANIC → FIX → REPEAT ☕ " * 4,
    "bio": """Hi! I'm Satish. I spend half my life telling software what it did wrong (QA),
and the other half telling concrete mixers what to do. Surprisingly, concrete listens better. 🏗️
I also build Python apps that do in 5 seconds what used to take someone a whole Monday.
Recruiters: I promise I'm the most interesting person you'll interview today. 😎
(My GitHub commits happen at 2am. That's not insomnia — that's PASSION.)""",
    "stats": [("∞", "☕ Coffees"), ("420+", "🐛 Bugs"), ("13", "Yrs of Chaos")],
    "jobs": [
        ("2025",      "Code Wizard 🧙",        "Alpine Cement",   ["Built dashboard so good, the spreadsheets cried.","Automated Monday mornings out of existence. Colleagues sent thank-you cake."]),
        ("2021–2024", "Professional Bug Finder 🔍", "Easy Games", ["Played slot games for work. Legally. In the name of QA.","Found bugs other testers couldn't — because I actually READ the requirements 📖.","Managed PMs, devs, and stakeholders without losing my mind (mostly)."]),
        ("2006–2015", "Concrete Philosopher 🏗️",  "Lafarge",       ["Mixed cement for 9 years. Learned patience. Concrete teaches patience.","Scheduled trucks. Trucks were late. I became very zen. 🧘","Built Excel tools because the AS400 system was basically a dinosaur 🦕."]),
    ],
    "skills": ["Bug Whispering 🐛","Concrete Diplomacy 🏗️","Excel Sorcery 🧙","Git Blame (others)","Python (and Pythons)","Coffee-Driven Development","Deadline Negotiation","Pretending to Understand Stakeholders"],
    "tools":  ["Coffee ☕","Python 🐍","Excel (100 tabs open)","Git (blame mode ON)","AS400 (pray it works)","Batchman (the mixer, not the hero)"],
    "projects": [
        ("Punters Challenge 🎲",    "Sports betting app. For research purposes. Obviously."),
        ("Cement Tracker 🏗️",       "Dashboard that knows more about cement than I do."),
        ("Moses Mabhida Stadium 🏟️", "Helped build the stadium. Didn't get a free ticket."),
        ("Ixopo Dam 💧",            "Made concrete go into ground. Ground stayed. Success!"),
    ],
    "education": [("2019","Hyperion Dev","Software Bootcamp (survived 🎉)"),("2016","Upskillist","Excel: Advanced (I now dream in VLOOKUP)"),("2001","Phoenix Secondary","Matric (Phase 1 Complete ✅)")],
    "contact": {"📞":"0827882373 (call before 9am, I dare you)","✉️":"surjoo@icloud.com","📍":"Durban (warm, near beach, 10/10)","🐙":"github.com/ss-247 (commit history = therapy)"},
    "sites": [("🌐 Old Portfolio (circa 2019)","https://satishsurjoo.co.za"),("⚡ Streamlit — I built stuff here","https://streamlit.io")],
},

"halloween": {
    "name_html": '💀 SATISH SURJOO 🎃',
    "tagline": "☠️ LURKER OF LEGACY CODE · HAUNTER OF DEADLINES · SPIRIT OF QA ☠️",
    "ticker": "🎃 BUG · 👻 GHOST COMMIT · 💀 LEGACY CODE · 🕷️ REGRESSION · 🦇 DEADLINE · 🕯️ HOTFIX · " * 4,
    "bio": """From the dark depths of Durban's ready-mix plants to the haunted corridors of iGaming QA...
I have survived 9 years of mixing concrete (summoning the grey beast),
3 years hunting software demons (QA is just exorcism with tickets),
and now I conjure Python daemons that automate the mundane.
My code does not sleep. Neither do the bugs I find.
Beware: I am equally comfortable debugging at 3am OR pouring a 200m³ slab at dawn. 🌑""",
    "stats": [("☠️ 13", "Cursed Years"), ("👻 ∞", "Haunted Bugs"), ("🎃 4", "Dark Projects")],
    "jobs": [
        ("2025",      "⚗️ Potion Coder",        "Alpine Cement (Lair)", ["Forged a dark dashboard from scattered supplier scrolls.", "Automated rituals that once took mortals entire Mondays."]),
        ("2021–2024", "🔮 QA Warlock",           "Easy Games (Crypt)",  ["Cast compliance spells on slot machines.", "Managed a coven of developers, PMs, and stakeholders.", "Tracked every cursed change via Git — nothing escapes the log."]),
        ("2006–2015", "🏗️ Concrete Necromancer", "Lafarge (Dungeon)",   ["Summoned thousands of m³ of grey matter from the earth.", "Dispatched iron chariots (trucks) on dark scheduling grimoires.", "Built enchanted Excel tomes for stock and production rituals."]),
    ],
    "skills": ["🔮 Bug Exorcism","🕷️ Regression Testing","💀 Legacy System Survival","🎃 Excel Summoning","🦇 Deadline Evasion","⚗️ Python Alchemy","🕯️ Git Necromancy","👻 Stakeholder Haunting"],
    "tools":  ["🐍 Python (serpent magic)","💀 Git / GitHub (the grimoire)","🎃 Excel / VBA (ancient runes)","👻 SQL (dark queries)","🕯️ Batchman (golem controller)","☠️ AS400 (elder relic)"],
    "projects": [
        ("💀 Cement Tracker",          "Dark dashboard that sees ALL supplier movements"),
        ("🎃 Punters Challenge",        "Cursed sports oracle — predictions from beyond"),
        ("🏟️ Moses Mabhida Stadium",    "Poured the concrete foundations — it still stands..."),
        ("💧 Ixopo Dam",               "Water held back. By MY concrete. You're welcome."),
    ],
    "education": [("2019","Hyperion Dev","Software Engineering (Dark Arts)"),("2016","Upskillist","Excel Sorcery — Advanced Level"),("2001","Phoenix Secondary","Survived The Matric Curse")],
    "contact": {"☠️":"0827882373","🦇":"surjoo@icloud.com","🎃":"Durban, The Haunted Coast","🕸️":"github.com/ss-247"},
    "sites": [("🕯️ Old Lair (Portfolio)","https://satishsurjoo.co.za"),("🔮 Streamlit Sanctum","https://streamlit.io")],
},

}

d = configs[mode]

# ─────────────────────────────────────────────
# TICKER
# ─────────────────────────────────────────────
ticker_text = d["ticker"]
st.markdown(f"""
<div class="ticker-wrap">
  <div class="ticker-inner">{ticker_text}{ticker_text}</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="hero-strip">
  <div class="hero-name">{d["name_html"]}</div>
  <div class="hero-tagline">{d["tagline"]}</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# STATS ROW
# ─────────────────────────────────────────────
stat_html = '<div class="stat-row">'
for num, lbl in d["stats"]:
    stat_html += f'<div class="stat-box"><div class="stat-num">{num}</div><div class="stat-lbl">{lbl}</div></div>'
stat_html += '</div>'
st.markdown(f'<div style="max-width:1200px;margin:0 auto;padding:0 24px;">{stat_html}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# MAIN GRID  (main | sidebar)
# ─────────────────────────────────────────────
st.markdown('<div class="cv-grid">', unsafe_allow_html=True)

# ── LEFT: main content ──
main_html = '<div class="cv-main">'

# Profile
main_html += '<div class="section-label">Profile</div>'
bio_lines = d["bio"].replace("\n","<br>")
main_html += f'<p class="profile-bio">{bio_lines}</p>'

# Websites
main_html += '<div class="sites-bar">'
for label, url in d["sites"]:
    main_html += f'<a class="site-link" href="{url}" target="_blank">{label}</a>'
main_html += '</div>'

# Experience
main_html += '<div class="section-label" style="margin-top:40px;">Experience</div>'
for year, title, company, bullets in d["jobs"]:
    bl = "".join(f"<li>{b}</li>" for b in bullets)
    main_html += f"""
    <div class="job-block">
        <div class="job-year">{year}</div>
        <div class="job-title">{title}</div>
        <div class="job-company">{company}</div>
        <div class="job-desc"><ul>{bl}</ul></div>
    </div>"""

# Projects
main_html += '<div class="section-label" style="margin-top:8px;">Projects</div>'
for pname, pdesc in d["projects"]:
    main_html += f"""
    <div class="proj-card">
        <div class="proj-name">{pname}</div>
        <div class="proj-desc">{pdesc}</div>
    </div>"""

main_html += '</div>'  # cv-main

# ── RIGHT: sidebar ──
side_html = '<div class="cv-sidebar">'

# Contact
side_html += '<div class="section-label">Contact</div>'
side_html += '<div class="contact-line">'
for icon, val in d["contact"].items():
    side_html += f'{icon} {val}<br>'
side_html += '</div>'

# Skills
side_html += '<div class="section-label" style="margin-top:32px;">Skills</div>'
side_html += '<div class="skill-cloud">'
for sk in d["skills"]:
    side_html += f'<span class="skill-pill">{sk}</span>'
side_html += '</div>'

# Tools
side_html += '<div class="section-label" style="margin-top:24px;">Tools</div>'
side_html += '<div class="skill-cloud">'
for t in d["tools"]:
    side_html += f'<span class="skill-pill">{t}</span>'
side_html += '</div>'

# Education
side_html += '<div class="section-label" style="margin-top:24px;">Education</div>'
for year, inst, qual in d["education"]:
    side_html += f"""
    <div class="job-block" style="margin-bottom:16px;">
        <div class="job-year">{year}</div>
        <div class="job-title" style="font-size:14px;">{inst}</div>
        <div class="job-company">{qual}</div>
    </div>"""

side_html += '</div>'  # cv-sidebar

# Render grid
st.markdown(main_html + side_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # cv-grid

# Close theme wrapper
st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ──
footer_color = {"tech":"#00f5d4","concrete":"#f5a623","funny":"#ff6b6b","halloween":"#ff6b00"}[mode]
st.markdown(f"""
<div style="text-align:center;padding:40px;font-family:'Space Mono',monospace;font-size:11px;opacity:0.3;color:{footer_color};">
    SATISH SURJOO · DURBAN · SOUTH AFRICA · {footer_color.upper()} MODE ACTIVE
</div>
""", unsafe_allow_html=True)