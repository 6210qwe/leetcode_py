# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1562
标题: People Whose List of Favorite Companies Is Not a Subset of Another List
难度: medium
链接: https://leetcode.cn/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1452. 收藏清单 - 给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。 请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。 示例 1： 输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]] 输出：[0,1,4] 解释： favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。 favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。 其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。 示例 2： 输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]] 输出：[0,1] 解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。 示例 3： 输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]] 输出：[0,1,2,3] 提示： * 1 <= favoriteCompanies.length <= 100 * 1 <= favoriteCompanies[i].length <= 500 * 1 <= favoriteCompanies[i][j].length <= 20 * favoriteCompanies[i] 中的所有字符串 各不相同 。 * 用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompanies[j] 仍然成立。 * 所有字符串仅包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合操作来判断一个列表是否是另一个列表的子集。

算法步骤:
1. 将每个用户的收藏清单转换为集合。
2. 遍历每个用户的收藏清单，检查它是否是其他任何用户的收藏清单的子集。
3. 如果某个用户的收藏清单不是其他任何用户的收藏清单的子集，则将其索引添加到结果列表中。

关键点:
- 使用集合操作来高效地判断子集关系。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是用户的数量，m 是每个用户收藏清单的平均长度。
空间复杂度: O(n * m)，用于存储每个用户的收藏清单集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(favoriteCompanies: List[List[str]]) -> List[int]:
    """
    函数式接口 - 返回不是其他任何人收藏的公司清单的子集的收藏清单的索引
    """
    n = len(favoriteCompanies)
    sets = [set(companies) for companies in favoriteCompanies]
    
    result = []
    
    for i in range(n):
        is_subset = False
        for j in range(n):
            if i != j and sets[i].issubset(sets[j]):
                is_subset = True
                break
        if not is_subset:
            result.append(i)
    
    return result


Solution = create_solution(solution_function_name)