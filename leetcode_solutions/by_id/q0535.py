# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 535
标题: Encode and Decode TinyURL
难度: medium
链接: https://leetcode.cn/problems/encode-and-decode-tinyurl/
题目类型: 设计、哈希表、字符串、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
535. TinyURL 的加密与解密 - TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk 。请你设计一个类来加密与解密 TinyURL 。 加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。 实现 Solution 类： * Solution() 初始化 TinyURL 系统对象。 * String encode(String longUrl) 返回 longUrl 对应的 TinyURL 。 * String decode(String shortUrl) 返回 shortUrl 原本的 URL 。题目数据保证给定的 shortUrl 是由同一个系统对象加密的。 示例： 输入：url = "https://leetcode.com/problems/design-tinyurl" 输出："https://leetcode.com/problems/design-tinyurl" 解释： Solution obj = new Solution(); string tiny = obj.encode(url); // 返回加密后得到的 TinyURL 。 string ans = obj.decode(tiny); // 返回解密后得到的原本的 URL 。 提示： * 1 <= url.length <= 104 * 题目数据保证 url 是一个有效的 URL
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储长 URL 和短 URL 之间的映射关系，并使用一个计数器生成唯一的短 URL。

算法步骤:
1. 初始化一个哈希表用于存储长 URL 和短 URL 之间的映射关系。
2. 使用一个计数器生成唯一的短 URL 标识符。
3. 在 `encode` 方法中，生成一个唯一的短 URL 标识符，并将其与长 URL 存储在哈希表中。
4. 在 `decode` 方法中，通过短 URL 标识符从哈希表中查找并返回对应的长 URL。

关键点:
- 使用哈希表存储长 URL 和短 URL 之间的映射关系，确保快速查找。
- 使用计数器生成唯一的短 URL 标识符，确保每个长 URL 有一个唯一的短 URL。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 生成和查找短 URL 的操作都是常数时间。
空间复杂度: O(n) - 需要存储 n 个长 URL 和短 URL 的映射关系。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict

class Codec:
    def __init__(self):
        self.url_map: Dict[str, str] = {}
        self.counter: int = 0
        self.base_url: str = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        short_id = self._generate_short_id()
        self.url_map[short_id] = longUrl
        return f"{self.base_url}{short_id}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        short_id = shortUrl.split('/')[-1]
        return self.url_map[short_id]

    def _generate_short_id(self) -> str:
        """Generates a unique short ID using the counter."""
        self.counter += 1
        return str(self.counter)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))