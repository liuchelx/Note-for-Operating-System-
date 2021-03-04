curl 
是用来传输或者发送数据到服务器上，支持的协议有：FTP.HTTP.HTTPS.IMAP,SCPD等等。
提供多种功能，FTP上传，HTTP请求，SSL链接，cookies，文件断点传输，限制带宽等

curl <website, for example www.google.com> # this command will return the html source code

curl -L <website> # 同上，如果网站有自动跳转功能，这个会自动跳到新网站

curl -i <website> # 显示response 的header info， 连同source code 一起

curl -v <website> # 显示整个通信过程,payload 信息，包括端口以及header file

curl -X POST --data "data=xxxx"  example.com/form.cgi # 可以用这种方式用POST方式传输数据

curl -o <new file name> <URL link> # 从某个URL下载文件， <new file name > 是文件下载之后新保存的名字， 如果不写<new file name> 则保存为源文件名，等同于wget

curl --limit-rate <rate> <website> # 限制带宽为<rate>里的值 
-----inly in this session

curl -S <website> # 只显示错误信息
curl -s <website> # 不显示错误信息，上面的是大写S，这个是小写

curl -u <username:password> <website> # 以<username>这个用户的身份使用<website>这个网站
