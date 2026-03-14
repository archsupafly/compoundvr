# Game Coverage Framework v1

**Owner:** Richard  
**Date:** 2026-03-14  
**Purpose:** Define what every article package for a given flat game with VR playability must include, how the site should classify/tag it, and what makes coverage commercially valuable rather than generic.

---

## 1. Core Principle

Each game page must answer the reader's real question:

> **"If I want to play this game in VR, what version exists, how hard is it to set up, how well does it work, and is it actually worth my time?"**

That is the editorial product.

Not lore.
Not filler.
Not an SEO summary padded around a YouTube embed.

Every piece of game coverage should reduce uncertainty for the reader and increase trust in the site.

---

## 2. What Counts as a Covered Game

A game qualifies for coverage if at least one of the following is true:

1. **Official hybrid support**  
   A flat game has an officially supported VR mode.

2. **Official standalone VR version**  
   A distinct VR edition exists, even if separate from the flat release.

3. **Full VR mod**  
   A game has a purpose-built VR mod with meaningful gameplay support.

4. **Framework-enabled VR play**  
   A game is meaningfully playable through a framework such as UEVR or similar injector/adapter systems.

The site should cover all four, but never pretend they are equivalent. The classification must be explicit.

---

## 3. The Core Page Model

For each game, the site should eventually support a **coverage package**, not just a single generic post.

### Recommended package structure
1. **Primary game page / pillar page**
   - The canonical page for the game's VR status
   - Best for SEO and updates
   - Should be evergreen and regularly refreshed

2. **Supporting articles** (only when justified)
   - setup guide
   - troubleshooting guide
   - performance guide
   - comparison article
   - update/news piece when the mod/framework meaningfully changes

The primary game page is the mandatory asset. Supporting pieces are optional but valuable when the game has enough audience demand or setup complexity.

---

## 4. Mandatory Reader Questions Every Primary Game Page Must Answer

Every primary game page must answer these questions clearly and early:

1. **Can I play this game in VR?**
2. **What type of VR support is it?**
   - official hybrid
   - official standalone VR version
   - full VR mod
   - framework/injector-based
3. **What do I need to make it work?**
4. **How difficult is setup?**
5. **How complete is the VR implementation?**
6. **How stable is it?**
7. **How good are controls and comfort?**
8. **What performance should I expect?**
9. **Who is this version for?**
10. **Is it worth playing in VR right now?**

If the article misses any of those, it is incomplete.

---

## 5. Required Article Structure for Every Primary Game Page

## 5.1 Hero Summary / Verdict Box
At the top of the page, include a high-signal summary block containing:

- **VR status:** Playable / Limited / Experimental / Not recommended
- **VR type:** Official hybrid / Official standalone / Full mod / Framework-based
- **Current recommendation:** Yes / Conditional / No
- **Setup difficulty:** Easy / Moderate / Hard / Expert-only
- **Controller support:** Motion controls / Gamepad / KBM / mixed
- **Comfort profile:** Comfortable / Moderate / Intense / highly variable
- **Performance profile:** Light / Moderate / Heavy / inconsistent
- **Testing status:** Tested directly / Partially tested / community-reported only
- **Last verified date**
- **Primary install method**

This is the conversion block. It should let a reader decide in under 20 seconds whether to keep reading.

## 5.2 Short Answer Intro
Open with a blunt answer in 2-4 paragraphs:

- whether the game is worth playing in VR
- what kind of VR implementation it uses
- the main tradeoff
- who should bother

Example structure:
- "Yes, but only if you're comfortable with moderate setup friction and occasional jank."
- "No, not yet — the concept works, but the current implementation is too incomplete to recommend broadly."

## 5.3 VR Implementation Overview
Explain exactly what the VR experience is:

- native or modded
- first-person only or partial support
- full 6DOF or limited head-look
- motion controls vs controller emulation
- roomscale/seated expectations
- major missing features
- whether UI/menus/cutscenes break immersion

## 5.4 Install and Requirements
Mandatory install section:

