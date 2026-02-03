# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 789
标题: Kth Largest Element in a Stream
难度: easy
链接: https://leetcode.cn/problems/kth-largest-element-in-a-stream/
题目类型: 树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
703. 数据流中的第 K 大元素 - 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。 请实现 KthLargest 类： * KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。 * int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。 示例 1： 输入： ["KthLargest", "add", "add", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]] 输出：[null, 4, 5, 5, 8, 8] 解释： KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); kthLargest.add(3); // 返回 4 kthLargest.add(5); // 返回 5 kthLargest.add(10); // 返回 5 kthLargest.add(9); // 返回 8 kthLargest.add(4); // 返回 8 示例 2： 输入： ["KthLargest", "add", "add", "add", "add"] [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]] 输出：[null, 7, 7, 7, 8] 解释： KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]); kthLargest.add(2); // 返回 7 kthLargest.add(10); // 返回 7 kthLargest.add(9); // 返回 7 kthLargest.add(9); // 返回 8 提示： * 0 <= nums.length <= 104 * 1 <= k <= nums.length + 1 * -104 <= nums[i] <= 104 * -104 <= val <= 104 * 最多调用 add 方法 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
