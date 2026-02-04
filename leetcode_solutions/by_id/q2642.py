# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2642
标题: Time to Cross a Bridge
难度: hard
链接: https://leetcode.cn/problems/time-to-cross-a-bridge/
题目类型: 数组、模拟、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2532. 过桥的时间 - 共有 k 位工人计划将 n 个箱子从右侧的（旧）仓库移动到左侧的（新）仓库。给你两个整数 n 和 k，以及一个二维整数数组 time ，数组的大小为 k x 4 ，其中 time[i] = [righti, picki, lefti, puti] 。 一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 k 位工人都在桥的左侧等待。为了移动这些箱子，第 i 位工人（下标从 0 开始）可以： * 从左岸（新仓库）跨过桥到右岸（旧仓库），用时 righti 分钟。 * 从旧仓库选择一个箱子，并返回到桥边，用时 picki 分钟。不同工人可以同时搬起所选的箱子。 * 从右岸（旧仓库）跨过桥到左岸（新仓库），用时 lefti 分钟。 * 将箱子放入新仓库，并返回到桥边，用时 puti 分钟。不同工人可以同时放下所选的箱子。 如果满足下面任一条件，则认为工人 i 的 效率低于 工人 j ： * lefti + righti > leftj + rightj * lefti + righti == leftj + rightj 且 i > j 工人通过桥时需要遵循以下规则： * 同时只能有一名工人过桥。 * 当桥梁未被使用时，优先让右侧 效率最低 的工人（已经拿起盒子的工人）过桥。如果不是，优先让左侧 效率最低 的工人通过。 * 如果左侧已经派出足够的工人来拾取所有剩余的箱子，则 不会 再从左侧派出工人。 请你返回最后一个箱子 到达桥左侧 的时间。 示例 1： 输入：n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]] 输出：6 解释： 从 0 到 1 分钟：工人 2 通过桥到达右侧。 从 1 到 2 分钟：工人 2 从右侧仓库拿起箱子。 从 2 到 6 分钟：工人 2 通过桥到达左侧。 从 6 到 7 分钟：工人 2 向左侧仓库放下箱子。 整个过程在 7 分钟后结束。我们返回 6 因为该问题要求的是最后一名工人到达桥梁左侧的时间。 示例 2： 输入：n = 3, k = 2, time = [[1,5,1,8],[10,10,10,10]] 输出：37 解释： [https://assets.leetcode.com/uploads/2024/11/21/378539249-c6ce3c73-40e7-4670-a8b5-7ddb9abede11.png] 最后一个盒子在37秒时到达左侧。请注意，我们并 没有 放下最后一个箱子，因为那样会花费更多时间，而且它们已经和工人们一起在左边。 提示： * 1 <= n, k <= 104 * time.length == k * time[i].length == 4 * 1 <= lefti, picki, righti, puti <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用优先队列（堆）来管理工人和箱子的状态，确保每次过桥的工人是最优选择。

算法步骤:
1. 初始化四个优先队列：left_queue, right_queue, picking_queue, putting_queue。
2. 将所有工人放入 left_queue，按效率排序。
3. 使用一个时间戳变量 current_time 来跟踪当前时间。
4. 在箱子数量 n 大于 0 或者还有工人在右边时，进行以下操作：
   - 从 right_queue 中取出效率最低的工人，如果该工人已经完成捡箱子任务，则将其加入 putting_queue。
   - 从 left_queue 中取出效率最低的工人，如果需要更多的工人去捡箱子，则将其加入 picking_queue。
   - 从 picking_queue 中取出效率最低的工人，更新时间并将其加入 right_queue。
   - 从 putting_queue 中取出效率最低的工人，更新时间并将其加入 left_queue。
5. 返回当前时间减去最后一个工人过桥的时间。

关键点:
- 使用优先队列确保每次过桥的工人是最优选择。
- 通过维护多个队列来跟踪工人的状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n + k) log k)
空间复杂度: O(k)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def find_crossing_time(n: int, k: int, time: List[List[int]]) -> int:
    """
    函数式接口 - 计算最后一个箱子到达桥左侧的时间
    """
    # 定义优先队列
    left_queue = []
    right_queue = []
    picking_queue = []
    putting_queue = []

    # 初始化 left_queue
    for i in range(k):
        heapq.heappush(left_queue, (time[i][0] + time[i][2], i))

    current_time = 0

    while n > 0 or right_queue or picking_queue:
        # 从 right_queue 中取出效率最低的工人
        while right_queue and right_queue[0][0] <= current_time:
            _, worker_id = heapq.heappop(right_queue)
            heapq.heappush(putting_queue, (time[worker_id][3], worker_id))

        # 从 left_queue 中取出效率最低的工人
        while left_queue and (n > 0 or picking_queue):
            _, worker_id = heapq.heappop(left_queue)
            if n > 0:
                n -= 1
                heapq.heappush(picking_queue, (current_time + time[worker_id][1], worker_id))
            else:
                heapq.heappush(left_queue, (time[worker_id][0] + time[worker_id][2], worker_id))
                break

        # 从 picking_queue 中取出效率最低的工人
        if picking_queue:
            next_time, worker_id = heapq.heappop(picking_queue)
            current_time = max(current_time, next_time)
            heapq.heappush(right_queue, (current_time + time[worker_id][2], worker_id))

        # 从 putting_queue 中取出效率最低的工人
        elif putting_queue:
            next_time, worker_id = heapq.heappop(putting_queue)
            current_time = max(current_time, next_time)
            heapq.heappush(left_queue, (time[worker_id][0] + time[worker_id][2], worker_id))

        # 更新时间
        if not right_queue and not picking_queue:
            if left_queue:
                current_time = min(current_time, left_queue[0][0])
            if putting_queue:
                current_time = min(current_time, putting_queue[0][0])

    return current_time

Solution = create_solution(find_crossing_time)