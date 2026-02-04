```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000330
标题: 键值映射
难度: medium
链接: https://leetcode.cn/problems/z1R5dt/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 066. 键值映射 - 实现一个 MapSum 类，支持两个方法，insert 和 sum： * MapSum() 初始化 MapSum 对象 * void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。 * int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。 示例： 输入： inputs = ["MapSum", "insert", "sum", "insert", "sum"] inputs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]] 输出： [null, null, 3, null, 5] 解释： MapSum mapSum = new MapSum(); mapSum.insert("apple", 3); mapSum.sum("ap"); // return 3 (apple = 3) mapSum.insert("app", 2); mapSum.sum("ap"); // return 5 (apple + app = 3 + 2 = 5) 提示： * 1 <= key.length, prefix.length <= 50 * key 和 prefix 仅由小写英文字母组成 * 1 <= val <= 1000 * 最多调用 50 次 insert 和 sum 注意：本题与主站 677 题相同： https://leetcode.cn/problems/map-sum-pairs/ [https://leetcode.cn/problems/map-sum-pairs/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储键值对，并在每个节点上维护一个值，以便快速计算前缀和。

算法步骤:
1. 初始化 Trie 树。
2. 在插入时，遍历键的每个字符，更新 Trie 节点的值。
3. 在求和时，遍历前缀的每个字符，找到对应的 Trie 节点，然后递归计算该节点下所有子节点的值之和。

关键点:
- 使用 Trie 树来高效存储和查找前缀。
- 在每个 Trie 节点上维护一个值，以便快速计算前缀和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L)，其中 L 是键或前缀的长度。
空间复杂度: O(N * L)，其中 N 是插入的键的数量，L 是键的平均长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.value: int = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        return self._sum_subtree(node)

    def _sum_subtree(self, node: TrieNode) -> int:
        total = node.value
        for child in node.children.values():
            total += self._sum_subtree(child)
        return total


# 示例测试
if __name__ == "__main__":
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    print(map_sum.sum("ap"))  # 输出 3
    map_sum.insert("app", 2)
    print(map_sum.sum("ap"))  # 输出 5
```

这个实现使用了字典树（Trie）来存储键值对，并在每个节点上维护一个值，以便快速计算前缀和。时间复杂度为 O(L)，空间复杂度为 O(N * L)。