from stem import Signal
from stem.control import Controller
import requests


def get_tor_session():
    # initialize a requests Session
    session = requests.Session()
    # this requires a running Tor service in your machine and listening on port 9050 (by default)
    session.proxies = {
        "http": "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050",
    }
    return session


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        # welcome password should be generated in the machine,
        # read the README file to know how to create it
        controller.authenticate(password="welcome")
        controller.signal(Signal.NEWNYM)
