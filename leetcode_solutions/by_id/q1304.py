# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1304
标题: Longest Happy String
难度: medium
链接: https://leetcode.cn/problems/longest-happy-string/
题目类型: 贪心、字符串、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1405. 最长快乐字符串 - 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s： * s 是一个尽可能长的快乐字符串。 * s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。 * s 中只含有 'a'、'b' 、'c' 三种字母。 如果不存在这样的字符串 s ，请返回一个空字符串 ""。 示例 1： 输入：a = 1, b = 1, c = 7 输出："ccaccbcc" 解释："ccbccacc" 也是一种正确答案。 示例 2： 输入：a = 2, b = 2, c = 1 输出："aabbc" 示例 3： 输入：a = 7, b = 1, c = 0 输出："aabaa" 解释：这是该测试用例的唯一正确答案。 提示： * 0 <= a, b, c <= 100 * a + b + c > 0
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和最大堆来构建最长的快乐字符串。

算法步骤:
1. 使用最大堆存储字符及其剩余数量。
2. 每次从堆中取出剩余数量最多的字符，如果可以添加到结果字符串中，则添加。
3. 如果不能添加（因为会形成三个连续相同的字符），则尝试取出下一个最多的字符。
4. 更新堆中的字符数量，并继续上述过程，直到堆为空或无法再添加字符。

关键点:
- 使用最大堆来确保每次选择剩余数量最多的字符。
- 确保不会形成三个连续相同的字符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k)，其中 n 是 a + b + c 的总和，k 是字符种类数（固定为 3）。
空间复杂度: O(k)，堆的空间复杂度是 O(k)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def longest_happy_string(a: int, b: int, c: int) -> str:
    """
    函数式接口 - 返回一个尽可能长的快乐字符串
    """
    # 最大堆存储字符及其剩余数量
    max_heap = []
    for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
        if count != 0:
            heapq.heappush(max_heap, (count, char))
    
    result = []
    
    while max_heap:
        count, char = heapq.heappop(max_heap)
        if len(result) >= 2 and result[-1] == char and result[-2] == char:
            if not max_heap:
                break
            count_next, char_next = heapq.heappop(max_heap)
            result.append(char_next)
            count_next += 1
            if count_next < 0:
                heapq.heappush(max_heap, (count_next, char_next))
        else:
            result.append(char)
            count += 1
            if count < 0:
                heapq.heappush(max_heap, (count, char))
    
    return ''.join(result)

Solution = create_solution(longest_happy_string)