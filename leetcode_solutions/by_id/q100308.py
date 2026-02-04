# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100308
标题: 套餐内商品的排列顺序
难度: medium
链接: https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/
题目类型: 字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 157. 套餐内商品的排列顺序 - 某店铺将用于组成套餐的商品记作字符串 goods，其中 goods[i] 表示对应商品。请返回该套餐内所含商品的 全部排列方式 。 返回结果 无顺序要求，但不能含有重复的元素。 示例 1： 输入：goods = "agew" 输出：["aegw","aewg","agew","agwe","aweg","awge","eagw","eawg","egaw","egwa","ewag","ewga","gaew","gawe","geaw","gewa","gwae","gwea","waeg","wage","weag","wega","wgae","wgea"] 提示： * 1 <= goods.length <= 8
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的排列，并使用集合去重。

算法步骤:
1. 将字符串转换为列表以便于操作。
2. 使用递归函数进行回溯，生成所有可能的排列。
3. 使用集合存储结果以去重。
4. 将结果转换为列表并返回。

关键点:
- 递归函数中通过交换字符位置来生成新的排列。
- 使用集合来去重。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * n!)，其中 n 是字符串的长度。n! 是排列的数量，每个排列需要 O(n) 的时间来生成。
空间复杂度: O(n * n!)，存储所有排列所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(goods: str) -> List[str]:
    """
    函数式接口 - 生成给定字符串的所有排列
    """
    def backtrack(start: int):
        if start == n:
            result.add(''.join(chars))
            return
        for i in range(start, n):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    chars = list(goods)
    n = len(chars)
    result = set()
    backtrack(0)
    return list(result)


Solution = create_solution(solution_function_name)