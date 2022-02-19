import requests
from multiprocessing import Pool


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
}


proxies = {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}

print("Your Public IP:", requests.get("https://ident.me").text)


def send_request(url_list):
    for url in url_list:
        html_content = requests.get(url, proxies=proxies, headers=headers).text
        print(url)
        print(
            "IP rotated to:",
            requests.get("https://ident.me", proxies=proxies, headers=headers).text,
        )

        # your html_content processing code goes here


if __name__ == "__main__":

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
    ] * 5

    send_request(urls)

    # with Pool(processes=10) as pool:
    #     pool.map(send_request, [urls[i : i + 10] for i in range(0, len(urls), 10)])
    #     pool.close()
    #     pool.join()
