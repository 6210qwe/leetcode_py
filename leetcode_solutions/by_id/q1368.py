# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1368
标题: Web Crawler Multithreaded
难度: medium
链接: https://leetcode.cn/problems/web-crawler-multithreaded/
题目类型: 深度优先搜索、广度优先搜索、多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1242. 多线程网页爬虫 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用多线程进行网页爬取，并利用深度优先搜索（DFS）或广度优先搜索（BFS）遍历所有相关页面。

算法步骤:
1. 初始化一个线程池和一个集合来存储已访问的 URL。
2. 从起始 URL 开始，使用 DFS 或 BFS 进行遍历。
3. 对于每个新的 URL，如果它还没有被访问过且满足条件（即与起始 URL 的主机名相同），则将其加入到待处理队列中。
4. 使用线程池并发地获取每个 URL 的内容，并解析出新的 URL。
5. 重复上述过程直到所有相关页面都被访问完毕。

关键点:
- 使用线程池来并发处理多个请求，提高效率。
- 使用集合来存储已访问的 URL，避免重复访问。
- 确保只访问与起始 URL 主机名相同的页面。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(V + E)，其中 V 是节点数（页面数），E 是边数（链接数）。
空间复杂度: O(V)，用于存储已访问的 URL 和待处理的 URL。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse
import requests
from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    full_url = urljoin(self.base_url, value)
                    self.links.append(full_url)


def fetch_page(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except (requests.RequestException, ValueError):
        return ''


def crawl(start_url: str, max_depth: int, max_workers: int) -> List[str]:
    visited = set()
    to_visit = [(start_url, 0)]
    start_host = urlparse(start_url).netloc
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while to_visit:
            futures = []
            for url, depth in to_visit:
                if url not in visited and depth <= max_depth and urlparse(url).netloc == start_host:
                    futures.append(executor.submit(fetch_page, url))
                    visited.add(url)

            to_visit = []
            for future in as_completed(futures):
                page_content = future.result()
                if page_content:
                    extractor = LinkExtractor(url)
                    extractor.feed(page_content)
                    to_visit.extend((link, depth + 1) for link in extractor.links)
                    results.append(url)

    return results


Solution = create_solution(crawl)