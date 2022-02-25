# Rotate IP address
Rotate IP address and send each requests with a different IP address using Python3

### Install tor browser and modify torrc:
```bash
sudo add-apt-repository ppa:micahflee/ppa
sudo apt install torbrowser-launcher
```
Now, you should have a torrc file in your `/etc/tor/` directory. 

##### Edit `torrc` file in your `/etc/tor/` directory

open the torrc file `$ nano torrc` and uncomment the following lines (usually these are commented out):

```bash
ControlPort 9051
HashedControlPassword 16:2D99FRCE35858C6F608DB3122A6C8DA4C35BE5E105B9B54A7E438B122F
CookieAuthentication 1
```
##### Create a new HashedControlPassword password 

```bash
tor --hash-password <password> 
```

For example, `tor --hash-password mypass`
This will generate a new `HashedControlPassword`, replace the torrc's  `HashedControlPassword` with your newly generated password. 
and remember which password you passed with `tor --hash-password <password>` command. You will use the `<password>` in your python
code. 

Now, replace `welcome` with your `<password>` in the following line of `change_IP.py` in line 21:

```bash
controller.authenticate(password="welcome")
```

##### Restart the tor service

```bash
sudo service tor restart
```

### Install required packages:
```bash
pip install stem
pip install requests
```

### Run the program
```bash
python3 send_request.py
```
---
*Program is tested on Ubuntu 20.04.3 LTS.*
