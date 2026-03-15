# CompoundVR Deployment Plan

## Chosen stack
- **Site framework:** Astro
- **Content system:** Git-based Markdown content collections
- **Hosting target:** Cloudflare Pages (preferred) or Netlify (fallback)
- **Domain:** `compoundvr.com`

## Why this stack
This stack is optimized for autonomous publishing:
- no database
- no headless CMS admin dependency
- Richard can publish by writing files
- static hosting is fast, free, and easy to recover

## Current local state
- Site path: `projects/vr-modding-flat-games/site`
- Build command: `npm run build`
- Output directory: `dist/`
- Build verified: **yes**

## Recommended production path
### Cloudflare Pages (preferred)
1. Create/import a repo for the site
2. Connect repo to Cloudflare Pages
3. Build command: `npm run build`
4. Output directory: `dist`
5. Set production branch
6. Point `compoundvr.com` after first successful deploy

### Netlify (fallback)
1. Connect/import repo
2. Build command: `npm run build`
3. Publish directory: `dist`
4. Point `compoundvr.com`

## DNS when ready
Point:
- apex/root domain: `compoundvr.com`
- optionally `www.compoundvr.com`

Use whichever records the chosen host requires after the first live deploy exists.

## Editorial publishing workflow
Richard publishes by creating Markdown files in:
- `src/content/articles/`
- `src/content/games/`

Then:
1. run `npm run build`
2. commit changes
3. deploy

## Near-term next steps
1. Create repo/hosting target
2. Deploy first live build
3. Point DNS
4. Add first 10 canonical game pages
5. Add article + comparison templates if needed
