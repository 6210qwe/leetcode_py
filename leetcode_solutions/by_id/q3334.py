# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3334
标题: Apple Redistribution into Boxes
难度: easy
链接: https://leetcode.cn/problems/apple-redistribution-into-boxes/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3074. 重新分装苹果 - 给你一个长度为 n 的数组 apple 和另一个长度为 m 的数组 capacity 。 一共有 n 个包裹，其中第 i 个包裹中装着 apple[i] 个苹果。同时，还有 m 个箱子，第 i 个箱子的容量为 capacity[i] 个苹果。 请你选择一些箱子来将这 n 个包裹中的苹果重新分装到箱子中，返回你需要选择的箱子的 最小 数量。 注意，同一个包裹中的苹果可以分装到不同的箱子中。 示例 1： 输入：apple = [1,3,2], capacity = [4,3,1,5,2] 输出：2 解释：使用容量为 4 和 5 的箱子。 总容量大于或等于苹果的总数，所以可以完成重新分装。 示例 2： 输入：apple = [5,5,5], capacity = [2,4,2,7] 输出：4 解释：需要使用所有箱子。 提示： * 1 <= n == apple.length <= 50 * 1 <= m == capacity.length <= 50 * 1 <= apple[i], capacity[i] <= 50 * 输入数据保证可以将包裹中的苹果重新分装到箱子中。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先选择容量最大的箱子来装苹果。

算法步骤:
1. 计算所有苹果的总数量。
2. 将箱子按容量从大到小排序。
3. 依次选择容量最大的箱子，直到总容量大于或等于苹果的总数量。

关键点:
- 优先选择容量大的箱子可以最小化所需的箱子数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m log m + n)，其中 m 是 capacity 的长度，n 是 apple 的长度。排序操作的时间复杂度是 O(m log m)，计算总苹果数和遍历箱子的时间复杂度是 O(n)。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_boxes_to_redistribute_apples(apple: List[int], capacity: List[int]) -> int:
    """
    函数式接口 - 返回重新分装苹果所需的最小箱子数量
    """
    # 计算所有苹果的总数量
    total_apples = sum(apple)
    
    # 将箱子按容量从大到小排序
    capacity.sort(reverse=True)
    
    # 依次选择容量最大的箱子，直到总容量大于或等于苹果的总数量
    boxes_needed = 0
    current_capacity = 0
    for box in capacity:
        current_capacity += box
        boxes_needed += 1
        if current_capacity >= total_apples:
            break
    
    return boxes_needed


Solution = create_solution(min_boxes_to_redistribute_apples)