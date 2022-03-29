#!/usr/bin/env python
# coding: utf-8

import functools

def prod(values):
    return functools.reduce(lambda a, b: a*b, values)
def greater_than(values):
    a, b = values
    return 1 if a > b else 0
def less_than(values):
    a, b = values
    return 1 if a < b else 0
def is_equal(values):
    a, b = values
    return 1 if a == b else 0

OPERATORS = {0:sum, 1:prod, 2:min, 3:max, 5:greater_than, 6:less_than, 7:is_equal}

class Binary:
    def __init__(self, myinput, bin_input = False):
        self.digits = self._generate_binary_from_hex(myinput) if not bin_input else self._generate_binary(myinput)
    
    def _generate_binary_from_hex(self, hex_input):
        binary = bin(int(hex_input,16))[2:].zfill(len(hex_input)*4)
        for n in binary:
            yield n
    
    def _generate_binary(self, bin_input):
        for n in bin_input:
            yield n

class Packet():
    def __init__(self, bin_input, version = None, type_id = None):
        self.bits = bin_input
        self.version = version if version is not None else self.next_int(3)
        self.type = type_id if type_id is not None else self.next_int(3)
        self.subpackets = []

    @classmethod
    def factory(cls, bin_input):
        packet = Packet(bin_input)
        if packet.type == 4:
            return Value(bin_input, packet.version, packet.type)
        else:
            return Operator(bin_input, packet.version, packet.type)
    
    def next_bin(self, n):
        return "".join([next(self.bits.digits) for _ in range(n)])
    
    def next_int(self, n):
        return int(self.next_bin(n), 2)
    
    def get_subpackets(self, length):
        subpackets = self.next_bin(length)
        return Binary(subpackets, bin_input=True)
    
    def sum_versions(self):
        version = self.version
        for p in self.subpackets:
            version += p.sum_versions()
        return version
    
    def evaluate(self):
        if self.subpackets:
            return OPERATORS[self.type]([s.evaluate() for s in self.subpackets])
        elif self.type == 4:
            return self.value
        
class Value(Packet):
    def __init__(self, bin_input, version, type_id):
        super().__init__(bin_input, version, type_id)
        group_prefix = self.next_bin(1)
        value = ""
        while True:     # concatenate all value blocks (the last is reached when prefix is 0)
            value = value + self.next_bin(4)
            if group_prefix == "0":
                break
            group_prefix = self.next_bin(1)
        self.value = int(value, 2)         
        
class Operator(Packet):
    def __init__(self, bin_input, version, type_id):
        super().__init__(bin_input, version, type_id)
        self.length_type = self.next_int(1)
        
        # parse subpackets: length of subpackets is specified
        if self.length_type == 0:
            subpacket_length = self.next_int(15)
            subpackets_binary = self.get_subpackets(subpacket_length)
            while True: # read from subpackets_binary until empty
                try:
                    self.subpackets.append(Packet.factory(subpackets_binary))
                except StopIteration:
                    break

        # parse subpackets: number of subpackets is specified
        elif self.length_type == 1:
            subpacket_count = self.next_int(11)
            for _ in range(subpacket_count):
                self.subpackets.append(Packet.factory(self.bits))

def read_input(my_input):
    with open(my_input, "r") as file:
        return file.readline().strip()

def solve_first(myinput):
    binary_input = Binary(myinput)
    packet = Packet.factory(binary_input)
    return packet.sum_versions()

def solve_second(myinput):
    binary_input = Binary(myinput)
    packet = Packet.factory(binary_input)
    return packet.evaluate()

if __name__ == "__main__":
    my_input = read_input("../../input/input_16.txt")
    print(solve_first(my_input))
    print(solve_second(my_input))
    print(solve_first("8A004A801A8002F478"))