# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000368
标题: 心算挑战
难度: easy
链接: https://leetcode.cn/problems/uOAnQW/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 40. 心算挑战 - 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 `N` 张卡牌中选出 `cnt` 张卡牌，若这 `cnt` 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 `cnt` 张卡牌数字总和。 给定数组 `cards` 和 `cnt`，其中 `cards[i]` 表示第 `i` 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。 **示例 1：** >输入：`cards = [1,2,8,9], cnt = 3` > >输出：`18` > >解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。 **示例 2：** >输入：`cards = [3,3,1], cnt = 1` > >输出：`0` > >解释：不存在获取有效得分的卡牌方案。 **提示：** - `1 <= cnt <= cards.length <= 10^5` - `1 <= cards[i] <= 1000`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 贪心算法，选择最大的cnt个数，如果和为奇数则替换一个奇数

算法步骤:
1. 将数组分为奇数和偶数两组
2. 从大到小排序
3. 选择最大的cnt个数
4. 如果和为奇数，尝试替换一个奇数或偶数

关键点:
- 贪心选择
- 处理奇偶性
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序
空间复杂度: O(n) - 存储分组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maxmium_score(cards: List[int], cnt: int) -> int:
    """
    函数式接口 - 心算挑战
    
    实现思路:
    贪心算法：选择最大的cnt个数，如果和为奇数则调整。
    
    Args:
        cards: 卡牌数组
        cnt: 选择的卡牌数
        
    Returns:
        最大的有效得分
        
    Example:
        >>> maxmium_score([1,2,8,9], 3)
        18
    """
    # 分为奇数和偶数
    odd = [x for x in cards if x % 2 == 1]
    even = [x for x in cards if x % 2 == 0]
    
    odd.sort(reverse=True)
    even.sort(reverse=True)
    
    # 前缀和
    odd_prefix = [0]
    even_prefix = [0]
    for x in odd:
        odd_prefix.append(odd_prefix[-1] + x)
    for x in even:
        even_prefix.append(even_prefix[-1] + x)
    
    max_score = 0
    
    # 枚举选择i个奇数，cnt-i个偶数
    for i in range(0, min(cnt, len(odd)) + 1, 2):  # 奇数个数必须是偶数
        j = cnt - i
        if j < 0 or j > len(even):
            continue
        if i > len(odd) or j > len(even):
            continue
        score = odd_prefix[i] + even_prefix[j]
        max_score = max(max_score, score)
    
    return max_score


Solution = create_solution(maxmium_score)
