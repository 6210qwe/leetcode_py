# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2228
标题: Watering Plants II
难度: medium
链接: https://leetcode.cn/problems/watering-plants-ii/
题目类型: 数组、双指针、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2105. 给植物浇水 II - Alice 和 Bob 打算给花园里的 n 株植物浇水。植物排成一行，从左到右进行标记，编号从 0 到 n - 1 。其中，第 i 株植物的位置是 x = i 。 每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐，最初是满的 。他们按下面描述的方式完成浇水： * Alice 按 从左到右 的顺序给植物浇水，从植物 0 开始。Bob 按 从右到左 的顺序给植物浇水，从植物 n - 1 开始。他们 同时 给植物浇水。 * 无论需要多少水，为每株植物浇水所需的时间都是相同的。 * 如果 Alice/Bob 水罐中的水足以 完全 灌溉植物，他们 必须 给植物浇水。否则，他们 首先（立即）重新装满罐子，然后给植物浇水。 * 如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水 更多 的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。 给你一个下标从 0 开始的整数数组 plants ，数组由 n 个整数组成。其中，plants[i] 为第 i 株植物需要的水量。另有两个整数 capacityA 和 capacityB 分别表示 Alice 和 Bob 水罐的容量。返回两人浇灌所有植物过程中重新灌满水罐的 次数 。 示例 1： 输入：plants = [2,2,3,3], capacityA = 5, capacityB = 5 输出：1 解释： - 最初，Alice 和 Bob 的水罐中各有 5 单元水。 - Alice 给植物 0 浇水，Bob 给植物 3 浇水。 - Alice 和 Bob 现在分别剩下 3 单元和 2 单元水。 - Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 2 ，所以他先重新装满水，再浇水。 所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 0 = 1 。 示例 2： 输入：plants = [2,2,3,3], capacityA = 3, capacityB = 4 输出：2 解释： - 最初，Alice 的水罐中有 3 单元水，Bob 的水罐中有 4 单元水。 - Alice 给植物 0 浇水，Bob 给植物 3 浇水。 - Alice 和 Bob 现在都只有 1 单元水，并分别需要给植物 1 和植物 2 浇水。 - 由于他们的水量均不足以浇水，所以他们重新灌满水罐再进行浇水。 所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 1 + 1 + 0 = 2 。 示例 3： 输入：plants = [5], capacityA = 10, capacityB = 8 输出：0 解释： - 只有一株植物 - Alice 的水罐有 10 单元水，Bob 的水罐有 8 单元水。因此 Alice 的水罐中水更多，她会给这株植物浇水。 所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 。 提示： * n == plants.length * 1 <= n <= 105 * 1 <= plants[i] <= 106 * max(plants[i]) <= capacityA, capacityB <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针模拟 Alice 和 Bob 浇水的过程，同时记录重新灌满水罐的次数。

算法步骤:
1. 初始化 Alice 和 Bob 的水罐容量，以及重新灌满水罐的次数。
2. 使用双指针分别从左到右和从右到左遍历植物数组。
3. 对于每一株植物，检查 Alice 和 Bob 是否有足够的水来浇水。
4. 如果没有足够的水，则重新灌满水罐并增加重新灌满水罐的次数。
5. 如果 Alice 和 Bob 到达同一株植物，比较两人的水罐剩余水量，决定谁来浇水。
6. 返回重新灌满水罐的总次数。

关键点:
- 使用双指针模拟 Alice 和 Bob 的浇水过程。
- 在每次浇水前检查水罐剩余水量，必要时重新灌满水罐。
- 处理 Alice 和 Bob 到达同一株植物的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是植物的数量。每个植物最多被访问一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(plants: List[int], capacityA: int, capacityB: int) -> int:
    """
    函数式接口 - 计算 Alice 和 Bob 浇灌所有植物过程中重新灌满水罐的次数
    """
    n = len(plants)
    waterA, waterB = capacityA, capacityB
    refill_count = 0
    left, right = 0, n - 1

    while left <= right:
        if left == right:
            if waterA >= plants[left] or waterB >= plants[right]:
                break
            else:
                refill_count += 1
                break

        if waterA < plants[left]:
            waterA = capacityA
            refill_count += 1
        waterA -= plants[left]
        left += 1

        if waterB < plants[right]:
            waterB = capacityB
            refill_count += 1
        waterB -= plants[right]
        right -= 1

    return refill_count


Solution = create_solution(solution_function_name)