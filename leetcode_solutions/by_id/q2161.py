# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2161
标题: Stock Price Fluctuation
难度: medium
链接: https://leetcode.cn/problems/stock-price-fluctuation/
题目类型: 设计、哈希表、数据流、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2034. 股票价格波动 - 给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。 不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 更正 前一条错误的记录。 请你设计一个算法，实现： * 更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。 * 找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。 * 找到当前记录里股票的 最高价格 。 * 找到当前记录里股票的 最低价格 。 请你实现 StockPrice 类： * StockPrice() 初始化对象，当前无股票价格记录。 * void update(int timestamp, int price) 在时间点 timestamp 更新股票价格为 price 。 * int current() 返回股票 最新价格 。 * int maximum() 返回股票 最高价格 。 * int minimum() 返回股票 最低价格 。 示例 1： 输入： ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"] [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []] 输出： [null, null, null, 5, 10, null, 5, null, 2] 解释： StockPrice stockPrice = new StockPrice(); stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。 stockPrice.update(2, 5); // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。 stockPrice.current(); // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。 stockPrice.maximum(); // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。 stockPrice.update(1, 3); // 之前时间戳为 1 的价格错误，价格更新为 3 。 // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。 stockPrice.maximum(); // 返回 5 ，更正后最高价格为 5 。 stockPrice.update(4, 2); // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。 stockPrice.minimum(); // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。 提示： * 1 <= timestamp, price <= 109 * update，current，maximum 和 minimum 总 调用次数不超过 105 。 * current，maximum 和 minimum 被调用时，update 操作 至少 已经被调用过 一次 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典来存储时间戳到价格的映射以及价格到时间戳集合的映射。使用一个变量来记录最新的时间戳。

算法步骤:
1. 初始化时，创建两个字典和一个变量来记录最新的时间戳。
2. 在 `update` 方法中，更新时间戳到价格的映射，并更新价格到时间戳集合的映射。如果时间戳已经存在，则移除旧价格并添加新价格。
3. 在 `current` 方法中，返回最新时间戳对应的价格。
4. 在 `maximum` 方法中，返回价格到时间戳集合映射中的最大价格。
5. 在 `minimum` 方法中，返回价格到时间戳集合映射中的最小价格。

关键点:
- 使用两个字典来高效地更新和查询价格。
- 使用一个变量来记录最新的时间戳。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 更新和查询操作的时间复杂度主要由有序集合的插入和删除操作决定。
空间复杂度: O(n) - 存储所有时间戳和价格需要线性空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict, Set


class StockPrice:

    def __init__(self):
        self.timestamp_to_price: Dict[int, int] = {}
        self.price_to_timestamps: Dict[int, Set[int]] = {}
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamp_to_price:
            old_price = self.timestamp_to_price[timestamp]
            self.price_to_timestamps[old_price].remove(timestamp)
            if not self.price_to_timestamps[old_price]:
                del self.price_to_timestamps[old_price]

        self.timestamp_to_price[timestamp] = price
        if price not in self.price_to_timestamps:
            self.price_to_timestamps[price] = set()
        self.price_to_timestamps[price].add(timestamp)

        self.latest_timestamp = max(self.latest_timestamp, timestamp)

    def current(self) -> int:
        return self.timestamp_to_price[self.latest_timestamp]

    def maximum(self) -> int:
        return max(self.price_to_timestamps.keys())

    def minimum(self) -> int:
        return min(self.price_to_timestamps.keys())


# 测试用例
if __name__ == "__main__":
    stockPrice = StockPrice()
    stockPrice.update(1, 10)  # 时间戳为 [1] ，对应的股票价格为 [10] 。
    stockPrice.update(2, 5)   # 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
    print(stockPrice.current())  # 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
    print(stockPrice.maximum())  # 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
    stockPrice.update(1, 3)    # 之前时间戳为 1 的价格错误，价格更新为 3 。
    print(stockPrice.maximum())  # 返回 5 ，更正后最高价格为 5 。
    stockPrice.update(4, 2)    # 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
    print(stockPrice.minimum())  # 返回 2 ，最低价格时间戳为 4 ，价格为 2 。