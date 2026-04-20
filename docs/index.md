---
hide:
  - navigation
  - toc
---

<style>
.hero {
  text-align: center;
  padding: 5rem 2rem 3rem;
}

.hero h1 {
  font-size: 3rem;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 1.25rem;
}

.hero p {
  font-size: 1.2rem;
  color: #555;
  max-width: 1100px;
  margin: 0 auto 2rem;
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
  transition: box-shadow 0.2s;
}

.story-card:hover {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.14);
}

.story-card-title {
  display: block;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #c8102e;
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
  color: #c8102e;
  margin-bottom: 0.4rem;
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
  <h1>Building the Foundation of Danish AI</h1>
  <p>Language models have become critical infrastructure — but smaller languages like Danish risk being left behind. Danish Foundation Models is a collaborative effort across Danish universities and research institutions to develop, evaluate, and adapt open language AI that serves Danish society.</p>
</div>

<div class="pillars">
  <div class="pillar">
    <span class="pillar-title">National Initiative, International Reach</span>
    <span class="pillar-desc">Danish in focus — but our models, benchmarks, and tools contribute to the broader European and global open-source AI community.</span>
  </div>
  <div class="pillar">
    <span class="pillar-title">The Full AI Stack</span>
    <span class="pillar-desc">From training data and model development to evaluation benchmarks and real-world adaptation — we cover the entire pipeline.</span>
  </div>
  <div class="pillar">
    <span class="pillar-title">20+ Industry Use Cases</span>
    <span class="pillar-desc">Built in close partnership with Danish industry and public institutions to ensure the infrastructure is relevant where it matters.</span>
  </div>
  <div class="pillar">
    <span class="pillar-title">Open by Design</span>
    <span class="pillar-desc">All models, datasets, and research are freely available — enabling transparency, reproducibility, and broad access.</span>
  </div>
</div>

<div class="logo-carousel">
  <div class="logo-carousel-track">
    <a href="https://www.sdu.dk">
      <img src="./_static/core-team/sdu.png" alt="University of Southern Denmark" style="height: 65px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/au.png" alt="Aarhus University" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ku.dk">
      <img src="./_static/core-team/ku.jpg" alt="University of Copenhagen" style="height: 70px; width: auto;">
    </a>
    <a href="https://alexandra.dk/">
      <img src="./_static/core-team/alexandra.webp" alt="Alexandra Institute" style="height: 50px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/chc.png" alt="Center for Humanities Computing Aarhus" style="height: 60px; width: auto;">
    </a>
    <!-- Duplicated for now to make it seamless, but if we add more we don't need it -->
    <a href="https://www.sdu.dk">
      <img src="./_static/core-team/sdu.png" alt="University of Southern Denmark" style="height: 65px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/au.png" alt="Aarhus University" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ku.dk">
      <img src="./_static/core-team/ku.jpg" alt="University of Copenhagen" style="height: 70px; width: auto;">
    </a>
    <a href="https://alexandra.dk/">
      <img src="./_static/core-team/alexandra.webp" alt="Alexandra Institute" style="height: 50px; width: auto;">
    </a>
    <a href="https://chc.au.dk/">
      <img src="./_static/core-team/chc.png" alt="Center for Humanities Computing Aarhus" style="height: 60px; width: auto;">
    </a>
  </div>
</div>

## Our Work

<div class="stories">
  <a class="story-card" href="https://huggingface.co/collections/danish-foundation-models/dynawords">
    <span class="story-card-title">Dynaword</span>
    <span class="story-card-desc">A continuously updated collection of Danish word resources and linguistic infrastructure, built to support the next generation of Danish NLP.</span>
  </a>
  <a class="story-card" href="https://euroeval.com">
    <span class="story-card-title">Evaluation for European AI</span>
    <span class="story-card-desc">Through EuroEval and MTEB we develop and maintain evaluation benchmarks for both generative and search models — across Danish and other European languages.</span>
  </a>
  <a class="story-card" href="https://github.com/centre-for-humanities-computing/danish-foundation-models">
    <span class="story-card-title">Open Source Contributions</span>
    <span class="story-card-desc">From deduplication pipelines to multilingual benchmarks — DFM contributes tools and datasets used well beyond the Danish language community.</span>
  </a>
  <a class="story-card" href="./news/">
    <span class="story-card-title">Latest News</span>
    <span class="story-card-desc">Follow our work — from new model releases and dataset updates to research findings and community contributions.</span>
  </a>
</div>

## Explore Our Resources

<div class="resources">
  <a class="resource-card" href="https://huggingface.co/danish-foundation-models">
    <span class="resource-card-title">Models</span>
    <span class="resource-card-desc">Browse and download all of our models on Hugging Face</span>
  </a>
  <a class="resource-card" href="https://huggingface.co/datasets?search=danish-foundation-models">
    <span class="resource-card-title">Datasets</span>
    <span class="resource-card-desc">Explore the datasets we use to train and evaluate our models</span>
  </a>
</div>

## Adoption and Collaboration

Real-world use is what makes AI infrastructure matter. The organisations below represent both active collaborators and adopters of DFM's work — spanning industry, public institutions, and cultural heritage. Their involvement shapes what we build and ensures it is relevant where it counts.

<div class="logo-carousel">
  <div class="logo-carousel-track">
    <a href="https://www.alvenir.ai/">
      <img src="./_static/collaborators-logos/alvenir.png" alt="Alvenir" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ordbogen.com/">
      <img src="./_static/collaborators-logos/ordbogen_com.png" alt="Ordbogen.com" style="height: 65px; width: auto;">
    </a>
    <a href="https://digst.dk/">
      <img src="./_static/collaborators-logos/digst.webp" alt="Agency for Digital Government" style="height: 55px; width: auto;">
    </a>
    <a href="https://lex.dk/">
      <img src="./_static/collaborators-logos/lex.png" alt="Lex.dk" style="height: 55px; width: auto;">
    </a>
    <!-- Duplicated to make seamless loop -->
    <a href="https://www.alvenir.ai/">
      <img src="./_static/collaborators-logos/alvenir.png" alt="Alvenir" style="height: 60px; width: auto;">
    </a>
    <a href="https://www.ordbogen.com/">
      <img src="./_static/collaborators-logos/ordbogen_com.png" alt="Ordbogen.com" style="height: 65px; width: auto;">
    </a>
    <a href="https://digst.dk/">
      <img src="./_static/collaborators-logos/digst.webp" alt="Agency for Digital Government" style="height: 55px; width: auto;">
    </a>
    <a href="https://lex.dk/">
      <img src="./_static/collaborators-logos/lex.png" alt="Lex.dk" style="height: 55px; width: auto;">
    </a>
  </div>
</div>
