import random as r
def find_number(n):
    print("let's play the number  guessing  game")
    print(f"i thought of a number between 1 and {n}, can you find it ")
    number=r.randint(1, n)
    number_guesses=1
    while True:
        
        guess=int(input(">>"))
        if number>guess:
            print("false, the number i thought is bigger , try again ")
        elif number<guess:
            print("false, the number i thought is smaller , try again ")
        else:
            print(f"i congrotulate you, that is true, you have {number_guesses} guesses\n")
            break
        number_guesses+=1
    return number_guesses
def find_number_pc(n):
    upper=n
    lower=1
   
    print(f"think one number between 1 and {n}, i try to find it ")
    input("if you have finished thinking, press the optional button ")
    k=0
    while True:
        number=r.randint(lower, upper)
        k+=1
        guess=input(f"you thought {number}, if my guess correct, enter (=), if my correct smaller , enter (+), else enter (-) ")
        if guess=='+':
            lower=number+1
        elif guess=='-':
            upper=number-1
        else:
            print(f"i find, i have {k} guesses")
            break
    return k

def play(n):
    guess_user=find_number(n)
    guess_pc=find_number_pc(n)
    if guess_user>guess_pc:
        print("i the winner ")
    elif guess_pc>guess_user:
        print("you the winner ")
    else:
        print("durrang ")
play(10)

        