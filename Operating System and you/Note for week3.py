package type:
windows: 
    exe (executable file)
    msi (microsoft install package)#
    appx #from windows store?

linux:
    deb (debian package)
    dpkg #use to install deb package
    sudo dpkg -i atom-amd64.deb #example to isntall  , i is install flag
    sudo dpkg -r atom-amd64.deb # example to remove, r is remove flag
    dpk -l #list all 
    dpk -l | grep atom # search the certain package

windows:
    Archive # 7-zip as tool to archive
    compress-Archive -Path <file name and direction> <direction+filename.zip># archive a file to certain place

linux:
    7z e <filename> #will archive this file to its current location

DLL #Dynamic-link libraries
side -by-side assemblies #sxs control shared library, support system access multple version of same lib

windows:
    Chocolatey# a place where all type of windows software package live
    register-packageSource -Name chocolatey -ProviderName chocolatey -Location http://chocolatey.org/api/v2
    get-packageSource
    Find-package sysinternals -includeDependencies #没太看懂这些命令是干啥的

    install-package -Name sysinternals #intsall the whole package of certain software
    get-package -name sysinternals #find the location where the package is
    uninstall-package -Name sysinternals #remove the package

linux:
    apt#will install the dependency for us
    /etc/apt/source.list #software link, or repsotory source, only the link is contained in the folder, the software can be installed by  apt

windows:
    process monitoring# a toole used to check the process of installation to see what happened during installing
    orca.exe # a tool provided by microsoft to create a MSI file and package an exe


windows:
    driver: each device has its own hardware ID, when plug in, the windows will ask for the hardware ID, the OS will use this ID to search the correct driver

linux:
    when device comes in, a file will be create in /dev
    character devices: transimit data character by character, like mouse and keyboard
    block device: transfer block of data,like USB, hard drives
    /dev/sda #sd means large storge device, a is the order the OS dected the device

    kernel module: extend the kernel function without make change of it

    uname -r #check the kernel version
    sudo apt update
    sudo apt full-upgrade #this command will upgrade the whole system, include the kernel
