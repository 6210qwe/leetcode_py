# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 384
标题: Shuffle an Array
难度: medium
链接: https://leetcode.cn/problems/shuffle-an-array/
题目类型: 设计、数组、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
384. 打乱数组 - 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。 实现 Solution class: * Solution(int[] nums) 使用整数数组 nums 初始化对象 * int[] reset() 重设数组到它的初始状态并返回 * int[] shuffle() 返回数组随机打乱后的结果 示例 1： 输入 ["Solution", "shuffle", "reset", "shuffle"] [[[1, 2, 3]], [], [], []] 输出 [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]] 解释 Solution solution = new Solution([1, 2, 3]); solution.shuffle(); // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2] solution.reset(); // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3] solution.shuffle(); // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2] 提示： * 1 <= nums.length <= 50 * -106 <= nums[i] <= 106 * nums 中的所有元素都是 唯一的 * 最多可以调用 104 次 reset 和 shuffle
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: Fisher-Yates洗牌算法

算法步骤:
1. 保存原始数组
2. reset: 返回原始数组的副本
3. shuffle: 使用Fisher-Yates算法随机打乱
   - 从后往前遍历
   - 对每个位置i，随机选择[0,i]中的一个位置j
   - 交换i和j位置的元素

关键点:
- Fisher-Yates算法保证每个排列等概率
- 需要保存原始数组用于reset
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - shuffle操作
空间复杂度: O(n) - 保存原始数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import random
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Solution:
    """
    打乱数组的Solution类
    """
    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.nums = nums.copy()
    
    def reset(self) -> List[int]:
        """重置数组到初始状态"""
        self.nums = self.original.copy()
        return self.nums
    
    def shuffle(self) -> List[int]:
        """随机打乱数组"""
        n = len(self.nums)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


def shuffle_an_array(nums: List[int]) -> Solution:
    """
    函数式接口 - 打乱数组
    
    实现思路:
    创建Solution对象，实现reset和shuffle方法。
    
    Args:
        nums: 整数数组
        
    Returns:
        Solution对象
        
    Example:
        >>> solution = shuffle_an_array([1,2,3])
        >>> solution.shuffle()
        [随机排列]
    """
    return Solution(nums)


# 注意：此题需要返回Solution类，而不是使用create_solution
# Solution类已在上面定义
