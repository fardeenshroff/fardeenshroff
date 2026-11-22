# Unpublished Research Projects — Recovery and Reproducibility Workspace

These folders prepare four research projects for **future dedicated repositories**. They are not copies of prior original project source files, and should not be cited as evidence that earlier performance numbers have been reproduced.

**Project owner:** Fardeen Shroff · **Scope audit:** November 22, 2026.

| Research project | Present evidence | New materials in this workspace | Release status |
|---|---|---|---|
| [Chipyard + Gemmini](chipyard-gemmini/README.md) | Prior project descriptions and reported cycle counts; source artifacts not located | Portable C matrix multiplication baseline and recovery checklist | Staging; no verified Gemmini run |
| [32-bit CPU / modified ALU](cpu32-modified-alu/README.md) | Prior descriptions of custom comparator and synthesis; original RTL/EDA reports not located | Newly written synthesizable **ALU reference component** and self-checking simulation bench | Staging; not original integrated CPU |
| [NeoCPU CNN inference](neocpu-cnn-inference/README.md) | Prior description of CPU CNN optimization; original source/measurements not located | Newly written NumPy convolution baseline, im2col variant, correctness tests | Staging; no historical optimization claim |
| [Diffusion-model backdoor research](diffusion-backdoor-research/README.md) | Previous research description and a cover-letter reference; source/paper not located | Experimental protocol, safety boundaries, evidence manifest | Documentation staging; no experiment claimed |

## Publication policy

1. Restore original user-authored source, simulation logs, reports, and paper files before attributing historical work to these workspaces.
2. Preserve source provenance and credit upstream research implementations, frameworks, and open-source designs.
3. Validate new reference implementations independently and keep their performance numbers separate from any previous claims.
4. Create standalone repositories **only after** verifying unique names, file integrity, license provenance, and a reproducible test command.
5. If restoring old files is impossible, describe the outcome as a **new reconstruction**, with a separate authorship and validation record.

The separate repositories already hosted under [the owner's GitHub account](https://github.com/fardeenshroff) are deliberately **not duplicated** here: CUDA/TVM LeNet-5, Relax/MetaSchedule (existing subproject), NeuPIMs (fork), GPU resiliency, FPGA image processing, RTL barrel shifter, secure ML, and other existing work.

