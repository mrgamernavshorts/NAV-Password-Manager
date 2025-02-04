from cryptography.fernet import Fernet
import os

if not os.path.exists("data/key.key"):
    if not os.path.exists("data"):
        os.mkdir("data")
    key = Fernet.generate_key()
    f = open("data/key.key", 'w')
    f.write(key.decode())

f = open("data/key.key", 'r')
key = f.read()

print("/c or /a Create or add a new Password")
print("/g - Get a password already stored")
print("/ls - List all the Passwords")
print("/d or /delete - Delete a password")
init = input("What do you want to do: ")

if init.startswith("/c") or init.startswith("/a"):
    Password = input("Enter the Password: ")
    Pname = input("What do you want to name it: ")
    
    if not os.path.exists("data/"+Pname+".pass"):
        print("encrypting password..........")
        content = Fernet(key).encrypt(Password.encode())
        content = content.decode()
    else:
        warn = input("WARNING:the password already exists!Do you want to Overwrite it ?(y/n): ")
        if warn == "n":
            input("rewrite of password aborted!")
            exit(0)
        print("Rewriting the password.........")
        content = Fernet(key).encrypt(Password.encode())
        content = content.decode()
        print("password rewrited!")

    pf = open("data/"+Pname+".pass", 'w')
    pf.write(content)
    print("password created!")
elif init.startswith("/g"):
    Pname = input("Enter the name of the password: ")

    pf = open("data/"+Pname+".pass", 'r')
    content = pf.read()
    content = Fernet(key).decrypt(content)
    print("The password is: "+content.decode())
elif init.startswith("/ls"):
    print("")
    for i in os.listdir("data"):
        if i == "key.key":
            continue
        print(i.replace(".pass",""), end=" ")
    print("\n")
elif init.startswith("/d") or init.startswith("/delete"):
    Pname = input("enter the password you want to delete(type * to delete all passwords): ")
    if Pname == "*":
        for i in os.listdir("data"):
            if i == "key.key":
                continue
            os.remove("data/"+i)
        print("removed all the passwords")
        input("")
        exit(0)
    for i in Pname.split(" "):
        if i == "key.key":
            continue
        os.remove("data/"+i+".pass")
        print("removed password "+i)
input("")
