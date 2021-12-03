# Level 8 → Level 9

URL : http://natas9.natas.labs.overthewire.org/

- Again we have something that accepts input from the user
- this takes the input and searches it
- let's try searching for something random, it returns nothing
- okay so let's see the source code, we can see php code
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```
- what this does is check if we have given input to the element `needle`
- then it executes `grep -i $key dictionary.txt`,
	- read more about grep by typing this `man grep` in the terminal, it basically searches for a word in a file
- important thing here is, it is done by a function called `passthru`, ([read more](https://www.php.net/manual/en/function.passthru.php)){target="_blank"} , here, this just executes a command without checking.
- let's use this to our advantage and try searching `; cat /etc/natas_webpass/natas10`
	- `;` semicolon is used to denote the end of the previous command ([read more](https://stackoverflow.com/a/20233998))
	- and `cat` is used to output a file, here the file containing the password
- this gives us the command for the next level!!