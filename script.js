const MODES=[
  ["tech","⚡ Tech · QA · Dev"],
  ["concrete","🏗️  Concrete Pro"],
  ["funny","😂 LOL CV"],
  ["halloween","💀 MUHAHA CV"],
  ["services","🛠 Services"]
];

const DATA={
  tech:{
    eyebrow:"DEVELOPER · QA ENGINEER · PROJECT MANAGER",
    name:"SATISH <em>SURJOO</em>",
    bio:["Experienced iGaming QA Tester & Project Manager in regulated slots and casino environments.","Focused on text accuracy, compliance, and cross-team coordination.","Proficient in Git/GitHub for managing updates, iterations, and release tracking.","Builder of bespoke Python tools that turn raw data into actionable dashboards."],
    ticker:"PYTHON · GIT · GITHUB · QA · AGILE · STREAMLIT · SQL · VBA · EXCEL · PROCESS AUTOMATION · iGAMING · COMPLIANCE · CI/CD · ".repeat(3),
    stats:[["13+","Years Exp"],["100+","Bugs Squashed"],["∞","Commits"]],
    jobs:[
      ["2025","Software Developer","Alpine Cement",["Built custom Python + Streamlit dashboard consolidating multi-format supplier reports into a unified live view.","Automated data pipelines — saved hours of weekly manual reconciliation for the operations team.","Designed an interface clean enough for non-technical staff to operate independently every day."]],
      ["2021 – 2024","iGaming QA Tester & Project Manager","Easy Games",["Owned full QA lifecycle for regulated slot & casino game releases across multiple jurisdictions.","Managed stakeholder communication, compliance sign-off, and coordinated cross-team releases.","Implemented Git-based review workflow for content change tracking and iteration history.","Drove process improvements that reduced re-test cycles and shortened release windows."]],
      ["2017 – 2018","Plant Supervisor","On-Time Readymix",["Supervised plant operations and maintained production schedules under high-demand conditions."]],
      ["2006 – 2015","Supervisor / Batcher / Sales","Lafarge Readymix",["High-volume batching, sales & orders, and scheduling logistics for major civil projects.","Built custom Excel automation tools for stock management and production planning."]]
    ],
    projects:[["Cement Tracker","Python + Excel dashboard consolidating live supplier data across multiple formats"],["Punters Challenge","QA & PM tasks on initial release of sports betting app"],["Moses Mabhida Stadium","Plant supervision & batching high quality concrete"],["Ixopo Dam","Plant supervision & concrete logistics for large-scale civil works"]],
    skills:["Project Management","Software QA & Testing","Git / GitHub","Python","SQL","VBA","Excel — Advanced","Data Analysis","Agile / Scrum","Stakeholder Communication","Process Automation","Compliance & Regulatory"],
    tools:["Python","Streamlit","Git / GitHub","Microsoft 365","Excel / VBA","SQL","GitHub Actions"],
    edu:[["2019","Hyperion Dev","Software Engineering Bootcamp"],["2016","Upskillist","Microsoft Excel — Advanced"],["2001","Phoenix Technical Secondary","Matric"]],
    contact:[["📞","<a href='tel:+27827882373'>0827882373</a>"],["✉️","<a href='mailto:surjoo@icloud.com'>surjoo@icloud.com</a>"],["📍","<a href='https://maps.google.com/?q=Durban,South+Africa' target='_blank' rel='noopener'>Durban, South Africa</a>"],["🐙","<a href='https://github.com/ss-247' target='_blank' rel='noopener'>github.com/ss-247</a>"]],
    links:[["🌐 Old Portfolio","https://ss247.github.io/Satish_Surjoo_profile/"],["⚡ Live Streamlit App","https://fleetcost.streamlit.app/"],["⚡ Sample Website Design","https://ss-247.github.io/services"]]
  },
  concrete:{
    eyebrow:"RMC PLANT SUPERVISOR · BATCHER · SCHEDULER",
    name:"SATISH <em>SURJOO</em>",
    bio:["Ready-Mix Concrete professional with 13 years across batching, supervision, sales & order management.","Specialized in accurate mix production, quality/safety compliance, and inventory control.","Fleet coordination and job scheduling to ensure on-time delivery and customer satisfaction.","Built custom Excel tools for production planning, stock management, truck dispatching & scheduling."],
    ticker:"BATCHMAN · AS400 · LAFARGE · READY-MIX · CONCRETE · PLANT OPS · SCHEDULING · LOGISTICS · STOCK CONTROL · TRUCK DISPATCH · ".repeat(3),
    stats:[["13","Yrs RMC"],["1000s","m³ Batched"],["2","Major Projects"]],
    jobs:[
      ["2017 – 2018","Plant Supervisor","On-Time Readymix",["Full plant operations supervision ensuring quality output and on-time dispatch.","Maintained production schedules in a high-demand commercial environment."]],
      ["2006 – 2015","Supervisor / Batcher / Sales","Lafarge Readymix",["High-volume batching on Batchman & AS400 systems for commercial and civil clients.","Sales & orders processing — managed accounts for major construction projects.","Scheduling logistics for truck fleet dispatch, reducing idle time and delivery delays.","Designed custom Excel VBA tools for daily stock reconciliation and production planning."]],
      ["2025","Software & Tools Developer","Alpine Cement",["Built bespoke reporting dashboard consolidating multi-supplier data formats.","Replaced manual stock-take sheets with automated, error-free Excel workflows.","Enabled management to view live plant status without opening a single file."]]
    ],
    projects:[["Moses Mabhida Stadium","Concrete supply, scheduling & quality for Durban's iconic stadium — delivered on time"],["Ixopo Dam","High-volume readymix production and logistics for major civil dam project"],["Stock Tracker (Excel/VBA)","Custom tool for daily stock reconciliation & automatic ordering thresholds"],["Truck Dispatch Board","Excel-based fleet scheduler — zero missed deliveries, full audit trail"]],
    skills:["Plant Supervision","Concrete Batching","Batchman","AS400","Job Scheduling","Truck Dispatch & Fleet","Stock Management","Excel Automation (VBA)","Sales & Orders","Quality Control","Team Leadership","Process Optimization"],
    tools:["Batchman","AS400","Microsoft Excel","VBA","MS Teams","Python (custom tools)"],
    edu:[["2019","Hyperion Dev","Software Engineering Bootcamp"],["2016","Upskillist","MS Excel — Advanced"],["2001","Phoenix Technical Secondary","Matric"]],
    contact:[["📞","<a href='tel:+27827882373'>0827882373</a>"],["✉️","<a href='mailto:surjoo@icloud.com'>surjoo@icloud.com</a>"],["📍","<a href='https://maps.google.com/?q=Durban,South+Africa' target='_blank' rel='noopener'>Durban, South Africa</a>"],["🐙","<a href='https://github.com/ss-247' target='_blank' rel='noopener'>github.com/ss-247</a>"]],
    links:[["🌐 Portfolio","https://ss247.github.io/Satish_Surjoo_profile/"],["⚡ Streamlit App","https://fleetcost.streamlit.app/"],["⚡ Sample Website Design","https://ss-247.github.io/services"]]
  },
  funny:{
    eyebrow:"🏆 PROFESSIONAL BUG WHISPERER · CONCRETE PHILOSOPHER · EXCEL SORCERER 🧙",
    name:"🤪 SATISH <em>SURJOO</em> 🤪",
    bio:["Hi! I'm Satish. I spend half my life telling software what it did wrong (QA) and the other half telling concrete mixers what to do. Spoiler: concrete listens better. 🏗️","I also build Python apps that do in 5 seconds what used to ruin someone's entire Monday morning. ☕","My GitHub commits happen at 2am. That's not insomnia — that's PASSION. 🔥","Recruiters: I am statistically the most interesting person you'll interview this week. Possibly this year."],
    ticker:"☕ COFFEE → CODE → TEST → BUG → PANIC → FIX → DEPLOY → COFFEE → REPEAT → ".repeat(3),
    stats:[["∞","☕ Coffees"],["420+","🐛 Bugs Zapped"],["13","Yrs of Chaos"]],
    jobs:[
      ["2025","Code Wizard 🧙","Alpine Cement",["Built a dashboard so good the spreadsheets literally cried. 😭","Automated Monday mornings out of existence. One colleague sent actual cake as thanks.","Powered by Python, caffeine, and mild existential dread."]],
      ["2021 – 2024","Professional Bug Finder 🔍","Easy Games (iGaming)",["Played slot games for work. Legally. In the name of QA. 🎰","Found bugs other testers couldn't — because I ACTUALLY READ THE REQUIREMENTS. 📖","Managed PMs, devs, and stakeholders simultaneously without losing my mind. (Mostly.)","Tracked every change in Git because 'I thought I fixed it' is not a release note."]],
      ["2006 – 2015","Concrete Philosopher 🏗️","Lafarge Readymix",["Mixed concrete for 9 years. Concrete teaches patience. Concrete does not care about your feelings.","Scheduled trucks. Trucks were late. I became very zen. 🧘","Built Excel tools because the AS400 system was basically a dinosaur in a suit. 🦕"]]
    ],
    projects:[["Punters Challenge 🎲","Sports oracle app. For research purposes. Obviously. It has a leaderboard."],["Cement Tracker 🏗️","Dashboard that now knows more about cement than I do. Which is saying a lot."],["Moses Mabhida Stadium 🏟️","Helped pour the foundation. Did not receive complimentary tickets. Still bitter."],["Ixopo Dam 💧","Made concrete go into ground. Ground stayed. A triumph of engineering."]],
    skills:["Bug Whispering 🐛","Concrete Diplomacy 🏗️","Excel Sorcery 🧙","Git Blame (Others)","Python (and actual Pythons)","Coffee-Driven Development ☕","Deadline Negotiation","Pretending to Understand Stakeholders 😇"],
    tools:["Coffee ☕ (primary tool)","Python 🐍","Excel (100 tabs open)","Git (blame mode: ON)","AS400 (pray before using)","Batchman (the mixer, not the hero)"],
    edu:[["2019","Hyperion Dev","Software Bootcamp — SURVIVED 🎉"],["2016","Upskillist","Excel Advanced (I dream in VLOOKUP)"],["2001","Phoenix Secondary","Matric — Phase 1 Complete ✅"]],
    contact:[["📞","<a href='tel:+27827882373'>0827882373 (please not before 9am)</a>"],["✉️","<a href='mailto:surjoo@icloud.com'>surjoo@icloud.com</a>"],["📍","<a href='https://maps.google.com/?q=Durban,South+Africa' target='_blank' rel='noopener'>Durban (warm, near beach, highly rated)</a>"],["🐙","<a href='https://github.com/ss-247' target='_blank' rel='noopener'>github.com/ss-247 (commit log = therapy)</a>"]],
    links:[["🌐 Old Portfolio (2019 vibes)","https://ss-247.github.io/Satish_Surjoo_profile/"],["⚡ Streamlit — I built stuff here","https://fleetcost.streamlit.app/"],["⚡ Sample Free Click Now","https://ss-247.github.io/services"]]
  },
  halloween:{
    eyebrow:"☠️ LURKER OF LEGACY CODE · HAUNTER OF DEADLINES · SPIRIT OF QA ☠️",
    name:"💀 SATISH <em>SURJOO</em> 🎃",
    bio:["From the dark depths of Durban's ready-mix plants to the haunted corridors of iGaming QA...","Nine years summoning the grey beast (concrete), three years hunting software demons (QA is just exorcism with tickets),","and now I conjure Python daemons that automate the mundane and make dashboards rise from the void.","My code does not sleep. Neither do the bugs I find. Proceed with caution."],
    ticker:"🎃 BUG · 👻 GHOST COMMIT · 💀 LEGACY CODE · 🕷️ REGRESSION · 🦇 DEADLINE · 🕯️ HOTFIX · ⚗️ PYTHON DAEMON · ☠️ ".repeat(3),
    stats:[["☠️ 13","Cursed Years"],["👻 ∞","Haunted Bugs"],["🎃 4","Dark Projects"]],
    jobs:[
      ["2025","⚗️ Potion Coder","Alpine Cement (The Lair)",["Forged a living dashboard from scattered supplier scrolls and cursed CSV files.","Automated rituals that once consumed mortals' entire Mondays without mercy.","The dashboard now breathes on its own. This was intentional. Mostly."]],
      ["2021 – 2024","🔮 QA Warlock","Easy Games (The Crypt)",["Cast compliance spells on slot machines in regulated gaming realms.","Managed a coven of developers, PMs, and stakeholders with arcane coordination.","Tracked every cursed change via Git — nothing escapes the eternal log.","Shortened release cycles using dark agile rituals and kanban sorcery."]],
      ["2006 – 2015","🏗️ Concrete Necromancer","Lafarge Readymix (The Dungeon)",["Summoned thousands of m³ of grey matter from the earth itself.","Dispatched iron chariots (trucks) using enchanted Excel scheduling grimoires.","Built custom Excel tomes that outlasted my tenure. They haunt the plant still."]]
    ],
    projects:[["💀 Cement Tracker","Dark dashboard that sees ALL supplier movements across the realm"],["🎃 Punters Challenge","Cursed sports oracle — predictions delivered from beyond the veil"],["🏟️ Moses Mabhida Stadium","Poured the concrete foundations — it still stands... for now"],["💧 Ixopo Dam","The water is held back by MY concrete. You're welcome, Ixopo."]],
    skills:["🔮 Bug Exorcism","🕷️ Regression Witchcraft","💀 Legacy System Survival","🎃 Excel Summoning","🦇 Deadline Evasion","⚗️ Python Alchemy","🕯️ Git Necromancy","👻 Stakeholder Haunting","☠️ Compliance Curses"],
    tools:["🐍 Python (serpent magic)","💀 Git / GitHub (the eternal grimoire)","🎃 Excel / VBA (ancient runes)","👻 SQL (dark queries from the deep)","🕯️ Batchman (golem controller)","☠️ AS400 (elder relic — use with caution)"],
    edu:[["2019","Hyperion Dev","Software Engineering — The Dark Arts"],["2016","Upskillist","Excel Sorcery, Advanced Tier"],["2001","Phoenix Secondary","Survived The Matric Curse"]],
    contact:[["☠️","<a href='tel:+27827882373'>0827882373</a>"],["🦇","<a href='mailto:surjoo@icloud.com'>surjoo@icloud.com</a>"],["🎃","<a href='https://maps.google.com/?q=Durban,South+Africa' target='_blank' rel='noopener'>Durban, The Haunted Coast</a>"],["🕸️","<a href='https://github.com/ss-247' target='_blank' rel='noopener'>github.com/ss-247</a>"]],
    links:[["🕯️ Old Lair (Portfolio)","https://ss247.github.io/Satish_Surjoo_profile/"],["🔮 Streamlit Sanctum","https://fleetcost.streamlit.app/"],["⚡ Do Not Click Here","https://ss-247.github.io/services"]]
  }
};

