# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 969
标题: Number of Recent Calls
难度: easy
链接: https://leetcode.cn/problems/number-of-recent-calls/
题目类型: 设计、队列、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
933. 最近的请求次数 - 写一个 RecentCounter 类来计算特定时间范围内最近的请求。 请你实现 RecentCounter 类： * RecentCounter() 初始化计数器，请求数为 0 。 * int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。 保证 每次对 ping 的调用都使用比之前更大的 t 值。 示例 1： 输入： ["RecentCounter", "ping", "ping", "ping", "ping"] [[], [1], [100], [3001], [3002]] 输出： [null, 1, 2, 3, 3] 解释： RecentCounter recentCounter = new RecentCounter(); recentCounter.ping(1); // requests = [1]，范围是 [-2999,1]，返回 1 recentCounter.ping(100); // requests = [1, 100]，范围是 [-2900,100]，返回 2 recentCounter.ping(3001); // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3 recentCounter.ping(3002); // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3 提示： * 1 <= t <= 109 * 保证每次对 ping 调用所使用的 t 值都 严格递增 * 至多调用 ping 方法 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个队列来存储所有的请求时间，并在每次 ping 时移除不在 [t-3000, t] 范围内的请求。

算法步骤:
1. 初始化一个空队列。
2. 在每次 ping 时，将新的请求时间 t 加入队列。
3. 移除队列中所有不在 [t-3000, t] 范围内的请求。
4. 返回队列的长度，即为过去 3000 毫秒内的请求数。

关键点:
- 使用队列来存储请求时间，确保队列中的时间都是最近 3000 毫秒内的。
- 每次 ping 时，移除队列头部不在 [t-3000, t] 范围内的请求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是队列的长度。最坏情况下，每次 ping 都需要遍历整个队列。
空间复杂度: O(w)，其中 w 是窗口大小（3000 毫秒），队列中最多存储 3000 毫秒内的请求。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # 移除不在 [t-3000, t] 范围内的请求
        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)


Solution = create_solution(RecentCounter)