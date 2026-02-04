# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2833
标题: Count Zero Request Servers
难度: medium
链接: https://leetcode.cn/problems/count-zero-request-servers/
题目类型: 数组、哈希表、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2747. 统计没有收到请求的服务器数目 - 给你一个整数 n ，表示服务器的总数目，再给你一个下标从 0 开始的 二维 整数数组 logs ，其中 logs[i] = [server_id, time] 表示 id 为 server_id 的服务器在 time 时收到了一个请求。 同时给你一个整数 x 和一个下标从 0 开始的整数数组 queries 。 请你返回一个长度等于 queries.length 的数组 arr ，其中 arr[i] 表示在时间区间 [queries[i] - x, queries[i]] 内没有收到请求的服务器数目。 注意时间区间是个闭区间。 示例 1： 输入：n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11] 输出：[1,2] 解释： 对于 queries[0]：id 为 1 和 2 的服务器在区间 [5, 10] 内收到了请求，所以只有服务器 3 没有收到请求。 对于 queries[1]：id 为 2 的服务器在区间 [6,11] 内收到了请求，所以 id 为 1 和 3 的服务器在这个时间段内没有收到请求。 示例 2： 输入：n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4] 输出：[0,1] 解释： 对于 queries[0]：区间 [1, 3] 内所有服务器都收到了请求。 对于 queries[1]：只有 id 为 3 的服务器在区间 [2,4] 内没有收到请求。 提示： * 1 <= n <= 105 * 1 <= logs.length <= 105 * 1 <= queries.length <= 105 * logs[i].length == 2 * 1 <= logs[i][0] <= n * 1 <= logs[i][1] <= 106 * 1 <= x <= 105 * x < queries[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和哈希表来统计每个查询区间内的活跃服务器，并计算没有收到请求的服务器数目。

算法步骤:
1. 将 logs 按照时间进行排序。
2. 将 queries 与它们的索引一起排序，以便处理完后可以恢复到原始顺序。
3. 使用两个指针来维护一个滑动窗口，窗口内的 logs 是在当前查询区间内的。
4. 使用哈希表记录当前窗口内的活跃服务器。
5. 对于每个查询，计算不在哈希表中的服务器数目。

关键点:
- 使用滑动窗口来高效地维护当前查询区间内的活跃服务器。
- 使用哈希表来快速查找活跃服务器。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((m + n) log m)，其中 m 是 logs 的长度，n 是 queries 的长度。排序操作的时间复杂度是 O(m log m) 和 O(n log n)，滑动窗口的时间复杂度是 O(m + n)。
空间复杂度: O(m + n)，用于存储排序后的 logs 和 queries，以及哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_zero_request_servers(n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
    """
    函数式接口 - 统计没有收到请求的服务器数目
    """
    # 将 logs 按照时间进行排序
    logs.sort(key=lambda log: log[1])
    
    # 将 queries 与它们的索引一起排序
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
    
    # 初始化结果数组
    result = [0] * len(queries)
    
    # 使用哈希表记录当前窗口内的活跃服务器
    active_servers = {}
    
    # 使用两个指针来维护滑动窗口
    left, right = 0, 0
    
    for i, query in sorted_queries:
        # 移动右指针，将符合条件的 logs 加入窗口
        while right < len(logs) and logs[right][1] <= query:
            server_id = logs[right][0]
            if server_id not in active_servers:
                active_servers[server_id] = 0
            active_servers[server_id] += 1
            right += 1
        
        # 移动左指针，移除不符合条件的 logs
        while left < right and logs[left][1] < query - x:
            server_id = logs[left][0]
            active_servers[server_id] -= 1
            if active_servers[server_id] == 0:
                del active_servers[server_id]
            left += 1
        
        # 计算没有收到请求的服务器数目
        result[i] = n - len(active_servers)
    
    return result


Solution = create_solution(count_zero_request_servers)