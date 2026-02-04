# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000476
标题: 气温变化趋势
难度: easy
链接: https://leetcode.cn/problems/6CE719/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 61. 气温变化趋势 - 力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 `i ~ (i+1)` 天的气温变化趋势，将根据以下规则判断： - 若第 `i+1` 天的气温 **高于** 第 `i` 天，为 **上升** 趋势 - 若第 `i+1` 天的气温 **等于** 第 `i` 天，为 **平稳** 趋势 - 若第 `i+1` 天的气温 **低于** 第 `i` 天，为 **下降** 趋势 已知 `temperatureA[i]` 和 `temperatureB[i]` 分别表示第 `i` 天两地区的气温。 组委会希望找到一段天数尽可能多，且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势**相同的最大连续天数**。 > 即最大的 `n`，使得第 `i~i+n` 天之间，两地气温变化趋势相同 **示例 1：** >输入： >`temperatureA = [21,18,18,18,31]` >`temperatureB = [34,32,16,16,17]` > >输出：`2` > >解释：如下表所示， 第 `2～4` 天两地气温变化趋势相同，且持续时间最长，因此返回 `4-2=2` ![image.png](https://pic.leetcode.cn/1663902654-hlrSvs-image.png){:width=1000px} **示例 2：** >输入： >`temperatureA = [5,10,16,-6,15,11,3]` >`temperatureB = [16,22,23,23,25,3,-16]` > >输出：`3` **提示：** - `2 <= temperatureA.length == temperatureB.length <= 1000` - `-20 <= temperatureA[i], temperatureB[i] <= 40`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针遍历两个温度数组，比较相邻两天的趋势是否相同，并记录最长的相同趋势天数。

算法步骤:
1. 初始化两个指针 `i` 和 `j`，分别指向 `temperatureA` 和 `temperatureB` 的起始位置。
2. 遍历数组，比较 `temperatureA[i]` 和 `temperatureA[i+1]` 以及 `temperatureB[j]` 和 `temperatureB[j+1]` 的趋势。
3. 如果趋势相同，增加计数器 `count`，否则重置 `count`。
4. 更新最大连续天数 `max_count`。
5. 返回 `max_count`。

关键点:
- 使用双指针遍历数组，确保每次比较相邻两天的趋势。
- 使用变量 `count` 记录当前连续相同趋势的天数，使用 `max_count` 记录最大连续天数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是温度数组的长度，因为我们需要遍历整个数组一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(temperatureA: List[int], temperatureB: List[int]) -> int:
    """
    函数式接口 - 返回两地气温变化趋势相同的最大连续天数
    """
    def get_trend(temp1: int, temp2: int) -> int:
        if temp1 < temp2:
            return 1  # 上升趋势
        elif temp1 == temp2:
            return 0  # 平稳趋势
        else:
            return -1  # 下降趋势

    max_count = 0
    count = 0
    n = len(temperatureA)

    for i in range(n - 1):
        trendA = get_trend(temperatureA[i], temperatureA[i + 1])
        trendB = get_trend(temperatureB[i], temperatureB[i + 1])

        if trendA == trendB:
            count += 1
        else:
            count = 0

        max_count = max(max_count, count)

    return max_count


Solution = create_solution(solution_function_name)