# rotate_IP
Rotate IP address periodically and send requests with changed IP addresses. 

Program is tested on Ubuntu 20.04.3 LTS.

### install tor browser and modify torrc:
```
sudo add-apt-repository ppa:micahflee/ppa
sudo apt install torbrowser-launcher
```
Now, you should have a torrc file in your `/etc/tor/` directory. 
- edit torrc file in your `/etc/tor/` directory:
open the torrc file `$ nano torrc` and uncomment the following lines (usually these are commented out):
```
ControlPort 9051
HashedControlPassword 16:2D99FRCE35858C6F608DB3122A6C8DA4C35BE5E105B9B54A7E438B122F
CookieAuthentication 1
```
- create a password with `tor --hash-password <password>` 
For example, `tor --hash-password mypass`
This will generate a new `HashedControlPassword`, replace the `torrc` HashedControlPassword with your newly generated password. 
and remmber which password you passed with `tor --hash-password <password>` command. You will use the `<password>` in your python
code. 

- replace `welcome` with your `<password>` in the following line of `change_IP.py` in line 10:
```
controller.authenticate(password="welcome")
```

- Now restart the tor service:
```
sudo service tor restart
```

### Install required packages:
```
pip install stem
pip install requests
```

### Run the program
```
chmod +x proxy.sh
./proxy.sh
```
This will send the `change_IP.py` in the background and will keep running with your `send_request.py` program.


##### This program might not work on windows but you can try, but with replacing the `pwd` to `cd` in the `proxy.sh` file. 