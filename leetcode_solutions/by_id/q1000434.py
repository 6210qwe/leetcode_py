# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000434
标题: 烹饪料理
难度: easy
链接: https://leetcode.cn/problems/UEcfPD/
题目类型: 位运算、数组、回溯、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 51. 烹饪料理 - 欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。 勇者背包内共有编号为 `0 ~ 4` 的五种食材，其中 `materials[j]` 表示第 `j` 种食材的数量。通过这些食材可以制作若干料理，`cookbooks[i][j]` 表示制作第 `i` 种料理需要第 `j` 种食材的数量，而 `attribute[i] = [x,y]` 表示第 `i` 道料理的美味度 `x` 和饱腹感 `y`。 在饱腹感不小于 `limit` 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 `-1`。 **注意：** - 每种料理只能制作一次。 **示例 1：** >输入：`materials = [3,2,4,1,2]` >`cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]` >`attribute = [[3,2],[2,4],[7,6]]` >`limit = 5` > >输出：`7` > >解释： >食材数量可以满足以下两种方案： >方案一：制作料理 0 和料理 1，可获得饱腹感 2+4、美味度 3+2 >方案二：仅制作料理 2， 可饱腹感为 6、美味度为 7 >因此在满足饱腹感的要求下，可获得最高美味度 7 **示例 2：** >输入：`materials = [10,10,10,10,10]` >`cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]` >`attribute = [[5,5],[6,6],[10,10]]` >`limit = 1` > >输出：`11` > >解释：通过制作料理 0 和 1，可满足饱腹感，并获得最高美味度 11 **提示：** + `materials.length == 5` + `1 <= cookbooks.length == attribute.length <= 8` + `cookbooks[i].length == 5` + `attribute[i].length == 2` + `0 <= materials[i], cookbooks[i][j], attribute[i][j] <= 20` + `1 <= limit <= 100`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯/枚举，尝试所有可能的料理组合

算法步骤:
1. 枚举所有可能的料理组合（2^n种）
2. 检查每种组合是否满足材料要求
3. 如果满足，检查饱腹感是否>=limit
4. 更新最大美味度

关键点:
- 位运算枚举或回溯
- 时间复杂度O(2^n * m)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * m) - n为料理数，m为材料数
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def perfect_menu(materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
    """
    函数式接口 - 烹饪料理
    
    实现思路:
    枚举所有可能的料理组合，找到满足饱腹感要求的最大美味度。
    
    Args:
        materials: 材料数组
        cookbooks: 料理所需材料
        attribute: 料理属性[美味度, 饱腹感]
        limit: 最低饱腹感要求
        
    Returns:
        最大美味度，无法满足返回-1
        
    Example:
        >>> perfect_menu([3,2,4,1,2], [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]], [[3,2],[2,4],[7,6]], 5)
        7
    """
    n = len(cookbooks)
    max_delicious = -1
    
    # 枚举所有可能的组合
    for mask in range(1, 1 << n):
        used_materials = [0] * 5
        total_delicious = 0
        total_satiety = 0
        
        for i in range(n):
            if mask & (1 << i):
                # 检查材料是否足够
                can_make = True
                for j in range(5):
                    used_materials[j] += cookbooks[i][j]
                    if used_materials[j] > materials[j]:
                        can_make = False
                        break
                
                if can_make:
                    total_delicious += attribute[i][0]
                    total_satiety += attribute[i][1]
                else:
                    break
        
        # 检查是否满足条件
        if total_satiety >= limit:
            max_delicious = max(max_delicious, total_delicious)
    
    return max_delicious


Solution = create_solution(perfect_menu)
