import sys

input_file = sys.argv[1] #used to store the file name entered by the user as argument 1
bit_length = int(sys.argv[2]) #used to store bit length entered by the user as argument 2
max_table_size = 2**bit_length #used to store maximum table size

#ASCII table of 256 characters of type Dictionary
ascii_table = {chr(i): i for i in range(256)}

temp = "" #store contents of the file temporarily
result = [] #array for storing final result
encoded_value = "" #used to store the binary value of the characters to be written into the file

#read from file
with open(input_file, 'r') as f:
    text_file = f.read() #store data into text variable

#loop over the contents of the file
for i in text_file:
    symbol = temp+i 
    if symbol in ascii_table: #if character is present in the array
        temp = symbol
    else: #if character is not present in the array
        if len(ascii_table) < max_table_size: #check if table is full, if not full add value to table
           ascii_table[symbol] = len(ascii_table)
        result.append(ascii_table[temp]) #storing the ascii form of the characters of the text file in an array to print at the end
        binary_representation = '0'*(16 - len(bin(ascii_table[temp])[2:])) + (bin(ascii_table[temp])[2:]) #16 bit format representation
        binary_representation=binary_representation[0:8]+" "+binary_representation[8:] #adding a space (" ") between the binary forms
        encoded_value = encoded_value + " " + binary_representation #concatenate with final result
        temp = i

#add the last value's binary representation into the array
if temp:
    result.append(ascii_table[temp])
    binary_representation = '0'*(16 - len(bin(ascii_table[temp])[2:])) + (bin(ascii_table[temp])[2:]) #convert decimal to binary (2 byte), pad output with 0's 
    binary_representation=binary_representation[0:8]+" "+binary_representation[8:] #split 2 bytes with " "
    encoded_value = encoded_value + " " + binary_representation 

#write output to file
with open(input_file[:-4]+'.lzw', 'w') as f: #saving the file as .lzw file in write mode
    f.write(encoded_value[1:])

#output the array with all decimal values of the contents of the file
print(result)
