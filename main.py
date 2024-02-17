master_pwd = input("Enter the master password: ")

def view():
    with open('passwords.txt', 'r') as f: 
    # this opens the file in readme mode
        for line in f.readlines(): 
            # readline() is used to select only one line at time which is stored in line variable.
            data = line.rstrip() 
            # this is used to remove the tailing character (/n), which is added at the end of every pwd.
            user, pwd = data.split("|") 
            # this would store the username in 'user' and password in 'pwd'.
            print(f"USER: {user} | PASSWORD: {pwd}")


def add():
    acc_name = input("Enter account name: ")
    acc_pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(f"{acc_name} | {acc_pwd} \n")
# 'open('file_name', 'open_mode')' cmd is used to open a file in a specific mode,
# main ones include 'r' for read only mode; 'w' for overwite mode and 'a' of append mode.
# ... more under 'leanings'.
# (\n) is used to prevent stacking of different password data in same line. 

while True:
    mode = input("Do you want to add a new password or view the existing ones or type 'q' to quit? (view/add): ")
    mode = mode.lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()
    else:
        print("Enter a valid mode.")
        continue
