# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2113
标题: Find the Kth Largest Integer in the Array
难度: medium
链接: https://leetcode.cn/problems/find-the-kth-largest-integer-in-the-array/
题目类型: 数组、字符串、分治、快速选择、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1985. 找出数组中的第 K 大整数 - 给你一个字符串数组 nums 和一个整数 k 。nums 中的每个字符串都表示一个不含前导零的整数。 返回 nums 中表示第 k 大整数的字符串。 注意：重复的数字在统计时会视为不同元素考虑。例如，如果 nums 是 ["1","2","2"]，那么 "2" 是最大的整数，"2" 是第二大的整数，"1" 是第三大的整数。 示例 1： 输入：nums = ["3","6","7","10"], k = 4 输出："3" 解释： nums 中的数字按非递减顺序排列为 ["3","6","7","10"] 其中第 4 大整数是 "3" 示例 2： 输入：nums = ["2","21","12","1"], k = 3 输出："2" 解释： nums 中的数字按非递减顺序排列为 ["1","2","12","21"] 其中第 3 大整数是 "2" 示例 3： 输入：nums = ["0","0"], k = 2 输出："0" 解释： nums 中的数字按非递减顺序排列为 ["0","0"] 其中第 2 大整数是 "0" 提示： * 1 <= k <= nums.length <= 104 * 1 <= nums[i].length <= 100 * nums[i] 仅由数字组成 * nums[i] 不含任何前导零
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用快速选择算法找到第 k 大的整数。

算法步骤:
1. 将字符串数组转换为整数数组。
2. 使用快速选择算法找到第 k 大的整数。
3. 将找到的整数转换回字符串并返回。

关键点:
- 快速选择算法的时间复杂度平均为 O(n)，最坏情况下为 O(n^2)。
- 通过随机化选择枢轴可以避免最坏情况的发生。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) 平均情况，O(n^2) 最坏情况
空间复杂度: O(1) 除了输入和输出外，不需要额外的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import random

def solution_function_name(nums: List[str], k: int) -> str:
    """
    函数式接口 - 找到数组中的第 k 大整数
    """
    # 将字符串数组转换为整数数组
    nums_int = [int(num) for num in nums]

    def quick_select(arr, left, right, k):
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(arr, left, right, pivot_index)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quick_select(arr, left, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, right, k)

    def partition(arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] > pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    # 使用快速选择算法找到第 k 大的整数
    kth_largest = quick_select(nums_int, 0, len(nums_int) - 1, k - 1)
    
    # 将找到的整数转换回字符串并返回
    return str(kth_largest)

Solution = create_solution(solution_function_name)