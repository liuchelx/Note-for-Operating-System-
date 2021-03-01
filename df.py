df 是disk filesystem，用来查看文件系统的整体磁盘使用情况，显示的磁盘容量默认最小值为1k
df -h #使用人类可读的形式显示，h是human readable
df -a #列出所有文件系统，包括系统特有的/proc文件系统
df -T #显示时包括文件类型


实际效果
# df 
Filesystem     1K-blocks    Used     Available Use% Mounted on 
/dev/sda1       29640780 4320704     23814388  16%     / 
udev             1536756       4     1536752    1%     /dev 
tmpfs             617620     888     616732     1%     /run 
none                5120       0     5120       0%     /run/lock 
none             1544044     156     1543888    1%     /run/shm 

Filesystem：文件名称，  1K-blocks：系统文件总大小，Used：已经使用了的大小，Available：剩余大小，use%:使用的百分比，
Mounted on: 磁盘挂载的所在目录。在linux中磁盘设备和文件是存在挂载的关系。比如上图中/dev/sda1, 这个其实代表的是一个磁盘。这个磁盘必须挂载(mount)到一个目录底下才能被用户访问到
如果输入时代了 -h， 单位会变成,Mb，Gb等等