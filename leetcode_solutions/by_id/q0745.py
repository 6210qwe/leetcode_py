# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 745
标题: Find Smallest Letter Greater Than Target
难度: easy
链接: https://leetcode.cn/problems/find-smallest-letter-greater-than-target/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
744. 寻找比目标字母大的最小字母 - 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。 示例 1： 输入: letters = ['c', 'f', 'j']，target = 'a' 输出: 'c' 解释：letters 中字典上比 'a' 大的最小字符是 'c'。 示例 2: 输入: letters = ['c','f','j'], target = 'c' 输出: 'f' 解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。 示例 3: 输入: letters = ['x','x','y','y'], target = 'z' 输出: 'x' 解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。 提示： * 2 <= letters.length <= 104 * letters[i] 是一个小写字母 * letters 按非递减顺序排序 * letters 最少包含两个不同的字母 * target 是一个小写字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到大于目标字母的最小字母。

算法步骤:
1. 初始化左右指针 left 和 right，分别指向数组的起始和末尾。
2. 进行二分查找：
   - 计算中间位置 mid。
   - 如果 letters[mid] 大于 target，则将 right 移动到 mid - 1。
   - 否则，将 left 移动到 mid + 1。
3. 最终返回 letters[left % len(letters)]，处理循环数组的情况。

关键点:
- 二分查找的时间复杂度为 O(log n)。
- 使用模运算处理循环数组的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)，其中 n 是 letters 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(letters: List[str], target: str) -> str:
    """
    函数式接口 - 实现最优解法
    """
    left, right = 0, len(letters) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return letters[left % len(letters)]


Solution = create_solution(solution_function_name)