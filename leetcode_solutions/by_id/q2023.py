# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2023
标题: Design Movie Rental System
难度: hard
链接: https://leetcode.cn/problems/design-movie-rental-system/
题目类型: 设计、数组、哈希表、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1912. 设计电影租借系统 - 你有一个电影租借公司和 n 个电影商店。你想要实现一个电影租借系统，它支持查询、预订和返还电影的操作。同时系统还能生成一份当前被借出电影的报告。 所有电影用二维整数数组 entries 表示，其中 entries[i] = [shopi, moviei, pricei] 表示商店 shopi 有一份电影 moviei 的拷贝，租借价格为 pricei 。每个商店有 至多一份 编号为 moviei 的电影拷贝。 系统需要支持以下操作： * Search：找到拥有指定电影且 未借出 的商店中 最便宜的 5 个 。商店需要按照 价格 升序排序，如果价格相同，则 shopi 较小 的商店排在前面。如果查询结果少于 5 个商店，则将它们全部返回。如果查询结果没有任何商店，则返回空列表。 * Rent：从指定商店借出指定电影，题目保证指定电影在指定商店 未借出 。 * Drop：在指定商店返还 之前已借出 的指定电影。 * Report：返回 最便宜的 5 部已借出电影 （可能有重复的电影 ID），将结果用二维列表 res 返回，其中 res[j] = [shopj, moviej] 表示第 j 便宜的已借出电影是从商店 shopj 借出的电影 moviej 。res 中的电影需要按 价格 升序排序；如果价格相同，则 shopj 较小 的排在前面；如果仍然相同，则 moviej 较小 的排在前面。如果当前借出的电影小于 5 部，则将它们全部返回。如果当前没有借出电影，则返回一个空的列表。 请你实现 MovieRentingSystem 类： * MovieRentingSystem(int n, int[][] entries) 将 MovieRentingSystem 对象用 n 个商店和 entries 表示的电影列表初始化。 * List<Integer> search(int movie) 如上所述，返回 未借出 指定 movie 的商店列表。 * void rent(int shop, int movie) 从指定商店 shop 借出指定电影 movie 。 * void drop(int shop, int movie) 在指定商店 shop 返还之前借出的电影 movie 。 * List<List<Integer>> report() 如上所述，返回最便宜的 已借出 电影列表。 注意：测试数据保证 rent 操作中指定商店拥有 未借出 的指定电影，且 drop 操作指定的商店 之前已借出 指定电影。 示例 1： 输入： ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"] [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]] 输出： [null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]] 解释： MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]); movieRentingSystem.search(1); // 返回 [1, 0, 2] ，商店 1，0 和 2 有未借出的 ID 为 1 的电影。商店 1 最便宜，商店 0 和 2 价格相同，所以按商店编号排序。 movieRentingSystem.rent(0, 1); // 从商店 0 借出电影 1 。现在商店 0 未借出电影编号为 [2,3] 。 movieRentingSystem.rent(1, 2); // 从商店 1 借出电影 2 。现在商店 1 未借出的电影编号为 [1] 。 movieRentingSystem.report(); // 返回 [[0, 1], [1, 2]] 。商店 0 借出的电影 1 最便宜，然后是商店 1 借出的电影 2 。 movieRentingSystem.drop(1, 2); // 在商店 1 返还电影 2 。现在商店 1 未借出的电影编号为 [1,2] 。 movieRentingSystem.search(2); // 返回 [0, 1] 。商店 0 和 1 有未借出的 ID 为 2 的电影。商店 0 最便宜，然后是商店 1 。 提示： * 1 <= n <= 3 * 105 * 1 <= entries.length <= 105 * 0 <= shopi < n * 1 <= moviei, pricei <= 104 * 每个商店 至多 有一份电影 moviei 的拷贝。 * search，rent，drop 和 report 的调用 总共 不超过 105 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用字典和有序集合来高效地管理和查询电影和商店信息。
- 使用两个有序集合分别存储未借出和已借出的电影信息。

算法步骤:
1. 初始化时，构建未借出电影的有序集合和已借出电影的有序集合。
2. `search` 方法通过有序集合快速找到未借出的电影，并返回前 5 个最便宜的商店。
3. `rent` 方法从未借出集合中移除并添加到已借出集合。
4. `drop` 方法从已借出集合中移除并添加到未借出集合。
5. `report` 方法通过已借出集合快速找到最便宜的 5 部已借出电影。

关键点:
- 使用有序集合（SortedSet）来保持电影和商店的有序性。
- 通过字典来快速查找电影和商店的信息。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- 初始化: O(E log E)，其中 E 是 entries 的长度。
- search: O(log S + min(5, S))，其中 S 是未借出该电影的商店数量。
- rent: O(log S)
- drop: O(log S)
- report: O(log R + min(5, R))，其中 R 是已借出的电影数量。

空间复杂度: 
- O(E + R)，其中 E 是 entries 的长度，R 是已借出的电影数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import sortedcontainers

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = {}  # {movie: SortedSet((price, shop))}
        self.shops = {}  # {shop: {movie: price}}
        self.rented = sortedcontainers.SortedSet()  # SortedSet((price, shop, movie))
        
        for shop, movie, price in entries:
            if movie not in self.movies:
                self.movies[movie] = sortedcontainers.SortedSet()
            self.movies[movie].add((price, shop))
            if shop not in self.shops:
                self.shops[shop] = {}
            self.shops[shop][movie] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies:
            return []
        result = []
        for price, shop in self.movies[movie]:
            if (price, shop, movie) not in self.rented:
                result.append(shop)
                if len(result) == 5:
                    break
        return result

    def rent(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.movies[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.rented.remove((price, shop, movie))
        self.movies[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        result = []
        for price, shop, movie in self.rented:
            result.append([shop, movie])
            if len(result) == 5:
                break
        return result


# 测试用例
if __name__ == "__main__":
    obj = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
    print(obj.search(1))  # [1, 0, 2]
    obj.rent(0, 1)
    obj.rent(1, 2)
    print(obj.report())  # [[0, 1], [1, 2]]
    obj.drop(1, 2)
    print(obj.search(2))  # [0, 1]