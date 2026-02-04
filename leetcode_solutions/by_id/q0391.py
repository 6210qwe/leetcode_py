# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 391
标题: Perfect Rectangle
难度: hard
链接: https://leetcode.cn/problems/perfect-rectangle/
题目类型: 几何、数组、哈希表、数学、扫描线
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
391. 完美矩形 - 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg] 输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]] 输出：true 解释：5 个矩形一起可以精确地覆盖一个矩形区域。 示例 2： [https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg] 输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]] 输出：false 解释：两个矩形之间有间隔，无法覆盖成一个矩形。 示例 3： [https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg] 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]] 输出：false 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。 提示： * 1 <= rectangles.length <= 2 * 104 * rectangles[i].length == 4 * -105 <= xi < ai <= 105 * -105 <= yi < bi <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 面积一致 + 顶点异或：所有小矩形的面积之和要等于大矩形面积，且所有小矩形四个顶点经「奇偶计数」后只剩大矩形的四个顶点。

算法步骤:
1. 遍历所有小矩形，更新外包矩形的 `min_x, min_y, max_x, max_y`，同时累加小矩形面积和 `area_sum`。
2. 使用集合 `corners` 记录顶点：对每个小矩形 (x1,y1,x2,y2) 的四个角，如果角点第一次出现则加入集合；第二次出现则从集合删除，相当于做异或。
3. 遍历结束后，检查：
   - `area_sum` 是否等于外包矩形面积 `(max_x-min_x)*(max_y-min_y)`；若不等说明有重叠或空洞。
   - `corners` 是否恰好包含外包矩形的四个角点，且不多不少。

关键点:
- 利用“内部顶点被覆盖偶数次会相互抵消”的性质，只留下外边界的四个顶点。
- 面积和与顶点集合这两个条件联合即可排除重叠与空洞。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，n 为矩形个数，每个矩形常数次操作。
空间复杂度: O(n)，最坏情况下 `corners` 中可能暂存 O(n) 个不同顶点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def perfect_rectangle(rectangles: List[List[int]]) -> bool:
    """
    判断若干小矩形是否能精确覆盖成一个大矩形而无重叠/间隙。

    核心检查：面积和等于外包矩形面积，且所有小矩形顶点经过异或后只剩外包矩形四个顶点。
    """
    if not rectangles:
        return False

    min_x = min(r[0] for r in rectangles)
    min_y = min(r[1] for r in rectangles)
    max_x = max(r[2] for r in rectangles)
    max_y = max(r[3] for r in rectangles)

    area_sum = 0
    corners: set[tuple[int, int]] = set()

    for x1, y1, x2, y2 in rectangles:
        area_sum += (x2 - x1) * (y2 - y1)
        for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
            if p in corners:
                corners.remove(p)
            else:
                corners.add(p)

    # 检查面积
    if area_sum != (max_x - min_x) * (max_y - min_y):
        return False

    # 角点必须正好是外包矩形的四个角
    expected = {
        (min_x, min_y),
        (min_x, max_y),
        (max_x, min_y),
        (max_x, max_y),
    }
    return corners == expected


# 自动生成Solution类（无需手动编写）
Solution = create_solution(perfect_rectangle)