const ACCENT={tech:'#00f5d4',concrete:'#f5a623',funny:'#ff6b6b',halloween:'#bf5cf3'};
const PROJ_A={tech:'#0066ff',concrete:'#e85d04',funny:'#6bcb77',halloween:'#1aff8c'};
const PILL_S={
  tech:"background:#00f5d412;border:1px solid #00f5d433;color:#00f5d4;",
  concrete:"background:#f5a62312;border:1px solid #f5a62333;color:#f5a623;",
  funny:"background:#ffd93d22;border:1px solid #ffd93d88;color:#8a6400;border-radius:20px;font-family:'Comic Neue',cursive;",
  halloween:"background:#bf5cf315;border:1px solid #bf5cf333;color:#d490ff;"
};
const BG={tech:'#0a0c10',concrete:'#0e0c08',funny:'#fdf6e3',halloween:'#06030e',services:'#080a0e'};
const MUSIC_STREAM_URL='https://edge.iono.fm/xice/ecr_live_high.aac';
let isPlaying=false;
let currentMode='services';

function makeNav(mode){
  const modeButtons=MODES.map(([m,l])=>`<button class="nav-btn ${m===mode?'active':''}" data-mode="${m}">${l}</button>`).join('');
  return `${modeButtons}<button class="nav-btn" id="musicBtn" type="button">▶ Play Music</button>`;
}
function bindNav(mode){
  currentMode=mode;
  for(const btn of document.querySelectorAll('.nav-btn')){
    if(btn.id==='musicBtn') continue;
    btn.addEventListener('click',()=>render(btn.dataset.mode));
  }
  bindMusicButton();
}

