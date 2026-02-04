# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2512
标题: Longest Uploaded Prefix
难度: medium
链接: https://leetcode.cn/problems/longest-uploaded-prefix/
题目类型: 并查集、设计、树状数组、线段树、哈希表、二分查找、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2424. 最长上传前缀 - 给你一个 n 个视频的上传序列，每个视频编号为 1 到 n 之间的 不同 数字，你需要依次将这些视频上传到服务器。请你实现一个数据结构，在上传的过程中计算 最长上传前缀 。 如果 闭区间 1 到 i 之间的视频全部都已经被上传到服务器，那么我们称 i 是上传前缀。最长上传前缀指的是符合定义的 i 中的 最大值 。 请你实现 LUPrefix 类： * LUPrefix(int n) 初始化一个 n 个视频的流对象。 * void upload(int video) 上传 video 到服务器。 * int longest() 返回上述定义的 最长上传前缀 的长度。 示例 1： 输入： ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"] [[4], [3], [], [1], [], [2], []] 输出： [null, null, 0, null, 1, null, 3] 解释： LUPrefix server = new LUPrefix(4); // 初始化 4个视频的上传流 server.upload(3); // 上传视频 3 。 server.longest(); // 由于视频 1 还没有被上传，最长上传前缀是 0 。 server.upload(1); // 上传视频 1 。 server.longest(); // 前缀 [1] 是最长上传前缀，所以我们返回 1 。 server.upload(2); // 上传视频 2 。 server.longest(); // 前缀 [1,2,3] 是最长上传前缀，所以我们返回 3 。 提示： * 1 <= n <= 105 * 1 <= video <= 105 * video 中所有值 互不相同 。 * upload 和 longest 总调用 次数至多不超过 2 * 105 次。 * 至少会调用 longest 一次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个布尔数组来记录每个视频是否已上传，并使用一个变量来跟踪当前的最长上传前缀。

算法步骤:
1. 初始化一个布尔数组 `uploaded` 来记录每个视频是否已上传，并初始化一个变量 `max_prefix` 来跟踪当前的最长上传前缀。
2. 在 `upload` 方法中，将对应的视频标记为已上传，并更新 `max_prefix`。
3. 在 `longest` 方法中，返回当前的 `max_prefix`。

关键点:
- 使用布尔数组来高效地记录每个视频的上传状态。
- 使用一个变量来跟踪当前的最长上传前缀，避免每次调用 `longest` 时都进行全量检查。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - `upload` 和 `longest` 方法的时间复杂度都是常数级。
空间复杂度: O(n) - 使用了一个大小为 n 的布尔数组来记录每个视频的上传状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = [False] * (n + 1)
        self.max_prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.max_prefix + 1 < len(self.uploaded) and self.uploaded[self.max_prefix + 1]:
            self.max_prefix += 1

    def longest(self) -> int:
        return self.max_prefix


Solution = create_solution(LUPrefix)