#cat is concatenate, can be used as create, view, link and operate files


#view the file or files
cat <filename>
cat <filename1> <filename2>

#create a file, user will input the content and exit with crtl+D
cat > <filename>  #example:cat >test

#check the content and show the line number
cat -n <filename>

#show the $ at the end of the file
cat -e <filename>

#overwrite the content of a file
cat <filename1> > <filename2> #example: cat test>test1, then the content of test1 will be overwrite

#add sth at the end of the file
cat <filename1> >> <filename2> #example cat test >> test1, the content of test will add at the end of test1

2>&1