def binaryToDecimal(binary): 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

test = int(input())
while test:
    length = int(input())
    encoded = input()
    sections = []
    size = 4
    for index in range(0,len(encoded),size):
        sections.append(encoded[index:index+size])
    
    letters = ''

    for letter in sections:
        decode = binaryToDecimal(int(letter))
        letters += chr(97+decode)
    print(letters)
    test -= 1
