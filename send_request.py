import requests
from multiprocessing import Pool
from stem import Signal
from stem.control import Controller
from change_IP import renew_connection, get_tor_session

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
}


def send_request(url_list):
    for url in url_list:
        try:
            renew_connection()
            session = get_tor_session()
            html_content = session.get(url, headers=headers).text
            print(url)
            print(
                "IP rotated to:",
                session.get("https://ident.me", headers=headers).text,
            )
            # your html parsing code goes here
            # html_content ....
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    # IP address before IP rotation
    print("Your Public IP:", requests.get("https://ident.me").text)

    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.amazon.com",
        "https://www.reddit.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.wikipedia.org",
        "https://www.twitter.com",
    ] * 10

    # send_request(urls)

    # send requests in parallel using multiprocessing
    with Pool(processes=20) as pool:
        pool.map(send_request, [urls[i : i + 10] for i in range(0, len(urls), 10)])
        pool.close()
        pool.join()
