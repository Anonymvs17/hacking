# checking files on detectablity

* go to virustotal.com and upload some file

# bypassing antivirus detection

## ondisk-envasion
* packers: smaller and completly new binary structure therefor a new signuture. bypass older and more simple AV programs
* Obfuscators: replacing instruction with semathic equivivalent code, reordering functions, etc.
* *Crypters* “Crypter” software cryptographically alters executable code, adding a decrypting stub that restores the original code upon execution. This decryption happens in-memory, leaving only the encrypted code on-disk. Encryption has become foundational in modern malware as one of the most effective AV evasion techniques

## in memory injection
popular technique to bypass AV
* focuses on manipulation of memory
* does not write any file to disk (which is the main focus of AV)
* Reflective ddl injection: shored by the attacked in the DLL memory (usually disk based), not using load libabry, windows op system does not expose any API to handle this => program needs to be written
* Process hollowing: When using process hollowing424 to bypass antivirus software, attackers first launch a nonmalicious process in a suspended state. Once launched, the image of the process is removed from memory and replaced with a malicious executable image. Finally, the process is then resumed and malicious code is executed instead of the legitimate process
* Inline hooking: As the name suggests, this technique involves modifying memory and introducing a hook (instructions that redirect the code execution) into a function to point the execution flow to our
malicious code. Upon executing our malicious code, the flow will return back to the modified
function and resume execution, appearing as if only the original code had executed

## powsershell inmemory expection

* f.e.: blocked binary file to start (f.e.: by avira)
* see pdf 498