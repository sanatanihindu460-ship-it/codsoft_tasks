import random
user_win=0
comp_win=0
draw=0
while True:
    choices=["rock","paper","scissor"]
    while True:
        try:
            user_choice=str(input("\nEnter your choice\nrock\npaper\nscissor\n\nYour choice is "))
            user_choice=user_choice.lower()
            if user_choice not in choices:
                print("Invalid choice. Please enter Rock, Paper, or Scissor.")
            else:
                break
        except ValueError:
            print("Enter your choice only in string...")
    comp_choice=random.choice(choices)
    print(f"Computer choice is {comp_choice}")
    comp_choice=comp_choice.lower()
    if user_choice==comp_choice:
        print("\nMatch Draw\nBetter luck next time...")
        draw+=1
    elif (comp_choice=="rock" and user_choice=="scissor") or (comp_choice=="scissor" and user_choice=="paper") or (comp_choice=="paper" and user_choice=="rock"):
        print("\nComputer win\nBetter luck next time...")
        comp_win+=1
    else:
        print("\nYou win\nCongratulations...")
        user_win+=1
    deci=input("\nDo you want to play again (y/n): ")
    deci=deci.lower()
    if deci=="n":
        break
print(f"Your win: {user_win}\nComputer win: {comp_win}\nDraw: {draw}")
