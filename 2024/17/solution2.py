import sys
import re

A = 4
B = 5
C = 6

class State:
    registers = [0,1,2,3,0,0,0]
    instructions = []
    output = []
    pointer = 0

    def __init__(self,a,b,c):
        self.registers[A] = a
        self.registers[B] = b
        self.registers[C] = c

    def print_outout(self):
        print(",".join([str(i) for i in self.output]))

    def read(self):
        value = self.instructions[self.pointer]
        self.pointer+=1
        return value

    def get(self, register):
        return self.registers[register]

    def set(self, register, value):
        self.registers[register] = value

    def adv(self):
        for _ in range(self.registers[self.read()]):
            self.set(A, self.get(A) // 2)

    def bxl(self):
        self.set(B, self.get(B) ^ self.read())

    def bst(self):
        self.set(B, self.registers[self.read()] % 8)

    def jnz(self):
        val = self.read()
        if (self.get(A) != 0):
            self.pointer = val

    def bxc(self):
        self.read()
        self.set(B, self.get(B) ^ self.get(C))

    def out(self):
        val = self.registers[self.read()] 
        self.output.append(val % 8)

    def bdv(self):
        self.set(B, self.get(A))
        for _ in range(self.registers[self.read()]):
            self.set(B, self.get(B) // 2)

    def cdv(self):
        self.set(C, self.get(A))
        for _ in range(self.registers[self.read()]):
            self.set(C, self.get(C) // 2)

    def run(self):
        operations = [self.adv,self.bxl,self.bst,self.jnz,self.bxc,self.out,self.bdv,self.cdv]

        while self.pointer < len(self.instructions):
            opcode = self.read()
            operations[opcode]()

initial_state = [
    int(input().split()[2]),
    int(input().split()[2]),
    int(input().split()[2]),
]

initial_state[0] = 0

input()
instructions = [int(i) for i in input().split()[1].split(',')]

while True:
    state = State(*initial_state)
    state.instructions = instructions
    state.run()
    print(initial_state)
    if state.output == state.instructions:
        break
    initial_state[0] += 1

    
