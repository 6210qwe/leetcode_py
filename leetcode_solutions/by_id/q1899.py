# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1899
标题: Count Items Matching a Rule
难度: easy
链接: https://leetcode.cn/problems/count-items-matching-a-rule/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1773. 统计匹配检索规则的物品数量 - 给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。 另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。 如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ： * ruleKey == "type" 且 ruleValue == typei 。 * ruleKey == "color" 且 ruleValue == colori 。 * ruleKey == "name" 且 ruleValue == namei 。 统计并返回 匹配检索规则的物品数量 。 示例 1： 输入：items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver" 输出：1 解释：只有一件物品匹配检索规则，这件物品是 ["computer","silver","lenovo"] 。 示例 2： 输入：items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone" 输出：2 解释：只有两件物品匹配检索规则，这两件物品分别是 ["phone","blue","pixel"] 和 ["phone","gold","iphone"] 。注意，["computer","silver","phone"] 未匹配检索规则。 提示： * 1 <= items.length <= 104 * 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10 * ruleKey 等于 "type"、"color" 或 "name" * 所有字符串仅由小写字母组成
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
