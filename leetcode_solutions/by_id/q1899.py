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
核心思想: 使用字典映射来确定需要检查的属性索引，然后遍历所有物品，统计符合条件的物品数量。

算法步骤:
1. 创建一个字典，将 ruleKey 映射到对应的属性索引。
2. 初始化一个计数器，用于记录匹配的物品数量。
3. 遍历每个物品，检查指定属性是否等于 ruleValue，如果是则增加计数器。
4. 返回计数器的值。

关键点:
- 使用字典映射来快速找到需要检查的属性索引。
- 一次遍历即可完成统计。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 items 的长度。我们需要遍历整个 items 数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_matches(items: List[List[str]], rule_key: str, rule_value: str) -> int:
    """
    统计匹配检索规则的物品数量
    """
    # 字典映射 ruleKey 到对应的属性索引
    key_to_index = {"type": 0, "color": 1, "name": 2}
    
    # 获取需要检查的属性索引
    index = key_to_index[rule_key]
    
    # 初始化计数器
    count = 0
    
    # 遍历每个物品，统计符合条件的物品数量
    for item in items:
        if item[index] == rule_value:
            count += 1
    
    return count


Solution = create_solution(count_matches)