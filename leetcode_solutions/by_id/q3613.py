# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3613
标题: Maximize Amount After Two Days of Conversions
难度: medium
链接: https://leetcode.cn/problems/maximize-amount-after-two-days-of-conversions/
题目类型: 深度优先搜索、广度优先搜索、图、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3387. 两天自由外汇交易后的最大货币数 - 给你一个字符串 initialCurrency，表示初始货币类型，并且你一开始拥有 1.0 单位的 initialCurrency。 另给你四个数组，分别表示货币对（字符串）和汇率（实数）： * pairs1[i] = [startCurrencyi, targetCurrencyi] 表示在 第 1 天，可以按照汇率 rates1[i] 将 startCurrencyi 转换为 targetCurrencyi。 * pairs2[i] = [startCurrencyi, targetCurrencyi] 表示在 第 2 天，可以按照汇率 rates2[i] 将 startCurrencyi 转换为 targetCurrencyi。 * 此外，每种 targetCurrency 都可以以汇率 1 / rate 转换回对应的 startCurrency。 你可以在 第 1 天 使用 rates1 进行任意次数的兑换（包括 0 次），然后在 第 2 天 使用 rates2 再进行任意次数的兑换（包括 0 次）。 返回在两天兑换后，最大可能拥有的 initialCurrency 的数量。 注意：汇率是有效的，并且第 1 天和第 2 天的汇率之间相互独立，不会产生矛盾。 示例 1： 输入： initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0] 输出： 720.00000 解释： 根据题目要求，需要最大化最终的 EUR 数量，从 1.0 EUR 开始： * 第 1 天： * 将 EUR 换成 USD，得到 2.0 USD。 * 将 USD 换成 JPY，得到 6.0 JPY。 * 第 2 天： * 将 JPY 换成 USD，得到 24.0 USD。 * 将 USD 换成 CHF，得到 120.0 CHF。 * 最后将 CHF 换回 EUR，得到 720.0 EUR。 示例 2： 输入： initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0] 输出： 1.50000 解释： 在第 1 天将 NGN 换成 EUR，并在第 2 天用反向汇率将 EUR 换回 NGN，可以最大化最终的 NGN 数量。 示例 3： 输入： initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0] 输出： 1.00000 解释： 在这个例子中，不需要在任何一天进行任何兑换。 提示： * 1 <= initialCurrency.length <= 3 * initialCurrency 仅由大写英文字母组成。 * 1 <= n == pairs1.length <= 10 * 1 <= m == pairs2.length <= 10 * pairs1[i] == [startCurrencyi, targetCurrencyi] * pairs2[i] == [startCurrencyi, targetCurrencyi] * 1 <= startCurrencyi.length, targetCurrencyi.length <= 3 * startCurrencyi 和 targetCurrencyi 仅由大写英文字母组成。 * rates1.length == n * rates2.length == m * 1.0 <= rates1[i], rates2[i] <= 10.0 * 输入保证两个转换图在各自的天数中没有矛盾或循环。 * 输入保证输出 最大 为 5 * 1010。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Floyd-Warshall 算法计算所有货币之间的最短路径，从而找到两天内最优的兑换路径。

算法步骤:
1. 构建第 1 天和第 2 天的汇率图。
2. 使用 Floyd-Warshall 算法计算第 1 天和第 2 天的所有货币之间的最短路径。
3. 计算从初始货币经过两天兑换后的最大值。

关键点:
- 使用 Floyd-Warshall 算法处理多对多的货币兑换问题。
- 通过两次应用 Floyd-Warshall 算法，分别计算第 1 天和第 2 天的最优兑换路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3 + m^3)，其中 n 是 pairs1 的长度，m 是 pairs2 的长度。
空间复杂度: O(n^2 + m^2)，用于存储汇率图。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import collections
import math

def floyd_warshall(graph):
    currencies = list(graph.keys())
    n = len(currencies)
    dist = [[-math.inf] * n for _ in range(n)]
    
    for i, cur in enumerate(currencies):
        dist[i][i] = 1.0
        for neighbor, rate in graph[cur].items():
            j = currencies.index(neighbor)
            dist[i][j] = rate
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] > 0 and dist[k][j] > 0:
                    dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])
    
    return dist, currencies

def maximize_amount(initial_currency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
    # 构建第 1 天和第 2 天的汇率图
    graph1 = collections.defaultdict(dict)
    graph2 = collections.defaultdict(dict)
    
    for (src, dst), rate in zip(pairs1, rates1):
        graph1[src][dst] = rate
        graph1[dst][src] = 1 / rate
    
    for (src, dst), rate in zip(pairs2, rates2):
        graph2[src][dst] = rate
        graph2[dst][src] = 1 / rate
    
    # 使用 Floyd-Warshall 算法计算第 1 天和第 2 天的所有货币之间的最短路径
    dist1, currencies1 = floyd_warshall(graph1)
    dist2, currencies2 = floyd_warshall(graph2)
    
    # 计算从初始货币经过两天兑换后的最大值
    max_amount = 0.0
    for currency in currencies1:
        if currency not in currencies2:
            continue
        i = currencies1.index(initial_currency)
        j = currencies1.index(currency)
        k = currencies2.index(currency)
        l = currencies2.index(initial_currency)
        amount = dist1[i][j] * dist2[k][l]
        max_amount = max(max_amount, amount)
    
    return max_amount

Solution = create_solution(maximize_amount)