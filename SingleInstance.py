from os import getpid, path
from psutil import Process

home_directory = path.expanduser("~")
# Construct the path to the desktop
desktop_path = path.join(home_directory, "Desktop")

#Give Path to save the PID file here
pid_file_path = path.join(desktop_path, "PIDfile.txt")

#A unique identifer to attach with PID's so the script does not accidently terminates another program's Process
identifier = "_singleInstance_"
  
#Write the PID of the script
def write_pid():  
    with open(pid_file_path, 'w') as pid_file:
        pid_file.write(f"{identifier}\n{getpid()}")

def read_pid(): #Read the PID from the file 
    if path.exists(pid_file_path): 
        with open(pid_file_path, 'r') as pid_file:
            lines = pid_file.readlines()
            if len(lines) >= 2:
                file_identifier = lines[0].strip()
                file_pid = lines[1].strip()
                try:
                    #Get the last saved PID
                    return file_identifier, int(file_pid) 
                except ValueError:
                    return None, None
    return None, None

def terminate_pid(pid):
    try:
        process = Process(pid)
        process.terminate()
    except Exception as e:
        print(f"Error caught: {e}")
        
        
previous_identifier, previous_pid = read_pid()


if previous_pid and previous_identifier == identifier: #Get the Identifier and PID of last instance, and terminate  
    terminate_pid(previous_pid)        
          
write_pid() #Write the PID of this (latest) instance


# Use Other Imports here (To ensure the script loads these only when it is the ONLY instance)
import os 

#Your code goes here
while(True):

    print("I'm inevitable")
    
