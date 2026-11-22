# Chipyard + Gemmini — RISC-V Matrix-Accelerator Study

**Status: evidence-recovery workspace; no original Gemmini source or benchmark logs verified here.**

## Research objective
Evaluate a Gemmini systolic-array accelerator within a Chipyard RISC-V simulation environment using matrix multiplication workloads. A previous project description reported runs at dimensions 64 and 128 and mentioned cycle counts of **2,334** and **10,711**, respectively. Those numbers are **historical self-reports, not reproduced or validated by this workspace**.

## What this folder contains
- `src/matmul_reference.c`: **new CPU reference** matrix multiplication implementation with deterministic inputs and a checksum. It contains **no Gemmini ISA commands or accelerator calls**.
- `Makefile`: local build and smoke test for the CPU reference.
- `EVIDENCE_CHECKLIST.md`: exact artifacts required to restore and verify the original Chipyard/Gemmini experiment.

## Run the new CPU reference

```bash
make
./matmul_reference 64
./matmul_reference 128
make test
```

This measures only software correctness and elapsed time on the host. It cannot substantiate Gemmini cycles or accelerator throughput.

## Proposed Gemmini replication
Recover the original Chipyard/Gemmini revision and submodules, RISC-V toolchain versions, `tiled_matmul_ws.c`, simulator configuration, workload sources, and command logs. Evaluate the original target with its supported simulator and include raw cycle counters and a baseline. No matrix-accelerator comparison belongs in a results table until that environment has actually run.

**Attribution:** Gemmini and Chipyard are research projects developed by upstream teams. Future documentation must clearly distinguish your own modifications, experiments, and new code from the upstream frameworks.

