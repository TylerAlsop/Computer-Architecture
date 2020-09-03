"""CPU functionality."""
# Do all your work in this file and run it in ls8.py
# This has a CPU class which needs an __init__, alu(), and run() implemented


import sys

## ALU ops
# ADD = 10100000
# SUB = 10100001
# MUL = 10100010
# DIV = 10100011
# MOD = 10100100

# INC = 01100101
# DEC = 01100110

# CMP = 10100111

# AND = 10101000
# NOT = 01101001
# OR = 10101010
# XOR = 10101011
# SHL = 10101100
# SHR = 10101101

# ## PC mutators

# CALL = 01010000
# RET = 00010001

# INT = 01010010
# IRET = 00010011

# JMP = 01010100
# JEQ = 01010101
# JNE = 01010110
# JGT = 01010111
# JLT = 01011000
# JLE = 01011001
# JGE = 01011010 

# ## Other
# NOP = 00000000

# HLT = 00000001 

# LDI = 10000010

# LD = 10000011
# ST = 10000100

# PUSH = 01000101
# POP = 01000110

# PRN = 01000111
# PRA = 01001000

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.running = True


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # This is where to add the while loop containing if, ifelse, else statements.
        instruction_register = [0] * 8

        instruction = self.ram[self.pc]

        operand_a = self.ram_read(self.pc + 1)
        operand_b = self.ram_read(self.pc + 2)

        while self.running:
            if instruction == LDI:
                instruction_register[operand_a] = operand_b
                self.pc += 3

            elif instruction == HLT:
                print("The program has reached a HALT function and is now ending. Thanks for playing.")
                self.running = False

            else:
                print(f'Unknown instruction: {instruction}. The program will now force exit.')
                self.running = False
                sys.exit(1)
            



    def ram_read(self, address):    # Should accept the address to read and return the value stored there.
        return self.ram[address]

    def ram_write(self, address, value):            # Should accept a value to write, and the address to write it to.
        # address could be replaced with MAR (Memory Address Register)
        # value could be replaced with MDR (Memory Data Register)
        self.ram[address] = value