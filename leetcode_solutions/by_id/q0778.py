# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 778
标题: Reorganize String
难度: medium
链接: https://leetcode.cn/problems/reorganize-string/
题目类型: 贪心、哈希表、字符串、计数、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
767. 重构字符串 - 给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。 返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。 示例 1: 输入: s = "aab" 输出: "aba" 示例 2: 输入: s = "aaab" 输出: "" 提示: * 1 <= s.length <= 500 * s 只包含小写字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最大堆来存储字符及其频率，每次从堆中取出频率最高的两个字符进行拼接，确保相邻字符不同。

算法步骤:
1. 统计每个字符的频率。
2. 将字符及其频率存入最大堆。
3. 每次从堆中取出频率最高的两个字符，拼接到结果字符串中，并将它们的频率减一后重新放入堆中。
4. 如果堆中只剩下一个字符且其频率大于1，则无法重构字符串，返回空字符串。
5. 最终返回重构后的字符串。

关键点:
- 使用最大堆来保证每次取出频率最高的字符。
- 确保每次拼接的两个字符不同。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。构建堆的时间复杂度是 O(n)，每次从堆中取出元素的时间复杂度是 O(log n)。
空间复杂度: O(n)，用于存储字符及其频率的堆。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def reorganize_string(s: str) -> str:
    """
    函数式接口 - 重构字符串
    """
    # 统计每个字符的频率
    char_count = [0] * 26
    for char in s:
        char_count[ord(char) - ord('a')] += 1
    
    # 构建最大堆
    max_heap = []
    for i, count in enumerate(char_count):
        if count > 0:
            heapq.heappush(max_heap, (-count, chr(i + ord('a'))))
    
    result = []
    while len(max_heap) >= 2:
        # 取出频率最高的两个字符
        count1, char1 = heapq.heappop(max_heap)
        count2, char2 = heapq.heappop(max_heap)
        
        # 拼接到结果字符串中
        result.extend([char1, char2])
        
        # 更新频率并重新放入堆中
        if count1 + 1 < 0:
            heapq.heappush(max_heap, (count1 + 1, char1))
        if count2 + 1 < 0:
            heapq.heappush(max_heap, (count2 + 1, char2))
    
    # 如果堆中只剩下一个字符且其频率大于1，则无法重构字符串
    if max_heap:
        count, char = heapq.heappop(max_heap)
        if count < -1:
            return ""
        result.append(char)
    
    return ''.join(result)

Solution = create_solution(reorganize_string)