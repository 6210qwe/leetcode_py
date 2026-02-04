# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1957
标题: Closest Room
难度: hard
链接: https://leetcode.cn/problems/closest-room/
题目类型: 数组、二分查找、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1847. 最近的房间 - 一个酒店里有 n 个房间，这些房间用二维整数数组 rooms 表示，其中 rooms[i] = [roomIdi, sizei] 表示有一个房间号为 roomIdi 的房间且它的面积为 sizei 。每一个房间号 roomIdi 保证是 独一无二 的。 同时给你 k 个查询，用二维数组 queries 表示，其中 queries[j] = [preferredj, minSizej] 。第 j 个查询的答案是满足如下条件的房间 id ： * 房间的面积 至少 为 minSizej ，且 * abs(id - preferredj) 的值 最小 ，其中 abs(x) 是 x 的绝对值。 如果差的绝对值有 相等 的，选择 最小 的 id 。如果 没有满足条件的房间 ，答案为 -1 。 请你返回长度为 k 的数组 answer ，其中 answer[j] 为第 j 个查询的结果。 示例 1： 输入：rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]] 输出：[3,-1,3] 解释：查询的答案如下： 查询 [3,1] ：房间 3 的面积为 2 ，大于等于 1 ，且号码是最接近 3 的，为 abs(3 - 3) = 0 ，所以答案为 3 。 查询 [3,3] ：没有房间的面积至少为 3 ，所以答案为 -1 。 查询 [5,2] ：房间 3 的面积为 2 ，大于等于 2 ，且号码是最接近 5 的，为 abs(3 - 5) = 2 ，所以答案为 3 。 示例 2： 输入：rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]] 输出：[2,1,3] 解释：查询的答案如下： 查询 [2,3] ：房间 2 的面积为 3 ，大于等于 3 ，且号码是最接近的，为 abs(2 - 2) = 0 ，所以答案为 2 。 查询 [2,4] ：房间 1 和 3 的面积都至少为 4 ，答案为 1 因为它房间编号更小。 查询 [2,5] ：房间 3 是唯一面积大于等于 5 的，所以答案为 3 。 提示： * n == rooms.length * 1 <= n <= 105 * k == queries.length * 1 <= k <= 104 * 1 <= roomIdi, preferredj <= 107 * 1 <= sizei, minSizej <= 107
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序集合和二分查找来高效处理查询。

算法步骤:
1. 对房间按面积从大到小排序。
2. 对查询按最小面积要求从大到小排序。
3. 使用有序集合维护当前可用的房间ID。
4. 遍历查询，对于每个查询：
   - 将所有面积大于等于当前查询最小面积要求的房间加入有序集合。
   - 使用二分查找在有序集合中找到最接近的房间ID。
   - 更新结果数组。

关键点:
- 使用有序集合可以高效地插入和查找最接近的房间ID。
- 通过排序和二分查找，可以在O(log n)时间内找到最接近的房间ID。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((n + k) log n)
- 排序操作的时间复杂度为O(n log n)。
- 每个查询的处理时间为O(log n)，总共有k个查询，因此总时间复杂度为O(k log n)。

空间复杂度: O(n)
- 有序集合的空间复杂度为O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from sortedcontainers import SortedList

def closestRoom(rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
    # 对房间按面积从大到小排序
    rooms.sort(key=lambda x: -x[1])
    
    # 对查询按最小面积要求从大到小排序，并记录原始索引
    queries = sorted(enumerate(queries), key=lambda x: -x[1][1])
    
    # 结果数组
    result = [-1] * len(queries)
    
    # 有序集合，用于存储当前可用的房间ID
    available_rooms = SortedList()
    
    # 当前处理的房间索引
    room_index = 0
    
    for original_index, (preferred, min_size) in queries:
        # 将所有面积大于等于当前查询最小面积要求的房间加入有序集合
        while room_index < len(rooms) and rooms[room_index][1] >= min_size:
            available_rooms.add(rooms[room_index][0])
            room_index += 1
        
        # 如果有序集合为空，说明没有满足条件的房间
        if not available_rooms:
            continue
        
        # 使用二分查找在有序集合中找到最接近的房间ID
        pos = available_rooms.bisect_left(preferred)
        
        # 找到最接近的房间ID
        candidates = []
        if pos > 0:
            candidates.append(available_rooms[pos - 1])
        if pos < len(available_rooms):
            candidates.append(available_rooms[pos])
        
        # 选择最接近的房间ID
        closest_room = min(candidates, key=lambda x: (abs(x - preferred), x))
        result[original_index] = closest_room
    
    return result

Solution = create_solution(closestRoom)