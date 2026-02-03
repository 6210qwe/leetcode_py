# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 458
标题: Poor Pigs
难度: hard
链接: https://leetcode.cn/problems/poor-pigs/
题目类型: 数学、动态规划、组合数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
458. 可怜的小猪 - 有 buckets 桶液体，其中 正好有一桶 含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 minutesToTest 分钟时间来确定哪桶液体是有毒的。 喂猪的规则如下： 1. 选择若干活猪进行喂养 2. 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。 3. 小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。 4. 过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。 5. 重复这一过程，直到时间用完。 给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回 在规定时间内判断哪个桶有毒所需的 最小 猪数 。 示例 1： 输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60 输出：5 示例 2： 输入：buckets = 4, minutesToDie = 15, minutesToTest = 15 输出：2 示例 3： 输入：buckets = 4, minutesToDie = 15, minutesToTest = 30 输出：2 提示： * 1 <= buckets <= 1000 * 1 <= minutesToDie <= minutesToTest <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 数学问题，信息论角度，每只猪可以测试多个时间点

算法步骤:
1. 每只猪可以测试 (minutesToTest // minutesToDie + 1) 个时间点
2. 每只猪可以区分多个桶（通过不同的时间点组合）
3. 需要的猪数 = ceil(log(buckets) / log(tests_per_pig))

关键点:
- 信息论：每只猪可以测试多个时间点
- 使用对数计算
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 常数时间计算
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import math
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def poor_pigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    """
    函数式接口 - 可怜的小猪
    
    实现思路:
    每只猪可以测试多个时间点，通过信息论计算最少需要的猪数。
    
    Args:
        buckets: 桶的数量
        minutesToDie: 猪死亡所需时间
        minutesToTest: 总测试时间
        
    Returns:
        最少需要的猪数
        
    Example:
        >>> poor_pigs(1000, 15, 60)
        5
    """
    # 每只猪可以测试的时间点数量
    tests_per_pig = minutesToTest // minutesToDie + 1
    
    # 计算需要的猪数：ceil(log(buckets) / log(tests_per_pig))
    return math.ceil(math.log(buckets) / math.log(tests_per_pig))


# 自动生成Solution类（无需手动编写）
Solution = create_solution(poor_pigs)
