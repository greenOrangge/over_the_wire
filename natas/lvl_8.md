# Level 7 → Level 8

URL : http://natas8.natas.labs.overthewire.org/

- here we find a box, where we can input some data (numbers, alphabets, symbols)
- let's try what it does by giving a random input say "passwd", it says `Wrong secret`
- now let's view the source code
- Oops, we can see the steps or ways in which our input is modified to match the correct secret
- the function does
	- `bin2hex` : converts binary to hex
	- `strrev` : reverses the string
	- `base64_encode` : encodes the string in base 64
	- and then compares it with the variable `secret`
	- if you don't know what these are, please google them
- now all we have to do is reverse these steps (you can try [this](https://www.w3schools.com/php/phptryit.asp?filename=tryphp_compiler) compiler)
```html+php
<!DOCTYPE html>
<html>
<body>

<?php
$secret = "3d3d516343746d4d6d6c315669563362";
# given function
# echo bin2hex(strrev(base64_encode($secret)));

# reversing the function to get the secret
echo base64_decode(strrev(hex2bin($secret)));
?>

</body>
</html>
```
- after reverseing we get the secret `oubWYf2kBq`, once we submit this, we get the password for the next level!!