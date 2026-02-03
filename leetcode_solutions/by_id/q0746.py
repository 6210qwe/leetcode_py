# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 746
标题: Prefix and Suffix Search
难度: hard
链接: https://leetcode.cn/problems/prefix-and-suffix-search/
题目类型: 设计、字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
745. 前缀和后缀搜索 - 设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。 实现 WordFilter 类： * WordFilter(string[] words) 使用词典中的单词 words 初始化对象。 * f(string pref, string suff) 返回词典中具有前缀 pref 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。 示例： 输入 ["WordFilter", "f"] [[["apple"]], ["a", "e"]] 输出 [null, 0] 解释 WordFilter wordFilter = new WordFilter(["apple"]); wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suffix = "e" 。 提示： * 1 <= words.length <= 104 * 1 <= words[i].length <= 7 * 1 <= pref.length, suff.length <= 7 * words[i]、pref 和 suff 仅由小写英文字母组成 * 最多对函数 f 执行 104 次调用
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
