IaaS(infrastructure as a service): using cloud and vitural machine tech, for example: AWS EC2, Linode, windows azure
Naas(Network as a service): network inside the cloud
SaaS(Software as a service): cloud provide the software
PaaS(Platform as a service): cloud support coding lib, env and so on, for example: Heroku, Windows Azure, Google app engine
DaaS(Directory as a Service): support user access, authorization and so on

network service:
    file transfer service:
        FTP:no encryption,authentication
        SFTP: secure version of FTP, SSH encryption and authentication
        TFTP: Trivial FTP, no encryption, no authentication

    NTP: betwork time protocol
        used to synchronized the time

    Intranet: an internal neywork inside a company acccessible if you're on a company's network
    Proxy server: acts as an intermediary between a company network and the internet

    DNS:
        1.buy a domain name
        2.point the file to the domain name, use the DNS setting by the domain name provider or Authoritative DNS srevers

    in linux: host file is in etc/hosts,it looks as below:
        127.0.0.1   localhost # if we change to 127.0.0.1   www.google.com, then when you type www.google.com in the webbrowser, it will lead back to the computer
        DNS query first local host file then local DNS servers
    
    DHCP: using DHCP server software 

trouble shoot:
    1.ping a website to check if the internet is connected
    2.nslookup <website> #to check if the DNS is correct
        this will give us the ip address, copy to the webbrowser, to see if can reach the website
    3.if DNS is wrong, then check the local DNS setting first

background processes:
    the program does not need to interact with a user through the graphical interface or the command line interface
    the behaviour is controled by configuration files

service ntp status：#check the status of certain service, for ntp, each time it will adjust the clcok 0.5ms until it reach the desired time
                    #but if the difference is larger than 128ms, then the service will not adjust the clock
                    #if we stop the service and restart it, then the clock will be adjust

For windows:
    Get-service wuauserv #to check the status of service
    Get-service wuauserv |Format-List * #will give more info

configure service in linux:
    lftp is an ftp client program that allows us to connect to an ftp server
    start,stop,restart,modify configuration,reload


dnsmasq:
-----still confuse 
    a program that provides DNS, DHCP,TFTP and PXE services in a simple package
    dig# command that let user query DNS servers and see their answers
    dig www.example.com @localhost # the @ indicate which DNS server we would like to use
    sudo dnsmasq -d -q # -d and -q means the dnsmasq will run in debug mode and will log the queries

configuring DHCP with dnsmasq:
    eth_srv #a interface is configured to be the DHCP server's interface
    ip address show eth_srv
    cat dhcp.conf # this command will let us view the DHCP setting
    DHClient # the most common DHCP client 
