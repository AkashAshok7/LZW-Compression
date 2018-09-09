import sys

input_file = sys.argv[1] #used to store the file name entered by the user as argument 1
bit_length = int(sys.argv[2]) #used to store bit length entered by the user as argument 2
max_table_size = 2**bit_length #used to store maximum table size

#ASCII table of 256 characters of type Dictionary
ascii_table = {i:chr(i) for i in range(256)}

with open(input_file, 'r') as f:
    text_from_file = f.read() #store the contents of the file in text form
    text_from_file = text_from_file.split(' ') #split binary text into array 1 byte each
    decimal_representation =[] #array to store decimal representation of 2 byte binary
    for i in range(0, len(text_from_file), 2): 
        decimal_representation.append(int('0b' + text_from_file[i] + text_from_file[i+1], 2)) #the decimal representation will be the ith and the (i+1)th contents of the file


#Access the first character 
string = ascii_table[decimal_representation.pop(0)]
result = string #will hold the final decoded string

#loop over each character in text
for i in decimal_representation:
    if i not in ascii_table: #check if symbol is in the table, if not present
        new_string = string+string[0]
    else: #if the symbol is present in the table
        new_string = ascii_table[i]
    result = result + new_string
    if len(ascii_table) < max_table_size: #Check if there is space for addition of new entries
        ascii_table[len(ascii_table)] = string + new_string[0]
    string=new_string

#copy the contents to a file to store the decoded data
with open(input_file[:-4]+'_decoded.txt', 'w') as f: #file will be saved as *_decoded.txt
    f.write(result)    

#display the decoded string onto the terminal
print(result)
