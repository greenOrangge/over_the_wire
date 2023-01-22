# Krypton Level 0 → Level 1

- We have to decode the given **base64** string.
- We can do it [here](https://www.base64decode.org/)
- Now let's ssh into `krypton.labs.overthewire.org` using the decoded string
- `ssh krypton1@krypton.labs.overthewire.org -p 2231`
***

# Krypton Level 1 → Level 2

- After we ssh into krypton1, the password for level2 is stored in `krypton2` which is encrypted using a **simple rotation**
- 