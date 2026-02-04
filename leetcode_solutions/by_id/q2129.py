# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2129
标题: Number of Pairs of Interchangeable Rectangles
难度: medium
链接: https://leetcode.cn/problems/number-of-pairs-of-interchangeable-rectangles/
题目类型: 数组、哈希表、数学、计数、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2001. 可互换矩形的组数 - 用一个下标从 0 开始的二维整数数组 rectangles 来表示 n 个矩形，其中 rectangles[i] = [widthi, heighti] 表示第 i 个矩形的宽度和高度。 如果两个矩形 i 和 j（i < j）的宽高比相同，则认为这两个矩形 可互换 。更规范的说法是，两个矩形满足 widthi/heighti == widthj/heightj（使用实数除法而非整数除法），则认为这两个矩形 可互换 。 计算并返回 rectangles 中有多少对 可互换 矩形。 示例 1： 输入：rectangles = [[4,8],[3,6],[10,20],[15,30]] 输出：6 解释：下面按下标（从 0 开始）列出可互换矩形的配对情况： - 矩形 0 和矩形 1 ：4/8 == 3/6 - 矩形 0 和矩形 2 ：4/8 == 10/20 - 矩形 0 和矩形 3 ：4/8 == 15/30 - 矩形 1 和矩形 2 ：3/6 == 10/20 - 矩形 1 和矩形 3 ：3/6 == 15/30 - 矩形 2 和矩形 3 ：10/20 == 15/30 示例 2： 输入：rectangles = [[4,5],[7,8]] 输出：0 解释：不存在成对的可互换矩形。 提示： * n == rectangles.length * 1 <= n <= 105 * rectangles[i].length == 2 * 1 <= widthi, heighti <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个宽高比出现的次数，并计算可互换矩形的对数。

算法步骤:
1. 初始化一个哈希表来记录每个宽高比出现的次数。
2. 遍历所有矩形，计算每个矩形的宽高比，并将其加入哈希表。
3. 遍历哈希表，对于每个宽高比，计算其对应的可互换矩形对数。

关键点:
- 使用最大公约数 (GCD) 来简化宽高比，以避免浮点数比较的问题。
- 使用组合公式 C(n, 2) = n * (n - 1) / 2 来计算每种宽高比的可互换矩形对数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max(width, height)))，其中 n 是矩形的数量，log(max(width, height)) 是计算 GCD 的时间复杂度。
空间复杂度: O(n)，哈希表的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from math import gcd

def solution_function_name(rectangles: List[List[int]]) -> int:
    """
    函数式接口 - 计算可互换矩形的对数
    """
    # 哈希表记录每个宽高比出现的次数
    ratio_count = {}
    
    for width, height in rectangles:
        # 计算宽高比的最简形式
        common_divisor = gcd(width, height)
        simplified_ratio = (width // common_divisor, height // common_divisor)
        
        if simplified_ratio in ratio_count:
            ratio_count[simplified_ratio] += 1
        else:
            ratio_count[simplified_ratio] = 1
    
    # 计算可互换矩形的对数
    interchangeable_pairs = 0
    for count in ratio_count.values():
        if count > 1:
            interchangeable_pairs += count * (count - 1) // 2
    
    return interchangeable_pairs

Solution = create_solution(solution_function_name)