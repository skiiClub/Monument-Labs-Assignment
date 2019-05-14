from subprocess import Popen
import time
import sys

#list given in prompt
commands = [
    'sleep 3',
    'sleep 4',
    'sleep 5'
]

#input_commands holds a tuple of the command and its Popen function
#command_times takes the command as a key and its runtime as a value 

input_commands = []
command_times = {}
total_time = float()

begin = time.time()

#starting all the commands using Popen. 
for command in commands:
    process = tuple((command, Popen(command, shell=True)))
    input_commands.append(process)


#variables that we will need to show the results. 

combined_time = 0
highest_value = sys.float_info.min
highest_name = ""

lowest_value = sys.float_info.max
lowest_name = "" 

#loop through the list. If the command ends add it to the dictionary command_times
#loop ends when every command is accounted for in the dictionary. 

while True:
    for command in input_commands:
        if command[1].poll() == 0 and command[0] not in command_times.keys():
            end = time.time()
            result = end-begin
            combined_time += result

            if result > highest_value:
                highest_value = result
                highest_name = command[0]

            if result < lowest_value:
                lowest_value = result
                lowest_name = command[0]
            
            command_times[command[0]] = result

#Breaks the loop when every command has been accounted for. 
    if len(commands) == len(command_times.keys()):
        process_end = time.time()
        total_time = process_end - begin 
        break

#displaying results

print("The total elapsed time to run the commands was: " + str(round(total_time,3)) + " seconds.")

print("The average time for each command to run was: " + str(round(combined_time/len(commands),3)) + " seconds.")

print("The longest time taken to run a command was the '" + highest_name + "' command which took " + str(round(highest_value,3)) + " seconds.")

print("The shortest time taken to run a command was the '" + lowest_name + "' command which took " + str(round(lowest_value,3)) + " seconds.")








            










      
    
