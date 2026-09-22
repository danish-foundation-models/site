/* Front page: the dot-matrix Denmark in the hero and the latest-news banner.
   Needs window.DFM_GEO (map/geo.js). */
(function () {
  const LANG = (document.documentElement.lang || "en").startsWith("da") ? "da" : "en";
  const NS = "http://www.w3.org/2000/svg";
  const el = (tag, attrs = {}) => {
    const n = document.createElementNS(NS, tag);
    for (const a in attrs) n.setAttribute(a, attrs[a]);
    return n;
  };

  /* ---------- hero: Denmark as a grid of dots, with the partner cities ---------- */
  const visual = document.querySelector(".home-hero__visual");
  if (visual && window.DFM_GEO) {
    // Same projection as the collaboration map (path units of DFM_GEO.dk)
    const S = 2.533934, OX = -1146.8864, OY = 14633.7636;
    const KX = Math.cos((56 * Math.PI) / 180) * 100 * S, KY = 100 * S;
    const project = (lon, lat) => [lon * KX + OX, -lat * KY + OY];
    const CITIES = [
      { name: "Aarhus", lon: 10.2039, lat: 56.1629, label: [22, -14] },
      { name: "Odense", lon: 10.3883, lat: 55.3961, label: [-128, 34] },
      { name: LANG === "da" ? "København" : "Copenhagen", lon: 12.5683, lat: 55.6761, label: [-18, -24], anchor: "end" },
    ];
    const W = 650, H = 810, STEP = 15;

    const canvas = document.createElement("canvas");
    canvas.width = W;
    canvas.height = H;
    const ctx = canvas.getContext("2d");
    const land = new Path2D(DFM_GEO.dk);

    const svg = el("svg", { viewBox: `-20 -20 ${W + 40} ${H + 40}`, "aria-hidden": "true" });
    const dots = el("g");
    for (let y = STEP / 2; y < H; y += STEP) {
      for (let x = STEP / 2; x < W; x += STEP) {
        if (ctx.isPointInPath(land, x, y)) dots.appendChild(el("circle", { cx: x, cy: y, r: 3.4, class: "dot" }));
      }
    }
    svg.appendChild(dots);

    const pts = CITIES.map((c) => project(c.lon, c.lat));
    const curve = ([x1, y1], [x2, y2], bend) => {
      const mx = (x1 + x2) / 2, my = (y1 + y2) / 2, dx = x2 - x1, dy = y2 - y1;
      return `M${x1},${y1} Q${mx - dy * bend},${my + dx * bend} ${x2},${y2}`;
    };
    [[0, 2, 0.25], [1, 2, -0.2], [0, 1, 0.35]].forEach(([a, b, bend]) =>
      svg.appendChild(el("path", { d: curve(pts[a], pts[b], bend), class: "link" })));

    CITIES.forEach((c, i) => {
      const [x, y] = pts[i];
      const pulse = el("circle", { cx: x, cy: y, r: 9, class: "pulse" });
      pulse.style.animationDelay = `${i * 0.8}s`;
      svg.appendChild(pulse);
      svg.appendChild(el("circle", { cx: x, cy: y, r: 7, class: "city" }));
      const label = el("text", { x: x + c.label[0], y: y + c.label[1], class: "city-label", "text-anchor": c.anchor || "start" });
      label.textContent = c.name;
      svg.appendChild(label);
    });
    visual.appendChild(svg);
  }

  /* ---------- header: dark over the hero, white once it has scrolled past ---------- */
  const hero = document.querySelector(".home-hero");
  const header = document.querySelector(".md-header");
  if (hero && header) {
    const update = () =>
      document.body.classList.toggle("dfm-scrolled", hero.getBoundingClientRect().bottom <= header.offsetHeight);
    update();
    addEventListener("scroll", update, { passive: true });
    addEventListener("resize", update);
  }

  /* ---------- latest news, read from the generated news index ---------- */
  const list = document.querySelector(".home-news__items[data-src]");
  if (list) {
    const src = new URL(list.dataset.src, document.baseURI);
    const WORDS = {
      en: { new: "New", read: "Read →" },
      da: { new: "Ny", read: "Læs →" },
    }[LANG];
    const fmt = new Intl.DateTimeFormat(LANG === "da" ? "da-DK" : "en-GB", {
      day: "numeric", month: "short", year: "numeric",
    });

    fetch(src)
      .then((r) => (r.ok ? r.text() : Promise.reject(r.status)))
      .then((html) => {
        const doc = new DOMParser().parseFromString(html, "text/html");
        const posts = [...doc.querySelectorAll("article.md-post")].slice(0, 3);
        if (!posts.length) return;
        list.textContent = "";
        posts.forEach((post) => {
          const link = post.querySelector(".md-post__content h2 a");
          const time = post.querySelector("time[datetime]");
          const meta = [...post.querySelectorAll(".md-meta__item")].map((n) => n.textContent.trim());
          if (!link || !time) return;

          const date = new Date(time.getAttribute("datetime").replace(" ", "T"));
          const isNew = Date.now() - date.getTime() < 30 * 24 * 3600 * 1000;

          const a = document.createElement("a");
          a.className = "home-news__item";
          a.href = new URL(link.getAttribute("href"), src).href;
          const metaRow = document.createElement("span");
          metaRow.className = "home-news__meta";
          if (isNew) {
            const badge = document.createElement("span");
            badge.className = "home-news__new";
            badge.textContent = WORDS.new;
            metaRow.appendChild(badge);
          }
          metaRow.appendChild(document.createTextNode([fmt.format(date), meta[1]].filter(Boolean).join(" · ")));
          const title = document.createElement("span");
          title.className = "home-news__title";
          title.textContent = link.textContent.trim();
          const read = document.createElement("span");
          read.className = "home-news__read";
          read.textContent = WORDS.read;
          a.append(metaRow, title, read);
          list.appendChild(a);
        });
      })
      .catch(() => {}); // keep the static fallback link
  }
})();
