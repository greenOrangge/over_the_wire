# Level 4 → Level 5

> login : `ssh bandit4@bandit.labs.overthewire.org -p 2220`

**the password is stored in a human-readable file in the `inhere` directory**

- let's `cd inhere` into the directory and see the contents of the directory using the `ls` command
- to find the _human readable_ file, we can use the command `file` this is used to determine the file type (please use the man pages `man file`, or google to learn more about it.)
- now executing `man ./-file00` `man ./-file01` is very time consuming, so
- let's do `file ./-file*` , this command returns the file types of all the files in the directory starting with `-file`
and ending with sequence of strings (we use `*` )
	![lvl_4](images/lvl_4.png)
- -file07, returned ASCII, i.e human readable text,
- now we can use `cat ./-file07` to get the password!

***
# Level 5 → Level 6

**The password is stored in a file under the `inhere` directory which is:** 
	- human-readable
	- 1033 bytes in size
	- not executable

- let's cd into the `inhere` directory, and list and contents. We find many directories and searching through each directory manually will be cumbersome and not the best way.
- so let's use the `find` command.
- let's try `find -size 1033c ! -executable`
	- here `-size` specifies the size to find, where `c` is used for bytes
	- `-executable` is used to find for files which are executable so we add a `!` → `! -executable` to tell, not executable
	- do read the man pages `man find` to find out more
	![lvl5](images/lvl5.png)