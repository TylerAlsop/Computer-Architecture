"""CPU functionality."""
# Do all your work in this file and run it in ls8.py
# This has a CPU class which needs an __init__, alu(), and run() implemented


import sys

## ALU Operation Codes
ADD = 0b10100000
SUB = 0b10100001
MUL = 0b10100010
DIV = 0b10100011
MOD = 0b10100100

INC = 0b01100101
DEC = 0b01100110

CMP = 0b10100111

AND = 0b10101000
NOT = 0b01101001
OR = 0b10101010
XOR = 0b10101011
SHL = 0b10101100
SHR = 0b10101101

## PC mutators

CALL = 0b01010000
RET = 0b00010001

INT = 0b01010010
IRET = 0b00010011

JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110
JGT = 0b01010111
JLT = 0b01011000
JLE = 0b01011001
JGE = 0b01011010 

## Other
NOP = 0b00000000

HLT = 0b00000001 

LDI = 0b10000010

LD = 0b10000011
ST = 0b10000100

PUSH = 0b01000101
POP = 0b01000110

PRN = 0b01000111
PRA = 0b01001000

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.registers = [0] * 8
        self.pc = 0
        self.running = True


    if len(sys.argv) != 2:
        print("Usage: example_cpu.py filename")
        sys.exit(1)

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        try: 
            with open(filename) as program_file:
                for line in program_file:
                    # Split the current line on the # symbol
                    split_line = line.split('#')
                    # print(split_line)

                    code_value = split_line[0].strip() # removes whitespace and /n character

                    # Make sure that the value before the # symbol is not empty
                    if code_value == '':
                        continue

                    num = int(code_value, base=2)
                    self.ram[address] = num
                    address += 1
                    
        except FileNotFoundError:
            print(f'{sys.argv[1]} File not found')
            sys.exit(2)

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.registers[reg_a] += self.reg[reg_b]
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
            print(" %02X" % self.registers[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # This is where to add the while loop containing if, ifelse, else statements.

        while self.running:
            instruction_register = self.ram_read(self.pc)

            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            self.trace()

            if instruction_register == LDI:
                self.registers[operand_a] = operand_b
                self.pc += 3

            elif instruction_register == PRN:
                print(self.registers[operand_a])
                self.pc += 2

            elif instruction_register == MUL:
                self.registers[operand_a] *= self.registers[operand_b]
                self.pc += 3

            elif instruction_register == HLT:
                print("The program has reached a HALT function and is now ending. Thanks for playing.")
                self.running = False

            else:
                print(f'Unknown instruction: {instruction_register}. The program will now force exit.')
                self.running = False
                sys.exit(1)
            



    def ram_read(self, address):    # Should accept the address to read and return the value stored there.
        return self.ram[address]

    def ram_write(self, address, value):            # Should accept a value to write, and the address to write it to.
        # address could be replaced with MAR (Memory Address Register)
        # value could be replaced with MDR (Memory Data Register)
        self.ram[address] = value


# self.load('print8.ls8')
