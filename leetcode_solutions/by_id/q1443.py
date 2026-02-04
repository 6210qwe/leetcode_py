# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1443
标题: Minimum Distance to Type a Word Using Two Fingers
难度: hard
链接: https://leetcode.cn/problems/minimum-distance-to-type-a-word-using-two-fingers/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1320. 二指输入的的最小距离 - [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/11/leetcode_keyboard.png] 二指输入法定制键盘在 X-Y 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处。 * 例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。 给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。 坐标 (x1,y1) 和 (x2,y2) 之间的 距离 是 |x1 - x2| + |y1 - y2|。 注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。 示例 1： 输入：word = "CAKE" 输出：3 解释： 使用两根手指输入 "CAKE" 的最佳方案之一是： 手指 1 在字母 'C' 上 -> 移动距离 = 0 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 手指 2 在字母 'K' 上 -> 移动距离 = 0 手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离 = 1 总距离 = 3 示例 2： 输入：word = "HAPPY" 输出：6 解释： 使用两根手指输入 "HAPPY" 的最佳方案之一是： 手指 1 在字母 'H' 上 -> 移动距离 = 0 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2 手指 2 在字母 'P' 上 -> 移动距离 = 0 手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0 手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4 总距离 = 6 提示： * 2 <= word.length <= 300 * 每个 word[i] 都是一个大写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 为输入到第 i 个字符时，手指 1 在字符 j 位置的最小移动距离。通过递推公式更新 dp 数组，最终得到答案。

算法步骤:
1. 初始化键盘布局，将每个字母映射到其对应的坐标。
2. 定义 dp 数组，dp[i][j] 表示输入到第 i 个字符时，手指 1 在字符 j 位置的最小移动距离。
3. 初始化 dp 数组，考虑第一个字符的情况。
4. 通过递推公式更新 dp 数组：
   - 如果手指 1 移动到当前字符，则 dp[i][curr_char] = min(dp[i-1][k]) + distance(k, curr_char)
   - 如果手指 2 移动到当前字符，则 dp[i][prev_char] = dp[i-1][prev_char] + distance(prev_char, curr_char)
5. 最终结果为 dp[len(word)-1] 中的最小值。

关键点:
- 使用动态规划来避免重复计算。
- 通过预处理键盘布局，快速计算字符间的距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * 26) = O(n^2)，其中 n 是 word 的长度。
空间复杂度: O(n * 26) = O(n)，存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(word: str) -> int:
    """
    函数式接口 - 计算使用两根手指输入字符串的最小移动总距离
    """
    # 键盘布局
    keyboard = [
        ['A', 'B', 'C', 'D', 'E', 'F'],
        ['G', 'H', 'I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W', 'X'],
        ['Y', 'Z']
    ]
    
    # 将字母映射到坐标
    char_to_pos = {}
    for i, row in enumerate(keyboard):
        for j, char in enumerate(row):
            char_to_pos[char] = (i, j)
    
    # 计算字符间的曼哈顿距离
    def distance(char1, char2):
        (x1, y1), (x2, y2) = char_to_pos[char1], char_to_pos[char2]
        return abs(x1 - x2) + abs(y1 - y2)
    
    n = len(word)
    if n == 0:
        return 0
    
    # 初始化 dp 数组
    dp = [[float('inf')] * 26 for _ in range(n)]
    
    # 第一个字符的情况
    for i in range(26):
        dp[0][i] = 0
    
    # 动态规划更新 dp 数组
    for i in range(1, n):
        curr_char = ord(word[i]) - ord('A')
        for prev_char in range(26):
            dp[i][curr_char] = min(dp[i][curr_char], dp[i-1][prev_char] + distance(chr(prev_char + ord('A')), word[i]))
            dp[i][prev_char] = min(dp[i][prev_char], dp[i-1][prev_char] + distance(word[i-1], chr(prev_char + ord('A'))))
    
    # 返回最终结果
    return min(dp[n-1])

Solution = create_solution(solution_function_name)