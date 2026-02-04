# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2459
标题: Minimum Hours of Training to Win a Competition
难度: easy
链接: https://leetcode.cn/problems/minimum-hours-of-training-to-win-a-competition/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2383. 赢得比赛需要的最少训练时长 - 你正在参加一场比赛，给你两个 正 整数 initialEnergy 和 initialExperience 分别表示你的初始精力和初始经验。 另给你两个下标从 0 开始的整数数组 energy 和 experience，长度均为 n 。 你将会 依次 对上 n 个对手。第 i 个对手的精力和经验分别用 energy[i] 和 experience[i] 表示。当你对上对手时，需要在经验和精力上都 严格 超过对手才能击败他们，然后在可能的情况下继续对上下一个对手。 击败第 i 个对手会使你的经验 增加 experience[i]，但会将你的精力 减少 energy[i] 。 在开始比赛前，你可以训练几个小时。每训练一个小时，你可以选择将增加经验增加 1 或者 将精力增加 1 。 返回击败全部 n 个对手需要训练的 最少 小时数目。 示例 1： 输入：initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1] 输出：8 解释：在 6 小时训练后，你可以将精力提高到 11 ，并且再训练 2 个小时将经验提高到 5 。 按以下顺序与对手比赛： - 你的精力与经验都超过第 0 个对手，所以获胜。 精力变为：11 - 1 = 10 ，经验变为：5 + 2 = 7 。 - 你的精力与经验都超过第 1 个对手，所以获胜。 精力变为：10 - 4 = 6 ，经验变为：7 + 6 = 13 。 - 你的精力与经验都超过第 2 个对手，所以获胜。 精力变为：6 - 3 = 3 ，经验变为：13 + 3 = 16 。 - 你的精力与经验都超过第 3 个对手，所以获胜。 精力变为：3 - 2 = 1 ，经验变为：16 + 1 = 17 。 在比赛前进行了 8 小时训练，所以返回 8 。 可以证明不存在更小的答案。 示例 2： 输入：initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3] 输出：0 解释：你不需要额外的精力和经验就可以赢得比赛，所以返回 0 。 提示： * n == energy.length == experience.length * 1 <= n <= 100 * 1 <= initialEnergy, initialExperience, energy[i], experience[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法计算所需的最少训练时间。首先计算所需的总精力，然后逐个检查每个对手的经验要求，并在必要时增加经验。

算法步骤:
1. 计算击败所有对手所需的总精力。
2. 初始化当前精力和经验。
3. 逐个检查每个对手：
   - 如果当前精力不足以击败对手，则增加训练时间以满足精力要求。
   - 如果当前经验不足以击败对手，则增加训练时间以满足经验要求。
   - 更新当前精力和经验。
4. 返回所需的训练时间。

关键点:
- 通过一次遍历计算所需的总精力。
- 通过逐个检查每个对手的经验要求，确保每次都能击败对手。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是对手的数量。我们只需要遍历一次对手列表。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_hours(initial_energy: int, initial_experience: int, energy: List[int], experience: List[int]) -> int:
    """
    计算击败所有对手所需的最少训练时间。
    
    :param initial_energy: 初始精力
    :param initial_experience: 初始经验
    :param energy: 对手的精力列表
    :param experience: 对手的经验列表
    :return: 所需的最少训练时间
    """
    # 计算所需的总精力
    total_energy = sum(energy)
    current_energy = initial_energy
    current_experience = initial_experience
    training_hours = 0
    
    for i in range(len(energy)):
        # 如果当前精力不足以击败对手
        if current_energy <= energy[i]:
            training_hours += (energy[i] - current_energy + 1)
            current_energy = energy[i] + 1
        
        # 如果当前经验不足以击败对手
        if current_experience <= experience[i]:
            training_hours += (experience[i] - current_experience + 1)
            current_experience = experience[i] + 1
        
        # 更新当前精力和经验
        current_energy -= energy[i]
        current_experience += experience[i]
    
    return training_hours


Solution = create_solution(minimum_hours)