# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2247
标题: Number of Unique Flavors After Sharing K Candies
难度: medium
链接: https://leetcode.cn/problems/number-of-unique-flavors-after-sharing-k-candies/
题目类型: 数组、哈希表、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2107. 分享 K 个糖果后独特口味的数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来追踪当前窗口内的唯一口味数量。

算法步骤:
1. 初始化一个哈希表来记录每个口味的出现次数。
2. 使用两个指针（left 和 right）来表示滑动窗口的左右边界。
3. 移动右指针扩展窗口，更新哈希表中的口味计数。
4. 如果窗口内的糖果总数超过 K，则移动左指针收缩窗口，并更新哈希表中的口味计数。
5. 维护一个变量来记录窗口内唯一口味的最大数量。

关键点:
- 使用哈希表来快速更新和查询口味的出现次数。
- 滑动窗口技术可以有效地在 O(n) 时间复杂度内解决问题。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(m)，其中 m 是不同口味的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def solution_function_name(candies: List[int], k: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    flavor_count = {}
    left = 0
    unique_flavors = 0
    max_unique_flavors = 0
    
    for right in range(len(candies)):
        if candies[right] not in flavor_count:
            flavor_count[candies[right]] = 0
        flavor_count[candies[right]] += 1
        
        if flavor_count[candies[right]] == 1:
            unique_flavors += 1
        
        while (right - left + 1) > k:
            flavor_count[candies[left]] -= 1
            if flavor_count[candies[left]] == 0:
                unique_flavors -= 1
            left += 1
        
        max_unique_flavors = max(max_unique_flavors, unique_flavors)
    
    return max_unique_flavors

Solution = create_solution(solution_function_name)