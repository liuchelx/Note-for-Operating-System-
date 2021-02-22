windows domain
a network of computers,users,files,etc that are added to a central database

windows:
Get-localUser  #
get-localGroup  # check all the group name
get-localgroupMember  <group name> #check who is in the group

linux:
root user: normally the first user who install the OS, has all the permission
cat /etc/sudoers #sudoers file is a protect file can only be read by root user
sudo cat/etc/sudoers
su command #change into superuser, default is root, example: sudo su -, exit will log out
group name: group password: group id: list of users  #example
sudo:X:27:dust  #X mean this password is been hidden
/etc/password #the file store user informantion

linux:
passwd <username># change the password for user
sudo passwd -e <username> #force the user to change their name next they log in

windows:
net user <username> * /add # add a new user for the computer
net user <username> /logonpasswordchg:yes #ask the user to change password next time log on
net user <username> password /add /logonpasswordchg: yes #create a new user and force to change the password

ACL:access control listst (ACLS)
icacls <folder name> #can check the access of the folder, icacls is stand for change acl,example icacls ~/Desktop
dust/dust:(OI)(CI)(F) # the result of icacls ,F: full control, OI:object inherit,container inherit. more result can see by icacls /?

linux:
ls -l ~/<filename> #check the info about the file
-rwxrw-r-- #represent the access, the first one - means it is a file, 3 a group, first 3 is for user, second 3 for group, last 3 is for others 
icacls "C\Vacation Pictures"/grant Everyone:(IO)(CI)(R). #cmd to change the permission
icacls 'C:\Vacation Pictures\' /grant 'Everyone: (OI)(CI)(R)' # power shell to change the permission
icacls 'C:\Vacation Pictures\' /remove Everyone # power shell to remove the permission

setUID #-rws the s instead of x, is setuid, make the file can be run like the root user without real root access, when change by chmod, it is the 4 of 4777

