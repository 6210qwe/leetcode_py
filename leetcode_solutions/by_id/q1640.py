# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1640
标题: Design a File Sharing System
难度: medium
链接: https://leetcode.cn/problems/design-a-file-sharing-system/
题目类型: 设计、哈希表、数据流、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1500. 设计文件分享系统 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表和最小堆来实现文件共享系统。

算法步骤:
1. 使用一个字典 `file_to_users` 来存储每个文件的用户列表。
2. 使用一个字典 `user_to_files` 来存储每个用户的文件列表。
3. 使用一个最小堆 `available_ids` 来管理可用的用户 ID。
4. 初始化时，将所有可能的用户 ID 放入最小堆中。
5. `join` 方法从最小堆中取出一个可用的用户 ID，并返回该 ID。
6. `leave` 方法将用户 ID 重新放回最小堆，并从 `user_to_files` 中移除该用户的所有文件。
7. `add_file` 方法将文件添加到用户的文件列表中，并更新 `file_to_users`。
8. `get_files` 方法返回用户拥有的所有文件。
9. `retrieve` 方法返回拥有指定文件的所有用户 ID 列表。

关键点:
- 使用最小堆来高效管理用户 ID 的分配和回收。
- 使用哈希表来快速查找文件和用户之间的关系。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- `join` 和 `leave` 方法的时间复杂度为 O(log n)，其中 n 是用户数量。
- `add_file` 和 `get_files` 方法的时间复杂度为 O(1)。
- `retrieve` 方法的时间复杂度为 O(m log m)，其中 m 是拥有指定文件的用户数量。

空间复杂度: 
- 总体空间复杂度为 O(n + f)，其中 n 是用户数量，f 是文件数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

class FileSharing:
    def __init__(self, m: int):
        self.file_to_users = {}
        self.user_to_files = {}
        self.available_ids = list(range(1, m + 1))
        heapq.heapify(self.available_ids)

    def join(self, ownedChunks: List[int]) -> int:
        user_id = heapq.heappop(self.available_ids)
        self.user_to_files[user_id] = set(ownedChunks)
        for chunk in ownedChunks:
            if chunk not in self.file_to_users:
                self.file_to_users[chunk] = set()
            self.file_to_users[chunk].add(user_id)
        return user_id

    def leave(self, userID: int) -> None:
        for chunk in self.user_to_files[userID]:
            self.file_to_users[chunk].remove(userID)
            if not self.file_to_users[chunk]:
                del self.file_to_users[chunk]
        del self.user_to_files[userID]
        heapq.heappush(self.available_ids, userID)

    def add_file(self, userID: int, chunk: int) -> None:
        self.user_to_files[userID].add(chunk)
        if chunk not in self.file_to_users:
            self.file_to_users[chunk] = set()
        self.file_to_users[chunk].add(userID)

    def get_files(self, userID: int) -> List[int]:
        return sorted(list(self.user_to_files[userID]))

    def retrieve(self, chunk: int) -> List[int]:
        if chunk in self.file_to_users:
            return sorted(list(self.file_to_users[chunk]))
        return []

# 示例用法
# file_sharing = FileSharing(10)
# print(file_sharing.join([1, 2, 3]))  # 返回 1
# print(file_sharing.join([]))         # 返回 2
# print(file_sharing.add_file(1, 4))   # 返回 None
# print(file_sharing.get_files(1))     # 返回 [1, 2, 3, 4]
# print(file_sharing.retrieve(4))      # 返回 [1]
# print(file_sharing.leave(1))         # 返回 None
# print(file_sharing.retrieve(4))      # 返回 []