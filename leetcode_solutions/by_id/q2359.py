# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2359
标题: Maximum White Tiles Covered by a Carpet
难度: medium
链接: https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/
题目类型: 贪心、数组、二分查找、前缀和、排序、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2271. 毯子覆盖的最多白色砖块数 - 给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。 同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子的长度。 请你返回使用这块毯子，最多 可以盖住多少块白色瓷砖。 示例 1： [https://assets.leetcode.com/uploads/2022/03/25/example1drawio3.png] 输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10 输出：9 解释：将毯子从瓷砖 10 开始放置。 总共覆盖 9 块瓷砖，所以返回 9 。 注意可能有其他方案也可以覆盖 9 块瓷砖。 可以看出，瓷砖无法覆盖超过 9 块瓷砖。 示例 2： [https://assets.leetcode.com/uploads/2022/03/24/example2drawio.png] 输入：tiles = [[10,11],[1,1]], carpetLen = 2 输出：2 解释：将毯子从瓷砖 10 开始放置。 总共覆盖 2 块瓷砖，所以我们返回 2 。 提示： * 1 <= tiles.length <= 5 * 104 * tiles[i].length == 2 * 1 <= li <= ri <= 109 * 1 <= carpetLen <= 109 * tiles 互相 不会重叠 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和前缀和来计算覆盖的最大白色瓷砖数量。

算法步骤:
1. 对 tiles 按起始位置进行排序。
2. 计算前缀和数组 prefix_sum，prefix_sum[i] 表示从第一个瓷砖到第 i 个瓷砖的总长度。
3. 使用滑动窗口遍历 tiles，维护一个窗口 [left, right]，使得窗口内的瓷砖总长度不超过 carpetLen。
4. 在每次移动右边界时，更新左边界，确保窗口内的瓷砖总长度不超过 carpetLen。
5. 计算当前窗口内的最大覆盖瓷砖数量，并更新结果。

关键点:
- 使用前缀和快速计算窗口内的瓷砖总长度。
- 滑动窗口确保了时间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 tiles 的长度。排序操作的时间复杂度为 O(n log n)，滑动窗口的时间复杂度为 O(n)。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def max_white_tiles(tiles: List[List[int]], carpetLen: int) -> int:
    # 按起始位置排序
    tiles.sort(key=lambda x: x[0])
    
    # 计算前缀和数组
    prefix_sum = [0]
    for tile in tiles:
        prefix_sum.append(prefix_sum[-1] + (tile[1] - tile[0] + 1))
    
    max_covered = 0
    left = 0
    for right in range(len(tiles)):
        while tiles[right][1] - tiles[left][0] + 1 > carpetLen:
            left += 1
        if tiles[right][1] - tiles[left][0] + 1 <= carpetLen:
            covered = prefix_sum[right + 1] - prefix_sum[left]
            if tiles[left][0] + carpetLen < tiles[right][1]:
                covered -= (tiles[right][1] - (tiles[left][0] + carpetLen - 1))
            max_covered = max(max_covered, covered)
    
    return max_covered

Solution = create_solution(max_white_tiles)