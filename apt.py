#APT is advance packaging tool , normally need sudo before it
#最早rpm格式，一组server存放系统软件的组件，到server上dl到本地

#update the software
sudo apt update

#list all the avaliable info
apt list --upgradeable
apt list --installed
apt list --all-versions

#updrade the software, the full-upgrade will delete the current package
sudo apt upgrade
sudo apt full-upgrade

#install, remove(the config document will be left), purge(all the document include config docment will be deleted)
sudo apt install <package name>
sudo apt remove <package name>
sudo apt purge <package name>

#remove the package that been autoinstalled, if the related package that has been deleted, then those autoinstalled package could be remove by this command
sudo apt autoremove

#search for command
sudo apt search <keyword>

#can also be combined by -y
sudo apt update && sudo apt upgrade -y

