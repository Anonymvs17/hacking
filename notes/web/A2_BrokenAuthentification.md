Paypal had a vuln where the user was asked about his secret question, in the post request a hacker could delete the secQuestion and it would work!
`secQuestion0=test&secQuestion1=test&jsEnabled=1&verifyMethod=SEC_QUESTIONS&userId=12309746`
* Also try instead of deleting the secQuestion to `secQuestion3`, `secQuestion4` or `secQuestionA` `secQuestionB`


# Token
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