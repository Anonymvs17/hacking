Paypal had a vuln where the user was asked about his secret question, in the post request a hacker could delete the secQuestion and it would work!
`secQuestion0=test&secQuestion1=test&jsEnabled=1&verifyMethod=SEC_QUESTIONS&userId=12309746`
* Also try instead of deleting the secQuestion to `secQuestion3`, `secQuestion4` or `secQuestionA` `secQuestionB`

# Password bruteforcing
* If IP blocking check if 'X-Forwared-For' header is supported and try to manipulate it
* Check for response times when providing a very long pw with valid and invalid logins

# Token
there are number of locations where applicaitons depend on unpredicted tokens.
* Password recovery tokens sent to the user’s registered e-mail address
* Tokens placed in hidden form fields to prevent cross-site request forgery attacks (see Chapter 13)
* Tokens used to give one-time access to protected resources
* Persistent tokens used in “remember me” functions
*  Tokens allowing customers of a shopping application

## Meaningful tokens
mighe be encripted with: 
* The numeric identifi er that the application uses to distinguish between
accounts
* The user’s fi rst and last names
* The user’s e-mail address
* The user’s group or role within the application
* A date/time stamp
* An incrementing or predictable number
* The client IP address

somethimes created like: 
`user=daf;app=admin;date=10/09/11`
generates long random string of `757365723d6461663b6170703d61646d696e3b646174653d30312f31322f3131`

Attackers can exploit the meaning within this session token to attempt to guess the current sessions of other application users

## Predictable token
Some session tokens do not contain any meaningful data associating them with a particular user. Nevertheless, they can be guessed because they contain sequences or patterns.

Arise from three different sources:
* Concealed sequences: 
* Time dependency
* Weak random number generation

Testing the Quality of Randomness with Burpsuite: 
* Interrupt on request
* send to Sequencer
* Select cookie (JSessionID and it will start via "start live attack")

## Encripted tokens

## ECB Cyphers

ECB (Electornic Code Book): encrypts everything in 8 byte blocks, f.e: 
`session might look like unencrypted: rnd=333133313;app=myApp;username=boris;uid=2021;`
ECP cyper is like this: 
uid=3333 3IEEISIJIESOKW
133313;a DDEEDSSSEEEESS
...

Now, because each block of ciphertext will always decrypt into the same block of plaintext, it is possible for an attacker to manipulate the sequence of ciphertext blocks so as to modify the corresponding plaintext in meaningful ways

rnd=2458    68BAC980742B9EF8
992;app=    0A27CBBBC0618E38
iTradeEU    0A27CBBBC0618E38
R_1;uid=    BD223F003A8309DD
992;app=    *B6B970C47BA2E249* => here we might change the uid.
218;user    D51A3E150EFC2E69
name=daf
ydd;time
=6344304
23694715

## CDC (cypher block chaining) Cyphers
With a CBC cipher, before each block of plaintext is encrypted it is XORed against the preceding block of ciphertext

Plain text to                    Plain text + Block cypher B(encrypted) to       and so on...
Block cypher encryption A           Block cypher encryption B

Because CBC ciphers avoid some of the problems with ECB ciphers, standar symmetric encryption algorithms such as DES and AES frequently are used
in CBC mod. the way in which CBC-encrypted tokens are often
employed in web applications means that an attacker may be able to manipulate
parts of the decrypted tokens without knowing the secret key.

Example: `rnd=191432758301;app=eBankProdTC;uid=216;time=6343303;`
Encrypted in: `0FB1F1AFB4C874E695AAFC9AA4C2269D3E8E66BBA9B2829B173F255D447C51321586257C6E459A93635636F45D7B1A43163201477`
By changing chars we might changed uid: 

In each case, the block that the attacker has modifi ed decrypts into junk, as expected (indicated by ???????? ). However, the following block decrypts into meaningful text that differs slightly from the original token

