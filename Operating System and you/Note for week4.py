file system:
windows:NTFS
Ubuntu: ext4
windows, MAC, linux:fat32: support all 3 system

Partition: the piece of a disk that you can manage
two main partition table schemes: MBR(Master boot record) #main on windows, only allow 2TB or less
                                  GPT(GUID partition Table)# 2TB or more, new, no partition limit

windows:
    Diskpart # format, after this command, we will enter a speical termianl window
    list disk # list all the dist
    select disk 1 # select the disk 
    clean# earse all the data in the disk
    create oartition promary # create a partition for the disk
    select partition 1 #select the partition just created
    active # active the partition
    format FS=NTFS label=<name of the disk> quick #format the disk with the factor you typed

linux:
    sudo parted -l #show all the disk info
    sudo parted /dev/sdb #enter the manage situation, there will be a new terminal , sdb means the  second disk, sda is the frist one
    print # after entering the special terminal, we can use print to check the state of the disk
    mklabel gpt #set the disk label with gpt partition
    mkpart primary ext4 1Mib 5Gib # the command used to slice the disk with factor
    quit # quit
    