- game store/platform requirements
- required mod/framework/software
- compatible game version/build if relevant
- headset/runtime requirements
- controller/input requirements
- launch steps in plain English
- known install pitfalls
- whether anti-cheat, DRM, or updates can break support

## 5.5 Testing Notes
This is non-negotiable.
Every article should contain a testing disclosure section with:

- hardware used
- headset used
- CPU/GPU/RAM where relevant
- controller/input method
- game version tested
- mod/framework version tested
- playtime tested
- what was personally verified versus sourced from community reports

This is one of the biggest trust signals on the site.

## 5.6 Experience Breakdown
Every page should evaluate at least these categories:

### A. Setup friction
- install clarity
- steps required
- break risk
- maintenance burden after updates

### B. VR functionality
- camera behavior
- scale/world presence
- stereoscopy
- head tracking quality
- motion controller implementation
- interaction fidelity

### C. Playability
- can you actually complete or meaningfully play the game this way
- which modes work
- what breaks progression
- whether certain chapters/areas are problematic

### D. Performance
- approximate performance behavior
- major bottlenecks
- shader compilation stutter if relevant
- recommended settings or compromises

### E. Comfort
- artificial locomotion vs teleport
- cutscene handling
- camera shake issues
- forced camera movement
- vehicle or traversal discomfort
- intensity expectations

### F. Stability and bugs
- crashes
- visual artifacts
- broken UI
- control failures
- save/load issues
- update fragility

### G. Value judgment
- is this a novelty test
- a strong alternative way to play
- a top-tier VR showcase
- or a curiosity better skipped

## 5.7 Who This Is For
Every article should contain a short segmentation section:

- best for VR enthusiasts willing to tinker
- best for fans of the original game
- good for new players vs not good for first-time players
- unsuitable for comfort-sensitive players
- unsuitable for non-technical users

## 5.8 Alternatives / Comparisons
Where useful, note:

- better official VR alternatives
- better mods in the same genre
- whether another version is superior to this route
- whether a standalone VR edition is better than modding the flat game

## 5.9 Final Recommendation
End with a decision-quality conclusion:

- **Recommended**
- **Recommended with caveats**
- **Only for enthusiasts/tinkerers**
- **Wait for updates**
- **Not recommended**

The conclusion must restate the main reason, not just the label.

---

## 6. Required Structured Data Fields / Internal CMS Fields Per Game

The site should store structured fields for every game so pages can power search, filters, comparison pages, and affiliate/commercial opportunities.

## 6.1 Identity Fields
- game title
- franchise
- developer
- publisher
- original release year
- genre
- perspective (first person / third person / mixed)
- engine
- platforms/stores

## 6.2 VR Classification Fields
- VR path type
  - official hybrid
  - official standalone VR edition
  - full VR mod
  - framework-based
- VR implementation owner
  - official developer
  - mod team
  - solo modder
  - framework ecosystem
- install dependency type
  - none
  - separate VR app
  - mod download
  - framework injector
- current support status
  - active
  - abandoned
  - uncertain
  - broken by latest update

## 6.3 Reader-Decision Fields
- recommended status
- setup difficulty
- tinkering level required
- controller type
- motion controls yes/no/partial
- seated/standing/roomscale
- comfort intensity
- performance demand
- stability level
- campaign playable yes/no/partial
- multiplayer playable yes/no/partial
- cutscenes in VR yes/no/partial
- UI readability quality
- save compatibility notes
- last verified date

## 6.4 Business/SEO Fields
- primary keyword target
- search intent type
  - informational
  - commercial investigation
  - navigational
  - troubleshooting
- article type
  - review
  - guide
  - compatibility explainer
  - comparison
- update cadence priority
  - high / medium / low
- evergreen value
  - high / medium / low
- monetization opportunity
  - affiliate headset/accessory
  - Patreon/community support angle
  - sponsorship candidate
  - premium guide candidate
  - low commercial value

---

## 7. Required Tagging / Labels on the Front End

Readers should be able to understand a game at a glance, and the site should be able to filter intelligently.

## 7.1 Mandatory visible labels
Each game page should visibly display:

- **VR type**
- **Recommendation level**
- **Setup difficulty**
- **Tested status**
- **Last verified date**
- **Motion controls support**
- **Comfort level**
- **Performance demand**

## 7.2 Recommended taxonomy tags
Use tags such as:

### VR route tags
- Official Hybrid VR
- Official VR Version
- Full VR Mod
- UEVR
- Injector-Based
- Framework-Based

### Quality/state tags
- Fully Playable
- Partially Playable
- Experimental
- Broken After Update
- Abandoned
- Recently Updated

### Setup tags
- Beginner Friendly
- Some Tinkering Required
- Advanced Setup
- Frequent Maintenance Risk

### Input tags
- Full Motion Controls
- Gamepad Only
- Motion Aiming
- KBM Required
- Seated-Friendly
- Roomscale-Friendly

### Experience tags
- Horror
- Racing
- Shooter
- Third-Person in VR
- Cockpit Game
- Open World
- Performance Heavy
- Comfort Intense

### Commercial/editorial tags
- Best in Class Candidate
- Good First VR Mod
- Hardcore Enthusiast Pick
- Needs Major Caveats
- Historical Interest Only

These tags matter because they make browsing, list-building, internal linking, and sponsored/affiliate packaging much easier.

---

## 8. Writer Deliverables for Each Game

A writer should not turn in just prose. They should turn in a **coverage bundle**.

## Mandatory deliverables
1. **Primary article draft**
2. **Verdict box data**
3. **Structured field sheet / CMS metadata**
4. **Testing notes**
5. **Source log**
6. **Asset list**
7. **SEO package**
8. **Update watch notes**

### 8.1 Primary article draft
Includes all required sections in this framework.

### 8.2 Verdict box data
A clean structured summary with all at-a-glance fields filled out.

### 8.3 Structured field sheet / CMS metadata
All internal tags, classifications, and searchable fields completed.

### 8.4 Testing notes
Writer must submit:
- exact setup tested
- time spent testing
- version/build info
- what worked
- what failed
- unresolved unknowns

### 8.5 Source log
Writers must distinguish:
- direct testing
- mod documentation
- official developer statements
- community reports
- Discord/GitHub issue references

No unsourced claims.

### 8.6 Asset list
At minimum:
- hero image or box art
- 3-6 screenshots showing the VR experience if available
- optional comparison image or performance chart
- alt text / captions

### 8.7 SEO package
Writers should submit:
- target primary keyword
- secondary keywords
- proposed SEO title
- meta description
- URL slug
- suggested internal links
- FAQ candidates
- snippet-friendly short answer

### 8.8 Update watch notes
Include:
- what future updates could invalidate the article
- which mod/framework channels to watch
- whether this page should be revisited after game patches or framework releases

---

## 9. The Standard Article Outline Writers Should Follow

# H1: [Game Title] in VR: Is It Worth Playing?

## Quick Verdict
## Can You Play [Game Title] in VR?
## What Type of VR Support Does It Use?
## How Hard Is It to Set Up?
## What You Need
## How Well Does It Work in Practice?
## Controls, Comfort, and Performance
## Biggest Problems / Known Issues
## Who Should Play It This Way?
## Alternatives and Better Options
## Final Verdict
## FAQ

This outline is search-friendly without becoming spammy.

---

## 10. What Makes Coverage Compelling

Compelling coverage in this niche does not come from word count. It comes from decision value.

## 10.1 What readers actually care about
- Can I trust this page?
- Will this waste my evening?
- Will this make me sick?
- Will it break after I spend an hour installing it?
- Is this better than just playing a native VR game instead?

## 10.2 What makes the site feel different
- clear recommendations
- test disclosures
- honest caveats
- concrete setup expectations
- comparison thinking, not isolated praise
- consistent taxonomies across every game page

## 10.3 What to avoid
- padded game-history intros
- generic plot summaries
- fake review language
- repeating mod page bullet points as though they were reporting
- burying the recommendation under 1,500 words of fluff

The audience is likely arriving from search with a practical question. Respect that.

---

## 11. SEO Strategy Without Becoming a Content Farm

SEO matters, but the right model is **high-intent, evergreen utility SEO**, not bulk low-value publishing.

