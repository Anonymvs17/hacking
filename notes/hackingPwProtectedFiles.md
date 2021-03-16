 # How are file encrypted
* Depending on the program used and its version, these sorts of files could be password protected using various encryption algorithms.

* For example, the Linux command line zip utility uses the older PKZIP algorithm, which is insecure and easy to crack. 
* Other programs, like WinZip and 7-Zip, use strong AES-256 encryption. Earlier versions of the RAR protocol use a proprietary encryption algorithm, while newer versions use AES. WinRAR and PeaZip, popular choices that can deal with RAR files, also use the AES standard.
* If you're using Linux, it's easy to create PDFs in LibreOffice by exporting regular word documents, and there's even an option to password protect the newly created file. 
* Older versions of LibreOffice use the Blowfish algorithm to encrypt files, but versions 3.5 and up use AES. 
* Other methods to create PDF files include Microsoft Office and Adobe Acrobat — Office versions 2007+ and Acrobat versions 7+ all support AES encryption.


 # Hacking pw protected files
 
 * Create hash for file to be cracked: zip2john secret_files.zip > hash.txt
 * Password cracking will be launched against the hash not the ziped file.
 * Run: `john hash.txt` and john the ripper will try to have the hash with it own pw file
 * with own word list `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`