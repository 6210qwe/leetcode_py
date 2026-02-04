# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2026
标题: Merge Triplets to Form Target Triplet
难度: medium
链接: https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1899. 合并若干三元组以形成目标三元组 - 三元组 是一个由三个整数组成的数组。给你一个二维整数数组 triplets ，其中 triplets[i] = [ai, bi, ci] 表示第 i 个 三元组 。同时，给你一个整数数组 target = [x, y, z] ，表示你想要得到的 三元组 。 为了得到 target ，你需要对 triplets 执行下面的操作 任意次（可能 零 次）： * 选出两个下标（下标 从 0 开始 计数）i 和 j（i != j），并 更新 triplets[j] 为 [max(ai, aj), max(bi, bj), max(ci, cj)] 。 * 例如，triplets[i] = [2, 5, 3] 且 triplets[j] = [1, 7, 5]，triplets[j] 将会更新为 [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5] 。 如果通过以上操作我们可以使得目标 三元组 target 成为 triplets 的一个 元素 ，则返回 true ；否则，返回 false 。 示例 1： 输入：triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5] 输出：true 解释：执行下述操作： - 选择第一个和最后一个三元组 [[2,5,3],[1,8,4],[1,7,5]] 。更新最后一个三元组为 [max(2,1), max(5,7), max(3,5)] = [2,7,5] 。triplets = [[2,5,3],[1,8,4],[2,7,5]] 目标三元组 [2,7,5] 现在是 triplets 的一个元素。 示例 2： 输入：triplets = [[1,3,4],[2,5,8]], target = [2,5,8] 输出：true 解释：目标三元组 [2,5,8] 已经是 triplets 的一个元素。 示例 3： 输入：triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5] 输出：true 解释：执行下述操作： - 选择第一个和第三个三元组 [[2,5,3],[2,3,4],[1,2,5],[5,2,3]] 。更新第三个三元组为 [max(2,1), max(5,2), max(3,5)] = [2,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]] 。 - 选择第三个和第四个三元组 [[2,5,3],[2,3,4],[2,5,5],[5,2,3]] 。更新第四个三元组为 [max(2,5), max(5,2), max(5,3)] = [5,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]] 。 目标三元组 [5,5,5] 现在是 triplets 的一个元素。 示例 4： 输入：triplets = [[3,4,5],[4,5,6]], target = [3,2,5] 输出：false 解释：无法得到 [3,2,5] ，因为 triplets 不含 2 。 提示： * 1 <= triplets.length <= 105 * triplets[i].length == target.length == 3 * 1 <= ai, bi, ci, x, y, z <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，筛选出符合条件的三元组，然后检查是否可以通过这些三元组合并得到目标三元组。

算法步骤:
1. 初始化三个布尔变量，分别表示是否找到了满足条件的 a, b, c。
2. 遍历所有三元组，对于每个三元组，如果它的三个值都小于等于目标三元组的对应值，则更新对应的布尔变量。
3. 最后检查这三个布尔变量是否都为 True，如果是，则返回 True，否则返回 False。

关键点:
- 只选择那些不会超过目标三元组的三元组进行合并。
- 通过三个布尔变量来跟踪是否找到了满足条件的 a, b, c。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 triplets 的长度。我们只需要遍历一次 triplets 数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
    """
    函数式接口 - 判断是否可以通过合并 triplets 中的三元组得到目标三元组 target。
    """
    found_a, found_b, found_c = False, False, False
    
    for triplet in triplets:
        if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
            found_a = found_a or (triplet[0] == target[0])
            found_b = found_b or (triplet[1] == target[1])
            found_c = found_c or (triplet[2] == target[2])
    
    return found_a and found_b and found_c


Solution = create_solution(can_merge_triplets)