function bindMusicButton(){
  const btn=document.getElementById('musicBtn');
  const audio=document.getElementById('ecrPlayer');
  if(!btn||!audio) return;

  if(audio.getAttribute('src')!==MUSIC_STREAM_URL){
    audio.src=MUSIC_STREAM_URL;
  }

  isPlaying=!audio.paused;
  updateMusicButtonText();

  btn.addEventListener('click',()=>toggleMusic());
  btn.addEventListener('mouseenter',()=>{
    if(currentMode==='funny') btn.textContent='🤣 Press if your CV needs a soundtrack';
    if(currentMode==='halloween') btn.textContent='🦇 Summon spooky radio from the void';
  });
  btn.addEventListener('mouseleave',()=>updateMusicButtonText());
}

function updateMusicButtonText(){
  const btn=document.getElementById('musicBtn');
  if(!btn) return;
  btn.textContent=isPlaying?'❚❚ Pause Music':'▶ Play Music';
}

function toggleMusic(){
  const audio=document.getElementById('ecrPlayer');
  if(!audio) return;
  if(isPlaying){
    audio.pause();
  }else{
    audio.play();
  }
  isPlaying=!isPlaying;
  updateMusicButtonText();
}

function renderServices(nav){
  document.body.style.background=BG.services;
  document.getElementById('app').innerHTML=`
<div class="theme-services">
  <div class="nav-bar">${nav}</div>
  <div class="ticker-wrap"><div class="ticker-inner">${('WEB DESIGN · PYTHON TOOLS · EXCEL AUTOMATION · DASHBOARDS · WORDPRESS · FLEET SYSTEMS · STOCK CONTROL · DURBAN · SOUTH AFRICA · ').repeat(4)}</div></div>
  <div class="svc-hero">
    <div class="svc-eyebrow">Developer · Durban &amp; Remote</div>
    <div class="svc-title">I BUILD TOOLS<em>for the industries I know.</em></div>
    <p class="svc-pitch"><strong>13 years hands-on in ready-mix concrete plants</strong> and 3 years in regulated software QA have given me a clear view of the daily challenges operators face. Today, I create custom websites, automation tools, and dashboards designed to solve real operational problems — built from the perspective of someone who’s actually been in your shoes, not just theorizing from the outside.<br><br>I work primarily with <strong>construction companies, ready-mix plants, fleet operators, truck managers, and small business owners</strong> who are still handling key processes manually and are ready for smarter, more efficient systems that fit their workflow.</p>
    <div class="market-strip">
      <span class="market-tag">🏗️ Construction</span>
      <span class="market-tag">🚛 Fleet &amp; Logistics</span>
      <span class="market-tag">🏭 RMC Plants</span>
      <span class="market-tag">📦 Stock &amp; Inventory</span>
      <span class="market-tag">🔧 Small Business</span>
      <span class="market-tag">📊 Operations Teams</span>
      <span class="market-tag">🌍 Remote Clients</span>
    </div>
  </div>



  <div class="svc-sec-title" style="margin-top:8px;">Online</div>
  <div class="svc-demo-wrap">
    <div class="svc-demo-card">
      <div>
        <div class="svc-demo-eyebrow">Live App · Python + Streamlit</div>
        <div class="svc-demo-name">FleetCost: Truck Cost Management</div>
        <p class="svc-demo-desc">A real fleet management and cost-tracking application built for truck operators. Tracks fuel logs, expenses, maintenance costs and generates per-vehicle reports. Check it out, Log in with Google, auto creates an account. Free to try.</p>
      </div>
      <a class="svc-demo-btn" href="https://fleetcost.streamlit.app/" target="_blank" rel="noopener">View Live App</a>
    </div>
  </div>

  <div class="svc-demo-wrap">
    <div class="svc-demo-card">
      <div>
        <div class="svc-demo-eyebrow">Sample Website · Dashboards + Features</div>
        <div class="svc-demo-name">DevCraft: Demo Website</div>
        <p class="svc-demo-desc">A sample website with demo features you can click through. Listen to some music while you browse this page Read the latest stories in andaround Durban.</p>
      </div>
      <a class="svc-demo-btn" href="https://ss-247.github.io/services" target="_blank" rel="noopener">Sample Web Design</a>
    </div>
  </div>



  <div class="svc-sec-title">What I Build</div>
  <div class="svc-grid">
    <div class="svc-card c1">
      <span class="svc-icon">🌐</span>
      <div class="svc-name">Website Design</div>
      <div class="svc-tagline">Custom-built. Fast. Mobile-first. Functional</div>
      <ul class="svc-bullets">        
        <li>Portfolio sites, landing pages, business websites</li>
        <li>Optimised for mobile and fast on slow connections</li>
        <li>SEO-ready from day one</li>
        <li>Ideal for contractors, suppliers, plant operators</li>
        <li>Hand coded HTML/CSS/JS. </li>
      </ul>
      <a class="svc-cta-link" href="mailto:surjoo@icloud.com?subject=Website Design Enquiry">Let's talk</a>
    </div>


    <div class="svc-card c2">
      <span class="svc-icon">🏗️</span>
      <div class="svc-name">WordPress Design</div>
      <div class="svc-tagline">You manage the content. I build the machine.</div>
      <ul class="svc-bullets">
        <li>Theme setup and full customisation</li>
        <li>Plugin configuration and optimisation</li>
        <li>Client can edit content after handover</li>
        <li>WooCommerce integration if needed</li>
        <li>Best for businesses needing self-management post-launch</li>
      </ul>
      <a class="svc-cta-link" href="mailto:surjoo@icloud.com?subject=WordPress Design Enquiry">Let's talk</a>
    </div>


    <div class="svc-card c3">
      <span class="svc-icon">🐍</span>
      <div class="svc-name">Python Tools &amp; Automation</div>
      <div class="svc-tagline">Replace manual work with scripts that just run.</div>
      <ul class="svc-bullets">
        <li>Custom scripts for data processing and file operations</li>
        <li>Scheduled automations that run without you</li>
        <li>PDF, Excel and report generators</li>
        <li>Multi-source data consolidation</li>
        <li>Ideal for plant managers and operations teams</li>
      </ul>
      <a class="svc-cta-link" href="mailto:surjoo@icloud.com?subject=Python Automation Enquiry">Let's talk</a>
    </div>


    <div class="svc-card c4">
      <span class="svc-icon">📊</span>
      <div class="svc-name">Dashboards &amp; Reports</div>
      <div class="svc-tagline">See your whole operation on one screen.</div>
      <ul class="svc-bullets">
        <li>Streamlit or Excel-based live dashboards</li>
        <li>Multi-supplier and multi-source data consolidation</li>
        <li>Fleet summaries, stock overviews, production reports</li>
        <li>One view replacing 10 spreadsheets</li>
        <li>Built for RMC plants, logistics and ops managers</li>
      </ul>
      <a class="svc-cta-link" href="mailto:surjoo@icloud.com?subject=Dashboard Enquiry">Let's talk</a>
    </div>


    <div class="svc-card c5">
      <span class="svc-icon">📋</span>
      <div class="svc-name">Excel Automation &amp; VBA</div>
      <div class="svc-tagline">One click where there used to be a Monday morning.</div>
      <ul class="svc-bullets">
        <li>Replace repetitive spreadsheet tasks with macros</li>
        <li>Stock-take, scheduling and ordering tools</li>
        <li>One-click report generation from raw data</li>
        <li>Works in Excel you already have — no new software</li>
        <li>For any business still doing things by hand</li>
      </ul>
      <a class="svc-cta-link" href="mailto:surjoo@icloud.com?subject=Excel Automation Enquiry">Let's talk</a>
    </div>


    <div class="svc-card c6">
      <span class="svc-icon">🚛</span>
      <div class="svc-name">Fleet &amp; Stock Management</div>
      <div class="svc-tagline">Built for the industry. Not adapted from something else.</div>
      <ul class="svc-bullets">
        <li>Truck dispatch and scheduling trackers</li>
        <li>Stock management and inventory control systems</li>
        <li>Designed specifically for construction and RMC</li>
        <li>Built on Excel or Python — no expensive licensing</li>
        <li>Run locally or on the web</li>
      </ul>
      <a class="svc-cta-link" href="mailto:surjoo@icloud.com?subject=Fleet &amp; Stock System Enquiry">Let's talk</a>
    </div>
  </div>
  
  <div class="svc-bottom-cta">
    <div class="svc-bottom-title">Ready to get something built?</div>
    <p class="svc-bottom-sub">Tell me what problem you're trying to solve.<br>We can chat about a digital solution.</p>
    <div class="svc-btns">
      <a class="svc-btn-p" href="mailto:surjoo@icloud.com?subject=Project Enquiry">✉️ &nbsp;surjoo@icloud.com</a>
      <a class="svc-btn-s" href="tel:+27827882373">📞 &nbsp;0827882373</a>
    </div>
  </div>


  <div style="text-align:center;padding:0 0 60px;font-family:'Space Mono',monospace;font-size:10px;letter-spacing:3px;color:#1a1f2e;text-transform:uppercase;">
    SATISH SURJOO · DURBAN · SOUTH AFRICA
  </div>
</div>`;
  bindNav('services');
  window.location.hash='services';
}

