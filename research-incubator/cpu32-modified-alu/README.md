# 32-Bit CPU / Modified ALU — RTL Reference Workspace

**Status: new ALU reference implementation, not recovered full 32-bit CPU project.**

Prior project descriptions discussed a 32-bit CPU with a comparator integrated as a fifth ALU operation, simulation, synthesis, and a reported **156.50 MHz** outcome. The original RTL, full processor design, timing constraints, netlist, and timing reports are **not available in this workspace**, so that frequency is not a verified result of the included files.

## New reproducible reference component

- `rtl/alu32.v`: combinational unsigned 32-bit ALU supporting ADD, SUB, AND, OR, and greater-than comparison.
- `tb/alu32_tb.v`: simulation testbench for basic functionality and corner cases.
- `Makefile`: compile/run with Icarus Verilog.

```bash
make test
```

Requires `iverilog` and `vvp`. If available, this checks the **new component only**. Integrating the ALU into a CPU datapath and measuring synthesis/timing require the recovered RTL and toolchain setup.

## Original-source recovery requirements

Provide the original CPU top module, register file, decode logic, pipeline or single-cycle implementation, memory model, comparator specification (signed/unsigned), constraints, testbench, waveforms, synthesis results and physical-design reports. Verify each before claiming specific clock-frequency, gate-count or power figures.

**Authoring boundary:** This scaffold is a new implementation prepared for reconstruction. It is not a republication of an unlocated historical design.

