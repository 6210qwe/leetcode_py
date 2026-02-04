# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1830
标题: Count Good Meals
难度: medium
链接: https://leetcode.cn/problems/count-good-meals/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1711. 大餐计数 - 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。 你可以搭配 任意 两道餐品做一顿大餐。 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。 示例 1： 输入：deliciousness = [1,3,5,7,9] 输出：4 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。 示例 2： 输入：deliciousness = [1,1,1,3,3,3,7] 输出：15 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。 提示： * 1 <= deliciousness.length <= 105 * 0 <= deliciousness[i] <= 220
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个美味程度出现的次数，然后遍历每个美味程度，检查是否存在另一个美味程度使得它们的和是2的幂。

算法步骤:
1. 初始化一个哈希表 `count` 来记录每个美味程度出现的次数。
2. 初始化一个变量 `result` 来记录大餐的数量。
3. 遍历 `deliciousness` 数组，对于每个美味程度 `val`：
   - 检查 `count` 中是否存在另一个美味程度 `target` 使得 `val + target` 是2的幂，并更新 `result`。
   - 更新 `count` 中 `val` 的出现次数。
4. 返回 `result` 对 10^9 + 7 取余的结果。

关键点:
- 使用哈希表来记录每个美味程度出现的次数，可以快速查找和更新。
- 通过预计算2的幂的范围，减少不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max_val))，其中 n 是 `deliciousness` 的长度，max_val 是 `deliciousness` 中的最大值。
空间复杂度: O(n)，哈希表的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_good_meals(deliciousness: List[int]) -> int:
    MOD = 10**9 + 7
    max_val = max(deliciousness)
    power_of_twos = {2**i for i in range(22)}  # 2^20 is the largest possible sum
    count = {}
    result = 0
    
    for val in deliciousness:
        for target in power_of_twos:
            if target - val in count:
                result += count[target - val]
                result %= MOD
        count[val] = count.get(val, 0) + 1
    
    return result


Solution = create_solution(count_good_meals)