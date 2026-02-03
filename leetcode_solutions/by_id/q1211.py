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
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
