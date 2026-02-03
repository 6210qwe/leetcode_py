# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 677
标题: Map Sum Pairs
难度: medium
链接: https://leetcode.cn/problems/map-sum-pairs/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
677. 键值映射 - 设计一个 map ，满足以下几点: * 字符串表示键，整数表示值 * 返回具有前缀等于给定字符串的键的值的总和 实现一个 MapSum 类： * MapSum() 初始化 MapSum 对象 * void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对 key-value 将被替代成新的键值对。 * int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。 示例 1： 输入： ["MapSum", "insert", "sum", "insert", "sum"] [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]] 输出： [null, null, 3, null, 5] 解释： MapSum mapSum = new MapSum(); mapSum.insert("apple", 3); mapSum.sum("ap"); // 返回 3 (apple = 3) mapSum.insert("app", 2); mapSum.sum("ap"); // 返回 5 (apple + app = 3 + 2 = 5) 提示： * 1 <= key.length, prefix.length <= 50 * key 和 prefix 仅由小写英文字母组成 * 1 <= val <= 1000 * 最多调用 50 次 insert 和 sum
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 设计数据结构存储 key->val，前缀求和时遍历所有 key

算法步骤:
1. 使用一个字典 map 存储所有插入的键值对 key -> val
2. insert(key, val):
   - 直接在 map 中更新 key 对应的值为 val
3. sum(prefix):
   - 遍历 map 中的所有 key，若 key 以 prefix 开头，则将其对应的 val 累加
   - 返回累加结果

关键点:
- 题目规模较小（最多 50 次 insert/sum），可以接受每次 sum 时 O(N * L) 的遍历
- 若需要更高效的方案，可用字典树 + 前缀和，这里用更简单的实现即可通过
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度:
- insert: O(1) 平均
- sum: O(N * L) - N 为当前键的数量，L 为键平均长度
空间复杂度: O(N * L) - 存储所有键值对
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode


class MapSum:
    """
    键值映射，实现 insert 和前缀和查询
    """

    def __init__(self):
        self.map: dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                total += v
        return total


# 注意：本题在 LeetCode 上直接使用 MapSum 类，不通过 create_solution
