# Changes — Catapultikon Highlights Gallery Images

## Files added
- `public/images/catapultikon-highlight-1.jpg` (from `cata1.jpeg`)
- `public/images/catapultikon-highlight-2.jpg` (from `cata2.jpeg`)
- `public/images/catapultikon-highlight-3.jpg` (from `cata3.jpeg`)

## Files modified
- `public/catapultikon.html`
  - `#highlights-gallery` section, "Ancient Artifacts" card: swapped remote Supabase URL → `images/catapultikon-highlight-1.jpg`
  - `#highlights-gallery` section, "Trial of Wisdom" card: swapped remote Supabase URL → `images/catapultikon-highlight-2.jpg`
  - `#highlights-gallery` section, "Final Showdown" card: swapped remote Supabase URL → `images/catapultikon-highlight-3.jpg`

## Notes
- Only the 3 "Highlights of Catapultikon 25" gallery images were replaced. The hero section image near the top of the page (a separate `<img>` with a different Supabase URL, alt="Hero Catapult Logo") was left untouched since it's not part of the gallery.
- Images are now bundled locally under `public/images/` instead of pointing at an external Supabase URL, so the page no longer depends on that external host for these three photos.
