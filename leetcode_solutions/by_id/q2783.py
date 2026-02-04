# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2783
标题: Nested Array Generator
难度: medium
链接: https://leetcode.cn/problems/nested-array-generator/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2649. 嵌套数组生成器 - 现给定一个整数的 多维数组 ，请你返回一个生成器对象，按照 中序遍历 的顺序逐个生成整数。 多维数组 是一个递归数据结构，包含整数和其他 多维数组。 中序遍历 是从左到右遍历每个数组，在遇到任何整数时生成它，遇到任何数组时递归应用 中序遍历 。 示例 1： 输入：arr = [[[6]],[1,3],[]] 输出：[6,1,3] 解释： const generator = inorderTraversal(arr); generator.next().value; // 6 generator.next().value; // 1 generator.next().value; // 3 generator.next().done; // true 示例 2： 输入：arr = [] 输出：[] 解释：输入的多维数组没有任何参数，所以生成器不需要生成任何值。 提示： * 0 <= arr.flat().length <= 105 * 0 <= arr.flat()[i] <= 105 * maxNestingDepth <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归生成器来实现中序遍历。

算法步骤:
1. 定义一个递归生成器函数 `inorder_traversal`。
2. 在生成器函数中，遍历当前数组：
   - 如果当前元素是整数，则生成该整数。
   - 如果当前元素是数组，则递归调用生成器函数继续遍历。

关键点:
- 递归生成器可以处理任意深度的嵌套数组。
- 生成器在每次迭代时只生成一个整数，节省内存。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是所有整数的总数。
空间复杂度: O(d)，其中 d 是嵌套数组的最大深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def inorder_traversal(arr):
    """
    递归生成器函数，用于中序遍历多维数组。
    """
    for item in arr:
        if isinstance(item, list):
            yield from inorder_traversal(item)
        else:
            yield item


def solution_function_name(arr: List) -> 'Generator[int, None, None]':
    """
    函数式接口 - 返回一个生成器对象，按照中序遍历的顺序逐个生成整数。
    """
    return inorder_traversal(arr)


Solution = create_solution(solution_function_name)