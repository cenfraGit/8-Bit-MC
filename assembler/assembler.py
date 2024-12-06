assembler_output = ""

register_binary = {
    "R0" : "00",
    "R1" : "01",
    "R2" : "10",
    "R3" : "11"
    }

alu_binary = {
    "ADD" : "000",
    "SHR" : "001",
    "SHL" : "010",
    "NOT" : "011",
    "AND" : "100",
    "OR"  : "101",
    "XOR" : "110"
}

other_binary = {
    "LOAD" : "000",
    "STR" : "001",
}

with open('fibo.txt', 'r') as file:
    assembly_instructions = file.readlines()
    
# parse instructions

for instruction in assembly_instructions:
    parts = instruction.split(None) # Separte by parts
    #print(parts)
    
    if (len(parts) == 0):
        continue
    
    ins = parts[0]
    
    if ins in list(alu_binary.keys()):
        assembler_output += "1" + alu_binary[ins] + register_binary[parts[1]] + register_binary[parts[2]] + "\n"
    
    else:
        if ins == "DATA":
            assembler_output += "0" + "010" + "00" + register_binary[parts[1]] + "\n"
            assembler_output += parts[2] + "\n"
        elif ins == "JMPA":
            assembler_output += "0" + "100" + "0000" + "\n"
            assembler_output += parts[1] + "\n"
        elif ins == "JMPIF":
            
            zeac_list = ["0", "0", "0", "0"]
            zeac_string = ""
            
            if "Z" in parts[1]:
                zeac_list[0] = "1"
            if "E" in parts[1]:
                zeac_list[1] = "1"
            if "A" in parts[1]:
                zeac_list[2] = "1"
            if "C" in parts[1]:
                zeac_list[3] = "1"
                
            for i in zeac_list:
                zeac_string += i
            
            assembler_output += "0" + "101" + zeac_string + "\n"
            
        elif ins == "DISPLAY":
            assembler_output += "0" + "111" + "0000" + "\n"
            assembler_output += parts[1] + "\n"
        elif ins == "JMPR":
            assembler_output += "0" + "011" + "00" + register_binary[parts[1]] + "\n"
        elif ins == "CLF":
            assembler_output += "01100000\n"
        elif ins == "END":
            assembler_output += "11001111\n"
        else:
            assembler_output += "0" + other_binary[ins] + register_binary[parts[1]] + register_binary[parts[2]] + "\n"
       
print(assembler_output)

with open('output.txt', 'w') as out:
    out.write(assembler_output)
