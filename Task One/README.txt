NOTE: The command 'uptime' would not run on my machine. My python script runs without it but does not work with 'uptime' included in the commands list. 
It does not work in my shell console either. 


Out of the two tasks given, this one was more difficult to implement. I originally tried to run all the commands at once by formatting the list
into a string and seperating the commands with a semicolon (e.g. "sleep 3; 'ls -l /'; etc), and then passing the string into the Popen function. 
Doing it this way did allow for all the commands to execute simultaneously, but it wouldn't allow me to record the individual times for each command. 

Since I needed to record the time of each command, I needed a new approach. My new process was to loop through each command in the list, call Popen() on
that command, and then append it to a list of tuples, which was made up of the name of the command and its Popen() function. After I finished iterating 
through the list, I then began to loop through the tuple list, checking whether or not the Popen() function ended by calling poll() on it. If the function
ended, I calculated the time it took to run and added the data to a dictionary (with the key being the commmand and its value being its time.) After all 
the commands had been added to the dictionary, I break out of the loop and calculate the time results. 

There are a few issues with my implementation. For one, the commands don't actually start at the same time. While the commands may run in parallel, their 
start times are incrementally further away from each other because they are declared in a loop. For this particular case, the results weren't tampered too
significantly, however it would be an issue if the command list is very large, as looping through the list is an O(N) process. Since the timer begins when 
the loop starts, the timer would be inaccuate for a large set of commands in the input list. Similarly, the way I check for whether or not the command 
has stopped running is not 100% accurate, as I only know if the function has stopped when I loop over it in the while True loop. This was not an issue 
for the problem given, but would be problematic if the command list was very large. 