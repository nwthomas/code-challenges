"""
Build a web crawler starting from a given URL. Find all URLs reachable from the start that belong to the same hostname.

Requirements:
• Use the urls dictionary to get links from a page (simulates Htm|Parser.getUrls)
• Avoid visiting the same URL twice

Example:
• Input: startUrl = "http://news.yahoo.com", urls contains yahoo.com links
• Output: All yahoo.com URLs (excluding google.com, etc.)

Related: Web Crawler - Concurrent Version - harder variant using threading/asyncio

Example 1
SAMPLE INPUT
startUrl="http://a.com/", urls={"http://a.com/": ["http://a.com/page1", "http://b.com/"]}

SAMPLE OUTPUT
["http://a.com/", "http://a.com/page1"]
"""

from tracemalloc import start
from urllib.parse import urlparse
from queue import Queue
import threading
import asyncio
from collections import deque

MAX_DEPTH = 3
MAX_WORKER_COUNT = 10


async def get_urls(current_url: str, urls: dict[str, list[str]]) -> list[str]:
    return urls[current_url] if current_url in urls else []


async def crawl_website_asyncio(
    start_url: str, urls: dict[str, list[str]]
) -> list[str]:
    hostname = urlparse(start_url).hostname
    visited = {start_url}
    queue = [(start_url, 1)]

    while queue:
        url, depth = queue.pop(0)
        current_urls = await get_urls(url, urls)

        for current_url in current_urls:
            current_hostname = urlparse(current_url).hostname

            if current_hostname == hostname and not current_url in visited:
                visited.add(current_url)
                next_depth = depth + 1

                if next_depth <= MAX_DEPTH:
                    queue.append((current_url, next_depth))

    print(visited)
    return list(visited)


def crawl_website_threading(start_url: str, urls: dict[str, list[str]]) -> list[str]:
    hostname = urlparse(start_url).hostname

    visited = {start_url}
    visited_lock = threading.Lock()

    queue = Queue[(str, int)]()
    queue.put((start_url, 1))

    def worker():
        nonlocal hostname

        while True:
            url, depth = queue.get()

            if url in urls:
                current_urls = urls[url]

                for current_url in current_urls:
                    current_hostname = urlparse(current_url).hostname

                    with visited_lock:
                        if current_hostname == hostname and current_url not in visited:
                            visited.add(current_url)

                            next_depth = depth + 1

                            if next_depth <= MAX_DEPTH:
                                print(current_url, next_depth)
                                queue.put((current_url, next_depth))

            queue.task_done()

    for _ in range(MAX_WORKER_COUNT):
        threading.Thread(target=worker, daemon=True).start()

    queue.join()

    return list(visited)
