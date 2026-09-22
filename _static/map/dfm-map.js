/* ============================================================
   DFM collaboration map
   ─ Danish organisations sit on the Denmark map at their real
     coordinates; dx,dy moves the logo off the city pin and a
     leader line ties it back. role:"member" paints it DFM red.
   ─ Everyone else is a pearl on the ring (an oval, to suit wide
     screens): a circle holding the outline of their country or region,
     with the logo inside and the name below. Pearls are spaced evenly
     in list order, clockwise from north, so keep the order roughly
     geographic.
   ─ A Danish node without a logo uses mode:"label" (name and kicker only).
   ─ Text is given as {en, da}; the page language picks one.
   ─ `detail` is shown in a card when hovering, tapping or focusing a node.
   ─ On narrow screens the map is swapped for a list built from the same
     data (see .home-map__list in home.css).
   Needs window.DFM_GEO (geo.js) and an <svg data-dfm-map> inside
   .home-map to draw into.
   ============================================================ */
(function () {
  const svg = document.querySelector("svg[data-dfm-map]");
  if (!svg || !window.DFM_GEO) return;

  const LANG = (document.documentElement.lang || "en").startsWith("da") ? "da" : "en";
  const t = (v) => (v && typeof v === "object" && !Array.isArray(v) ? v[LANG] || v.en : v);
  const BASE = new URL("./", document.currentScript.src).href;

  const LOGOS = {
    au: { w: 121.0, h: 52.9 }, ku: { w: 145.9, h: 41.7 }, sdu: { w: 118.4, h: 48.8 },
    alex: { w: 167.1, h: 29.3 }, digst: { w: 118.5, h: 39.0 }, lex: { w: 44.0, h: 48.1 },
    ordbogen: { w: 55.1, h: 41.8 }, text: { w: 105.0, h: 35.0, ext: "svg" },
    iceland: { w: 80.3, h: 79.7 }, faroe: { w: 80.0, h: 80.0 }, comparia: { w: 81.7, h: 78.3 },
    mistral: { w: 95.1, h: 67.3 }, apertus: { w: 182.0, h: 17.6 }, euroeval: { w: 75.1, h: 85.2 },
    mteb: { w: 78.5, h: 81.5 }, trustllm: { w: 81.1, h: 78.9 }, gptnl: { w: 154.6, h: 41.4 },
    elexai: { w: 116.5, h: 54.9 }, latvia: { w: 80.0, h: 80.0 }, oslo: { w: 80.0, h: 80.0 },
    gothenburg: { w: 80.0, h: 80.0 }, esilv: { w: 80.0, h: 80.0 },
    polimi: { w: 154.0, h: 44.1 }, openeurollm: { w: 134.0, h: 61.0, ext: "svg" },
    ucloud: { w: 40.0, h: 43.6, ext: "svg" },
  };
  const logoUrl = (id) => `${BASE}logos/${id}.${LOGOS[id].ext || "png"}`;

  const VIEW = { w: 1560, h: 1030 };
  const RING = { cx: 780, cy: 490, rx: 660, ry: 400, pearl: 60 };
  // Denmark is scaled by k and placed so the area centroid of its land
  // (DK_CENTROID, in path units) lands on the centre of the ring
  const DK = { k: 0.62 };
  const DK_CENTROID = { x: 267.9, y: 449.5 };

  // Shared words, so kickers stay consistent between nodes
  const W = {
    partner: { en: "Partner", da: "Partner" },
    usecase: { en: "Use case", da: "Use case" },
    evaluation: { en: "Evaluation", da: "Evaluering" },
    datasets: { en: "Datasets", da: "Datasæt" },
    research: { en: "Research", da: "Forskning" },
    phd: { en: "Industrial PhDs", da: "Erhvervs-ph.d.er" },
    compute: { en: "Compute", da: "Beregningskraft" },
    lexicography: { en: "Lexicography", da: "Leksikografi" },
    openmodels: { en: "Open models", da: "Åbne modeller" },
    basemodel: { en: "Base model", da: "Basismodel" },
    models: { en: "Models", da: "Modeller" },
    copenhagen: { en: "Copenhagen", da: "København" },
    denmark: { en: "Denmark", da: "Danmark" },
    europe: { en: "Europe", da: "Europa" },
    international: { en: "International", da: "International" },
  };
  const k = (...parts) => parts.map(t).join(" · ");

  const NODES = [
    /* ——— Denmark ——— */
    { id: "au", logo: "au", mode: "wordmark", role: "member",
      name: { en: "Aarhus University", da: "Aarhus Universitet" },
      kicker: [k(W.partner, "Aarhus")],
      lat: 56.1629, lon: 10.2039, dx: -330, dy: -150 },
    { id: "text", logo: "text", mode: "wordmark",
      name: { en: "TEXT, Aarhus University", da: "TEXT, Aarhus Universitet" },
      kicker: [k(W.research, "Aarhus")],
      lat: 56.1700, lon: 10.1900, dx: -320, dy: -40,
      detail: {
        en: "Research on cultural and social alignment of language models, and on the effects of AI on society and on how we produce text.",
        da: "Forskning i sprogmodellers kulturelle og sociale alignment og i AI's betydning for samfundet og for den måde, vi producerer tekst på.",
      } },
    { id: "grundtvig", mode: "label",
      name: "Center for Grundtvigforskning",
      kicker: [k(W.datasets, "Aarhus")],
      lat: 56.1680, lon: 10.2000, dx: -345, dy: 55,
      detail: {
        en: "Data work to ensure that Danish history and cultural heritage are represented in the models.",
        da: "Arbejde med data, der sikrer, at dansk historie og kulturarv er repræsenteret i modellerne.",
      } },
    { id: "ku", logo: "ku", mode: "wordmark", role: "member",
      name: { en: "University of Copenhagen", da: "Københavns Universitet" },
      kicker: [k(W.partner, W.copenhagen)],
      lat: 55.6761, lon: 12.5683, dx: -35, dy: -200 },
    { id: "alex", logo: "alex", mode: "wordmark", role: "member",
      name: { en: "Alexandra Institute", da: "Alexandra Instituttet" },
      kicker: [k(W.partner, W.denmark)],
      lat: 55.6620, lon: 12.5900, dx: 110, dy: -75 },
    { id: "sdu", logo: "sdu", mode: "wordmark", role: "member",
      name: { en: "University of Southern Denmark", da: "Syddansk Universitet" },
      kicker: [k(W.partner, "Odense")],
      lat: 55.3617, lon: 10.4295, dx: -310, dy: 60 },
    { id: "ucloud", logo: "ucloud", mode: "mark",
      name: "UCloud", kicker: [k(W.compute, "Sønderborg")],
      lat: 54.9138, lon: 9.7922, dx: -250, dy: 75,
      detail: {
        en: "DFM uses UCloud, the national interactive HPC platform (DeiC Interactive HPC) run by the SDU eScience Center, for compute. Its hardware is housed in a new green data centre in Sønderborg.",
        da: "DFM bruger UCloud, den nationale interaktive HPC-platform (DeiC Interactive HPC) drevet af SDU eScience Center, til beregningskraft. Hardwaren står i et nyt grønt datacenter i Sønderborg.",
      } },
    { id: "lex", logo: "lex", mode: "mark",
      name: "Lex.dk", kicker: [k(W.usecase, W.copenhagen)],
      lat: 55.6790, lon: 12.5760, dx: 60, dy: 72,
      detail: {
        en: "In a collaboration with Aarhus University, Lex seeks to utilise AI to improve democratic accessibility to correct and verified knowledge across Denmark.",
        da: "I et samarbejde med Aarhus Universitet vil Lex bruge AI til at gøre korrekt og verificeret viden mere demokratisk tilgængelig i hele Danmark.",
      } },
    { id: "digst", logo: "digst", mode: "wordmark",
      name: { en: "Agency for Digital Government", da: "Digitaliseringsstyrelsen" },
      kicker: [k(W.evaluation, W.copenhagen), t(W.datasets)],
      lat: 55.6828, lon: 12.5860, dx: -15, dy: 170,
      detail: {
        en: "Work with the Danish public sector on how Danish language models are evaluated, and on opening up public data for training — so models are judged against the settings they will actually be used in.",
        da: "Samarbejde med den danske offentlige sektor om, hvordan danske sprogmodeller evalueres, og om at åbne offentlige data for træning — så modellerne bedømmes i de sammenhænge, de faktisk skal bruges i.",
      } },
    { id: "ordbogen", logo: "ordbogen", mode: "mark",
      name: "Ordbogen", kicker: [k(W.phd, "Odense")],
      lat: 55.3961, lon: 10.3883, dx: -70, dy: 185,
      detail: {
        en: "Industrial PhDs placed between the university and a Danish language-technology company, keeping the research anchored in dictionaries and writing tools people use every day.",
        da: "Erhvervs-ph.d.er placeret mellem universitetet og en dansk sprogteknologivirksomhed, så forskningen er forankret i de ordbøger og skriveværktøjer, folk bruger hver dag.",
      } },

    /* ——— pearls, clockwise from north ——— */
    { id: "oslo", logo: "oslo", plate: "no",
      name: { en: "University of Oslo", da: "Oslo Universitet" },
      kicker: [k("CAALLM", { en: "Norway", da: "Norge" })],
      detail: {
        en: "A partner in CAALLM, a Nordic–Baltic project on adapting language models to the languages and cultures of the region, and on the open datasets that make that possible.",
        da: "Partner i CAALLM, et nordisk-baltisk projekt om at tilpasse sprogmodeller til regionens sprog og kulturer og om de åbne datasæt, der gør det muligt.",
      } },
    { id: "gothenburg", logo: "gothenburg", plate: "se",
      name: { en: "University of Gothenburg", da: "Göteborgs Universitet" },
      kicker: [k("CAALLM", { en: "Sweden", da: "Sverige" })],
      detail: {
        en: "A partner in CAALLM, bringing Swedish language resources into a shared Nordic–Baltic effort to assess and adjust language models for the region.",
        da: "Partner i CAALLM, der bringer svenske sprogressourcer ind i en fælles nordisk-baltisk indsats for at vurdere og tilpasse sprogmodeller til regionen.",
      } },
    { id: "latvia", logo: "latvia", plate: "lv",
      name: { en: "University of Latvia", da: "Letlands Universitet" },
      kicker: [k("CAALLM", { en: "Latvia", da: "Letland" })],
      detail: {
        en: "A partner in CAALLM, extending the work beyond the Nordic languages to Latvian so the project covers the Baltic region as well as Scandinavia.",
        da: "Partner i CAALLM, der udvider arbejdet fra de nordiske sprog til lettisk, så projektet dækker både Baltikum og Skandinavien.",
      } },
    { id: "mteb", logo: "mteb", plate: "world", logoScale: 0.86,
      name: "MTEB", kicker: [k(W.evaluation, W.international)],
      detail: {
        en: "Danish and Nordic tasks contributed to an international benchmark for text embeddings, so models built here can be measured against the global state of the art.",
        da: "Danske og nordiske opgaver bidraget til et internationalt benchmark for tekst-embeddings, så modeller bygget her kan måles mod det bedste i verden.",
      } },
    { id: "euroeval", logo: "euroeval", plate: "eu",
      name: "EuroEval", kicker: [k(W.evaluation, W.europe)],
      detail: {
        en: "Shared evaluation infrastructure for European languages, used to benchmark Danish models alongside their neighbours on comparable tasks.",
        da: "Fælles evalueringsinfrastruktur for europæiske sprog, der bruges til at benchmarke danske modeller side om side med nabosprogene på sammenlignelige opgaver.",
      } },
    { id: "elexai", logo: "elexai", plate: "eu",
      name: "ELEX-AI", kicker: [k(W.lexicography, W.europe)],
      detail: {
        en: "A European infrastructure project connecting lexicography and language models: dictionary data to improve models, and models to help enrich dictionaries.",
        da: "Et europæisk infrastrukturprojekt, der forbinder leksikografi og sprogmodeller: ordbogsdata til at forbedre modellerne og modeller til at berige ordbøgerne.",
      } },
    { id: "trustllm", logo: "trustllm", plate: "eu",
      name: "TrustLLM", kicker: [k(W.openmodels, W.europe)],
      detail: {
        en: "A European effort to build open, trustworthy language models for Europe's languages, sharing data, training practice and evaluation across the participating countries.",
        da: "En europæisk indsats for at bygge åbne, troværdige sprogmodeller til Europas sprog, med fælles data, træningspraksis og evaluering på tværs af de deltagende lande.",
      } },
    { id: "polimi", logo: "polimi", plate: "it",
      name: "Politecnico di Milano", kicker: [k(W.models, { en: "Italy", da: "Italien" })],
      detail: {
        en: "Research on parameter- and compute-efficient post-training and model adaptation.",
        da: "Forskning i parameter- og beregningseffektiv eftertræning og tilpasning af modeller.",
      } },
    { id: "apertus", logo: "apertus", plate: "ch",
      name: "Apertus", kicker: [k(W.basemodel, { en: "Switzerland", da: "Schweiz" })],
      detail: {
        en: "A fully open Swiss base model that DFM post-trains for Danish — one of the European models the project builds on rather than training from scratch.",
        da: "En fuldt åben schweizisk basismodel, som DFM eftertræner til dansk — en af de europæiske modeller, projektet bygger videre på i stedet for at træne fra bunden.",
      } },
    { id: "esilv", logo: "esilv", plate: "fr",
      name: { en: "Léonard de Vinci Engineering School", da: "Léonard de Vinci-ingeniørskolen" },
      kicker: [k(W.models, { en: "France", da: "Frankrig" })],
      detail: {
        en: "Research on efficient recurrent model architectures, such as the one used by Mimir, and on extending them to graphs (think knowledge graphs) and vision (think multimodality).",
        da: "Forskning i effektive rekurrente modelarkitekturer som den, Mimir bygger på, og i at udvide dem til grafer (tænk vidensgrafer) og billeder (tænk multimodalitet).",
      } },
    { id: "mistral", logo: "mistral", plate: "fr",
      name: "Mistral", kicker: [k(W.basemodel, { en: "France", da: "Frankrig" })],
      detail: {
        en: "Openly released European base models that DFM post-trains on Danish data, rather than training from scratch.",
        da: "Åbent udgivne europæiske basismodeller, som DFM eftertræner på danske data i stedet for at træne fra bunden.",
      } },
    { id: "comparia", logo: "comparia", plate: "fr",
      name: "compar:IA", kicker: [k(W.evaluation, { en: "France", da: "Frankrig" })],
      detail: {
        en: "A shared approach to comparing models by human preference, so speakers judge models in their own language rather than through English-centric leaderboards.",
        da: "En fælles tilgang til at sammenligne modeller ud fra menneskelige præferencer, så sprogbrugere bedømmer modellerne på deres eget sprog frem for via engelskcentrerede ranglister.",
      } },
    { id: "openeurollm", logo: "openeurollm", plate: "nl",
      name: "OpenEuroLLM", kicker: [k(W.models, { en: "Netherlands", da: "Holland" }), { en: "through SURF", da: "gennem SURF" }],
      detail: {
        en: "Through SURF, the Dutch IT cooperative for education and research, DFM is part of OpenEuroLLM, working on a multilingual Mimir for the Germanic and wider European languages.",
        da: "Gennem SURF, det hollandske it-kooperativ for uddannelse og forskning, er DFM med i OpenEuroLLM og arbejder på en flersproget Mimir til de germanske og øvrige europæiske sprog.",
      } },
    { id: "gptnl", logo: "gptnl", plate: "nl",
      name: "GPT-NL", kicker: [k(W.datasets, { en: "Netherlands", da: "Holland" })],
      detail: {
        en: "A counterpart initiative for Dutch. The collaboration centres on openly licensed training data, extending the Dynaword approach beyond Danish.",
        da: "Et søsterinitiativ for nederlandsk. Samarbejdet handler om åbent licenserede træningsdata og udvider Dynaword-tilgangen ud over dansk.",
      } },
    { id: "iceland", logo: "iceland", plate: "is",
      name: { en: "University of Iceland", da: "Islands Universitet" },
      kicker: [k(W.datasets, { en: "Iceland", da: "Island" })],
      detail: {
        en: "A dataset collaboration across the North Atlantic, sharing sources and methods so the smaller Nordic languages get resources of the same quality as the large ones.",
        da: "Et datasætsamarbejde på tværs af Nordatlanten, hvor kilder og metoder deles, så de mindre nordiske sprog får ressourcer af samme kvalitet som de store.",
      } },
    { id: "faroe", logo: "faroe", plate: "fo",
      name: { en: "University of the Faroe Islands", da: "Færøernes Universitet" },
      kicker: [k(W.datasets, { en: "Faroe Islands", da: "Færøerne" }), "CAALLM"],
      detail: {
        en: "Part of the same North Atlantic dataset work, and of CAALLM — the Nordic–Baltic project on adapting language models to the region's languages and cultures.",
        da: "En del af det samme nordatlantiske datasætarbejde og af CAALLM — det nordisk-baltiske projekt om at tilpasse sprogmodeller til regionens sprog og kulturer.",
      } },
  ];

  const UI = {
    hint: {
      en: "Hover over or tap a collaborator to read about the work together.",
      da: "Hold musen over eller tryk på en samarbejdspartner for at læse om samarbejdet.",
    },
    member: { en: "DFM partner", da: "DFM-partner" },
    other: { en: "Collaborator", da: "Samarbejdspartner" },
    denmark: { en: "In Denmark", da: "I Danmark" },
    abroad: { en: "Across the Nordics and Europe", da: "I Norden og Europa" },
  };

  /* ---------- projection: equirectangular, standard parallel 56°N ---------- */
  const S = 2.533934, OX = -1146.8864, OY = 14633.7636;
  const KX = Math.cos((56 * Math.PI) / 180) * 100 * S, KY = 100 * S;
  const TX = RING.cx - DK_CENTROID.x * DK.k;
  const TY = RING.cy - DK_CENTROID.y * DK.k;
  const geo = (lon, lat) => [(lon * KX + OX) * DK.k + TX, (-lat * KY + OY) * DK.k + TY];

  const NS = "http://www.w3.org/2000/svg";
  const el = (tag, attrs = {}) => {
    const n = document.createElementNS(NS, tag);
    for (const a in attrs) n.setAttribute(a, attrs[a]);
    return n;
  };
  const html = (tag, cls, content) => {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (content) n.textContent = content;
    return n;
  };
  const text = (x, y, s, cls, anchor) => {
    const n = el("text", { x, y, class: cls });
    if (anchor) n.setAttribute("text-anchor", anchor);
    n.textContent = s;
    return n;
  };
  function wrap(s, max) {
    const out = [];
    let line = "";
    for (const w of s.split(" ")) {
      if ((line + " " + w).trim().length > max) { out.push(line.trim()); line = w; }
      else line += " " + w;
    }
    if (line.trim()) out.push(line.trim());
    return out;
  }

  // Points spaced evenly by arc length along the oval, clockwise from north,
  // offset by half a step so no pearl sits straight above Denmark
  function ovalPoints(count) {
    const STEPS = 3600, pts = [], cum = [0];
    for (let i = 0; i <= STEPS; i++) {
      const a = (i / STEPS) * 2 * Math.PI;
      pts.push([RING.cx + RING.rx * Math.sin(a), RING.cy - RING.ry * Math.cos(a)]);
      if (i) cum.push(cum[i - 1] + Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]));
    }
    const total = cum[STEPS], out = [];
    for (let j = 0, i = 0; j < count; j++) {
      const target = ((j + 0.5) / count) * total;
      while (cum[i] < target) i++;
      out.push(pts[i]);
    }
    return out;
  }

  NODES.forEach((n) => {
    n.name = t(n.name);
    n.kicker = n.kicker.map(t);
    n.detail = t(n.detail);
    n.isGeo = "lat" in n;
  });
  const pearls = NODES.filter((n) => !n.isGeo);
  ovalPoints(pearls.length).forEach(([x, y], i) => { pearls[i].px = x; pearls[i].py = y; });
  NODES.filter((n) => n.isGeo).forEach((n) => {
    [n.ax, n.ay] = geo(n.lon, n.lat);
    n.px = n.ax + (n.dx || 0);
    n.py = n.ay + (n.dy || 0);
  });

  const figure = svg.closest(".home-map");
  svg.setAttribute("viewBox", `0 0 ${VIEW.w} ${VIEW.h}`);
  const defs = svg.appendChild(el("defs"));
  const layers = {};
  for (const name of ["chain", "map", "nodes"]) layers[name] = svg.appendChild(el("g"));

  /* ---------- the ring and Denmark ---------- */
  layers.chain.appendChild(el("ellipse", { cx: RING.cx, cy: RING.cy, rx: RING.rx, ry: RING.ry, class: "chain" }));
  const dk = el("g", { transform: `translate(${TX},${TY}) scale(${DK.k})` });
  dk.appendChild(el("path", { d: DFM_GEO.dk, class: "land" }));
  layers.map.appendChild(dk);

  /* ---------- nodes ---------- */
  const R = RING.pearl;
  const FIT = { w: R * 1.6, h: R * 1.2 }; // logo fit box inside a pearl
  NODES.forEach((n) => {
    const m = n.role === "member" ? " member" : "";
    const grp = el("g", { class: "node", tabindex: "0", role: "button" });
    grp.setAttribute("aria-label", n.name + " — " + n.kicker.join(", "));
    const L = n.logo ? LOGOS[n.logo] : null;

    if (n.isGeo) {
      grp.appendChild(el("path", { d: `M${n.ax},${n.ay} L${n.px},${n.py}`, class: "leader" + m }));
      grp.appendChild(el("circle", { cx: n.ax, cy: n.ay, r: 2.6, class: "pin-dot" + m }));
      grp.appendChild(el("circle", { cx: n.px, cy: n.py, r: 4.6, class: "pin" + m }));
      let cx = n.px + 13, y0;
      if (L) grp.appendChild(el("image", { href: logoUrl(n.logo), x: cx, y: n.py - L.h / 2, width: L.w, height: L.h }));
      if (n.mode === "label") {
        grp.appendChild(text(cx, n.py + 5, n.name, "n-name halo", "start"));
        y0 = n.py + 22;
      } else if (n.mode === "wordmark") {
        y0 = n.py + L.h / 2 + 15;
      } else {
        cx = cx + L.w + 12;
        grp.appendChild(text(cx, n.py + 1, n.name, "n-name halo", "start"));
        y0 = n.py + 18;
      }
      n.kicker.forEach((line, i) =>
        grp.appendChild(text(cx, y0 + i * 14, line.toUpperCase(), "n-kicker halo" + m, "start")));
      const box = L || { w: 120, h: 20 };
      grp.appendChild(el("rect", {
        x: n.px - 24, y: n.py - box.h / 2 - 12, width: box.w + 140,
        height: box.h + 34 + n.kicker.length * 14, class: "hit",
      }));
    } else {
      const art = DFM_GEO.plates[n.plate], cid = "dfm-clip-" + n.id;
      const cp = el("clipPath", { id: cid });
      cp.appendChild(el("circle", { cx: n.px, cy: n.py, r: R - 1 }));
      defs.appendChild(cp);
      grp.appendChild(el("circle", { cx: n.px, cy: n.py, r: R, class: "pearl" }));
      const clipped = el("g", { "clip-path": `url(#${cid})` });
      const scale = (R / 72) * 1; // outlines are drawn for a 72-unit pearl
      const shape = el("g", {
        transform: `translate(${n.px - (art.box * scale) / 2},${n.py - (art.box * scale) / 2}) scale(${scale})`,
      });
      shape.appendChild(el("path", { d: art.d, class: "land flat" }));
      clipped.appendChild(shape);
      grp.appendChild(clipped);
      const s = Math.min(FIT.w / L.w, FIT.h / L.h) * (n.logoScale || 1), lw = L.w * s, lh = L.h * s;
      grp.appendChild(el("image", { href: logoUrl(n.logo), x: n.px - lw / 2, y: n.py - lh / 2, width: lw, height: lh }));
      let y = n.py + R + 22;
      wrap(n.name, 22).forEach((line) => { grp.appendChild(text(n.px, y, line, "p-name halo", "middle")); y += 19; });
      y += 1;
      n.kicker.forEach((line) => { grp.appendChild(text(n.px, y, line.toUpperCase(), "n-kicker halo", "middle")); y += 13; });
      grp.appendChild(el("circle", { cx: n.px, cy: n.py, r: R, class: "hit" }));
    }
    const on = () => focusNode(n), off = () => focusNode(null);
    grp.addEventListener("pointerenter", on);
    grp.addEventListener("focus", on);
    grp.addEventListener("pointerleave", off);
    grp.addEventListener("blur", off);
    n._el = grp;
    layers.nodes.appendChild(grp);
  });

  /* ---------- detail card, placed beside the active node ---------- */
  const stage = svg.parentElement;
  const tip = stage.appendChild(html("div", "home-map__tip"));
  tip.setAttribute("role", "status");
  function focusNode(n) {
    svg.querySelectorAll(".node.on").forEach((e) => e.classList.remove("on"));
    if (!n) {
      svg.classList.remove("busy");
      tip.classList.remove("is-visible");
      return;
    }
    svg.classList.add("busy");
    n._el.classList.add("on");

    tip.textContent = "";
    tip.appendChild(html("strong", "home-map__tip-name", n.name));
    n.kicker.forEach((line) => tip.appendChild(html("span", "home-map__tip-kick" + (n.role === "member" ? " member" : ""), line)));
    if (n.detail) tip.appendChild(html("p", "", n.detail));

    const box = stage.getBoundingClientRect(), r = n._el.getBoundingClientRect();
    const gap = 12, w = tip.offsetWidth, h = tip.offsetHeight;
    const cx = r.left + r.width / 2 - box.left;
    let x = cx > box.width / 2 ? r.left - box.left - w - gap : r.right - box.left + gap;
    x = Math.max(0, Math.min(box.width - w, x));
    let y = r.top + r.height / 2 - box.top - h / 2;
    y = Math.max(0, Math.min(box.height - h, y));
    tip.style.transform = `translate(${x}px, ${y}px)`;
    tip.classList.add("is-visible");
  }

  /* ---------- legend and hint below the map ---------- */
  const legend = figure.appendChild(html("figcaption", "home-map__legend"));
  legend.append(
    html("span", "home-map__key member", t(UI.member)),
    html("span", "home-map__key", t(UI.other)),
    html("span", "home-map__hint", t(UI.hint)),
  );

  /* ---------- list version for narrow screens ---------- */
  const list = figure.appendChild(html("div", "home-map__list"));
  [[t(UI.denmark), NODES.filter((n) => n.isGeo)], [t(UI.abroad), pearls]].forEach(([title, nodes]) => {
    list.appendChild(html("h3", "", title));
    const grid = list.appendChild(html("div", "home-map__cards"));
    nodes.forEach((n) => {
      const card = grid.appendChild(html("div", "home-map__card" + (n.role === "member" ? " member" : "")));
      const head = card.appendChild(html("div", "home-map__card-head"));
      if (n.logo) {
        const img = head.appendChild(html("img"));
        img.src = logoUrl(n.logo);
        img.alt = "";
        img.loading = "lazy";
      }
      const names = head.appendChild(html("div"));
      names.append(html("strong", "", n.name), html("span", "", n.kicker.join(" · ")));
      if (n.detail) card.appendChild(html("p", "", n.detail));
    });
  });
})();
