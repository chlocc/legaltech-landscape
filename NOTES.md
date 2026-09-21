# The lay of the land — 2026-09-21

## 1. The model vendors stopped being suppliers

For two years the deal was simple: OpenAI and Anthropic sold tokens, Harvey and Legora sold
software, and nobody had to think too hard about the boundary. That ended in four months.

**Anthropic, 12 May 2026 — Claude for Legal.** 20+ MCP connectors, 12 practice-area plugins
(Commercial, Corporate, Employment, Privacy, Product, Regulatory, AI Governance, IP, Litigation,
plus Law Student, Legal Clinic, Legal Builder Hub), native Word/Outlook/Excel/PowerPoint, Cowork
for multi-document work, Projects as matter workspaces, scheduled tasks for recurring sweeps.
Four plugins also ship as Managed Agents on the API. Each plugin runs a cold-start interview that
learns the team's playbook, escalation matrix and house style — which is the tell: this is not a
demo, it's a product designed to be configured once and lived in.

**Google Cloud, 25 August 2026 — Gemini Enterprise for Legal.** Legal skills, pre-built agents,
connectors into the DMS/e-discovery/research stack with permissions preserved. Preview at launch.
Cleary, Freshfields, Weil and Williams & Connolly as launch firms. Sold through Accenture, Deloitte,
KPMG et al. Google's first vertical packaging of Gemini Enterprise, with financial services
alongside and healthcare next — legal is a wedge in a horizontal strategy, not a legal bet.

**OpenAI, 17 September 2026 — Astra for Law.** GPT-6 Astra plus a Legal Search Index across 230M+
URLs of US case law, statutes, regulations, court rules and administrative decisions, built using
CourtListener data. 26 vendor plugins, 9 community plugins, 47 user-built skills. ChatGPT for Word.
A "Trusted Access" program for Am Law 200 firms with zero data retention and no human review,
designed with Latham & Watkins on permissions and ethical walls — roughly 30 pages of agreement.
Jason Boehmig, who co-founded Ironclad, runs it.

Three genuinely different bets:

- Anthropic bet the **workflow** is the valuable layer and is putting it inside Claude.
- Google bet the **substrate** is, and is refusing to own the workflow at all.
- OpenAI bet **retrieval over primary law** is, and went at the research duopoly directly.

Note who is missing from OpenAI's index story: nobody had to license Westlaw or Lexis. CourtListener
— a nonprofit — is now load-bearing infrastructure for a frontier lab's legal product. That is the
single most underrated fact in the whole landscape.

## 2. Nobody in the app layer picked a side

The obvious read of a model vendor shipping legal software is that the app layer gets squeezed.
The observed behaviour is the opposite of retreat: **Harvey, Legora, Thomson Reuters, Relativity,
Everlaw, iManage, Intapp and DeepJudge all joined multiple ecosystems.** Harvey is an OpenAI
Startup Fund company that added Anthropic and Google models in 2025, sits as an MCP connector
inside Claude, is an Astra API customer, and is building its own model. Thomson Reuters built
next-gen CoCounsel on Anthropic's Claude Agent SDK *and* ships a ChatGPT plugin.

Bob Ambrogi's framing of the open question is the right one: how much appetite does a model vendor
actually have to compete in legal, and how do the vendors built on it respond? So far the answer to
the second half is *by being everywhere*. Being a connector in every ecosystem is the hedge against
being disintermediated in any one of them. It is also, notably, a hedge that costs the app layer its
pricing power: if you are a connector, you are a feature.

## 3. What's actually defensible

Helen Fan's Legal AI Value Stack (V2) is the most useful lens here, and it maps cleanly onto the data:

| Level | What it is | Who is actually there |
|---|---|---|
| 1. Raw AI | A model with a chat box | Table stakes. Commoditised by definition — this is exactly what the model vendors now give away inside their own products. |
| 2. Workflow redesigned around agents | Not AI bolted onto a process — the process rebuilt for agent execution, lawyer as chief of staff | Legora's Tabular Review, CoCounsel's agentic planning, Claude's practice-area plugins. Contested, crowded. |
| 3. Self-learning data layer within boundaries | Systems that learn from the work, inside agent / client / ethical-wall boundaries | **The real moat.** DeepJudge, iManage, NetDocuments, Relativity's review corpus, and any firm that has actually organised its own work product. Hardest to cross because the blocker is organisational, not technical. |
| 4. System of record | AI as the unified operating layer across email, matters, billing, documents, research | Almost nobody. Thomson Reuters and Clio have the best structural shot via distribution. |
| 5. AI-native | AI first, then human | Crosby, Garfield, Lawhive, Eudia — small, but the only ones not retrofitting. |

The uncomfortable implication for the app layer: most of the funding has gone to Level 2, which is
precisely where the model vendors just landed. The companies sitting on Level 3 assets — the DMS
vendors, the e-discovery incumbents with the corpus, the firms with organised knowledge — are
better positioned than their valuations suggest.

