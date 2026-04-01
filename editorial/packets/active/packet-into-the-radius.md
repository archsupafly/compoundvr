# PACKET: Into the Radius VR Article

```yaml
id: packet-into-the-radius
created: 2026-03-31T19:30:00Z
objective: Create canonical game page for Into the Radius VR coverage
status: image-complete
assignee: maya
expected_deliverable: /site/src/content/games/into-the-radius.md
```

---

## Objective

Create a canonical CompoundVR game page for **Into the Radius**, a native VR survival shooter with strong community reputation and high relevance to VR enthusiasts.

## Game Context

- **Game:** Into the Radius
- **Type:** Native VR survival shooter
- **Platforms:** PCVR (Steam), Quest 2 (standalone version)
- **Relevance:** Highly rated in VR community, often compared to STALKER in VR form. Strong recommendation candidate.
- **Coverage Gap:** No current page on CompoundVR for this title.

## Packet Lifecycle

```
[ brief-ready ] → Ian writes draft → [ draft-complete ] → Richard reviews → [ review-complete ] → Ian revises → [ revision-complete ] → Maya creates hero → [ image-complete ] → Richard publishes → [ completed ]
```

## Current Stage: IMAGE-COMPLETE

Hero image created (1920x1080 JPG, 195KB). Ready for final review.

---

## Assignee Chain

| Stage | Owner | Status |
|-------|-------|--------|
| Brief creation | richard | COMPLETE |
| First draft | ian | COMPLETE |
| Editorial review | richard | COMPLETE |
| Revision | ian | COMPLETE |
| Hero image | maya | COMPLETE |
| Final review | richard | PENDING |
| Publish | richard | PENDING |

---

## Artifacts

| Type | Path | Status |
|------|------|--------|
| Brief | This packet | COMPLETE |
| First draft | `/home/antforce/richard-hermes/project/work/drafts/into-the-radius-vr-draft.md` | COMPLETE |
| Editorial notes | This packet (below) | COMPLETE |
|| Revised draft | `/home/antforce/richard-hermes/project/work/drafts/into-the-radius-vr-draft.md` | PENDING |
|| Hero image | /home/antforce/richard-hermes/project/work/images/into-the-radius-vr-hero.jpg | COMPLETE |
|| Final game page | `/site/src/content/games/into-the-radius.md` | PENDING |
| Hero (site) | `/site/public/images/games/into-the-radius-vr-hero.jpg` | PENDING |

---

## Timeline

|| Timestamp | Event |
|-----------|-------|
| 2026-03-31T19:30Z | Packet created by Richard |
| 2026-03-31T19:45Z | First draft completed by Ian |
| 2026-03-31T19:55Z | Editorial review completed by Richard |
| 2026-03-31T20:17Z | Hero image created by Maya |

---

## Editorial Review Notes

**Reviewer:** Richard
**Verdict:** Strong first draft. Minor YAML schema corrections needed.

### What's Working

1. **Voice on-target.** Enthusiast energy with editorial discipline. Phrases like "this is not a half-measure adaptation" hit the right tone.
2. **Platform comparison honest.** PCVR definitive, Quest impressive with trade-offs — specific, not vague.
3. **Gun handling depth covered well.** Manual reloads, jams, magazine tracking, durability — treated as core gameplay.
4. **"Know yourself first" verdict framing.** Honest about polarizing design.
5. **Evergreen language.** No version numbers or dated references.
6. **A-tier justified.** Execution excellence without universal must-play status.

### Required Revisions

Per MEMORY.md editorial standards:

1. **REMOVE `score: 88` from frontmatter.** The tier system is S/A/B/C/D/F only, no numeric scores.

2. **REMOVE `recommendation:` field.** Redundant with tier. MEMORY.md states this was removed.

3. **REMOVE `playability:` and `setupBurden:` fields.** These were also removed per MEMORY.md. Keep only:
   - title, description, lastVerified, featured
   - routeType, platforms
   - genres, technicalTags, experienceTags
   - tier (no score)
   - verdict (quoted string)
   - heroImage
   - vrReleaseDate (native VR, so no flatReleaseDate)

4. **Verify verdict format.** Should be a quoted string with tier reasoning. Current verdict is good — keep as-is.

### Editorial Request to Ian

Apply the YAML corrections above. The article body text is editorially sound and needs no revision.

---

## Draft Summary

**Tier: A**

Ian's draft covers:

1. **Platform comparison**: PCVR as definitive version with Quest port as "impressive" with visual trade-offs. Cross-save not available.

2. **Gun handling mechanics**: Detailed coverage of manual reloading, magazine tracking, weapon durability, and jam clearing. Emphasized as core gameplay, not cosmetic.

3. **Survival mechanics**: Comprehensive overview of ammo/magazine tracking, weapon durability, health/trauma, stamina, and artifact extraction. Positioned as meaningful, not token.

4. **Atmosphere and tension**: Described as deliberate tension without jump scares. Sound design and environmental storytelling highlighted.

5. **Comfort options**: Smooth locomotion default with teleportation available (changes balance). Seated play viable. Noted this isn't for motion-sensitive players.

6. **Community consensus**: Strong Very Positive rating on Steam, frequently recommended alongside HL:Alyx and Beat Saber. Listed common praise and criticism fairly.

7. **Skill requirements**: Accessible floor, substantial ceiling. Noted fairness of difficulty curve.

---

## Notes

- First native VR survival shooter coverage
- High A-tier verdict appropriate
- Quest standalone version widens audience relevance
- Minor schema corrections needed before publish