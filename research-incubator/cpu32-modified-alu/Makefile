IVERILOG ?= iverilog
VVP ?= vvp
.PHONY: test clean
test:
	$(IVERILOG) -g2012 -Wall -s alu32_tb -o alu32_sim rtl/alu32.v tb/alu32_tb.v
	$(VVP) alu32_sim
clean:
	rm -f alu32_sim