function render(mode){
  document.body.style.background=BG[mode]||'#0a0c10';
  const nav=makeNav(mode);
  if(mode==='services'){renderServices(nav);return;}

  const d=DATA[mode];
  const accent=ACCENT[mode];
  const bats=mode==='halloween'?'<div class="bat">🦇</div><div class="bat">🦇</div><div class="bat">🦇</div><div class="bat">🦇</div>':'';
  const bio=d.bio.map(l=>`<p>${l}</p>`).join('');
  const links=d.links.map(([l,u])=>`<a class="hero-link" href="${u}" target="_blank" rel="noopener">${l}</a>`).join('');
  const stats=d.stats.map(([n,l])=>`<div class="stat-box"><div class="stat-num">${n}</div><div class="stat-lbl">${l}</div></div>`).join('');
  const jobs=d.jobs.map(([y,t,c,b])=>`<div class="job-card"><div class="jc-year">${y}</div><div class="jc-title">${t}</div><div class="jc-co">${c}</div><ul>${b.map(x=>`<li>${x}</li>`).join('')}</ul></div>`).join('');
  const projects=d.projects.map(([n,desc])=>`<div class="proj-card" style="border-top:3px solid ${PROJ_A[mode]};"><div class="pc-name">${n}</div><div class="pc-desc">${desc}</div></div>`).join('');
  const contact=d.contact.map(([i,v])=>`<div class="contact-line"><span class="ci">${i}</span>${v}</div>`).join('');
  const skills=d.skills.map(s=>`<span class="pill" style="${PILL_S[mode]}">${s}</span>`).join('');
  const tools=d.tools.map(t=>`<span class="pill" style="${PILL_S[mode]}">${t}</span>`).join('');
  const edu=d.edu.map(([y,i,q])=>`<div class="edu-block" style="border-color:${accent}33;"><div class="e-year">${y}</div><div class="e-inst">${i}</div><div class="e-qual">${q}</div></div>`).join('');

  document.getElementById('app').innerHTML=`
<div class="theme-${mode}">
  ${bats}
  <div class="nav-bar">${nav}</div>
  <div class="ticker-wrap"><div class="ticker-inner">${d.ticker}${d.ticker}</div></div>
  <div class="hero">
    <div class="hero-eyebrow">${d.eyebrow}</div>
    <div class="hero-name">${d.name}</div>
    <div class="hero-sub">${bio}</div>
    <div class="hero-links">${links}</div>
  </div>
  <div class="stats-row">${stats}</div>
  <div class="cv-layout">
    <div class="cv-main">
      <div class="sec-title" style="color:${accent}">Experience</div>
      ${jobs}
      <div class="sec-title" style="color:${accent};margin-top:28px;">Projects</div>
      ${projects}
    </div>
    <div class="cv-side">
      <div class="sec-title" style="color:${accent}">Contact</div>
      <div class="contact-block">${contact}</div>
      <div class="sec-title" style="color:${accent}">Skills</div>
      <div class="pill-group">${skills}</div>
      <div class="sec-title" style="color:${accent}">Tools</div>
      <div class="pill-group">${tools}</div>
      <div class="sec-title" style="color:${accent};margin-top:4px;">Education</div>
      ${edu}
    </div>
  </div>
  <div style="text-align:center;padding:44px 0 64px;font-family:'Space Mono',monospace;font-size:10px;letter-spacing:3px;color:${accent};opacity:0.28;text-transform:uppercase;">
    Satish Surjoo &nbsp;·&nbsp; Durban, South Africa &nbsp;·&nbsp; 
  </div>
</div>`;
  bindNav(mode);
  window.location.hash=mode;
}

render(window.location.hash.replace('#','')||'tech');