????????320*8*58301;app=eBankProdTC;uid=216;time=6343303;
????????3278321;app=*e*BankProdTC;uid=216;time=6343303;
rnd=1914????????;aqp=eBankProdTC;uid=*216*;time=6343303;
rnd=1914????????;app=eAankProdTC;uid=216;time=6343303;
rnd=191432758301????????nkPqodTC;uid=216;time=6343303;
rnd=191432758301????????nkProdUC;uid=216;time=6343303;
rnd=191432758301;app=eBa????????;uie=216;time=6343303;
rnd=191432758301;app=eBa????????;uid=226;time=6343303;
rnd=191432758301;app=eBankProdTC????????;timd=6343303;
rnd=191432758301;app=eBankProdTC????????;time=6343503;`

You can easily test applications for this vulnerability using the “bit flipper” *payload* type in Burp Intruder.

## Weaknesses of tokens

* Network: http traffic
* Logs: get and redirect in header: http://www.webjunction.org/do/Navigation;jsessionid=F27ED2A6AAE4C6DA409A3044E79B8B48?category=327
* Mapping: The simplest weakness to allow multiple valid tokens to be concurrently assigned to the same user account, using always the same token for a user (sometimes even "poorly designed" remeber me function), Liberal cookie scope (check domain, security, etc.)

# Json Web Token (JWT)
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object

example token: `eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MTM5MDMxMzgsImFkbWluIjoidHJ1ZSIsInVzZXIiOiJUb20ifQ.ZMogKrHPkVcm57kB4Bzza0BG0Ysi13cewSpNcgGFGjISsaHraDefAHg1jO9ZZu6TYiEk38jfx0Bw3S2X0bGe6Q`

In this flow you can see the user logs in with a username and password on a successful authentication the server returns. The server creates a new token and returns this one to the client. When the client makes a successive call toward the server it attaches the new token in the "Authorization" header. The server reads the token and first validates the signature after a successful verification the server uses the information in the token to identify the user.

The token contains claims to identify the user and all other information necessary for the server to fulfil the request. Be aware not to store sensitive information in the token and always send them over a secure channel.
Each JWT token should at least be signed before sending it to a client, if a token is not signed the client application would be able to change the contents of the token

* use to test tokens and decode them: https://jwt.io/

## JWT none attack
https://pvxs.medium.com/webgoat-jwt-tokens-4-5-ff5bd88e76f

## cracking secret key for JWT
With the HMAC with SHA-2 Functions you use a secret key to sign and verify the token. Once we figure out this key we can create a new token and sign it. So it is very important the key is strong enough so a brute force or dictionary attack is not feasible

use hashcat for JWT like: `hashcat token.txt -m 16500 -a 3 -w 3 /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt --force`

# Oauth

Usually secure, but not many minumum security restrictions, therefor a lot of security issues left to developers.

Usually used when logging in a a website via Gmail or Facebook login.

## implicit
Example of implicit way (more fragile)

* use is on side A and clicks to login via facebook, server sende following to oath server: 
GET /auth?client_id=d1z7f0i81d1qzs3nb1new&redirect_uri=https://ac1b1f021f0f10b6801d701b00ac00b1.web-security-academy.net/oauth-callback&response_type=token&nonce=45977936&scope=openid%20profile%20email HTTP/1.1
* Once usr logins and cofirms a token is being send to the side A

## usualy
In contrast to the implicit, not the token is being send from the oauth server but the code, with this code the server has to register a token for the user (so the user browser does not know what is happening there) and then gets the token (bearer)

{stamp:%274Zv73YrV0wYtJVkUPrAW+8jdY2aiOQV8mERBqz4OP/jUAcaKLXk8uQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1613557218737%2Cregion:%27at%27}

# Multifactor Auth

* Check for bruteforcing of 1st and 2nd step
* Check for login flaws (not validting successful 1st step in 2nd step)

# Vulnerabilities in other authentication mechanisms

* Keeping users logged in: to stay logged in even after closing a browser session. This is usually a simple checkbox labeled something like "Remember me" or "Keep me logged in". Usually this "Remember me" token is stored in cookies which allows to bypass the login. if you have base64 encoded string and you decode it you might get: wiener:0330DIEDLO => then to find out the hash algo for the pw just has you pw. 
* 