# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 451
标题: Sort Characters By Frequency
难度: medium
链接: https://leetcode.cn/problems/sort-characters-by-frequency/
题目类型: 哈希表、字符串、桶排序、计数、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
451. 根据字符出现频率排序 - 给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。 返回 已排序的字符串 。如果有多个答案，返回其中任何一个。 示例 1: 输入: s = "tree" 输出: "eert" 解释: 'e'出现两次，'r'和't'都只出现一次。 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。 示例 2: 输入: s = "cccaaa" 输出: "cccaaa" 解释: 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。 注意"cacaca"是不正确的，因为相同的字母必须放在一起。 示例 3: 输入: s = "Aabb" 输出: "bbAa" 解释: 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。 注意'A'和'a'被认为是两种不同的字符。 提示: * 1 <= s.length <= 5 * 105 * s 由大小写英文字母和数字组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 统计字符频率，按频率降序排序

算法步骤:
1. 使用Counter统计每个字符的出现频率
2. 按频率降序排序字符
3. 按排序后的顺序，每个字符重复其频率次数

关键点:
- 使用桶排序或直接排序
- 时间复杂度O(n + k log k)，k为不同字符数
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + k log k) - n为字符串长度，k为不同字符数
空间复杂度: O(n) - 存储结果字符串
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sort_characters_by_frequency(s: str) -> str:
    """
    函数式接口 - 根据字符出现频率排序
    
    实现思路:
    统计字符频率，按频率降序排序后重新构建字符串。
    
    Args:
        s: 输入字符串
        
    Returns:
        按频率降序排序的字符串
        
    Example:
        >>> sort_characters_by_frequency("tree")
        'eert'
    """
    # 统计字符频率
    counter = Counter(s)
    
    # 按频率降序排序
    sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    # 构建结果字符串
    result = []
    for char, count in sorted_chars:
        result.append(char * count)
    
    return ''.join(result)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(sort_characters_by_frequency)
