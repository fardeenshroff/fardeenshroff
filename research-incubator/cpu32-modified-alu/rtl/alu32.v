`timescale 1ns/1ps
// Newly authored ALU reference. Not a full CPU and not recovered coursework RTL.
// operation: 000 ADD, 001 SUB, 010 AND, 011 OR, 100 unsigned (a>b).
module alu32 (
    input  wire [31:0] a,
    input  wire [31:0] b,
    input  wire [2:0]  operation,
    output reg  [31:0] result,
    output wire        zero
);
    always @* begin
        case (operation)
            3'b000: result = a + b;
            3'b001: result = a - b;
            3'b010: result = a & b;
            3'b011: result = a | b;
            3'b100: result = {31'b0, (a > b)};
            default: result = 32'b0;
        endcase
    end
    assign zero = (result == 32'b0);
endmodule

