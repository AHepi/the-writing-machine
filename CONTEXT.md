# CONTEXT.md — Layer 1 router

*Read after your Layer 0 card, before any stage contract. This file decides
**which** contract you run. It routes two kinds of work: pipeline runs and
maintenance requests. Pick the row that matches what the human asked, go to the
named file, and do what that file says — nothing more.*

---

## A. The pipeline — turning a brief into a finished piece

Five stages, in order. Each reads the previous stage's `output/` and writes its
own. Never skip; never reorder. Each stage's `CONTEXT.md` is its contract.

| Stage | Contract | Reads | Writes |
|---|---|---|---|
| **00 — Brief** | `stages/00_brief/CONTEXT.md` | the user's raw request + `_config/defaults.md` | `output/brief.md` (fully resolved — no pointers, no fuzzy values) |
| **01 — Research** | `stages/01_research/CONTEXT.md` | `00_brief/output/brief.md` | `output/findings.md`, `output/sources.md` |
| **02 — Compile** | `stages/02_compile/CONTEXT.md` | brief + findings + sources | `output/factsheet.md`, `output/outline.md` (with `## Imagery` + visual marks) |
| **03 — Write** | `stages/03_write/CONTEXT.md` | brief + factsheet + outline + style files | `output/draft.md` |
| **04 — Audit** | `stages/04_audit/CONTEXT.md` | brief + factsheet + outline + draft | `output/audit.md`, `output/final.md` |

**Provenance chain.** Facts gain an `F-tag` in stage 01 and an `S-register`
(source reliability) in stage 02; deliverables gain `D-tags` in stage 00. These
tags travel down the pipeline and are checked at 03 and audited at 04. A claim
with no F-tag and a D-item with no evidence are both defects.

**Where to start.** New request → stage 00. Re-running after an edit → start at
the earliest stage whose inputs changed.

---

## B. Maintenance — growing the library by asking

The library grows when the human asks, not by editing the pipeline. These
routes never change a stage contract; they add or amend one file.

| The human says | You do |
|---|---|
| "Add an audience: *retired tradies*" | Copy `_config/audiences/_template.md`, fill all sections from the worked example, save as `retired-tradies.md`. Show the result. |
| "Add a format: *LinkedIn post*" | Same, from `_config/formats/_template.md`, save as `linkedin.md`. Show the result. |
| "Add a model: *Qwen 3.7*" | Run `_navigation/models/_add-a-model.md` end to end. Probe, then write `nav_qwen-3-7.md`. Report for approval. |
| "Add an expert audience: *economist*" | Audience template, but flip the register: dense, citations expected, basics forbidden (`rules.md` respect floor, expert side). |
| "*DeepSeek skipped the CHECK again*" | Append a dated line to §7 of `_navigation/models/nav_deepseek-v4.md` and tighten the matching countermeasure in §4. |
| "Add a style rule / change the prose floor" | Edit the relevant `_config/style/` file. Do not fork it. |

**Two guarantees that make this safe:**
1. The brief points at config **by name**; `_config/defaults.md` covers absence;
   stage 00 maps fuzzy requests onto whatever the library currently holds. So a
   new file never breaks an old run.
2. Per-run cost stays flat. The library can hold fifty audiences; the brief
   still loads exactly one.

---

## C. If you are not sure which mode you are in

- A **topic + goal** (even sloppy) → pipeline, stage 00.
- A request to **add / change / fix a config or model file** → maintenance.
- A request to **change how a stage works** → that is a contract edit; surface
  it to the human before touching `stages/*/CONTEXT.md`. The contracts are the
  constitution; do not amend them casually.
