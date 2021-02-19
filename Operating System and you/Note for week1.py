for Windows
    GUI(Graphical User Interface)
    CLI(Command line interpreter)
for Linux
    command line only(know as shell, the language is called bash)
# GUI sub-system in Unix like OS is call "X window". Particularly, on Linux there are
# multiple popular GUI desktop manager software. Please google to read more.

windows: using \
linux: using /

windows
# More original command on windows is "dir". This is from DOS. google "MS-DOS" if you don't know about it.
ls c:\ #查看特定目录下的文件
get-help ls #查看帮助
get-help ls-full #查看完整版帮助
ls -force C:\ #查看隐藏文件

linux:
ls --help
man ls #跟help差不多，信息更详细，主要用来查看manual
ls -l / #以long list 形式显示
ls -a -l / #the same as ls -la /

<permission> <number of link file> <owner> <group> <size> <time stamp of modify> <name of file>

linux:
pwd #show current dir
cd ~ #enter home directry. Just "cd" with no option does the same.

windows:
# you can go by "md" in windows
mkdir <foldername>
mkdir 'folder name with space'
mkdir folder`name`with`space
#use `as space only in windows

linux:
mkdir folder\name\with\space
mkdir 'folder with space'

windows &linux:
history command make u can see all the command u used
ctrl + R #search the command ,same as type '#'


windows:
# orignal command on windows is "copy" and "xcopy"
cp <file name>  C:\Users\  #copy the file to the certain destnation
cp *.jpg  
cp <file name>  C:\Users\ Desktop\ -Recurse -Verbose  
#-recurse will include all the content in th folder, include child folder 
#verbose will output the cp result

Linux:
the same as windows, -recurse is -r

windows &linux:
# orignal command is "ren"
mv <filename> <filename> #change name
mv <filename> C:\Users\ Desktop\ #move file location

windows:
# original command is "del"
rm #delete file, not into recycle bin, for good
rm <filename> -force #force to delete

windows:
# original command is "type"
cat command
cat <filename> -Head 10 #show the first 10 line
cat <filename> -tail 10 #show the last 10 line
more command #fill the content the whole page, enter will move forward one line, space will forward one page,q will exit

linux:
less <filename>
#g move to the beginning, G move to the end
#/<the word you want to search> search the word, n for next match
#q exit
head <filename> #default 10 line the first
tail <filename> #default the last 10 line

windows:
# you can just use the name of the executable file without "start"
start notepad++ <filename> #open the file with notepad++, if you do not have this file, create it with confirm window

linux:
nano <filename>  #edit file with nano

windows:
# This is power shell script syntax. Does not work in "cmd" window.
Get-Alias <command name> #check the real command we are using, for example: ls  ----> Get-ChildItem
select-string <keyword> <filename> #will return the key word and the line of it
select-string <keyword> *.txt #find all the key word in the txt file in the current directories
ls <directories> -recurse -filter *.exe #search all the exe file

linux:
grep <keyword> <filename>
grep <keyword> *.txt  #search for multiply file

windows:
echo # write-output
#there are three stream in windows, stdin, stdout, stderr
> #rediectory, > will change the output to the palce we chose, if file DNE, it will create it.
>> #simliar as >, but will not overwrite
|#pipline symble
cat word.txt | select-string <keyword> #search all the keyword in the word.txt file and stdout them
1:stdout
2:stderr,, #how to indicate it is output or normal number 1?
$null #redirectory to nowhere. $null means nothing

linux:
< #is used for input from file
/dev/null #is same as $null