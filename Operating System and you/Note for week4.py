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

    mount #  这个命令是干啥的？
    sudo mount /dev/sdb1/my_usb/  #create a accessable directory so we use new file system
    umount #uninstall the file system
    /etc/fstab #the direc we used to mount a disk permanently
    sudo blkid #to get the block id , which is the uuid for the disk

    swap space
    enter the parted terminal, then use mkpart primary linux-swap 5GiB 100% #100% means use all the avaiable space
    quit the parted, then 
    sudo mkswap /dev/sdb2
    sudo swap on /dev/sdb2
    #if we want auto boot a disk every time, then add a swap item in the /etc fstab

windows:
    MFT(master file table) #each file has at least one record in MFT, usually it's one on one. but if a file may has more.
    MFT:
        file name  
        timestamp
        Permission
        compression
        location
        etc.....
    file record number: the index of MFT
    symbolic link # similar to short cut, but what is the differece????
    mklink #we can use this command to make a symbolic link , follwed by -H, will make a hrad link, 
    #hard link means even change the name, the short cut still point to the orgin file

linxu:
    inode#similar to the MFT of windows, contain all the 
    softlink # point to a file
    hardlink # point to a inode in inode table
    ln <filename> <filename_hardlink >
    ls -l <filename># the last digit, which is a number, indicate the amount of hard link of the file
    du -h # to check the usage of the disk, -h make it readable
    df-h # disk free, how much free disk on your disk