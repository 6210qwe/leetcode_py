# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 816
标题: Design HashSet
难度: easy
链接: https://leetcode.cn/problems/design-hashset/
题目类型: 设计、数组、哈希表、链表、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
705. 设计哈希集合 - 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。 实现 MyHashSet 类： * void add(key) 向哈希集合中插入值 key 。 * bool contains(key) 返回哈希集合中是否存在这个值 key 。 * void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。 示例： 输入： ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"] [[], [1], [2], [1], [3], [2], [2], [2], [2]] 输出： [null, null, null, true, false, null, true, null, false] 解释： MyHashSet myHashSet = new MyHashSet(); myHashSet.add(1); // set = [1] myHashSet.add(2); // set = [1, 2] myHashSet.contains(1); // 返回 True myHashSet.contains(3); // 返回 False ，（未找到） myHashSet.add(2); // set = [1, 2] myHashSet.contains(2); // 返回 True myHashSet.remove(2); // set = [1] myHashSet.contains(2); // 返回 False ，（已移除） 提示： * 0 <= key <= 106 * 最多调用 104 次 add、remove 和 contains
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用开放寻址法实现哈希集合。

算法步骤:
1. 初始化一个大小为 1000001 的布尔数组，所有元素初始化为 False。
2. 对于 add 操作，将对应位置的布尔值设为 True。
3. 对于 remove 操作，将对应位置的布尔值设为 False。
4. 对于 contains 操作，检查对应位置的布尔值是否为 True。

关键点:
- 使用布尔数组来表示哈希集合中的元素。
- 通过索引直接访问和修改布尔数组，实现 O(1) 时间复杂度的操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作（add, remove, contains）的时间复杂度均为 O(1)。
空间复杂度: O(1000001) - 布尔数组的大小固定为 1000001。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class MyHashSet:

    def __init__(self):
        self.size = 1000001
        self.set = [False] * self.size

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key]


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)