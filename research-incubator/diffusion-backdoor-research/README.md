# Backdoor Attacks on Diffusion Models — Research Recovery Workspace

**Status: source-recovery and research-protocol documentation only.** The original notebook, model checkpoints, attack scripts, data provenance, and run logs have not been located. Previous application materials identify the topic, but do not independently establish a completed reproducible experiment.

## Scope and motivation
Study whether training-data contamination and triggered inputs can alter generative diffusion model behavior, and evaluate detection, robustness and mitigation strategies in controlled, appropriately licensed test environments. This is security research, not instructions for compromising third-party models.

## Research artifacts
- [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md): reproducibility, safety and evaluation design.
- [EVIDENCE_MANIFEST.md](EVIDENCE_MANIFEST.md): artifacts to recover before publishing claims.

## Responsible experiment design
Use authorized small-scale models and synthetic or properly licensed datasets. Record provenance, control trigger conditions, preserve training parameters, establish clean and modified-model baselines, and document detector false positives. Publish reproducible summaries without exposing sensitive third-party weights, private data or adversarial material that exceeds your authorizations.

**This folder does not include an attack implementation, observed attack success rate, or a claim that the original research results were reproduced.**

