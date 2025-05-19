#Defines conversion functions
#Decodes a single hexadecimal digit and returns its value
def hex_char_decode(digit):
    if digit.upper() == "A":
        value = 10
    elif digit.upper() == "B":
        value = 11
    elif digit.upper() == "C":
        value = 12
    elif digit.upper() == "D":
        value = 13
    elif digit.upper() == "E":
        value = 14
    elif digit.upper() == "F":
        value = 15
    else:
        #Converts the string value of digit into an integer
        value = int(digit)
    return value


#Decodes an entire hexadecimal string and returns its value
def hex_string_decode(hex): #0x
    if hex[1] == "x" or hex[1] =="X":
        #removes the prefix
        hex = hex[2:]

    sum = 0
    power = len(hex) - 1
    #Looks at the elements of hex one by one
    for i in hex:
        num = hex_char_decode(i)
        sum += num *  (16 ** power)
        power -= 1
    return sum



#Decodes a binary string and returns its value
def binary_string_decode(binary):
    if binary[1] == "b" or binary [1] == "B":
        binary = binary[2:]
    sum = 0
    power = len(binary) - 1
    #Iterate over the binary string in reverse order
    for i in binary:
        #Converts the character to an integer
        num = int(i)
        sum += num *  (2 ** power)
        power -= 1

    return sum

#Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal
def binary_to_hex(binary):
    if binary[1] == "b" or binary[1] == "B":
        binary = binary[2:]

    while len(binary) % 4 != 0:
        binary = '0' + binary

    hex = ""
    l = len(binary)

    for i in range(0, l, 4):
        #Groups four elements
        bin = binary[i:i+4]
        val = binary_string_decode(bin)
        if val >= 10:
           hex += chr(65 + (val - 10))
        else:
            hex += str(val)

    return hex

#Creates a function to display the menu
def menu():
    print(f'Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit')

#Displays the menu initially
menu()

#Creates a while loop that runs until the user
while True:
    # Asks for the users initial selection
    selection = input("Please enter an option: ")

    #Converts the numeric string based on the user's selection
    if selection == '1':
        # Asks the user to input what they want to convert
        convert = input("Please enter the numeric string to convert: ")
        print(f'Result: {hex_string_decode(convert)}')

    elif selection == '2':
        # Asks the user to input what they want to convert
        convert = input("Please enter the numeric string to convert: ")
        print(f'Result: {binary_string_decode(convert)}')

    elif selection == '3':
        # Asks the user to input what they want to convert
        convert = input("Please enter the numeric string to convert: ")
        print(f'Result: {binary_to_hex(convert)}')

    elif selection == '4':
        print("Goodbye!")
        break
    #Displays the menu again
    menu()
