# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3934
标题: Coupon Code Validator
难度: easy
链接: https://leetcode.cn/problems/coupon-code-validator/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3606. 优惠券校验器 - 给你三个长度为 n 的数组，分别描述 n 个优惠券的属性：code、businessLine 和 isActive。其中，第 i 个优惠券具有以下属性： * code[i]：一个 字符串，表示优惠券的标识符。 * businessLine[i]：一个 字符串，表示优惠券所属的业务类别。 * isActive[i]：一个 布尔值，表示优惠券是否当前有效。 当以下所有条件都满足时，优惠券被认为是 有效的 ： 1. code[i] 不能为空，并且仅由字母数字字符（a-z、A-Z、0-9）和下划线（_）组成。 2. businessLine[i] 必须是以下四个类别之一："electronics"、"grocery"、"pharmacy"、"restaurant"。 3. isActive[i] 为 true 。 返回所有 有效优惠券的标识符 组成的数组，按照以下规则排序： * 先按照其 businessLine 的顺序排序："electronics"、"grocery"、"pharmacy"、"restaurant"。 * 在每个类别内，再按照 标识符的字典序（升序）排序。 示例 1： 输入： code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true] 输出： ["PHARMA5","SAVE20"] 解释： * 第一个优惠券有效。 * 第二个优惠券的标识符为空（无效）。 * 第三个优惠券有效。 * 第四个优惠券的标识符包含特殊字符 @（无效）。 示例 2： 输入： code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true] 输出： ["ELECTRONICS_50"] 解释： * 第一个优惠券无效，因为它未激活。 * 第二个优惠券有效。 * 第三个优惠券无效，因为其业务类别无效。 提示： * n == code.length == businessLine.length == isActive.length * 1 <= n <= 100 * 0 <= code[i].length, businessLine[i].length <= 100 * code[i] 和 businessLine[i] 由可打印的 ASCII 字符组成。 * isActive[i] 的值为 true 或 false。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过过滤和排序来找到所有有效的优惠券。

算法步骤:
1. 定义一个函数 `is_valid_code` 来检查优惠券代码是否有效。
2. 过滤出所有有效的优惠券。
3. 对有效的优惠券按业务类别和标识符进行排序。
4. 返回排序后的有效优惠券标识符列表。

关键点:
- 使用正则表达式来验证优惠券代码的有效性。
- 使用 Python 的 `sorted` 函数来进行多级排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是优惠券的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，存储有效优惠券的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import re

def is_valid_code(code: str) -> bool:
    """检查优惠券代码是否有效"""
    if not code:
        return False
    return bool(re.match(r'^[a-zA-Z0-9_]+$', code))

def solution_function_name(code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
    """
    函数式接口 - 找到所有有效的优惠券标识符并按规则排序
    """
    valid_coupons = []
    for i in range(len(code)):
        if (is_valid_code(code[i]) and 
            businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and 
            isActive[i]):
            valid_coupons.append((code[i], businessLine[i]))

    # 按业务类别和标识符排序
    sorted_coupons = sorted(valid_coupons, key=lambda x: (["electronics", "grocery", "pharmacy", "restaurant"].index(x[1]), x[0]))

    return [coupon[0] for coupon in sorted_coupons]

Solution = create_solution(solution_function_name)