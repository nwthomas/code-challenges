from web_crawler import crawl_website_threading
from web_crawler import crawl_website_asyncio

import pytest

### THREADED VERSION ###


def test_crawls_website_with_same_hostname_threading():
    urls = {
        "http://a.com/": [
            "http://a.com/page1",
            "http://b.com/",
            "http://a.com/page2",
            "http://a.com/another-link",
        ],
        "http://b.com/": ["http://b.com/page2", "http://c.com/"],
        "http://c.com/": ["http://c.com/page3", "http://d.com/"],
        "http://d.com/": ["http://d.com/page4", "http://e.com/"],
        "http://e.com/": ["http://e.com/page5", "http://f.com/"],
        "http://a.com/another-link": ["http://test.com"],
    }
    result = crawl_website_threading("http://a.com/", urls)
    assert sorted(result) == sorted(
        [
            "http://a.com/page1",
            "http://a.com/",
            "http://a.com/page2",
            "http://a.com/another-link",
        ]
    )


def test_crawls_max_depth_3_with_same_hostname_threading():
    urls = {}
    for i in range(1001):
        urls[f"http://a.com/{i}/"] = [f"http://a.com/{i + 1}/"]

    result = crawl_website_threading("http://a.com/0/", urls)
    assert sorted(result) == sorted([f"http://a.com/{i}/" for i in range(4)])


### ASYNCIO VERSION ###


@pytest.mark.asyncio
async def test_crawls_website_with_same_hostname_asyncio():
    urls = {
        "http://a.com/": [
            "http://a.com/page1",
            "http://b.com/",
            "http://a.com/page2",
            "http://a.com/another-link",
        ],
        "http://b.com/": ["http://b.com/page2", "http://c.com/"],
        "http://c.com/": ["http://c.com/page3", "http://d.com/"],
        "http://d.com/": ["http://d.com/page4", "http://e.com/"],
        "http://e.com/": ["http://e.com/page5", "http://f.com/"],
        "http://a.com/another-link": ["http://test.com"],
    }
    result = await crawl_website_asyncio("http://a.com/", urls)
    assert sorted(result) == sorted(
        [
            "http://a.com/page1",
            "http://a.com/",
            "http://a.com/page2",
            "http://a.com/another-link",
        ]
    )


@pytest.mark.asyncio
async def test_crawls_max_depth_3_with_same_hostname_asyncio():
    urls = {}
    for i in range(1001):
        urls[f"http://a.com/{i}/"] = [f"http://a.com/{i + 1}/"]

    result = await crawl_website_asyncio("http://a.com/0/", urls)
    assert sorted(result) == sorted([f"http://a.com/{i}/" for i in range(4)])
