Name: Akash Ashok
UNCC ID: 800991236

Programmed in Python, 2.7

Files encountered in this Project:
1. Encode.py : contains the code for encoding the contents of a file
2. Decode.py : contains the code for decoding the contents of a file
3. Text.txt : contains the data to be encoded
4. Text.lzw : contains the encoded data
5. Text_decoded : contains the data after decoding

Encode.py:

"input_file" is the file which is obtained as the first argument from the command line. It contains the string to be encoded.
The data structure used is the Dictionary data structure which holds values in the form of key-value pair. 
The algorithm steps are perfomed and the binary representation is obtained in Python using the bin() function. The binary representation
stores the values in the form "ob" followed by the binary representation. 
The binary representations of all the contents of the file read are stored in another file of the same name but of format ".lzw".
The result is printed onto the terminal.

Decode.py

This contains the same input variables as Encode.py. The file is read and the data is stored in a variable. The text is split byte-by-byte
and is read 2 elements at a time to convert it into a decimal form. All the elements are converted the same way.
All the converted elements are then concatenated into the variable "result".
The contents of the variable result are then copied to a file which has the same name as the input file followed by "_decoded".
The decoded contents are also displayed onto the console.

Execution procedure:

1. Open the terminal with the path of the project directory.
2. Enter the text to be encoded into the file "text.txt".
3. Run the following command in the terminal to encode the contents of the file:
	python encode.py text.txt bit_length
4. Check the output on the terminal and also check the encoded content in the file text.lzw.
5. Run the following command in the terminal to decode the contents of the file:
	python decode.py text.lzw bit_length
6. Check the output on the terminal and also check the decoded content in the file text_decoded.txt