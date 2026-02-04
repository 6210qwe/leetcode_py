# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2396
标题: Design Video Sharing Platform
难度: hard
链接: https://leetcode.cn/problems/design-video-sharing-platform/
题目类型: 栈、设计、哈希表、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2254. 设计视频共享平台 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典和堆来实现视频的存储和排序。

算法步骤:
1. 初始化时，使用字典存储视频信息，使用最小堆存储可用的视频ID。
2. 上传视频时，从堆中获取最小的可用ID，并将其与视频信息关联。
3. 删除视频时，将视频ID放回堆中，并从字典中移除视频信息。
4. 搜索视频时，直接从字典中查找视频信息。
5. 获取视频列表时，从字典中获取所有视频信息并按要求排序。

关键点:
- 使用字典存储视频信息，支持快速查找和删除。
- 使用最小堆管理可用的视频ID，确保每次上传时都能获得最小的可用ID。
- 使用有序集合（如SortedList）来维护视频列表，支持高效的插入和排序操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- 上传视频: O(log n) （堆操作）
- 删除视频: O(log n) （堆操作）
- 搜索视频: O(1) （字典查找）
- 获取视频列表: O(n log n) （排序操作）

空间复杂度: O(n) （存储视频信息和可用ID）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from sortedcontainers import SortedList

class VideoSharingPlatform:

    def __init__(self):
        self.next_video_id = 1
        self.video_info = {}
        self.available_ids = []
        self.video_list = SortedList()

    def upload(self, video: str) -> int:
        if self.available_ids:
            video_id = heapq.heappop(self.available_ids)
        else:
            video_id = self.next_video_id
            self.next_video_id += 1
        self.video_info[video_id] = (video, 0)
        self.video_list.add((0, video_id))
        return video_id

    def remove(self, videoId: int) -> None:
        if videoId in self.video_info:
            _, views = self.video_info[videoId]
            self.video_list.remove((views, videoId))
            del self.video_info[videoId]
            heapq.heappush(self.available_ids, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId in self.video_info:
            video, _ = self.video_info[videoId]
            return video[startMinute * 60: min(endMinute * 60, len(video))]
        return "-1"

    def like(self, videoId: int) -> None:
        if videoId in self.video_info:
            video, likes = self.video_info[videoId]
            self.video_info[videoId] = (video, likes + 1)
            self.video_list.remove((likes, videoId))
            self.video_list.add((likes + 1, videoId))

    def dislike(self, videoId: int) -> None:
        if videoId in self.video_info:
            video, dislikes = self.video_info[videoId]
            self.video_info[videoId] = (video, dislikes + 1)
            self.video_list.remove((dislikes, videoId))
            self.video_list.add((dislikes + 1, videoId))

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.video_info:
            _, likes = self.video_info[videoId]
            return [likes, 0]
        return [-1]

    def getViews(self, videoId: int) -> int:
        if videoId in self.video_info:
            _, views = self.video_info[videoId]
            return views
        return -1

    def getMostPopularVideos(self, n: int) -> List[int]:
        return [videoId for _, videoId in self.video_list[-n:]][::-1]


# 示例用法
# platform = VideoSharingPlatform()
# print(platform.upload("catvideo"))
# print(platform.upload("dogvideo"))
# print(platform.watch(1, 0, 5))
# print(platform.like(1))
# print(platform.dislike(2))
# print(platform.getLikesAndDislikes(1))
# print(platform.getViews(1))
# print(platform.getMostPopularVideos(1))
# platform.remove(1)
# print(platform.getMostPopularVideos(1))

Solution = create_solution(VideoSharingPlatform)