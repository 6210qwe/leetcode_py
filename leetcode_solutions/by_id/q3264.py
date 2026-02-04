# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3264
标题: Maximum Points After Enemy Battles
难度: medium
链接: https://leetcode.cn/problems/maximum-points-after-enemy-battles/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3207. 与敌人战斗后的最大分数 - 给你一个下标从 0 开始的整数数组 enemyEnergies ，它表示一个下标从 0 开始的敌人能量数组。 同时给你一个整数 currentEnergy ，它表示你一开始拥有的能量值总量。 你一开始的分数为 0 ，且一开始所有的敌人都未标记。 你可以通过以下操作 之一 任意次（也可以 0 次）来得分： * 选择一个 未标记 且满足 currentEnergy >= enemyEnergies[i] 的敌人 i 。在这个操作中： * 你会获得 1 分。 * 你的能量值减少 enemyEnergies[i] ，也就是说 currentEnergy = currentEnergy - enemyEnergies[i] 。 * 如果你目前 至少 有 1 分，你可以选择一个 未标记 的敌人 i 。在这个操作中： * 你的能量值增加 enemyEnergies[i] ，也就是说 currentEnergy = currentEnergy + enemyEnergies[i] 。 * 敌人 i 被标记 。 请你返回通过以上操作，最多 可以获得多少分。 示例 1： 输入：enemyEnergies = [3,2,2], currentEnergy = 2 输出：3 解释： 通过以下操作可以得到最大得分 3 分： * 对敌人 1 使用第一种操作：points 增加 1 ，currentEnergy 减少 2 。所以 points = 1 且 currentEnergy = 0 。 * 对敌人 0 使用第二种操作：currentEnergy 增加 3 ，敌人 0 被标记。所以 points = 1 ，currentEnergy = 3 ，被标记的敌人包括 [0] 。 * 对敌人 2 使用第一种操作：points 增加 1 ，currentEnergy 减少 2 。所以 points = 2 且 currentEnergy = 1 ，被标记的敌人包括[0] 。 * 对敌人 2 使用第二种操作：currentEnergy 增加 2 ，敌人 2 被标记。所以 points = 2 ，currentEnergy = 3 且被标记的敌人包括 [0, 2] 。 * 对敌人 1 使用第一种操作：points 增加 1 ，currentEnergy 减少 2 。所以 points = 3 ，currentEnergy = 1 ，被标记的敌人包括 [0, 2] 。 示例 2： 输入：enemyEnergies = [2], currentEnergy = 10 输出：5 解释： 通过对敌人 0 进行第一种操作 5 次，得到最大得分。 提示： * 1 <= enemyEnergies.length <= 105 * 1 <= enemyEnergies[i] <= 109 * 0 <= currentEnergy <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先处理能量值较小的敌人，以最大化得分。

算法步骤:
1. 将敌人能量数组按升序排序。
2. 初始化当前能量和得分为初始值。
3. 遍历排序后的敌人能量数组：
   - 如果当前能量大于等于敌人能量，则进行第一种操作，增加得分并减少当前能量。
   - 如果当前得分大于等于1，则进行第二种操作，增加当前能量并将敌人标记。
4. 返回最终得分。

关键点:
- 通过排序确保优先处理能量值较小的敌人，从而最大化得分。
- 动态调整当前能量和得分，确保在每一步都能做出最优选择。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 enemyEnergies 的长度，主要由排序操作决定。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def solution_function_name(enemy_energies: List[int], current_energy: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    # 将敌人能量数组按升序排序
    enemy_energies.sort()
    
    points = 0
    for energy in enemy_energies:
        if current_energy >= energy:
            # 进行第一种操作，增加得分并减少当前能量
            points += 1
            current_energy -= energy
        elif points > 0:
            # 进行第二种操作，增加当前能量并将敌人标记
            current_energy += energy
            points -= 1
    
    return points

Solution = create_solution(solution_function_name)