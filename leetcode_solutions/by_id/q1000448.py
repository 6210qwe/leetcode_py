# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000448
标题: 积木拼接
难度: hard
链接: https://leetcode.cn/problems/De4qBB/
题目类型: 数组、回溯、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 58. 积木拼接 - 欢迎各位勇者来到力扣城，本次试炼主题为「积木拼接」。 勇者面前有 `6` 片积木（厚度均为 1），每片积木的形状记录于二维字符串数组 `shapes` 中，`shapes[i]` 表示第 `i` 片积木，其中 `1` 表示积木对应位置无空缺，`0` 表示积木对应位置有空缺。 例如 `["010","111","010"]` 对应积木形状为 ![image.png](https://pic.leetcode.cn/1616125620-nXMCxX-image.png) 拼接积木的规则如下： - 积木片可以旋转、翻面 - 积木片边缘必须完全吻合才能拼接在一起 - **每片积木片 `shapes[i]` 的中心点在拼接时必须处于正方体对应面的中心点** 例如 `3*3`、`4*4` 的积木片的中心点如图所示（红色点）： ![middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png](https://pic.leetcode.cn/1650509082-wObiEp-middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png){:height="150px"} 请返回这 6 片积木能否拼接成一个**严丝合缝的正方体**且每片积木正好对应正方体的一个面。 **注意：** - 输入确保每片积木均无空心情况（即输入数据保证对于大小 `N*N` 的 `shapes[i]`，内部的 `(N-2)*(N-2)` 的区域必然均为 1） - 输入确保每片积木的所有 `1` 位置均连通 **示例 1：** >输入：`shapes = [["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]` > >输出：`true` > >解释： ![cube.gif](https://pic.leetcode.cn/1616125823-hkXAeN-cube.gif) **示例 2：** >输入：`shapes = [["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]` > >输出：`false` > >解释： >由于每片积木片的中心点在拼接时必须处于正方体对应面的中心点，积木片 `["010","011","000"]` 不能作为 `["100","110","000"]` 使用，因此无法构成正方体 **提示：** - `shapes.length == 6` - `shapes[i].length == shapes[j].length` - `shapes[i].length == shapes[i][j].length` - `3 <= shapes[i].length <= 10`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯法 + 状态压缩

算法步骤:
1. 将每片积木的所有可能旋转和翻转状态存储在一个集合中。
2. 使用状态压缩表示当前已经使用的积木片，并使用回溯法尝试所有可能的组合。
3. 检查每种组合是否能形成一个完整的正方体。

关键点:
- 通过状态压缩减少状态空间。
- 通过预处理积木的所有可能状态减少重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(6! * 8^6)
- 6! 是排列组合的总数。
- 每片积木最多有 8 种状态（4 种旋转 + 4 种翻转）。

空间复杂度: O(8^6)
- 存储每片积木的所有可能状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def rotate(shape: List[str]) -> List[str]:
    """顺时针旋转 90 度"""
    return ["".join(row[i] for row in shape[::-1]) for i in range(len(shape))]

def flip(shape: List[str]) -> List[str]:
    """水平翻转"""
    return [row[::-1] for row in shape]

def get_all_transforms(shape: List[str]) -> set:
    """获取所有可能的旋转和翻转状态"""
    transforms = set()
    for _ in range(4):
        shape = rotate(shape)
        transforms.add(tuple(shape))
        transforms.add(tuple(flip(shape)))
    return transforms

def can_form_cube(shapes: List[List[str]]) -> bool:
    n = len(shapes[0])
    all_shapes = [get_all_transforms(shape) for shape in shapes]
    
    def backtrack(index: int, used: int, current: List[List[str]]) -> bool:
        if index == 6:
            return True
        for i in range(6):
            if (used & (1 << i)) == 0:
                for shape in all_shapes[i]:
                    if is_valid(current, shape):
                        current.append(list(shape))
                        if backtrack(index + 1, used | (1 << i), current):
                            return True
                        current.pop()
        return False
    
    def is_valid(current: List[List[str]], new_shape: List[str]) -> bool:
        if not current:
            return True
        for i in range(n):
            if current[-1][i] + new_shape[i] != "1" * n:
                return False
        return True
    
    return backtrack(0, 0, [])

def solution_function_name(shapes: List[List[str]]) -> bool:
    """
    函数式接口 - 判断是否能拼接成一个严丝合缝的正方体
    """
    return can_form_cube(shapes)

Solution = create_solution(solution_function_name)