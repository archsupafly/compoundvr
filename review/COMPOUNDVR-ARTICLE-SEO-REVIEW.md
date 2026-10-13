# CompoundVR Article SEO Review — Checklist

Human-readable companion to the `article-seo-review` skill. Run this on a draft before publish, or on a live page that isn't performing. Roughly ten minutes.

Owner of this process: **Richard** (approval) · Reviewer: Lupe (SEO) or Ian (self-check) · Publish path: Richard only.

---

## 0. Before you start

Three things needed, or stop and ask:

- File path under `src/content/` — draft or live.
- What this review decides: pre-publish, title/meta fix, or a page that isn't ranking.
- Target query, if the author has one.

A review never publishes. It produces findings and exact edits for approval.

---

## 1. Intent first

Write a one-line answer to "what does this page answer that nothing else on the site does?"

- Game page → "should I play this"
- Guide → "how do I install and run this"

Two pages can't hold the same intent. If both a game page and a guide exist for one title, confirm the game page owns the brand and review queries, and the guide owns the how-to and install queries. Neither absorbs the other's job.

---

## 2. Title

Check in this order:

- **Cannibalization** — grep `src/content/` for existing pages targeting the same head term. Two pages sharing a head term split the query and Google picks one. Fix by assigning the brand name to the entity page and the how-to term to the guide. **This is the highest-value finding on the list; catch it before anything else.**
- **Matches site convention** — colon separator, head term before the colon, at most one modifier after it. (All 71 existing article titles use a colon.)
- **Curly apostrophe**, matching the rest of the site.
- **Survives SERP truncation** at ~60 characters.
- **Overflow keywords go into `description:`**, not into more title words.

Worked example — Simon's Destiny guide:

| | Title |
|---|---|
| ✅ | `How to Play Castlevania VR on Quest for Free: Simon's Destiny Setup Guide` |
| ❌ | `Castlevania: Simon's Destiny VR: Complete Installation & Optimization Guide` |

The second one leads with the game name and competes with the game page for the branded query. Front-load the head term; let the entity page keep the name.

---

## 3. Description

One sentence or ~150 characters, whichever is shorter. This is where tool names and model numbers belong when they don't fit the title: QuestZDoom, SideQuest, Quest 2/3.

> How to install and play Castlevania: Simon's Destiny VR on Quest 2 and Quest 3 for free — QuestZDoom and SideQuest sideloading steps, performance settings, and fixes.

---

## 4. `relatedPages` block

- Every `id` must match a real file. Dead ids are crawl-path bookmarks that fail.
- **The note rule:** one sentence or 150 characters, whichever is shorter. Explicit `note` only when it adds context the target page's own `description` cannot. Otherwise omit it and let the description render.
- Never restate the title. The same note string repeated across many pages is a failure signal.
- **Cap is five.** A longer list silently drops entries in the render.

```yaml
relatedPages:
  - id: castlevania-ii-simon-s-quest
    kind: article
  - id: doom-3-bfg
    kind: article
```

---

## 5. Links and images

- Every `](/games/x)` / `](/articles/x)` matches a real file.
- Every `/images/` path exists under `public/images/`.
- Body images: descriptive filename, alt text stating **what the screenshot proves**. No filler images.
- The set is reciprocal: a hub or listicle covering the topic should list the page, and the page should list the hub.

---

## 6. Guides only — content checklist

From the guide-structure rules (full version: `references/guide-structure.md`):

- [ ] **One primary intent** — install and run this, nothing else.
- [ ] **Headings use query words.** Installation, download, prerequisites, headset compatibility, controls, performance, errors, troubleshooting, FAQ. No clever labels.
- [ ] **Answer first.** Quick-start steps and links above the fold; explanation underneath. Returning users get steps, not an introduction.
- [ ] **Exact technical specificity** — filenames, versions, launcher names, settings, error strings, folder paths, validated fixes. Verify each version string before publishing and record when.
- [ ] **Original screenshots** of the real flow: download selection, folder contents, bindings, performance options, successful launch.
- [ ] **Date changes mean substance.** `history:` entry per meaningful revision. Never bump a date for a no-change republish.
- [ ] **Structured data** where accurate — schema clarifies, it doesn't rank.

**The rule:** don't write a guide designed to look definitive to Google. Build the guide that deserves to be the definitive result, then make its structure and details easy for Google to understand.

---

## 7. Verify the build

```bash
npx astro build
```

Then grep the built HTML in `dist/` for expected links, note text, and image srcs. The built page is the artifact — markdown alone proves nothing. Count rendered items to confirm the five-item cap held.

---

## 8. Verify live

After deploy, `curl` the page. A missing result is usually deploy lag, not failure: retry once, and before reporting a problem check that a link from an older, already-deployed commit renders on the same page.

---

## Reporting

Findings in priority order. Each one: observation + `file:line` evidence → mechanism → smallest change → how we'd know it failed.

Label heuristics as heuristics. Cite data claims with source, date range, property. Missing data is reported as missing — never interpolated.

Close with what the build rendered and what the live page returned.
