# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1436
标题: Get Watched Videos by Your Friends
难度: medium
链接: https://leetcode.cn/problems/get-watched-videos-by-your-friends/
题目类型: 广度优先搜索、图、数组、哈希表、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1311. 获取你好友已观看的视频 - 有 n 个人，每个人都有一个 0 到 n-1 的唯一 id 。 给你数组 watchedVideos 和 friends ，其中 watchedVideos[i] 和 friends[i] 分别表示 id = i 的人观看过的视频列表和他的好友列表。 Level 1 的视频包含所有你好友观看过的视频，level 2 的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 k 的视频包含所有从你出发，最短距离为 k 的好友观看过的视频。 给定你的 id 和一个 level 值，请你找出所有指定 level 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_1.png] 输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1 输出：["B","C"] 解释： 你的 id 为 0（绿色），你的朋友包括（黄色）： id 为 1 -> watchedVideos = ["C"] id 为 2 -> watchedVideos = ["B","C"] 你朋友观看过视频的频率为： B -> 1 C -> 2 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_2.png] 输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2 输出：["D"] 解释： 你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。 提示： * n == watchedVideos.length == friends.length * 2 <= n <= 100 * 1 <= watchedVideos[i].length <= 100 * 1 <= watchedVideos[i][j].length <= 8 * 0 <= friends[i].length < n * 0 <= friends[i][j] < n * 0 <= id < n * 1 <= level < n * 如果 friends[i] 包含 j ，那么 friends[j] 包含 i
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到指定层级的好友，然后统计这些好友观看的视频频率，并按要求排序。

算法步骤:
1. 使用 BFS 从给定的 id 开始遍历，直到达到指定的 level。
2. 在达到指定 level 时，记录该层级的所有好友。
3. 统计这些好友观看的视频频率。
4. 按照观看频率升序和字母顺序对视频进行排序。

关键点:
- 使用队列进行 BFS 遍历。
- 使用集合来记录已经访问过的好友，避免重复访问。
- 使用字典来统计视频的观看频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log m)，其中 n 是节点数，m 是视频数量。BFS 的时间复杂度是 O(n)，排序的时间复杂度是 O(m log m)。
空间复杂度: O(n + m)，其中 n 是节点数，m 是视频数量。需要存储节点和视频的频率。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict, deque

def watched_videos_by_friends(watched_videos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    # 初始化队列和访问集合
    queue = deque([id])
    visited = {id}
    current_level = 0
    
    # 进行 BFS 遍历
    while queue and current_level < level:
        for _ in range(len(queue)):
            current_id = queue.popleft()
            for friend_id in friends[current_id]:
                if friend_id not in visited:
                    visited.add(friend_id)
                    queue.append(friend_id)
        current_level += 1
    
    # 统计指定层级好友观看的视频频率
    video_count = defaultdict(int)
    for friend_id in queue:
        for video in watched_videos[friend_id]:
            video_count[video] += 1
    
    # 按照观看频率和字母顺序排序
    sorted_videos = sorted(video_count.items(), key=lambda x: (x[1], x[0]))
    
    return [video for video, count in sorted_videos]

Solution = create_solution(watched_videos_by_friends)