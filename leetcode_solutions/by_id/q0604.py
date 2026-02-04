```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 604
标题: Design Compressed String Iterator
难度: easy
链接: https://leetcode.cn/problems/design-compressed-string-iterator/
题目类型: 设计、数组、字符串、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
604. 迭代压缩字符串 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储字符及其对应的重复次数，并使用两个指针来跟踪当前字符和剩余的重复次数。

算法步骤:
1. 初始化时解析压缩字符串，将每个字符及其重复次数存储在列表中。
2. 提供 next() 方法返回下一个字符，并更新指针。
3. 提供 hasNext() 方法检查是否还有剩余字符。

关键点:
- 解析压缩字符串时，使用正则表达式来提取字符及其重复次数。
- 使用两个指针分别跟踪当前字符的位置和剩余的重复次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是压缩字符串的长度，初始化时需要遍历整个字符串。
空间复杂度: O(m) - 其中 m 是压缩字符串中不同字符的数量，存储每个字符及其重复次数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import re

class StringIterator:

    def __init__(self, compressedString: str):
        self.tokens = []
        self.index = 0
        self.current_count = 0
        for token in re.findall(r'(\D+)(\d+)', compressedString):
            char, count = token
            self.tokens.append((char, int(count)))

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.current_count == 0:
            self.current_char, self.current_count = self.tokens[self.index]
            self.index += 1
        self.current_count -= 1
        return self.current_char

    def hasNext(self) -> bool:
        return self.index < len(self.tokens) or self.current_count > 0


# 示例用法
if __name__ == "__main__":
    iterator = StringIterator("L1e2t1C1o1d1e1")
    while iterator.hasNext():
        print(iterator.next())
```

这个实现中，`StringIterator` 类解析了压缩字符串，并提供了 `next()` 和 `hasNext()` 方法来迭代字符。时间复杂度为 O(n)，空间复杂度为 O(m)，其中 n 是压缩字符串的长度，m 是压缩字符串中不同字符的数量。