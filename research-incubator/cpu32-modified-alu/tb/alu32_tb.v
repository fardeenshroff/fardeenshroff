`timescale 1ns/1ps
module alu32_tb;
  reg [31:0] a, b;
  reg [2:0] op;
  wire [31:0] result;
  wire zero;
  integer tests;
  alu32 uut(.a(a), .b(b), .operation(op), .result(result), .zero(zero));

  task verify;
    input [31:0] aa, bb;
    input [2:0] operation;
    input [31:0] expected;
    begin
      a=aa; b=bb; op=operation; #1;
      if (result !== expected || zero !== (expected == 0)) begin
        $display("FAIL a=%h b=%h op=%b got=%h expected=%h zero=%b",
                 a,b,op,result,expected,zero);
        $fatal(1);
      end
      tests = tests + 1;
    end
  endtask

  initial begin
    tests = 0;
    verify(32'd5,32'd3,3'b000,32'd8);
    verify(32'd5,32'd3,3'b001,32'd2);
    verify(32'hFFFFFFFF,32'd1,3'b000,32'd0);
    verify(32'd0,32'd1,3'b001,32'hFFFFFFFF);
    verify(32'hAAAA5555,32'hFFFF0000,3'b010,32'hAAAA0000);
    verify(32'hAAAA5555,32'h0000FFFF,3'b011,32'hAAAAFFFF);
    verify(32'd5,32'd3,3'b100,32'd1);
    verify(32'd3,32'd5,3'b100,32'd0);
    verify(32'd3,32'd3,3'b100,32'd0);
    verify(32'hFFFFFFFF,32'd1,3'b100,32'd1);
    verify(32'd4,32'd4,3'b111,32'd0);
    $display("PASS: %0d ALU cases", tests);
    $finish;
  end
endmodule

