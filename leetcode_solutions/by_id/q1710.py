# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1710
标题: Find Servers That Handled Most Number of Requests
难度: hard
链接: https://leetcode.cn/problems/find-servers-that-handled-most-number-of-requests/
题目类型: 数组、有序集合、模拟、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1606. 找到处理最多请求的服务器 - 你有 k 个服务器，编号为 0 到 k-1 ，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 不能同时处理超过一个请求 。请求分配到服务器的规则如下： * 第 i （序号从 0 开始）个请求到达。 * 如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。 * 如果第 (i % k) 个服务器空闲，那么对应服务器会处理该请求。 * 否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。比方说，如果第 i 个服务器在忙，那么会查看第 (i+1) 个服务器，第 (i+2) 个服务器等等。 给你一个 严格递增 的正整数数组 arrival ，表示第 i 个任务的到达时间，和另一个数组 load ，其中 load[i] 表示第 i 个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是找到 最繁忙的服务器 。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。 请你返回包含所有 最繁忙服务器 序号的列表，你可以以任意顺序返回这个列表。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/10/03/load-1.png] 输入：k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 输出：[1] 解释： 所有服务器一开始都是空闲的。 前 3 个请求分别由前 3 台服务器依次处理。 请求 3 进来的时候，服务器 0 被占据，所以它被安排到下一台空闲的服务器，也就是服务器 1 。 请求 4 进来的时候，由于所有服务器都被占据，该请求被舍弃。 服务器 0 和 2 分别都处理了一个请求，服务器 1 处理了两个请求。所以服务器 1 是最忙的服务器。 示例 2： 输入：k = 3, arrival = [1,2,3,4], load = [1,2,1,2] 输出：[0] 解释： 前 3 个请求分别被前 3 个服务器处理。 请求 3 进来，由于服务器 0 空闲，它被服务器 0 处理。 服务器 0 处理了两个请求，服务器 1 和 2 分别处理了一个请求。所以服务器 0 是最忙的服务器。 示例 3： 输入：k = 3, arrival = [1,2,3], load = [10,12,11] 输出：[0,1,2] 解释：每个服务器分别处理了一个请求，所以它们都是最忙的服务器。 示例 4： 输入：k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2] 输出：[1] 示例 5： 输入：k = 1, arrival = [1], load = [1] 输出：[0] 提示： * 1 <= k <= 105 * 1 <= arrival.length, load.length <= 105 * arrival.length == load.length * 1 <= arrival[i], load[i] <= 109 * arrival 保证 严格递增 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序集合和最小堆来管理空闲服务器和忙碌服务器。

算法步骤:
1. 初始化一个有序集合 `free_servers` 来存储当前空闲的服务器。
2. 初始化一个最小堆 `busy_servers` 来存储正在处理请求的服务器及其结束时间。
3. 遍历每个请求：
   - 从 `busy_servers` 中移除所有已经完成处理的服务器，并将其添加回 `free_servers`。
   - 如果 `free_servers` 为空，跳过当前请求。
   - 否则，从 `free_servers` 中选择一个服务器来处理当前请求，并将其从 `free_servers` 中移除，然后将其添加到 `busy_servers` 中。
4. 记录每个服务器处理的请求数。
5. 找出处理请求数最多的服务器并返回。

关键点:
- 使用有序集合来快速找到下一个空闲服务器。
- 使用最小堆来管理忙碌服务器及其结束时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k)，其中 n 是请求的数量，k 是服务器的数量。每个请求的处理时间复杂度为 O(log k)。
空间复杂度: O(k)，用于存储空闲服务器和忙碌服务器的信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq
from sortedcontainers import SortedSet

def busiest_servers(k: int, arrival: List[int], load: List[int]) -> List[int]:
    free_servers = SortedSet(range(k))
    busy_servers = []
    request_count = [0] * k
    
    for i, (start, duration) in enumerate(zip(arrival, load)):
        # 释放已完成处理的服务器
        while busy_servers and busy_servers[0][0] <= start:
            _, server_id = heapq.heappop(busy_servers)
            free_servers.add(server_id)
        
        if not free_servers:
            continue
        
        # 选择下一个空闲服务器
        server_id = free_servers.bisect_left(i % k) % len(free_servers)
        server_id = free_servers[server_id]
        free_servers.remove(server_id)
        
        # 将服务器标记为忙碌
        end_time = start + duration
        heapq.heappush(busy_servers, (end_time, server_id))
        
        # 记录请求处理次数
        request_count[server_id] += 1
    
    max_requests = max(request_count)
    return [i for i, count in enumerate(request_count) if count == max_requests]

Solution = create_solution(busiest_servers)