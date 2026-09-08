import secrets
import string
choices=list(string.ascii_letters+string.digits+string.punctuation)

while True:
    try:
        pass_len=int(input("Enter the length of the pass you want: "))

        if pass_len <= 0:
            print("Password length must be greater than 0.")
            continue

        break
    except ValueError:
        print("Please Enter valid length of password...")


while True:
    try:
        pass_type=int(input("What type of password do you want\n1.Normal password\n2.Strong password\nEnter your choice: "))
        break
    except ValueError:
        print("Please Enter in the form of integer.....")

if pass_type==1:
    for i in range(pass_len):
        gen_pass=secrets.choice(choices)
        print(gen_pass,end="")

elif pass_type == 2:
    if pass_len < 4:
        print("For this password type, length must be at least 4.")

    else:
        choices = string.ascii_letters + string.digits + string.punctuation

        gen_pass = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation)
        ]

        for i in range(pass_len - 4):
            gen_pass.append(secrets.choice(choices))

        secrets.SystemRandom().shuffle(gen_pass)

        print("".join(gen_pass))

else:
    print("Your choice is out of range!")
