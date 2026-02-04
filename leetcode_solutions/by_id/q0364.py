# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 364
标题: Nested List Weight Sum II
难度: medium
链接: https://leetcode.cn/problems/nested-list-weight-sum-ii/
题目类型: 栈、深度优先搜索、广度优先搜索
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
364. 嵌套列表加权和 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 逐层 BFS 统计每一层的整数和，最后从外到内用权重累加。

算法步骤:
1. 使用队列按层遍历嵌套列表 `nestedList`，初始将最外层所有 `NestedInteger` 入队。
2. 对于每一层：遍历当前队列中的元素，若是整数则加入当前层和 `s`，若是列表则将其内部元素加入下一层队列；然后将这一层的和 `s` 记录到数组 `level_sums` 中。
3. 遍历完所有层后，最外层在 `level_sums[0]`，最内层在 `level_sums[-1]`。设权重从最外层开始为 `len(level_sums)` 递减到 1，累加 `sum_i level_sums[i] * weight_i` 即为答案。

关键点:
- 通过自外向内层序遍历获得每一层的和，再自外向内赋予权重，避免显式计算最大深度。
- 避免递归深度过深，BFS 更稳健。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N)，N 为所有整数和列表节点总数，每个元素仅访问一次。
空间复杂度: O(D)，D 为最大宽度，需要队列和 `level_sums` 存储每一层的信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def nested_list_weight_sum_ii(nestedList) -> int:
    """
    计算嵌套列表的加权和 II：越外层权重越大。

    使用层序遍历，记录每一层的整数和，最后从外层到内层累加。
    nestedList 元素需符合 LeetCode 的 NestedInteger 接口。
    """
    from collections import deque

    if not nestedList:
        return 0

    level_sums: list[int] = []
    q = deque(nestedList)

    while q:
        size = len(q)
        s = 0
        for _ in range(size):
            ni = q.popleft()
            if ni.isInteger():
                s += ni.getInteger()
            else:
                q.extend(ni.getList())
        level_sums.append(s)

    # 最外层权重最大
    total = 0
    weight = len(level_sums)
    for s in level_sums:
        total += s * weight
        weight -= 1
    return total


# 自动生成Solution类（无需手动编写）
Solution = create_solution(nested_list_weight_sum_ii)
