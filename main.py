import random,os,string


numberindex = [True, True, True ,True ,True]
userinput = []
number = random.choices(string.digits, k=5)
displaynumber = int("".join(number))
score = 5
win = False
counter_index_1 = 0




for i in range(5):
    counter = 1
    os.system("cls")
    print("\n\n         ", end="")
    for j in range(5):
        if numberindex[j] == True:
            print("_", end=" ")
        else:
            print(number[j], end=" ")
    print(f"      Tries left: {score}")
    print("\n\n")
    for j in userinput:
        print(f'{counter}- {j}')
        counter += 1

    numberinput = int(input("\n\nGuess the number: "))

    if numberinput == displaynumber:
        userinput.append(numberinput)
        win = True
        break
    else:
        userinput.append(numberinput)
        for i in range(0,5):
            for j in str(numberinput):
                if int(number[i]) == int(j):
                    numberindex[i] = False
        score -= 1
        

os.system("cls")
counter = 1
if win:
    print("\n         CONGRATS YOU WON!!!")
    for j in userinput:
        print(f'{counter}- {j}')
        counter += 1
    
    input(" ")
else:
    print(f'''\n
            The number was {displaynumber}\n\n
    ''')

    for j in userinput:
        print(f'{counter}- {j}')
        counter += 1

    input(" ")
