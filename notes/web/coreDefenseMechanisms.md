# Handling User Access

## Basics

- Authentication: establishing that the user is in fact who he claims to be (typical login form). Common attacks: guessing usernames, passwords, bruteforcing those, bypass login functionality, etc.
- Session Management: Different users leads to different session which needs to be managed, usually handled via tokens. Token is a unique string that the application maps to this session. When a user received a token the browser automatically submits this back to th server in each HTTP request. HTTP cookies are the standard methods of transmitting tokens. Sessions should expire. Attacker might mascaraed as a victim user
- Access control (Authorization): decisions wether each individual request should be denied or allowed. Example: 403 - Access denied.

## Handing user input

"All user input is untrusty"

### Approaches of input handling

#### Reject known bad

employs a blacklist with a word list.
is the least affective

#### Accept good known

allows data that matches the white list

#### Sanitization

Instead of preventing the malicious content the application sanitizes it. Might encode the data, f.e.: usual behavior again XSS attacks is HTML encoding of dangerous chars.

#### Safe Data Handling

many vulns arise because the data is processed in unsafe ways. Often said that vulnerabilities can be avoided not by validating data, but by safer data processing. F.e.: SQL injection can be prevented trough a correct use of parameterized queries for database access.

#### Semantic checks

Sometimes the input provided in not malicious, f.e.: an attacker might want to gain access to another user account by changing the account number transmitted hidden in the form field.

#### Boundary Validation

While checks on client side might be good from a performance perspective, they do not provide any assurance of data that reaches the server.
Here each functional unit or individual component treat each input as coming from a potentially malicious source. Data validation is performed on each of these trust boundaries.

Example Login:
User - Application Server -SQL queries--> Database
-SOAP Message-> SOAP Service

1. General checks on user login form data before reaching the application server. f.i.: for permitted chars, length, does not contain known attack signatures
2. Clean SQL before transporting to database: Application performance SQL query to verify user credentials. To prevent SQL injection chars that may be used to attack are escaped in the user input.
3. If login succeeded user profile is received from soap services. To prevent SOAP injection attacks: Encode XML metacharacters before calling the SOAP services:
4. The application wants to display user account data to the client, server HTML encodes any user-supplied data to avoid XSS.

#### Multistep validation

f.e: `<script>`

- if the `<script>` is just filtered non-recursively following might work: `<scr<script>ipt>`
- or `<scr"ipt>` when only `"` gets removed
- When input is send from users browser it might be encoded. F.e: application might defend against SQL attack with removing the `'` sign and attacked might avoid this by entering the url encoded form `%27` but also with `%%2727` if the application strips `%27` non recursively
