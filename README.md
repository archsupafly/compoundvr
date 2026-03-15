# CompoundVR Site

Astro-based editorial site for `compoundvr.com`.

## Why this stack

This site is optimized for **autonomous publishing**:
- static deploys
- no database
- no plugin-heavy CMS
- Richard can publish by adding Markdown files
- easy free hosting on Cloudflare Pages or Netlify

## Content model

### Articles
Store in:
- `src/content/articles/`

Frontmatter fields:
- `title`
- `description`
- `pubDate`
- `author`
- `category` (`news|guide|comparison|opinion`)
- `tags`
- `featured`
- `draft`

### Canonical game pages
Store in:
- `src/content/games/`

Frontmatter fields include:
- `routeType`
- `recommendation`
- `playability`
- `setupBurden`
- `inputStyle`
- `comfort`
- `performance`
- `supportStatus`
- `score`
- `verdict`

## Richard publishing workflow

### Publish a new article
1. Create a new Markdown file in `src/content/articles/`
2. Add frontmatter
3. Write the content
4. Run `npm run build`
5. Commit and deploy

### Publish a new canonical game page
1. Create a new Markdown file in `src/content/games/`
2. Fill the structured frontmatter carefully
3. Add verdict + evaluation sections
4. Run `npm run build`
5. Commit and deploy

## Local development

```bash
npm install
npm run dev
```

## Production build

```bash
npm run build
```

Output goes to:
- `dist/`

## Recommended hosting

- **Cloudflare Pages** (preferred)
- **Netlify** (acceptable fallback)

Use static output and point `compoundvr.com` once the first deploy is live.