## 11.1 Primary keyword themes
Each game should usually target one main theme:
- "[Game] VR mod"
- "[Game] in VR"
- "Does [Game] support VR"
- "[Game] UEVR"
- "[Game] VR review"
- "How to play [Game] in VR"

## 11.2 Secondary keyword themes
- setup and install
- controls
- motion controls
- performance
- compatibility
- worth it / review / recommendation

## 11.3 SERP features to target
- featured snippet via direct answer intro
- People Also Ask via FAQ
- comparison/list internal links
- freshness signal via last verified date

## 11.4 SEO rules for writers
- answer the main query in the first screenful
- use the game title + VR path naturally, not mechanically
- include FAQ sections only when useful
- include comparison/internal links to adjacent coverage
- optimize for satisfaction, not just ranking

A page that ranks but does not solve the user's problem will not build trust, links, or repeat traffic.

---

## 12. Traffic and Business Value

The site becomes a business when coverage does more than attract random clicks.

## 12.1 Traffic that matters
Prioritize games/mods that offer at least one of these:
- high search demand
- persistent evergreen demand
- high affiliate relevance
- strong community discussion
- repeat update cycles that justify revisits
- authority-building value even if traffic is moderate

## 12.2 Commercial leverage from each game page
A strong page can support:
- affiliate links for headsets, GPUs, routers, accessories, PC parts
- newsletter capture for mod update tracking
- sponsored coverage only if trust is protected
- premium buyer/setup guides later
- internal links into comparison pages and best-of lists
- market intelligence for future first-party mod opportunities

## 12.3 High-value supporting content opportunities
When justified, game pages can spin off:
- best settings guides
- troubleshooting pages
- mod install walkthroughs
- comparison pages
- update coverage
- "best games for UEVR" or "best official hybrid VR games" lists

---

## 13. Editorial Scoring Recommendation

To maintain consistency, every game page should include internal scoring across a fixed rubric, even if only some scores are displayed publicly.

### Suggested internal scoring buckets (1-5)
- setup friction
- VR implementation quality
- playability/completeness
- controls/input quality
- comfort
- performance efficiency
- stability
- recommendation strength

These scores should support the final recommendation, not replace judgment.

---

## 14. Publication Gate: What a Writer Must Deliver Before an Editor Approves

A game page is not publishable unless it includes:

- direct answer to whether the game is worth playing in VR
- explicit VR classification
- verified install method
- testing disclosure
- clear statement of limitations and caveats
- structured metadata/tags
- SEO title/meta/slugs
- at least one useful asset or visual
- internal links plan
- final recommendation label

If any of those are missing, the piece is draft-quality, not publishable.

---

## 15. Recommended Internal Page Types Per Game

For planning purposes, the site should classify each game into one of these content levels:

### Tier 1: Full coverage candidate
Use for high-interest, high-demand, high-value titles.
Deliver:
- primary game page
- install guide
- troubleshooting/performance guide
- update coverage as needed

### Tier 2: Standard coverage candidate
Deliver:
- primary game page only
- maybe one supporting guide if setup complexity is substantial

### Tier 3: Catalog-only / light coverage candidate
Deliver:
- shorter canonical page with clear verdict and metadata
- no extra articles unless traffic proves out

This prevents wasting editorial effort on low-value long-tail pages.

---

## 16. Writer Checklist

Before filing a draft, the writer must confirm:

- I clearly stated what kind of VR version this is.
- I explained what the reader needs to install/run it.
- I disclosed what I tested personally.
- I separated testing from community claims.
- I described controls, comfort, performance, and stability.
- I stated who this is for and who should avoid it.
- I gave a clear recommendation.
- I filled in all CMS fields/tags.
- I supplied the SEO package.
- I identified whether this page deserves future updates.

---

## 17. Bottom Line

The winning editorial product is not "content about a VR-enabled game."

It is:

> **a trusted decision page that tells readers whether a flat game's VR route is real, usable, painful, impressive, broken, or worth their time.**

That is what earns search traffic, repeat visits, trust, monetization leverage, and eventually product insight.
