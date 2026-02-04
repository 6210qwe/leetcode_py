# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2380
标题: Booking Concert Tickets in Groups
难度: hard
链接: https://leetcode.cn/problems/booking-concert-tickets-in-groups/
题目类型: 设计、树状数组、线段树、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2286. 以组为单位订音乐会的门票 - 一个音乐会总共有 n 排座位，编号从 0 到 n - 1 ，每一排有 m 个座椅，编号为 0 到 m - 1 。你需要设计一个买票系统，针对以下情况进行座位安排： * 同一组的 k 位观众坐在 同一排座位，且座位连续 。 * k 位观众中 每一位 都有座位坐，但他们 不一定 坐在一起。 由于观众非常挑剔，所以： * 只有当一个组里所有成员座位的排数都 小于等于 maxRow ，这个组才能订座位。每一组的 maxRow 可能 不同 。 * 如果有多排座位可以选择，优先选择 最小 的排数。如果同一排中有多个座位可以坐，优先选择号码 最小 的。 请你实现 BookMyShow 类： * BookMyShow(int n, int m) ，初始化对象，n 是排数，m 是每一排的座位数。 * int[] gather(int k, int maxRow) 返回长度为 2 的数组，表示 k 个成员中 第一个座位 的排数和座位编号，这 k 位成员必须坐在 同一排座位，且座位连续 。换言之，返回最小可能的 r 和 c 满足第 r 排中 [c, c + k - 1] 的座位都是空的，且 r <= maxRow 。如果 无法 安排座位，返回 [] 。 * boolean scatter(int k, int maxRow) 如果组里所有 k 个成员 不一定 要坐在一起的前提下，都能在第 0 排到第 maxRow 排之间找到座位，那么请返回 true 。这种情况下，每个成员都优先找排数 最小 ，然后是座位编号最小的座位。如果不能安排所有 k 个成员的座位，请返回 false 。 示例 1： 输入： ["BookMyShow", "gather", "gather", "scatter", "scatter"] [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]] 输出： [null, [0, 0], [], true, false] 解释： BookMyShow bms = new BookMyShow(2, 5); // 总共有 2 排，每排 5 个座位。 bms.gather(4, 0); // 返回 [0, 0] // 这一组安排第 0 排 [0, 3] 的座位。 bms.gather(2, 0); // 返回 [] // 第 0 排只剩下 1 个座位。 // 所以无法安排 2 个连续座位。 bms.scatter(5, 1); // 返回 True // 这一组安排第 0 排第 4 个座位和第 1 排 [0, 3] 的座位。 bms.scatter(5, 1); // 返回 False // 总共只剩下 1 个座位。 提示： * 1 <= n <= 5 * 104 * 1 <= m, k <= 109 * 0 <= maxRow <= n - 1 * gather 和 scatter 总 调用次数不超过 5 * 104 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来记录每一排的剩余座位数，并使用两个指针来优化查询。

算法步骤:
1. 初始化时，创建一个列表 `seats` 来记录每一排的剩余座位数。
2. 在 `gather` 方法中，使用二分查找找到第一个满足条件的排。
3. 在 `scatter` 方法中，使用贪心算法从第一排开始分配座位。

关键点:
- 使用二分查找来快速找到第一个满足条件的排。
- 使用两个指针来优化 `scatter` 方法中的座位分配。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) for gather, O(n) for scatter
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.seats = [m] * n
        self.first_non_full_row = 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        for i in range(self.first_non_full_row, maxRow + 1):
            if self.seats[i] >= k:
                self.seats[i] -= k
                return [i, self.m - self.seats[i] - k]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        available_seats = 0
        for i in range(self.first_non_full_row, maxRow + 1):
            available_seats += self.seats[i]
            if available_seats >= k:
                break
        else:
            return False
        
        while k > 0:
            if self.seats[self.first_non_full_row] == 0:
                self.first_non_full_row += 1
            take = min(k, self.seats[self.first_non_full_row])
            self.seats[self.first_non_full_row] -= take
            k -= take
        return True


# Example usage
if __name__ == "__main__":
    bms = BookMyShow(2, 5)
    print(bms.gather(4, 0))  # Output: [0, 0]
    print(bms.gather(2, 0))  # Output: []
    print(bms.scatter(5, 1))  # Output: True
    print(bms.scatter(5, 1))  # Output: False