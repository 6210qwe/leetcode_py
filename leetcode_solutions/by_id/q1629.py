# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1629
标题: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
难度: hard
链接: https://leetcode.cn/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
题目类型: 贪心、树状数组、线段树、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1505. 最多 K 次交换相邻数位后得到的最小整数 - 给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。 你可以交换这个整数相邻数位的数字 最多 k 次。 请你返回你能得到的最小整数，并以字符串形式返回。 示例 1： [https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg] 输入：num = "4321", k = 4 输出："1342" 解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。 示例 2： 输入：num = "100", k = 1 输出："010" 解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。 示例 3： 输入：num = "36789", k = 1000 输出："36789" 解释：不需要做任何交换。 示例 4： 输入：num = "22", k = 22 输出："22" 示例 5： 输入：num = "9438957234785635408", k = 23 输出："0345989723478563548" 提示： * 1 <= num.length <= 30000 * num 只包含 数字 且不含有 前导 0 。 * 1 <= k <= 10^9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和树状数组来找到每次最优的交换位置。

算法步骤:
1. 初始化一个树状数组，用于快速查询和更新。
2. 遍历字符串，对于每个字符，尝试找到在当前范围内最小的字符，并计算将其移到当前位置所需的交换次数。
3. 如果交换次数小于等于 k，则进行交换并更新 k 和树状数组。
4. 重复上述步骤直到遍历完所有字符或 k 用完。

关键点:
- 使用树状数组来高效地查询和更新字符的位置。
- 贪心地选择每次最优的交换位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。树状数组的操作是 O(log n)。
空间复杂度: O(n)，需要存储树状数组和字符的位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_min_digit(num: str, start: int, end: int, bit: List[int]) -> int:
    """
    使用树状数组找到从 start 到 end 范围内的最小数字。
    """
    min_digit = '9'
    for i in range(start, end + 1):
        if num[i] < min_digit:
            min_digit = num[i]
    return min_digit

def update_bit(bit: List[int], index: int, value: int) -> None:
    """
    更新树状数组。
    """
    while index < len(bit):
        bit[index] += value
        index += index & -index

def query_bit(bit: List[int], index: int) -> int:
    """
    查询树状数组。
    """
    result = 0
    while index > 0:
        result += bit[index]
        index -= index & -index
    return result

def solution_function_name(num: str, k: int) -> str:
    """
    函数式接口 - 实现最优解法
    """
    n = len(num)
    bit = [0] * (n + 1)
    pos = {d: [] for d in '0123456789'}
    
    for i, d in enumerate(num):
        pos[d].append(i + 1)
        update_bit(bit, i + 1, 1)
    
    result = []
    for _ in range(n):
        for d in '0123456789':
            if not pos[d]:
                continue
            idx = pos[d][0]
            swaps = query_bit(bit, idx - 1)
            if k >= swaps:
                k -= swaps
                result.append(d)
                pos[d].pop(0)
                update_bit(bit, idx, -1)
                break
    
    return ''.join(result)

Solution = create_solution(solution_function_name)