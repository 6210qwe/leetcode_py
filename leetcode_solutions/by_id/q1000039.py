# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000039
标题: Find Closest LCCI
难度: medium
链接: https://leetcode.cn/problems/find-closest-lcci/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.11. 单词距离 - 有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗? 示例： 输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student" 输出：1 提示： * words.length <= 100000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历数组，记录每个单词的位置，并在遍历过程中更新最小距离。

算法步骤:
1. 初始化两个指针 idx1 和 idx2 分别记录 word1 和 word2 的位置。
2. 初始化最小距离 min_distance 为无穷大。
3. 遍历 words 数组：
   - 如果当前单词是 word1，更新 idx1 并计算与 idx2 的距离，更新 min_distance。
   - 如果当前单词是 word2，更新 idx2 并计算与 idx1 的距离，更新 min_distance。
4. 返回 min_distance。

关键点:
- 通过一次遍历即可找到最短距离，避免了多次遍历。
- 使用两个指针分别记录 word1 和 word2 的位置，实时更新最小距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 words 的长度，因为只需要一次遍历。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_closest(words: List[str], word1: str, word2: str) -> int:
    """
    函数式接口 - 找到两个单词在数组中的最短距离
    """
    idx1, idx2 = -1, -1
    min_distance = float('inf')
    
    for i, word in enumerate(words):
        if word == word1:
            idx1 = i
            if idx2 != -1:
                min_distance = min(min_distance, abs(idx1 - idx2))
        elif word == word2:
            idx2 = i
            if idx1 != -1:
                min_distance = min(min_distance, abs(idx1 - idx2))
    
    return min_distance


Solution = create_solution(find_closest)