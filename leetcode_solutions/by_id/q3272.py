# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3272
标题: Find the Grid of Region Average
难度: medium
链接: https://leetcode.cn/problems/find-the-grid-of-region-average/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3030. 找出网格的区域平均强度 - 给你一个下标从 0 开始、大小为 m x n 的网格 image ，表示一个灰度图像，其中 image[i][j] 表示在范围 [0..255] 内的某个像素强度。另给你一个 非负 整数 threshold 。 如果 image[a][b] 和 image[c][d] 满足 |a - c| + |b - d| == 1 ，则称这两个像素是 相邻像素 。 区域 是一个 3 x 3 的子网格，且满足区域中任意两个 相邻 像素之间，像素强度的 绝对差 小于或等于 threshold 。 区域 内的所有像素都认为属于该区域，而一个像素 可以 属于 多个 区域。 你需要计算一个下标从 0 开始、大小为 m x n 的网格 result ，其中 result[i][j] 是 image[i][j] 所属区域的 平均 强度，向下取整 到最接近的整数。如果 image[i][j] 属于多个区域，result[i][j] 是这些区域的 “取整后的平均强度” 的 平均值，也 向下取整 到最接近的整数。如果 image[i][j] 不属于任何区域，则 result[i][j] 等于 image[i][j] 。 返回网格 result 。 示例 1： [https://assets.leetcode.com/uploads/2023/12/21/example0corrected.png] 输入：image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3 输出：[[9,9,9,9],[9,9,9,9],[9,9,9,9]] 解释：图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 9 ，而第二个区域的平均强度为 9.67 ，向下取整为 9 。两个区域的平均强度为 (9 + 9) / 2 = 9 。由于所有像素都属于区域 1 、区域 2 或两者，因此 result 中每个像素的强度都为 9 。 注意，在计算多个区域的平均值时使用了向下取整的值，因此使用区域 2 的平均强度 9 来进行计算，而不是 9.67 。 示例 2： [https://assets.leetcode.com/uploads/2023/12/21/example1corrected.png] 输入：image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12 输出：[[25,25,25],[27,27,27],[27,27,27],[30,30,30]] 解释：图像中存在两个区域，如图片中的阴影区域所示。第一个区域的平均强度为 25 ，而第二个区域的平均强度为 30 。两个区域的平均强度为 (25 + 30) / 2 = 27.5 ，向下取整为 27 。图像中第 0 行的所有像素属于区域 1 ，因此 result 中第 0 行的所有像素为 25 。同理，result 中第 3 行的所有像素为 30 。图像中第 1 行和第 2 行的像素属于区域 1 和区域 2 ，因此它们在 result 中的值为 27 。 示例 3： 输入：image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1 输出：[[5,6,7],[8,9,10],[11,12,13]] 解释：图像中不存在任何区域，因此对于所有像素，result[i][j] == image[i][j] 。 提示： * 3 <= n, m <= 500 * 0 <= image[i][j] <= 255 * 0 <= threshold <= 255
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 
1. 遍历每一个 3x3 的子网格，检查是否满足区域条件。
2. 对于每个满足条件的区域，计算其平均强度，并记录每个像素所属的区域及其平均强度。
3. 最后，根据每个像素所属的区域及其平均强度，计算结果网格。

算法步骤:
1. 初始化结果网格 `result`，初始值与 `image` 相同。
2. 使用双重循环遍历每一个 3x3 的子网格。
3. 对于每个子网格，检查是否满足区域条件（相邻像素的绝对差小于等于阈值）。
4. 如果满足条件，计算该区域的平均强度，并更新每个像素所属的区域及其平均强度。
5. 最后，根据每个像素所属的区域及其平均强度，计算结果网格。

关键点:
- 使用集合来记录每个像素所属的区域及其平均强度。
- 使用双重循环遍历每一个 3x3 的子网格。
- 计算每个区域的平均强度并更新结果网格。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def find_region_average(image: List[List[int]], threshold: int) -> List[List[int]]:
    m, n = len(image), len(image[0])
    result = [[image[i][j] for j in range(n)] for i in range(m)]
    region_averages = {}

    def is_valid_region(x, y):
        for dx in range(3):
            for dy in range(3):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    for dx2 in range(-1, 2):
                        for dy2 in range(-1, 2):
                            if abs(dx2) + abs(dy2) == 1:
                                nx2, ny2 = nx + dx2, ny + dy2
                                if 0 <= nx2 < m and 0 <= ny2 < n:
                                    if abs(image[nx][ny] - image[nx2][ny2]) > threshold:
                                        return False
        return True

    def calculate_average(x, y):
        total = 0
        count = 0
        for dx in range(3):
            for dy in range(3):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    total += image[nx][ny]
                    count += 1
        return total // count

    for i in range(m - 2):
        for j in range(n - 2):
            if is_valid_region(i, j):
                avg = calculate_average(i, j)
                for dx in range(3):
                    for dy in range(3):
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n:
                            if (x, y) not in region_averages:
                                region_averages[(x, y)] = []
                            region_averages[(x, y)].append(avg)

    for (x, y), avgs in region_averages.items():
        result[x][y] = sum(avgs) // len(avgs)

    return result

Solution = create_solution(find_region_average)