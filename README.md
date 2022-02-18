# rotate_IP
Rotate IP address periodically 

Program is tested on Ubuntu 20.04.3 LTS

# install tor browser and modify torrc:
```
sudo add-apt-repository ppa:micahflee/ppa
sudo apt install torbrowser-launcher
```

- edit torrc file in your `/etc/tor/` directory:
- make port 9051 available
- create a password with `tor --hash-password <password>` and replace the HashedPassword with the new password
- replace `welcome` with your password in the following line of `change_IP.py`:
```
controller.authenticate(password="welcome")
```

## Run the program
```
chmod +x proxy.sh
./proxy.sh
```