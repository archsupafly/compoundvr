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
      '/games/hitman-world-of-assassination-vr/',
      '/games/borderlands-2-vr/',
      '/games/dcs-world-vr/',
      '/games/fallout-4-vr/',
      '/games/garrys-mod/',
      '/games/left-4-dead-2-vr/',
      '/games/minecraft/',
      '/games/resident-evil-7-biohazard-vr/',
      '/games/skyrim-vr/',
      '/games/the-elder-scrolls-v-skyrim/',
      '/games/the-elder-scrolls-v-skyrim-vr/',
      '/games/tie-fighter/',
        '/articles/castlevania-simons-destiny-quest-guide/',
    ].includes(new URL(page).pathname),
  })],
});
