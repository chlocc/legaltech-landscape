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

## 6. What I'd watch next

1. **Does Anthropic go further up the stack?** The plugins already do practice-area workflow with
   playbook configuration. The gap between that and competing with Harvey is one product decision.
2. **Whether the app layer's pricing holds.** If a firm can get 80% of Legora's tabular review from
   Claude Cowork plus an iManage connector, seat pricing at Level 2 is hard to defend.
3. **Primary-law licensing.** OpenAI routed around Westlaw and Lexis using nonprofit data. Whether
   the incumbents respond by restricting, litigating, or partnering will shape the research layer.
4. **AI-native firm regulation.** Garfield's SRA authorisation is the precedent. Whether a US state
   follows — and what happens to UPL and fee-sharing rules if one does — is the real structural
   question underneath all of this.
5. **Level 3 M&A.** If the moat is the proprietary data layer, expect the platforms to start buying
   DMS and knowledge-search companies rather than building against them.

---

*Sources are attached per entry in `data/companies.json` and `data/platforms.json`, and render as
bracketed links on the site.*
