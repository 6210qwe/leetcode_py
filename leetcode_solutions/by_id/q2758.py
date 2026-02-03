# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2758
标题: Check if Object Instance of Class
难度: medium
链接: https://leetcode.cn/problems/check-if-object-instance-of-class/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2618. 检查是否是类的对象实例 - 请你编写一个函数，检查给定的值是否是给定类或超类的实例。 可以传递给函数的数据类型没有限制。例如，值或类可能是 undefined 。 示例 1： 输入：func = () => checkIfInstance(new Date(), Date) 输出：true 解释：根据定义，Date 构造函数返回的对象是 Date 的一个实例。 示例 2： 输入：func = () => { class Animal {}; class Dog extends Animal {}; return checkIfInstance(new Dog(), Animal); } 输出：true 解释： class Animal {}; class Dog extends Animal {}; checkIfInstanceOf(new Dog(), Animal); // true Dog 是 Animal 的子类。因此，Dog 对象同时是 Dog 和 Animal 的实例。 示例 3： 输入：func = () => checkIfInstance(Date, Date) 输出：false 解释：日期的构造函数在逻辑上不能是其自身的实例。 示例 4： 输入：func = () => checkIfInstance(5, Number) 输出：true 解释：5 是一个 Number。注意，"instanceof" 关键字将返回 false。
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
