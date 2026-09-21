# Legal AI Landscape

A tracker of the legal AI market, weighted toward the **foundation-model integration layer** —
who is building on whose model, and which platform ecosystems each vendor has joined.

Live site: _(not yet published)_

## Why this exists

Between May and September 2026 all three major model vendors shipped legal products:

| | Product | Launched | The bet |
|---|---|---|---|
| Anthropic | Claude for Legal | 2026-05-12 | **Distribution** — put the workflow inside Claude, make every vendor a connector |
| Google Cloud | Gemini Enterprise for Legal | 2026-08-25 | **Integration** — be the substrate, sell through the SIs |
| OpenAI | Astra for Law | 2026-09-17 | **Content** — own primary-law retrieval, sell direct to the Am Law 200 |

That compresses the interesting question for every app-layer company into one thing:
*what do you have that the model vendor doesn't?* This repo tracks the answer, vendor by vendor.

## Layout

```
data/platforms.json    the three model-vendor legal products, in detail
data/companies.json    60 companies/firms: what they sell, funding, model use, integrations
data/frictions.json    bottlenecks and openings, with the survey/sanctions data behind them
build.py               renders site/ from data/ — no dependencies
site/index.html        generated, self-contained, filterable
site/data.json         the full dataset as one file
NOTES.md               the landscape read — what the data adds up to
scripts/refresh.md     the prompt used by the scheduled update
```

## Rebuild

```bash
python3 build.py
```

Then open `site/index.html`. Editing `data/*.json` and re-running is the whole workflow.

## Data conventions

- **Valuations and funding** are as last publicly reported. They go stale fast; the date is in the field.
- **`models`** records only *publicly disclosed* foundation-model use. Most vendors are multi-model
  and don't disclose routing, so `["multiple, undisclosed"]` means undisclosed, not none.
- **`platform_integrations`** records a named, announced relationship (MCP connector, ecosystem
  plugin, launch partner, named customer) — not "they probably call the API".
- **`confidence`** appears only on entries where a specific field is shaky. Those render as a caveat line.
- Every entry carries `sources`. Nothing in the dataset should be unattributed.

## Known gaps

- European and APAC vendors are under-covered relative to US ones.
- Pricing is almost entirely absent — legal AI pricing is rarely public, and what is public is list price.
- Adoption figures ("40+ Am Law 100 firms") come from vendor claims and are not independently verified.
- LexisNexis model attribution is low confidence.
