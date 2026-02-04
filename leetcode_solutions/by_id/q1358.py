# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1358
标题: Find Positive Integer Solution for a Given Equation
难度: medium
链接: https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/
题目类型: 数学、双指针、二分查找、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1237. 找出给定方程的正整数解 - 给你一个函数 f(x, y) 和一个目标结果 z，函数公式未知，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。满足条件的结果数对可以按任意顺序返回。 尽管函数的具体式子未知，但它是单调递增函数，也就是说： * f(x, y) < f(x + 1, y) * f(x, y) < f(x, y + 1) 函数接口定义如下： interface CustomFunction { public: // Returns some positive integer f(x, y) for two positive integers x and y based on a formula. int f(int x, int y); }; 你的解决方案将按如下规则进行评判： * 判题程序有一个由 CustomFunction 的 9 种实现组成的列表，以及一种为特定的 z 生成所有有效数对的答案的方法。 * 判题程序接受两个输入：function_id（决定使用哪种实现测试你的代码）以及目标结果 z 。 * 判题程序将会调用你实现的 findSolution 并将你的结果与答案进行比较。 * 如果你的结果与答案相符，那么解决方案将被视作正确答案，即 Accepted 。 示例 1： 输入：function_id = 1, z = 5 输出：[[1,4],[2,3],[3,2],[4,1]] 解释：function_id = 1 暗含的函数式子为 f(x, y) = x + y 以下 x 和 y 满足 f(x, y) 等于 5： x=1, y=4 -> f(1, 4) = 1 + 4 = 5 x=2, y=3 -> f(2, 3) = 2 + 3 = 5 x=3, y=2 -> f(3, 2) = 3 + 2 = 5 x=4, y=1 -> f(4, 1) = 4 + 1 = 5 示例 2： 输入：function_id = 2, z = 5 输出：[[1,5],[5,1]] 解释：function_id = 2 暗含的函数式子为 f(x, y) = x * y 以下 x 和 y 满足 f(x, y) 等于 5： x=1, y=5 -> f(1, 5) = 1 * 5 = 5 x=5, y=1 -> f(5, 1) = 5 * 1 = 5 提示： * 1 <= function_id <= 9 * 1 <= z <= 100 * 题目保证 f(x, y) == z 的解处于 1 <= x, y <= 1000 的范围内。 * 在 1 <= x, y <= 1000 的前提下，题目保证 f(x, y) 是一个 32 位有符号整数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法来寻找满足 f(x, y) == z 的所有正整数对 (x, y)。

算法步骤:
1. 初始化两个指针，left 指向 1，right 指向 1000。
2. 当 left 不大于 1000 且 right 不小于 1 时，执行以下操作：
   - 计算 f(left, right)。
   - 如果 f(left, right) 等于 z，则将 (left, right) 添加到结果列表中，并同时移动 left 和 right。
   - 如果 f(left, right) 小于 z，则增加 left。
   - 如果 f(left, right) 大于 z，则减少 right。
3. 返回结果列表。

关键点:
- 由于 f(x, y) 是单调递增的，因此可以通过双指针方法高效地找到所有解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 x 或 y 的最大值（在这里是 1000）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class CustomFunction:
    def f(self, x: int, y: int) -> int:
        # 具体实现由 LeetCode 提供
        pass

def findSolution(customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    """
    寻找满足 f(x, y) == z 的所有正整数对 (x, y)。
    """
    result = []
    left, right = 1, 1000
    
    while left <= 1000 and right >= 1:
        value = customfunction.f(left, right)
        if value == z:
            result.append([left, right])
            left += 1
            right -= 1
        elif value < z:
            left += 1
        else:
            right -= 1
    
    return result

Solution = create_solution(findSolution)