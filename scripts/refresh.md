# Refresh prompt (used by the scheduled update)

Working directory: `~/Desktop/legaltech-landscape`

1. Search for legal AI news since the `as_of` date in `data/companies.json`. Cover:
   - Foundation-model vendors' legal products: Anthropic (Claude for Legal), OpenAI (Astra for
     Law), Google Cloud (Gemini Enterprise for Legal). New connectors, plugins, models, pricing,
     named firms, access programs.
   - New funding rounds, valuations, acquisitions among tracked companies.
   - New entrants worth adding, and any tracked company that has shut down or been acquired.
   - Law firm announcements: build-vs-buy, enterprise deployments, AI-native firm authorisations.
   - Check LawSites (lawnext.com), Artificial Lawyer, Legaltech Hub, and Helen Fan's Substack
     (helenfan1.substack.com) for anything the general searches missed.

2. Update `data/companies.json` and `data/platforms.json` in place. Rules:
   - Every new or changed claim needs a source URL in that entry's `sources`.
   - Don't overwrite a sourced figure with an unsourced one.
   - If a figure is uncertain, say so in `confidence` rather than dropping it.
   - Bump `as_of` in both files to today.

3. Run `python3 build.py`.

4. If anything material changed, append a dated entry to `CHANGELOG.md` saying what moved and why
   it matters — one short paragraph, not a list of diffs. If nothing material changed, say so and
   make no commit.

5. Commit and push. Do not restructure the schema or the site in a scheduled run; flag schema
   problems in the changelog instead.
