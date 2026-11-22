# Source restoration checklist

- [ ] Exact Chipyard Git commit, upstream forks, licenses, and recursive submodule hashes
- [ ] Exact Gemmini Git commit, hardware configurations, systolic-array dimensions and datatype
- [ ] User-authored C and/or RTL changes, with authorship and commit history
- [ ] Original `tiled_matmul_ws.c` and any additional bare-metal workloads
- [ ] RISC-V toolchain, compiler flags, Spike/Verilator versions, simulator config
- [ ] Reproduction commands for workload sizes 64³ and 128³
- [ ] Simulator logs with cycle-count extraction and timing definitions
- [ ] Baseline, output correctness checks, and variance from independent runs
- [ ] EDA/simulation screenshots or reports, if genuinely produced
- [ ] Distinguish user results from upstream Gemmini/Chipyard paper claims

**Do not fill missing items with synthetic measurements.**

