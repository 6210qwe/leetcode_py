# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1645
标题: Find a Value of a Mysterious Function Closest to Target
难度: hard
链接: https://leetcode.cn/problems/find-a-value-of-a-mysterious-function-closest-to-target/
题目类型: 位运算、线段树、数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1521. 找到最接近目标值的函数值 - [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/19/change.png] Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。 请你返回 |func(arr, l, r) - target| 的最小值。 请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。 示例 1： 输入：arr = [9,12,3,7,15], target = 5 输出：2 解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。 示例 2： 输入：arr = [1000000,1000000,1000000], target = 1 输出：999999 解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。 示例 3： 输入：arr = [1,2,4,8,16], target = 0 输出：0 提示： * 1 <= arr.length <= 10^5 * 1 <= arr[i] <= 10^6 * 0 <= target <= 10^7
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和集合来优化查找过程。

算法步骤:
1. 初始化一个集合 `seen` 来存储已经计算过的 `func` 值。
2. 遍历数组 `arr`，对于每个元素 `num`，更新 `seen` 集合。
3. 对于每个 `num`，计算 `func` 值，并使用二分查找来找到最接近 `target` 的值。
4. 更新最小差值。

关键点:
- 使用集合来存储已经计算过的 `func` 值，避免重复计算。
- 使用位运算来快速计算 `func` 值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_closest_value(arr: List[int], target: int) -> int:
    """
    函数式接口 - 找到最接近目标值的函数值
    """
    seen = set()
    closest_diff = float('inf')
    current_and = (1 << 30) - 1  # 初始化为全1
    
    for num in arr:
        current_and &= num
        seen.add(current_and)
        
        # 二分查找最接近 target 的值
        for value in seen:
            diff = abs(value - target)
            if diff < closest_diff:
                closest_diff = diff
                if closest_diff == 0:
                    return 0
    
    return closest_diff


Solution = create_solution(find_closest_value)