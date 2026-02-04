# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000293
标题: 最近的请求次数
难度: easy
链接: https://leetcode.cn/problems/H8086Q/
题目类型: 设计、队列、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 042. 最近的请求次数 - 写一个 RecentCounter 类来计算特定时间范围内最近的请求。 请实现 RecentCounter 类： * RecentCounter() 初始化计数器，请求数为 0 。 * int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。 保证 每次对 ping 的调用都使用比之前更大的 t 值。 示例： 输入： inputs = ["RecentCounter", "ping", "ping", "ping", "ping"] inputs = [[], [1], [100], [3001], [3002]] 输出： [null, 1, 2, 3, 3] 解释： RecentCounter recentCounter = new RecentCounter(); recentCounter.ping(1); // requests = [1]，范围是 [-2999,1]，返回 1 recentCounter.ping(100); // requests = [1, 100]，范围是 [-2900,100]，返回 2 recentCounter.ping(3001); // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3 recentCounter.ping(3002); // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3 提示： * 1 <= t <= 109 * 保证每次对 ping 调用所使用的 t 值都 严格递增 * 至多调用 ping 方法 104 次 注意：本题与主站 933 题相同： https://leetcode.cn/problems/number-of-recent-calls/ [https://leetcode.cn/problems/number-of-recent-calls/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个队列来存储所有的请求时间，并在每次调用 ping 时移除不在 [t-3000, t] 范围内的请求。

算法步骤:
1. 初始化一个空队列。
2. 每次调用 ping 时，将当前时间 t 加入队列。
3. 移除队列中所有小于 t-3000 的请求。
4. 返回队列的长度，即为 [t-3000, t] 范围内的请求数。

关键点:
- 使用队列来存储请求时间，确保每次操作的时间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次 ping 操作的时间复杂度为 O(1)，因为每个元素最多只会被加入和移除一次。
空间复杂度: O(W) - 其中 W 是窗口大小 3000，队列中最多存储 3000 个请求。
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import deque


class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # 将当前时间 t 加入队列
        self.requests.append(t)
        
        # 移除队列中所有小于 t-3000 的请求
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # 返回队列的长度
        return len(self.requests)


# 工厂函数
def create_recent_counter():
    return RecentCounter()


# 示例测试
if __name__ == "__main__":
    recent_counter = create_recent_counter()
    print(recent_counter.ping(1))    # 输出: 1
    print(recent_counter.ping(100))  # 输出: 2
    print(recent_counter.ping(3001)) # 输出: 3
    print(recent_counter.ping(3002)) # 输出: 3