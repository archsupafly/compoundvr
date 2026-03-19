import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('Richard'),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    category: z.enum(['news', 'guide', 'comparison', 'opinion']).default('guide'),
    featured: z.boolean().default(false),
  }),
});

const games = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/games' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    lastVerified: z.coerce.date(),
    featured: z.boolean().default(false),
    routeType: z.enum(['Official Hybrid', 'Official Standalone VR Version', 'Full VR Mod', 'Framework-Based', 'Injection Driver']),
    recommendation: z.enum([
      'Recommended',
      'Recommended with Caveats',
      'Enthusiasts/Tinkerers Only',
      'Wait for Updates',
      'Not Recommended',
    ]),
    playability: z.enum(['Fully Playable', 'Mostly Playable', 'Partially Playable', 'Experimental', 'Broken']),
    setupBurden: z.enum(['Beginner Friendly', 'Moderate Setup', 'Advanced Setup', 'Expert Only']),
    inputStyle: z.enum(['Full Motion Controls', 'Partial Motion Controls', 'Gamepad Preferred', 'KBM Required', 'Mixed Input']),
    comfort: z.enum(['Comfortable', 'Moderate Intensity', 'Intense', 'Highly Variable']),
    performance: z.enum(['Efficient', 'Moderate Demand', 'Heavy Demand', 'Inconsistent / Unpredictable']),
    supportStatus: z.enum(['Active', 'Recently Updated', 'Stable but Quiet', 'Uncertain', 'Abandoned', 'Broken by Update']),
    genres: z.array(z.string()).default([]),
    technicalTags: z.array(z.string()).default([]),
    experienceTags: z.array(z.string()).default([]),
    score: z.number().min(0).max(100).optional(), // deprecated, use tier
    tier: z.enum(['S', 'A', 'B', 'C', 'D', 'F']).optional(),
    verdict: z.string(),
    heroImage: z.string().optional(),
  }),
});

export const collections = { articles, games };
