# CompoundVR Article SEO Review — Checklist

Human-readable companion to the `article-seo-review` skill. Run this on any draft before publish, or on a live page that isn't performing. Roughly ten minutes.

**Covers every page type:** game pages, guides, listicles, news, comparisons, and opinion.

Owner of this process: **Richard** (approval) · Reviewer: Lupe (SEO) or Ian (self-check) · Publish path: Richard only.

---

## 0. Before you start

Three things needed, or stop and ask:

- File path under `src/content/` — draft or live.
- What this review decides: pre-publish, title/meta fix, or a page that isn't ranking.
- Target query, if the author has one.

A review never publishes. It produces findings and exact edits for approval.

---

## 1. Identify the type, then the intent

| Where to look | Type |
|---|---|
| `src/content/games/` | Game page |
| `listicle: true` | Listicle (still one of the categories below) |
| `category: news` | News |
| `category: guide` | Guide |
| `category: comparison` | Comparison |
| `category: opinion` | Opinion |

Write a one-line answer to **"what does this page answer that nothing else on the site does?"**

| Type | Intent |
|---|---|
| Game page | Should I play this, and what will it cost me |
| Guide | How do I install and run this |
| Listicle | Which of these should I pick |
| News | What changed, and when |
| Comparison | Which should I choose, for me |
| Opinion | Why this matters |

Two pages can't hold the same intent. Where both a game page and a guide exist for one title, the game page owns the brand and review queries and the guide owns the how-to and install queries. Neither absorbs the other's job — link them to each other.

The rest of this review is shaped by the answer. Get it wrong and every finding scores the wrong target.

---

## 2. Title

Check in this order:

- **Cannibalization** — grep `src/content/games/` *and* `src/content/articles/` for existing pages targeting the same head term. Two pages sharing a head term split the query and Google picks one, usually the weaker. Fix by assigning the brand name to the entity page and the how-to term to the guide. **This is the highest-value finding on the list; catch it before anything else.**
- **Matches site convention** — colon separator, head term before the colon, at most one modifier after it. (All 71 existing article titles use a colon.)
- **Curly apostrophe**, matching the rest of the site.
- **Survives SERP truncation** at ~60 characters.
- **Overflow keywords go into `description:`**, not into more title words.

Per-type title shapes:

| Type | Shape | Example |
|---|---|---|
| Game page | Brand/name first | `Castlevania: Simon's Destiny VR` |
| Guide | How-to head term, brand after colon | `How to Play Castlevania VR on Quest for Free: Simon's Destiny Setup Guide` |
| Listicle | `Top N <Modifier> <Topic>` | `Top 10 VR Games to Play in 2015` |
| Comparison | `X vs Y: <the real question>` | `Quest 1 vs Quest 2: Is the Upgrade Worth It?` |
| News | Entity plus change, fact-shaped | `DLSS 5 Modded Into Skyrim: What Nvidia's Hottest Tech Means for VR` |
| Opinion | Pointed, but never over-promising | `Apple Vision Pro: Brilliant Hardware, Absurd Math` |

Worked example — a guide that competes with its own game page:

| | Title |
|---|---|
| ✅ | `How to Play Castlevania VR on Quest for Free: Simon's Destiny Setup Guide` |
| ❌ | `Castlevania: Simon's Destiny VR: Complete Installation & Optimization Guide` |

The second one leads with the game name and splits the branded query with the game page. Front-load the head term; let the entity page keep the name.

---

## 3. Description

One sentence or ~150 characters, whichever is shorter. Tool names, model numbers, and version strings belong here when they don't fit the title.

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

**Reciprocal placement.** Where a hub or listicle already covers the topic, the entry must exist in *both* directions. One crawled detail page linking to an uncrawled hub unlocks every spoke that hub links out to; a game-to-game link does not.

---

## 5. Links and images

- Every `](/games/x)` / `](/articles/x)` matches a real file.
- Every `/images/` path exists under `public/images/`.
- Body images: descriptive filename, alt text stating **what the image proves**. No filler images.
- Decorative related-page thumbs stay `alt=""` by design — don't "fix" that.

---

