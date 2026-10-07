import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://compoundvr.com',
  output: 'static',
  // Alias redirect stubs (meta-refresh + noindex) must not be indexed:
  // their canonical twins carry the ranking signals.
  integrations: [sitemap({
    filter: (page) => ![
      '/games/five-nights-at-freddy-s-vr-help-wanted/',
      '/games/gta-v/',
      '/games/moss-book-i/',
      '/games/zelda-ii-the-adventure-of-link/',
      '/games/zelda/',
      '/games/zelda-ocarina-of-time/',
    ].includes(new URL(page).pathname),
  })],
});
