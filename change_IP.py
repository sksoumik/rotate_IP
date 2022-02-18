import time
from stem import Signal
from stem.control import Controller


def main():
    while True:
        # time.sleep(10)
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="welcome")
            controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    main()
