# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1271
标题: Web Crawler
难度: medium
链接: https://leetcode.cn/problems/web-crawler/
题目类型: 深度优先搜索、广度优先搜索、字符串、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1271. 网络爬虫 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 或广度优先搜索 (BFS) 来遍历网页，并使用哈希集合来记录已访问的 URL 以避免重复访问。

算法步骤:
1. 初始化一个哈希集合 `visited` 来存储已访问的 URL。
2. 定义一个递归函数 `dfs` 或者迭代函数 `bfs` 来遍历网页。
3. 在 `dfs` 或 `bfs` 函数中，对于每个 URL，检查是否已经访问过。如果未访问过，则调用 `htmlParser.getUrls(url)` 获取所有子 URL，并将当前 URL 标记为已访问。
4. 对于每个子 URL，递归调用 `dfs` 或将其加入队列进行 `bfs`。
5. 返回所有已访问的 URL。

关键点:
- 使用哈希集合来记录已访问的 URL 以避免重复访问。
- 选择 DFS 或 BFS 来遍历网页，根据具体需求选择合适的遍历方式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N + E)，其中 N 是 URL 的数量，E 是 URL 之间的边的数量。
空间复杂度: O(N)，用于存储已访问的 URL 和递归调用栈（或队列）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import collections

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_host(url):
            return url.split('/')[2]

        def dfs(url):
            if url in visited:
                return
            visited.add(url)
            for next_url in htmlParser.getUrls(url):
                if get_host(next_url) == start_host:
                    dfs(next_url)

        # 使用 BFS
        def bfs(startUrl):
            queue = collections.deque([startUrl])
            while queue:
                url = queue.popleft()
                if url in visited:
                    continue
                visited.add(url)
                for next_url in htmlParser.getUrls(url):
                    if get_host(next_url) == start_host:
                        queue.append(next_url)

        start_host = get_host(startUrl)
        visited = set()
        # 选择 DFS 或 BFS
        dfs(startUrl)
        # bfs(startUrl)
        return list(visited)

# 示例 HtmlParser 类
class HtmlParser:
    def getUrls(self, url: str) -> List[str]:
        # 假设这是一个从给定 URL 获取所有子 URL 的方法
        pass

# 创建解决方案实例
Solution = create_solution(Solution)