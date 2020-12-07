# basics

![Buffer Overflow](img/x86Memory.png)

## Stack
* When a tread is running it execute code form the progam image or the DDLs.
* The thread requieres shor term data areas for functions, variable, program control information => stack.
* Each threat has its own stack
* LIFO (push/pop)

## Function return mechanics
When code wihting a thread calls a function is must know on which address to return to once the function is completed

Example of return mechanics (stored in a section of stack called stack frame):
| Thread stack frame example|
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


