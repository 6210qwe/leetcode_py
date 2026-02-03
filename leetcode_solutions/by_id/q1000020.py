# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000020
标题: Re-Space LCCI
难度: medium
链接: https://leetcode.cn/problems/re-space-lcci/
题目类型: 字典树、数组、哈希表、字符串、动态规划、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.13. 恢复空格 - 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。 注意：本题相对原题稍作改动，只需返回未识别的字符数 示例： 输入： dictionary = ["looked","just","like","her","brother"] sentence = "jesslookedjustliketimherbrother" 输出： 7 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。 提示： * 0 <= len(sentence) <= 1000 * dictionary中总字符数不超过 150000。 * 你可以认为dictionary和sentence中只包含小写字母。
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
