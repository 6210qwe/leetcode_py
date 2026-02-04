# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1401
标题: Number of Burgers with No Waste of Ingredients
难度: medium
链接: https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1276. 不浪费原料的汉堡制作方案 - 圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。 给你两个整数 tomatoSlices 和 cheeseSlices，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下： * 巨无霸汉堡：4 片番茄和 1 片奶酪 * 小皇堡：2 片番茄和 1 片奶酪 请你以 [total_jumbo, total_small]（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量都是 0。 如果无法使剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量为 0，就请返回 []。 示例 1： 输入：tomatoSlices = 16, cheeseSlices = 7 输出：[1,6] 解释：制作 1 个巨无霸汉堡和 6 个小皇堡需要 4*1 + 2*6 = 16 片番茄和 1 + 6 = 7 片奶酪。不会剩下原料。 示例 2： 输入：tomatoSlices = 17, cheeseSlices = 4 输出：[] 解释：只制作小皇堡和巨无霸汉堡无法用光全部原料。 示例 3： 输入：tomatoSlices = 4, cheeseSlices = 17 输出：[] 解释：制作 1 个巨无霸汉堡会剩下 16 片奶酪，制作 2 个小皇堡会剩下 15 片奶酪。 示例 4： 输入：tomatoSlices = 0, cheeseSlices = 0 输出：[0,0] 示例 5： 输入：tomatoSlices = 2, cheeseSlices = 1 输出：[0,1] 提示： * 0 <= tomatoSlices <= 10^7 * 0 <= cheeseSlices <= 10^7
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过数学方程求解巨无霸汉堡和小皇堡的数量。

算法步骤:
1. 根据番茄片和奶酪片的数量，建立方程组：
   - 4 * jumbo + 2 * small = tomatoSlices
   - jumbo + small = cheeseSlices
2. 解方程组，得到 jumbo 和 small 的值。
3. 检查解是否为非负整数，如果是则返回 [jumbo, small]，否则返回 []。

关键点:
- 通过简单的代数运算求解方程组。
- 检查解的有效性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(tomato_slices: int, cheese_slices: int) -> List[int]:
    """
    函数式接口 - 返回制作巨无霸汉堡和小皇堡的数量，使得剩余的番茄片和奶酪片为 0。
    """
    # 计算巨无霸汉堡和小皇堡的数量
    if (tomato_slices - 2 * cheese_slices) % 2 == 0 and (tomato_slices - 2 * cheese_slices) >= 0:
        jumbo = (tomato_slices - 2 * cheese_slices) // 2
        small = cheese_slices - jumbo
        if small >= 0:
            return [jumbo, small]
    return []


Solution = create_solution(solution_function_name)