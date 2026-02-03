# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 187
标题: Repeated DNA Sequences
难度: medium
链接: https://leetcode.cn/problems/repeated-dna-sequences/
题目类型: 位运算、哈希表、字符串、滑动窗口、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
187. 重复的DNA序列 - DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。 * 例如，"ACGAATTCCG" 是一个 DNA序列 。 在研究 DNA 时，识别 DNA 中的重复序列非常有用。 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。 示例 1： 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" 输出：["AAAAACCCCC","CCCCCAAAAA"] 示例 2： 输入：s = "AAAAAAAAAAAAA" 输出：["AAAAAAAAAA"] 提示： * 0 <= s.length <= 105 * s[i]=='A'、'C'、'G' or 'T'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表，记录所有长度为10的子串出现次数

算法步骤:
1. 使用滑动窗口遍历字符串，提取所有长度为10的子串
2. 使用哈希表记录每个子串出现的次数
3. 返回出现次数大于1的子串

关键点:
- 使用滑动窗口和哈希表
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历字符串一次
空间复杂度: O(n) - 哈希表存储子串
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict
from leetcode_solutions.utils.solution import create_solution


def repeated_dna_sequences(s: str) -> List[str]:
    """
    函数式接口 - 重复的DNA序列
    
    实现思路:
    使用滑动窗口和哈希表，记录所有长度为10的子串出现次数。
    
    Args:
        s: DNA序列字符串
        
    Returns:
        所有出现不止一次的长度为10的序列列表
        
    Example:
        >>> repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
        ['AAAAACCCCC', 'CCCCCAAAAA']
    """
    if len(s) < 10:
        return []
    
    seen = defaultdict(int)
    result = []
    
    for i in range(len(s) - 9):
        substr = s[i:i+10]
        seen[substr] += 1
        if seen[substr] == 2:
            result.append(substr)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(repeated_dna_sequences)
