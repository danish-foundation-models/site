---
hide:
  - navigation
  - toc
---

<style>
.md-content__inner {
  padding-top: 0 !important;
  margin-top: 0 !important;
}

.md-main__inner {
  margin-top: 0 !important;
  padding-top: 0 !important;
}

.md-content {
  padding-top: 0 !important;
}

.md-typeset > :first-child {
  margin-top: 0 !important;
}

.hero {
  text-align: center;
  padding: 6rem 2rem 5rem;
  background: linear-gradient(135deg, #6b0010 0%, #c8102e 100%);
  width: 100vw;
  margin-left: 50%;
  transform: translateX(-50%);
  margin-bottom: 0;
}

.hero h1 {
  font-size: 3rem;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 1.25rem;
  color: white !important;
}

.hero p {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.85);
  max-width: 1100px;
  margin: 0 auto;
  line-height: 1.7;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.pillars {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  padding: 2rem 0 0;
  margin-bottom: 1rem;
}

.pillar {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pillar-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.5rem;
  height: 2.5rem;
  background: #fce8eb;
  border-radius: 8px;
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.pillar-title {
  display: block;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #1a1a1a;
}

.pillar-desc {
  display: block;
  font-size: 0.9rem;
  color: #555;
  line-height: 1.6;
}

.stories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.story-card {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  color: inherit;
  display: block;
  transition: box-shadow 0.2s, transform 0.2s;
  border-top: 3px solid #c8102e;
}

.story-card:hover {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.14);
  transform: translateY(-2px);
}

.story-card-title {
  display: block;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #1a1a1a;
  transition: color 0.2s;
}

.story-card:hover .story-card-title {
  color: #c8102e;
}

.story-card-more {
  background: transparent;
  box-shadow: none;
  border-top: none;
  border: 2px dashed #ddd;
  justify-content: center;
}

.story-card-more:hover {
  border-color: #c8102e;
  box-shadow: none;
  transform: none;
}

.story-card-more .story-card-title {
  color: #c8102e;
  font-size: 0.95rem;
}

.story-card-more .story-card-desc {
  font-size: 0.85rem;
  color: #888;
}

.story-card-desc {
  display: block;
  font-size: 0.9rem;
  color: #555;
  line-height: 1.6;
}

.resources {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.resource-card {
  background: white;
  border-radius: 12px;
  padding: 1.75rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  color: inherit;
  display: block;
  text-align: center;
  transition: box-shadow 0.2s;
}

.resource-card:hover {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.14);
}

.resource-card-title {
  display: block;
  font-size: 1.1rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.4rem;
  transition: color 0.2s;
}

.resource-card:hover .resource-card-title {
  color: #c8102e;
}

.resource-card-desc {
  display: block;
  font-size: 0.85rem;
  color: #666;
}

.logo-carousel {
  overflow: hidden;
  padding: 2rem 0;
  position: relative;
  width: 100%;
  background: white;
  border-radius: 12px;
  margin: 4rem 0;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
}

.logo-carousel-track {
  display: flex;
  gap: 4rem;
  align-items: center;
  width: fit-content;
  animation: scroll 30s linear infinite;
}

.logo-carousel-track:hover {
  animation-play-state: paused;
}

.logo-carousel a {
  flex-shrink: 0;
  display: flex;
  align-items: center;
}

.logo-carousel img {
  display: block;
  object-fit: contain;
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}
</style>

<div class="hero">
  <h1>Vi bygger fundamentet for dansk AI</h1>
  <p>Sprogmodeller er blevet kritisk infrastruktur — men mindre sprog som dansk risikerer at blive efterladt. Danish Foundation Models er et samarbejde på tværs af danske universiteter og forskningsinstitutioner om at udvikle, evaluere og tilpasse sprog-AI til gavn for det danske samfund.</p>
</div>

<div class="pillars">
  <div class="pillar">
    <span class="pillar-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c8102e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <line x1="2" y1="12" x2="22" y2="12"/>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
      </svg>
    </span>
    <span class="pillar-title">Nationalt initiativ, global rækkevidde</span>
    <span class="pillar-desc">Dansk i fokus — men vores modeller, benchmarks og værktøjer bidrager til det bredere europæiske og globale open source AI-fællesskab.</span>
  </div>
  <div class="pillar">
    <span class="pillar-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c8102e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <rect x="2" y="3" width="6" height="6" rx="1"/>
        <rect x="9" y="3" width="6" height="6" rx="1"/>
        <rect x="16" y="3" width="6" height="6" rx="1"/>
        <rect x="2" y="12" width="6" height="6" rx="1"/>
        <rect x="9" y="12" width="6" height="6" rx="1"/>
        <rect x="16" y="12" width="6" height="6" rx="1"/>
      </svg>
    </span>
    <span class="pillar-title">Hele AI-stakken</span>
    <span class="pillar-desc">Fra træningsdata og modeludvikling til evalueringsbenchmarks og tilpasning i praksis — vi dækker hele pipeline.</span>
  </div>
  <div class="pillar">
    <span class="pillar-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c8102e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2a7 7 0 0 1 7 7c0 3-1.8 5.4-4.5 6.5V17a1 1 0 0 1-1 1h-3a1 1 0 0 1-1-1v-1.5C6.8 14.4 5 12 5 9a7 7 0 0 1 7-7z"/>
        <line x1="9" y1="21" x2="15" y2="21"/>
        <line x1="10" y1="18" x2="14" y2="18"/>
      </svg>
    </span>
    <span class="pillar-title">20+ industrielle anvendelsesscenarier</span>
    <span class="pillar-desc">Bygget i tæt samarbejde med dansk industri og offentlige institutioner for at sikre infrastrukturens relevans i praksis.</span>
  </div>
  <div class="pillar">
    <span class="pillar-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c8102e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
      </svg>
    </span>
    <span class="pillar-title">Åbenhed som grundprincip</span>
    <span class="pillar-desc">Alle modeller, datasæt og forskning er frit tilgængelige — for at sikre transparens, reproducerbarhed og bred adgang.</span>
  </div>
</div>

<div class="logo-carousel">
  <div class="logo-carousel-track">
    <a href="https://www.sdu.dk">
      <img src="./_static/core-team/sdu.png" alt="Syddansk Universitet" style="height: 65px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/au.png" alt="Aarhus Universitet" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ku.dk">
      <img src="./_static/core-team/ku.jpg" alt="Københavns Universitet" style="height: 70px; width: auto;">
    </a>
    <a href="https://alexandra.dk/">
      <img src="./_static/core-team/alexandra.webp" alt="Alexandra Instituttet" style="height: 50px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/chc.png" alt="Center for Humanities Computing Aarhus" style="height: 60px; width: auto;">
    </a>
    <!-- Duplikeret for at skabe sømløs løkke -->
    <a href="https://www.sdu.dk">
      <img src="./_static/core-team/sdu.png" alt="Syddansk Universitet" style="height: 65px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/au.png" alt="Aarhus Universitet" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ku.dk">
      <img src="./_static/core-team/ku.jpg" alt="Københavns Universitet" style="height: 70px; width: auto;">
    </a>
    <a href="https://alexandra.dk/">
      <img src="./_static/core-team/alexandra.webp" alt="Alexandra Instituttet" style="height: 50px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/chc.png" alt="Center for Humanities Computing Aarhus" style="height: 60px; width: auto;">
    </a>
  </div>
</div>

## Vores arbejde

<div class="stories">
  <a class="story-card" href="https://huggingface.co/collections/danish-foundation-models/dynawords">
    <span class="story-card-title">Dynaword</span>
    <span class="story-card-desc">En ramme for udvikling af åbne danske datasæt, der har muliggjort bidrag fra kommuner, erhvervsliv og forskning til fælles sproglig infrastruktur.</span>
  </a>
  <a class="story-card" href="https://euroeval.com">
    <span class="story-card-title">Evaluering til europæisk AI</span>
    <span class="story-card-desc">Gennem EuroEval og MTEB sikrer vi, at dansk er repræsenteret i de vigtigste benchmarks — på tværs af Europa og internationalt.</span>
  </a>
  <a class="story-card">
    <span class="story-card-title">Open source-bidrag</span>
    <span class="story-card-desc">Fra flersproget til multimodal evaluering — DFM bidrager med værktøjer og datasæt brugt langt ud over det dansksprogede miljø.</span>
  </a>
  <a class="story-card story-card-more" href="./news/">
    <span class="story-card-title">Se alle nyheder →</span>
    <span class="story-card-desc">Modeludgivelser, artikler og opdateringer fra projektet.</span>
  </a>
</div>

## Udforsk vores ressourcer

<div class="resources">
  <a class="resource-card" href="https://huggingface.co/danish-foundation-models">
    <span class="resource-card-title">Modeller</span>
    <span class="resource-card-desc">Gennemse og download alle vores modeller på Hugging Face</span>
  </a>
  <a class="resource-card" href="https://huggingface.co/datasets?search=danish-foundation-models">
    <span class="resource-card-title">Datasæt</span>
    <span class="resource-card-desc">Udforsk de datasæt vi bruger til at træne og evaluere vores modeller</span>
  </a>
</div>

## Samarbejde og anvendelse

Praktisk brug er det, der giver AI-infrastruktur mening. Organisationerne nedenfor er både aktive samarbejdspartnere og brugere af DFM's arbejde — på tværs af erhvervsliv, offentlige institutioner og kulturarv. Deres deltagelse former, hvad vi bygger, og sikrer at det er relevant der, hvor det tæller.

<div class="logo-carousel">
  <div class="logo-carousel-track">
    <a href="https://www.alvenir.ai/">
      <img src="./_static/collaborators-logos/alvenir.png" alt="Alvenir" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ordbogen.com/">
      <img src="./_static/collaborators-logos/ordbogen_com.png" alt="Ordbogen.com" style="height: 65px; width: auto;">
    </a>
    <a href="https://digst.dk/">
      <img src="./_static/collaborators-logos/digst.webp" alt="Digitaliseringsstyrelsen" style="height: 55px; width: auto;">
    </a>
    <a href="https://lex.dk/">
      <img src="./_static/collaborators-logos/lex.png" alt="Lex.dk" style="height: 55px; width: auto;">
    </a>
    <a href="https://arts.au.dk/forskning/forskningscentre-og-programmer/text">
      <img src="./_static/collaborators-logos/text.svg" alt="TEXT" style="height: 50px; width: auto;">
    </a>
    <!-- Duplikeret for sømløs løkke -->
    <a href="https://www.alvenir.ai/">
      <img src="./_static/collaborators-logos/alvenir.png" alt="Alvenir" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ordbogen.com/">
      <img src="./_static/collaborators-logos/ordbogen_com.png" alt="Ordbogen.com" style="height: 65px; width: auto;">
    </a>
    <a href="https://digst.dk/">
      <img src="./_static/collaborators-logos/digst.webp" alt="Digitaliseringsstyrelsen" style="height: 55px; width: auto;">
    </a>
    <a href="https://lex.dk/">
      <img src="./_static/collaborators-logos/lex.png" alt="Lex.dk" style="height: 55px; width: auto;">
    </a>
    <a href="https://arts.au.dk/forskning/forskningscentre-og-programmer/text">
      <img src="./_static/collaborators-logos/text.svg" alt="TEXT" style="height: 50px; width: auto;">
    </a>
  </div>
</div>
