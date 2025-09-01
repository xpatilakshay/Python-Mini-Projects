'''
📍 Concepts: Variables, Data Types, Type Casting, Input/Output, Operators, Strings, 
Control Flow (if/else), Loops, Functions (basic).

📝 Task: Simple Calculator + Text Analyzer

Ask user for two numbers and perform all arithmetic operations.

Ask user for a sentence → count vowels, consonants, digits, and spaces.

Functions must be used for each operation.

'''

# print(eval(input("enter expression in one go eg.(12+3,10*2) : ")))

def arith(num1,num2):
    print("\nChoose the operation to perform arithmetic operation (+,-,/,*.**,//,%)")
    opr = input("choose the operation from above : ")
    result = None
    match opr:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "/":
            result = num1 / num2
        case "//":
            result = num1 // num2
        case "*":
            result = num1 * num2
        case "**":
            result = num1 ** num2
        case "%":
            result = num1 % num2
        case _:
            print("Kindly choose valid arithmetic operation from (+,-,/,*.**,//,%)")
    print(f"{num1} {opr} {num2} : {result}")

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
arith(num1,num2)

print("-----------------------------------------------------------------------------------")

def counter(sentence):
    vowels = "aeiou"
    vowels_count = consonant_count = space_count = digit_count = other_count = 0
    for c in sentence.strip().lower():
        if c in vowels:
            vowels_count+=1
        elif c.isalpha():
            consonant_count+=1
        elif c.isdigit():
            digit_count+=1
        elif c.isspace():
            space_count+=1
        else:
            other_count +=1

    print(f"\nVowels : {vowels_count}\nConsonants : {consonant_count}\nSpaces : {space_count}\nDigits : {digit_count}\nOther Characters : {other_count}")


sentence = input("Enter your sentence : ")
counter(sentence)