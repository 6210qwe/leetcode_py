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
核心思想: 使用 Python 的 isinstance 函数来检查对象是否是某个类或其子类的实例。

算法步骤:
1. 检查 obj 是否为 None，如果是则返回 False。
2. 使用 isinstance 函数检查 obj 是否是 cls 或其子类的实例。

关键点:
- 使用 isinstance 函数可以处理继承关系。
- 处理 obj 为 None 的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - isinstance 函数的时间复杂度是常数级别的。
空间复杂度: O(1) - 不需要额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Any, Type


def check_if_instance(obj: Any, cls: Type) -> bool:
    """
    检查给定的对象是否是给定类或其子类的实例。

    :param obj: 待检查的对象
    :param cls: 类
    :return: 如果 obj 是 cls 或其子类的实例，则返回 True，否则返回 False
    """
    if obj is None:
        return False
    return isinstance(obj, cls)


Solution = create_solution(check_if_instance)