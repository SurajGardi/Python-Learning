# 6. Concurrency: Use asyncio to fetch data from multiple URLs concurrently and process the results.
# requests_fetch.py

import requests


def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} | Status: {response.status_code}")
    return len(response.text)


def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts"
    ]

    results = []

    for url in urls:
        size = fetch_url(url)
        results.append(size)

    print("\nProcessing results:")
    for url, size in zip(urls, results):
        print(f"{url} -> {size} characters")


if __name__ == "__main__":
    main()