## 4. The money

- **Harvey $11B** (Mar 2026, $200M co-led by GIC and Sequoia) — $3B → $5B → $8B → $11B in thirteen months.
- **Legora $5.6B** (Series D $550M at $5.55B in March, +$50M extension in April with Atlassian and
  NVentures). Building out NY, Denver, Houston, Chicago; 300+ US staff targeted by year end.
- **Clio $5B**, having bought vLex for ~$1B — practice management buying its way into research.
- **Relativity $3.6B**, **Ironclad $3.2B**, **Filevine ~$3B**, **EvenUp $2B+**, **Eve $1B+**.
- Harvey, Legora, Clio and Filevine absorbed more than half of all tracked legal tech funding
  across 2025 and Q1 2026. Capital is consolidating into platforms, not features.
- The plaintiff bar produced three unicorns in one autumn (Eve, EvenUp, Filevine). It is a
  structurally different market — contingency fees mean buyers who think in ROI, not in headcount —
  and it is under-discussed relative to BigLaw.

## 5. What the firms are doing

**Kirkland is building.** $500M over three to four years on a proprietary platform, $100M in 2026,
~50 AI engineers (roughly 35 via partnerships, 15+ in-house). They still license third-party tools.
This is the reference case for build-vs-buy at the top of the market, and the quote that travelled —
a GC calling it "a few steps closer to killing the billable hour" — is the part the market is
actually reacting to.

**Everyone else is multi-sourcing.** Freshfields is a named Claude user *and* a Gemini launch firm.
Accenture Legal is a named Claude user *and* a Google SI partner. Latham designed OpenAI's ethical
wall model. Firms are deliberately avoiding model lock-in, which tells you they expect the
capability gap between labs to keep closing and the switching costs to stay low.

Reported adoption: 40+ Am Law 100 firms with active enterprise AI contracts, Harvey claiming the
largest share. Treat these as vendor claims — none are independently audited.

## 6. AI-native law firms — the segment where the constraint is law, not AI

Eleven tracked here; the category directory (Matt Pollins' [AI Firm Index](https://aifirmindex.com/),
launched March 2026) counted 27 at launch, 40 by late April, and just over 50 globally by late June —
31 of them US. Its scoping rule is the useful one: **regulated entities**, not SaaS and not marketplaces.

What makes these different from vendors is that they sell outcomes and price per artefact:

- **Manifest OS** — $60M Series A at $750M (Apr 2026, Menlo/Kleiner/First Round/Quiet), reported as
  the largest Series A in legal tech history. Not a firm itself: an operating system that firms
  practise on under the Manifest Law brand. 100+ attorneys, 3,000+ clients. First incubated firm is
  business immigration, under Arizona ABS.
- **Crosby** — $60M Series B at ~$400M. Contract review with licensed attorney sign-off in a median
  of 58 minutes, priced per document. Clients include Cursor and Clay.
- **Moritz** — $9M seed (YC, 20VC, Urban Innovation). AI does ~80%, clients pay lawyers for the last
  20%, flat price, same-day. 100+ companies and $2B+ aggregate contract value since launching in 2026.
- **Soxton** — the most legible pricing in the category: ~$100–200 per contract, $50–100 per attorney
  conversation. That is what unbundling actually looks like on an invoice.
- **General Legal** ($11.5M, ~$2M ARR, 14 lawyers), **Alaro** (ex-Paul Hastings, Seattle),
  **Talairis** (May 2026, 10–15% of a comparable BigLaw bill), **Eudia** ($105M+), **Lawhive**,
  **Garfield**, **Justpoint**.

**The binding constraint is regulatory, not technical.** You cannot build most of these firms in most
US states, because non-lawyer ownership is prohibited. Arizona's Alternative Business Structure
programme is the workaround — 100+ ABSs approved since 2021, including KPMG Law — and in July 2025
Justpoint Law took the first ABS licence for an AI-native PI and mass tort firm. Manifest is
incubating the same way. The UK equivalent is Garfield AI's SRA authorisation.

So the interesting question in this segment is not model quality. It is whether a second US state
follows Arizona, and what happens to UPL and fee-sharing rules when one does. Everything else here —
the pricing experiments, the talent flow out of Big Law, the equity-instead-of-lockstep pitch — is
downstream of that one regulatory fact.

## 7. Where it's stuck, and what's open

Worth stating plainly: **almost none of the stated blockers are about whether the models are good
enough.** The capability argument is largely over. What's left is commercial, organisational and
regulatory — and that's where the openings are too.

### Bottlenecks

**The verification tax.** Damien Charlotin's public database tracks ~1,490 court decisions worldwide
where a party relied on AI-hallucinated material and a court responded — 1,000+ of them US, running
at more than one new decision per day. Penalties went from four figures to $15,000 per attorney in a
federal appeals court, ~$109,700 aggregate across two lawyers in one matter, and the first
suspensions: Colorado (a year and a day, 90 to serve) and an indefinite suspension in Nebraska. The
time the model saves is being spent back on checking it.

