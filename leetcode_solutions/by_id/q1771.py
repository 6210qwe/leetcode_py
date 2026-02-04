# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1771
标题: Sell Diminishing-Valued Colored Balls
难度: medium
链接: https://leetcode.cn/problems/sell-diminishing-valued-colored-balls/
题目类型: 贪心、数组、数学、二分查找、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1648. 销售价值减少的颜色球 - 你有一些球的库存 inventory ，里面包含着不同颜色的球。一个顾客想要 任意颜色 总数为 orders 的球。 这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 同色球 的数目。比方说还剩下 6 个黄球，那么顾客买第一个黄球的时候该黄球的价值为 6 。这笔交易以后，只剩下 5 个黄球了，所以下一个黄球的价值为 5 （也就是球的价值随着顾客购买同色球是递减的） 给你整数数组 inventory ，其中 inventory[i] 表示第 i 种颜色球一开始的数目。同时给你整数 orders ，表示顾客总共想买的球数目。你可以按照 任意顺序 卖球。 请你返回卖了 orders 个球以后 最大 总价值之和。由于答案可能会很大，请你返回答案对 109 + 7 取余数 的结果。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/08/jj.gif] 输入：inventory = [2,5], orders = 4 输出：14 解释：卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。 最大总和为 2 + 5 + 4 + 3 = 14 。 示例 2： 输入：inventory = [3,5], orders = 6 输出：19 解释：卖 2 个第一种颜色的球（价值为 3 + 2），卖 4 个第二种颜色的球（价值为 5 + 4 + 3 + 2）。 最大总和为 3 + 2 + 5 + 4 + 3 + 2 = 19 。 示例 3： 输入：inventory = [2,8,4,10,6], orders = 20 输出：110 示例 4： 输入：inventory = [1000000000], orders = 1000000000 输出：21 解释：卖 1000000000 次第一种颜色的球，总价值为 500000000500000000 。 500000000500000000 对 109 + 7 取余为 21 。 提示： * 1 <= inventory.length <= 105 * 1 <= inventory[i] <= 109 * 1 <= orders <= min(sum(inventory[i]), 109)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和二分查找来最大化总价值。

算法步骤:
1. 将库存中的球按数量从大到小排序。
2. 使用二分查找确定可以卖出的最大球数，并计算总价值。
3. 逐步减少库存中的球数，直到满足订单要求。

关键点:
- 通过二分查找确定可以卖出的最大球数。
- 计算每次卖出球的总价值，并使用模运算防止溢出。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 inventory 的长度。排序操作的时间复杂度为 O(n log n)，二分查找和遍历的时间复杂度为 O(n)。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_profit(inventory: List[int], orders: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    MOD = 10**9 + 7
    inventory.sort(reverse=True)
    inventory.append(0)  # 添加一个哨兵节点
    n = len(inventory)
    total = 0
    k = 1
    
    for i in range(n - 1):
        if inventory[i] > inventory[i + 1]:
            diff = inventory[i] - inventory[i + 1]
            if k * diff < orders:
                total += (inventory[i] + inventory[i + 1] + 1) * diff // 2 * k
                orders -= k * diff
            else:
                q, r = divmod(orders, k)
                total += (inventory[i] + inventory[i] - q + 1) * q // 2 * k
                total += (inventory[i] - q) * r
                return total % MOD
        k += 1
    return total % MOD


Solution = create_solution(max_profit)