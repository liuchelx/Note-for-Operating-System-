windows:
    session manager subsystem(smss.exe) # this process in charge of setting up for OS to work
    winlogon.exe # the smss.exe will lanuch this 
    csrss.exe (Client/server runtime subsystem) # run windows GUI and command line consult
    taskkill /pid <process ID> # kill the process with its ID

Linux:
    all the process comes from another one, the first process start everything is init, which pid is 1

windows:
    tasklist #show all the process on cmd
    get-process # get all the process on power shell
 
 linux:
    ps -x #check all the process output as follow
    PID#PROCESS Id
    TTY#associate with termial and process, no detail for now
    stat#the state of the process, R fmeans running, T for stop, s is interruptible sleep, mean it wait for sth then resume
    time# the total cpu time the process take
    command#the name of the command we are running

    ps-ef#-e means get all the process, even other users,-f means full, show the full info
    UID #the user id who lanched the process
    PPID# partent process ID of the process 
    C #the children process of this process
    stime # the start time of the process

    ps- ef | grep chrome # output certain process
    everything in linux has a file, even for processes, the process file in the proc direc
    ls -l /proc #check all the process
    cat /proc/1805/status # 1805 is the pid, this will give more info about the process

signal: a way to tell a process that sth just happened
SIGINT: signal interrupte 

Windows:
    process explorer: created by Microsoft to look at running processes
    MUI: multilingual user interface, contain a package to support different language

linux:
    kill <pid> # terminate a process with pid, and give some time for the process to clean up
    kill -kill <pid> #sigkill command, this will immediately kill the process
    kill -tstp <pid> # sigtstp command, signal stop, this will pause the process
    kill -cont <pid> #resume the stopped process

    top#this command will list the process use the most resources
    uptime#this command will list all the following info: start time, how long this machine has been running, how many user has logged in and load average
    #for load average, there will be three number, its the load average for 1, 5 and 15 mins
    lsof#list the file and which process is using them