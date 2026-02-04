# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 423
标题: Reconstruct Original Digits from English
难度: medium
链接: https://leetcode.cn/problems/reconstruct-original-digits-from-english/
题目类型: 哈希表、数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
423. 从英文中重建数字 - 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。 示例 1： 输入：s = "owoztneoer" 输出："012" 示例 2： 输入：s = "fviefuro" 输出："45" 提示： * 1 <= s.length <= 105 * s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一 * s 保证是一个符合题目要求的字符串
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 利用每个数字在英文单词中的唯一字符来确定每个数字的数量

算法步骤:
1. 统计输入字符串中每个字符的出现次数
2. 根据唯一字符确定每个数字的数量
3. 按升序构建结果字符串

关键点:
- 注意边界条件，确保所有字符都被正确处理
- 优化时间和空间复杂度，避免不必要的重复计算
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历字符串和统计字符出现次数
空间复杂度: O(1) - 使用常数级额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def reconstruct_original_digits_from_english(s: str) -> str:
    """
    函数式接口 - 从英文中重建数字
    
    实现思路:
    利用每个数字在英文单词中的唯一字符来确定每个数字的数量，然后按升序构建结果字符串
    
    Args:
        s: 字符串，包含字母顺序打乱的用英文单词表示的若干数字
        
    Returns:
        按升序返回原始的数字字符串
        
    Example:
        >>> reconstruct_original_digits_from_english("owoztneoer")
        "012"
        >>> reconstruct_original_digits_from_english("fviefuro")
        "45"
    """
    # 统计输入字符串中每个字符的出现次数
    count = [0] * 10
    for c in s:
        if c == 'z': count[0] += 1  # zero
        if c == 'w': count[2] += 1  # two
        if c == 'u': count[4] += 1  # four
        if c == 'x': count[6] += 1  # six
        if c == 'g': count[8] += 1  # eight
        if c == 'o': count[1] += 1  # one
        if c == 'h': count[3] += 1  # three
        if c == 'f': count[5] += 1  # five
        if c == 's': count[7] += 1  # seven
        if c == 'i': count[9] += 1  # nine

    # 调整共享字符的计数
    count[1] -= count[0] + count[2] + count[4]
    count[3] -= count[8]
    count[5] -= count[4]
    count[7] -= count[6]
    count[9] -= count[5] + count[6] + count[8]

    # 构建结果字符串
    result = []
    for i in range(10):
        result.append(str(i) * count[i])
    return ''.join(result)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(reconstruct_original_digits_from_english)