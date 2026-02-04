# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100310
标题: 库存管理 II
难度: easy
链接: https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
题目类型: 数组、哈希表、分治、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 158. 库存管理 II - 仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。请返回库存表中数量大于 stock.length / 2 的商品 id。 示例 1： 输入：stock = [6, 1, 3, 1, 1, 1] 输出：1 提示： * 1 <= stock.length <= 50000 * 给定数组为非空数组，且存在结果数字 注意：本题与主站 169 题相同：https://leetcode.cn/problems/majority-element/ [https://leetcode.cn/problems/majority-element/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Boyer-Moore 投票算法

算法步骤:
1. 初始化候选元素和计数器。
2. 遍历数组，更新候选元素和计数器。
3. 返回候选元素。

关键点:
- Boyer-Moore 投票算法能够在 O(n) 时间复杂度和 O(1) 空间复杂度内找到主要元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(stock: List[int]) -> int:
    """
    函数式接口 - 使用 Boyer-Moore 投票算法找到数量大于一半的商品 id
    """
    candidate = None
    count = 0
    
    for num in stock:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate


Solution = create_solution(solution_function_name)