**Per-seat pricing against outcome value.** Cut a five-hour task to one and billable revenue falls
80% for identical work product. Firms have mostly responded by not responding: 58% say AI changed
neither billing nor hours, 86% of solo and 78% of small firms haven't touched pricing, only ~a third
report any revenue increase. And only 6% say clients are explicitly pushing for AI-linked cost cuts —
so the pressure isn't coming from where everyone assumed.

**Individuals adopted; institutions didn't.** 27% → 31% → 69% of individual practitioners in three
years, against 46% of firms with general-purpose tools and 34% with legal-specific ones. The delta is
shadow AI: the work is already being done on unsanctioned tools.

**The governance vacuum.** 43% of firms have no AI policy and no plans to write one; 9% have one
that's actually enforced. 54% provide no training; 11% make it mandatory. 19% call themselves "very
prepared." Every sanctions case above happened at a firm with better-than-even odds of having no
policy at all.

**Security, privilege, trust — not accuracy.** Stated blockers: data security 46%, ethics 42%,
privilege 39%, trust in outputs 39%, cost a distant fifth. This is exactly why OpenAI's Trusted
Access (ZDR, no human review, Latham-designed ethical walls) is aimed at the contract rather than the
benchmark.

**The data layer is an org chart problem.** Level 3 is where defensibility lives and the blocker
isn't technical — someone has to decide who owns which precedent, what a client's data may train,
and how reader-writer separation maps onto information barriers. No vendor can sell a firm past that.

**Clients are ahead of their firms.** 87% of GCs use genAI, up from 44% a year earlier; corporate
legal adoption went 23% → 52%. 64% of in-house teams expect to need outside counsel less. And 60%
don't know whether their firms use genAI on their matters — a disclosure gap that will close on the
client's terms, not the firm's.

**Regulation caps the best business model.** Outcome pricing with an AI first pass needs non-lawyer
ownership to take capital, and in the US that is Arizona and essentially nowhere else.

### Openings

1. **Citation integrity as infrastructure.** A thousand sanctions decisions is a market signal, not a
   cautionary tale. The gap isn't better retrieval — it's court-defensible provenance with an audit
   artefact a judge or a malpractice carrier would accept. Midpage is closest in research; nobody
   owns it across drafting, and no insurer has productised it.
2. **Permissions-aware knowledge plumbing.** The thing that makes the Level 3 decision executable:
   ethical walls, reader-writer separation, per-client training consent, enforced at retrieval.
   DeepJudge, iManage, NetDocuments sit here. This is the one asset a model vendor can't ship from
   a connector directory — expect acquisitions.
3. **Pricing and margin tooling.** 86% of small firms haven't changed pricing because nobody gave
   them a way to. Scoping an AFA, measuring realisation when a model did 80% of the work, proving
   the saving to a client — all unserved. Manifest OS is the first real attempt and it raised the
   largest Series A in the sector's history, which tells you how empty the space is.
4. **Governance, training and attestation as product.** Policy generated against the firm's actual
   tool estate, enforced logging, mandatory training with completion records, client-facing
   attestation. It's what insurers will start pricing against.
5. **Client-facing AI.** Closing the 60% disclosure gap turns a transparency liability into the
   reason the client stays. Helen Fan's thesis; almost nobody is building the client-side surface.
6. **The long tail and the plaintiff bar.** Contingency firms buy on ROI, which is why Eve, EvenUp
   and Filevine all crossed a billion in one autumn. Same logic for solo and small firms, where
   adoption is highest and tooling is priced for a market they're not in.
7. **Primary law outside the US.** OpenAI's index is 230M+ US URLs; Anthropic's research connectors
   are US-weighted. Non-US and non-English primary law is substantially unbuilt at frontier quality —
   and CourtListener shows the data can come from public sources.
8. **A second ABS state.** The highest-leverage single event in the sector.

## 8. What I'd watch next

1. **Does Anthropic go further up the stack?** The plugins already do practice-area workflow with
   playbook configuration. The gap between that and competing with Harvey is one product decision.
2. **Whether the app layer's pricing holds.** If a firm can get 80% of Legora's tabular review from
   Claude Cowork plus an iManage connector, seat pricing at Level 2 is hard to defend.
3. **Primary-law licensing.** OpenAI routed around Westlaw and Lexis using nonprofit data. Whether
   the incumbents respond by restricting, litigating, or partnering will shape the research layer.
4. **A second ABS state.** Arizona is currently the whole US story. Utah's sandbox is narrower and
   other states have actively resisted. If one more opens, the AI-native segment stops being a
   regulatory-arbitrage niche and becomes the default structure for commodity legal work.
5. **Level 3 M&A.** If the moat is the proprietary data layer, expect the platforms to start buying
   DMS and knowledge-search companies rather than building against them.

---

*Sources are attached per entry in `data/companies.json` and `data/platforms.json`, and render as
bracketed links on the site.*
