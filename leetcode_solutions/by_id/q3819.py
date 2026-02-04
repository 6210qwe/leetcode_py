# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3819
标题: Count Covered Buildings
难度: medium
链接: https://leetcode.cn/problems/count-covered-buildings/
题目类型: 数组、哈希表、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3531. 统计被覆盖的建筑 - 给你一个正整数 n，表示一个 n x n 的城市，同时给定一个二维数组 buildings，其中 buildings[i] = [x, y] 表示位于坐标 [x, y] 的一个 唯一 建筑。 如果一个建筑在四个方向（左、右、上、下）中每个方向上都至少存在一个建筑，则称该建筑 被覆盖 。 返回 被覆盖 的建筑数量。 示例 1： [https://pic.leetcode.cn/1745660407-qtNUjI-telegram-cloud-photo-size-5-6212982906394101085-m.jpg] 输入: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]] 输出: 1 解释: * 只有建筑 [2,2] 被覆盖，因为它在每个方向上都至少存在一个建筑： * 上方 ([1,2]) * 下方 ([3,2]) * 左方 ([2,1]) * 右方 ([2,3]) * 因此，被覆盖的建筑数量是 1。 示例 2： [https://pic.leetcode.cn/1745660407-tUMUKl-telegram-cloud-photo-size-5-6212982906394101086-m.jpg] 输入: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]] 输出: 0 解释: * 没有任何一个建筑在每个方向上都有至少一个建筑。 示例 3： [https://pic.leetcode.cn/1745660407-bQIwBX-telegram-cloud-photo-size-5-6248862251436067566-x.jpg] 输入: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]] 输出: 1 解释: * 只有建筑 [3,3] 被覆盖，因为它在每个方向上至少存在一个建筑： * 上方 ([1,3]) * 下方 ([5,3]) * 左方 ([3,2]) * 右方 ([3,5]) * 因此，被覆盖的建筑数量是 1。 提示： * 2 <= n <= 105 * 1 <= buildings.length <= 105 * buildings[i] = [x, y] * 1 <= x, y <= n * buildings 中所有坐标均 唯一 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来记录每个坐标的建筑，并检查每个建筑是否在四个方向上都有其他建筑。

算法步骤:
1. 将所有建筑的坐标存入集合。
2. 遍历每个建筑，检查其上下左右四个方向是否有其他建筑。
3. 计算并返回被覆盖的建筑数量。

关键点:
- 使用集合来快速查找是否存在某个建筑。
- 通过遍历和方向检查来确定每个建筑是否被覆盖。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是城市的大小，m 是建筑的数量。遍历建筑和方向检查的时间复杂度为 O(m)。
空间复杂度: O(m)，用于存储建筑的集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_covered_buildings(n: int, buildings: List[List[int]]) -> int:
    """
    函数式接口 - 统计被覆盖的建筑
    """
    # 将所有建筑的坐标存入集合
    building_set = set(tuple(building) for building in buildings)
    
    # 检查建筑是否在四个方向上都被覆盖
    def is_covered(x: int, y: int) -> bool:
        return (x - 1, y) in building_set and (x + 1, y) in building_set and (x, y - 1) in building_set and (x, y + 1) in building_set
    
    # 计算被覆盖的建筑数量
    covered_count = sum(is_covered(x, y) for x, y in building_set)
    
    return covered_count


Solution = create_solution(count_covered_buildings)