## 6. Per-type content checklist

Find your type below and work the list.

### Game page

- [ ] Schema fields filled **and consistent with the verdict prose**: `routeType`, `recommendation`, `playability`, `setupBurden`, `comfort`, `performance`, `inputStyle`, `vrReleaseDate`, `platforms`. An empty field is a finding; a field contradicting the body is critical.
- [ ] **No `## Scoring` table.** Ten pages had one; they were removed on 2026-10-13 and the rule is now enforced. A per-category `/5` table adds nothing the verdict and spec grid don't already carry, the scales ran in inconsistent directions (higher-is-better on most rows, inverted on `Setup Friction`), and no JSON-LD is emitted, so nothing feeds structured data. Score through the schema fields only — `tier`, `recommendation` — never in prose.
- [ ] No guide intent (install / how-to) absorbed into the page — those live in the linked guide.
- [ ] `relatedPages` points at this title's guide plus cluster peers.
- [ ] A reader can tell whether to play within a few paragraphs.

### Guide

- [ ] **One primary intent** — install and run this, nothing else.
- [ ] **Headings use query words.** Installation, download, prerequisites, headset compatibility, controls, performance, errors, troubleshooting, FAQ. No clever labels.
- [ ] **Answer first.** Quick-start steps and links above the fold; explanation underneath. Returning users get steps, not an introduction.
- [ ] **Exact technical specificity** — filenames, versions, launcher names, settings, error strings, folder paths, validated fixes. Verify each version string before publishing and record when.
- [ ] **Original screenshots** of the real flow: download selection, folder contents, bindings, performance options, successful launch.
- [ ] **Date changes mean substance.** `history:` entry per meaningful revision. Never bump a date for a no-change republish.
- [ ] **Structured data** where accurate — schema clarifies, it doesn't rank.

### Listicle

- [ ] Number in the title; ranking criterion stated up front.
- [ ] Criteria in the intro → entries in rank order → conclusion carrying the cutoff logic. One-paragraph verdict plus a link per entry; same for honorable mentions.
- [ ] **Every entry has a thumbnail**, `![Alt](/images/games/x-hero.jpg)` under the heading. A missing thumb on one entry and not its siblings is the signature finding here.
- [ ] Treat it as a hub: reciprocal `relatedPages` on every entry that's a real member. This is the highest-leverage structural check for this type.
- [ ] Entries that leave a platform get removed, not left to rot.

### News

- [ ] **Delta in the first sentence** — what shipped or changed, on what date, what it means for owners of the affected hardware.
- [ ] `pubDate` is the real publish date. Never backdate; never bump for a republication. Revisions go in `history:` with their own date and note.
- [ ] Fact-shaped title; avoid superlatives that force constant revision.
- [ ] If the story implies a follow-up (launch, fix, measurement), the day-28 check is recorded — or don't write it.

### Comparison

- [ ] **Verdict per user type, early.** A comparison that never commits has failed.
- [ ] Compared on attributes that actually differ in VR play: comfort, setup burden, resolution and refresh, library, tethering, weight — not marketing bullets.
- [ ] `X vs Y: <the real question>` title.

### Opinion

- [ ] **Claim and stakes in the first paragraph**, not after the scene-setting.
- [ ] Every data claim cited with source, date range, property. Heuristics labeled as heuristics. Fabricated numbers do the most damage here because the form invites them.
- [ ] `author` field set — an unattributed opinion has no E-E-A-T.
- [ ] Title doesn't promise what the body doesn't deliver.

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

## 9. New page type?

Fall through to sections 0–5 and 8, answer the intent question in section 1, and **record the gap** so the type gains a section here instead of being silently skipped.

---

## Reporting

Findings in priority order. Each one: observation + `file:line` evidence → mechanism → smallest change → how we'd know it failed.

Label heuristics as heuristics. Cite data claims with source, date range, property. Missing data is reported as missing — never interpolated.

Close with what the build rendered and what the live page returned.

**The rule that governs the whole thing:** don't write a page designed to *look* definitive to Google. Build the page that deserves to be the definitive result, then make its structure, language, and technical details easy for Google to understand.
