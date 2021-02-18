#stand for change mode, u==user, g=group,o=others(all the others users), a=all(all the users),
#operator: + :add new authority, -: remove authority, =: set user authority, all the authority will be reset
#permission: r: read, set it readable. w:write, set it writable. x:excute, set it excutable.X:special excute
#7 == rwx
#6 == rw-
#5 == r-x
#4 == r--
#3 == -wx
#2 == -w-
#1 == --x
#0 == ---

#set file to all user can read
chmod ugo+r <filename> or chmod a+r <filename>

#set current user and the group can write, others can not
chmod ug+w,o-w <filename>

#also, this can be represent by numbers
chmod 777 <filename> #this commond is the same as chmod a=rwx <filename>
chmod 771 <filename> # chmod ug=rwx,o=x <filename> 

chmod 0755 ? why there's four digits? 0,1,2,4
chmod 4755