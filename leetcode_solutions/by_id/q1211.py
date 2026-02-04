# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1211
标题: Iterator for Combination
难度: medium
链接: https://leetcode.cn/problems/iterator-for-combination/
题目类型: 设计、字符串、回溯、迭代器
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1286. 字母组合迭代器 - 请你设计一个迭代器类 CombinationIterator ，包括以下内容： * CombinationIterator(string characters, int combinationLength) 一个构造函数，输入参数包括：用一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。 * 函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。 * 函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 true 示例 1： 输入: ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"] [["abc", 2], [], [], [], [], [], []] 输出： [null, "ab", true, "ac", true, "bc", false] 解释： CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator iterator.next(); // 返回 "ab" iterator.hasNext(); // 返回 true iterator.next(); // 返回 "ac" iterator.hasNext(); // 返回 true iterator.next(); // 返回 "bc" iterator.hasNext(); // 返回 false 提示： * 1 <= combinationLength <= characters.length <= 15 * characters 中每个字符都 不同 * 每组测试数据最多对 next 和 hasNext 调用 104次 * 题目保证每次调用函数 next 时都存在下一个字母组合。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的组合，并存储在一个列表中。然后使用迭代器来遍历这些组合。

算法步骤:
1. 在构造函数中，使用回溯法生成所有长度为 combinationLength 的组合，并将它们存储在一个列表中。
2. 初始化一个索引来跟踪当前访问到的组合。
3. 在 next() 方法中，返回当前索引指向的组合，并将索引加一。
4. 在 hasNext() 方法中，检查当前索引是否已经超出组合列表的范围。

关键点:
- 使用回溯法生成所有可能的组合。
- 使用列表存储组合，以便快速访问。
- 使用索引来跟踪当前访问到的组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(C(n, k))，其中 n 是 characters 的长度，k 是 combinationLength。生成所有组合的时间复杂度是组合数 C(n, k)。
空间复杂度: O(C(n, k))，存储所有组合的空间复杂度是组合数 C(n, k)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.index = 0
        self._generate_combinations(characters, combinationLength, 0, "")

    def _generate_combinations(self, characters: str, length: int, start: int, current: str):
        if len(current) == length:
            self.combinations.append(current)
            return
        for i in range(start, len(characters)):
            self._generate_combinations(characters, length, i + 1, current + characters[i])

    def next(self) -> str:
        result = self.combinations[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)


Solution = create_solution(CombinationIterator)