# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1477
标题: Product of the Last K Numbers
难度: medium
链接: https://leetcode.cn/problems/product-of-the-last-k-numbers/
题目类型: 设计、数组、数学、数据流、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1352. 最后 K 个数的乘积 - 设计一个算法，该算法接受一个整数流并检索该流中最后 k 个整数的乘积。 实现 ProductOfNumbers 类： * ProductOfNumbers() 用一个空的流初始化对象。 * void add(int num) 将数字 num 添加到当前数字列表的最后面。 * int getProduct(int k) 返回当前数字列表中，最后 k 个数字的乘积。你可以假设当前列表中始终 至少 包含 k 个数字。 题目数据保证：任何时候，任一连续数字序列的乘积都在 32 位整数范围内，不会溢出。 示例： 输入： ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"] [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]] 输出： [null,null,null,null,null,null,20,40,0,null,32] 解释： ProductOfNumbers productOfNumbers = new ProductOfNumbers(); productOfNumbers.add(3); // [3] productOfNumbers.add(0); // [3,0] productOfNumbers.add(2); // [3,0,2] productOfNumbers.add(5); // [3,0,2,5] productOfNumbers.add(4); // [3,0,2,5,4] productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20 productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40 productOfNumbers.getProduct(4); // 返回 0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0 productOfNumbers.add(8); // [3,0,2,5,4,8] productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 提示： * 0 <= num <= 100 * 1 <= k <= 4 * 104 * add 和 getProduct 最多被调用 4 * 104 次。 * 在任何时间点流的乘积都在 32 位整数范围内。 进阶：您能否 同时 将 GetProduct 和 Add 的实现改为 O(1) 时间复杂度，而不是 O(k) 时间复杂度？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
