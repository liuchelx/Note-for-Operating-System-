windows:
    session manager subsystem(smss.exe) # this process in charge of setting up for OS to work
    winlogon.exe # the smss.exe will lanuch this 
    csrss.exe (Client/server runtime subsystem) # run windows GUI and command line consult
    taskkill /pid <process ID> # kill the process with its ID

Linux:
    all the process comes from another one, the first process start everything is init, which pid is 1