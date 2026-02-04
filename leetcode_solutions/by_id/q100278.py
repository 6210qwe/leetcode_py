# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100278
标题: 库存管理 I
难度: easy
链接: https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 128. 库存管理 I - 仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。原库存表按商品 id 升序排列。现因突发情况需要进行商品紧急调拨，管理员将这批商品 id 提前依次整理至库存表最后。请你找到并返回库存表中编号的 最小的元素 以便及时记录本次调拨。 示例 1： 输入：stock = [4,5,8,3,4] 输出：3 示例 2： 输入：stock = [5,7,9,1,2] 输出：1 提示： * 1 <= stock.length <= 5000 * -5000 <= stock[i] <= 5000 注意：本题与主站 154 题相同：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/ [https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到旋转排序数组中的最小值。

算法步骤:
1. 初始化左右指针 left 和 right 分别指向数组的起始和末尾。
2. 进行二分查找：
   - 计算中间位置 mid。
   - 如果 stock[mid] > stock[right]，说明最小值在 mid 右侧，更新 left = mid + 1。
   - 如果 stock[mid] < stock[right]，说明最小值在 mid 或左侧，更新 right = mid。
   - 如果 stock[mid] == stock[right]，无法确定最小值的位置，right -= 1 缩小范围。
3. 当 left == right 时，left 指向的就是最小值。

关键点:
- 通过二分查找缩小查找范围，减少比较次数。
- 处理重复元素的情况，避免陷入死循环。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 在最好的情况下（没有重复元素），每次可以将搜索范围减半。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(stock: List[int]) -> int:
    """
    函数式接口 - 使用二分查找找到旋转排序数组中的最小值
    """
    if not stock:
        return -1

    left, right = 0, len(stock) - 1

    while left < right:
        mid = (left + right) // 2
        if stock[mid] > stock[right]:
            left = mid + 1
        elif stock[mid] < stock[right]:
            right = mid
        else:
            right -= 1

    return stock[left]


Solution = create_solution(solution_function_name)