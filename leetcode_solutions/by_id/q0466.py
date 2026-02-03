# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 466
标题: Count The Repetitions
难度: hard
链接: https://leetcode.cn/problems/count-the-repetitions/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
466. 统计重复个数 - 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。 * 例如，str == ["abc", 3] =="abcabcabc" 。 如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。 * 例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。 现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, n2] 。 请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。 示例 1： 输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2 输出：2 示例 2： 输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1 输出：1 提示： * 1 <= s1.length, s2.length <= 100 * s1 和 s2 由小写英文字母组成 * 1 <= n1, n2 <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划，记录每个s1重复周期匹配s2的次数

算法步骤:
1. 对于每个s1的重复周期，记录匹配s2的进度
2. 使用记忆化避免重复计算
3. 计算总共能匹配多少个s2

关键点:
- 状态压缩，记录匹配进度
- 处理循环节
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n1 * len(s1) * len(s2)) - 遍历s1重复次数和字符串
空间复杂度: O(len(s2)) - 存储匹配状态
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_the_repetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    """
    函数式接口 - 统计重复个数
    
    实现思路:
    使用动态规划，记录每个s1重复周期匹配s2的进度。
    
    Args:
        s1: 第一个字符串
        n1: s1的重复次数
        s2: 第二个字符串
        n2: s2的重复次数
        
    Returns:
        最大整数m，使得[str2, m]可以从str1获得
        
    Example:
        >>> count_the_repetitions("acb", 4, "ab", 2)
        2
    """
    # 记录每个s1周期结束时，匹配s2的进度
    # next_index[i]表示从s2的第i个位置开始，匹配一个s1后到达的位置
    next_index = {}
    
    def get_next_index(s2_index: int) -> int:
        """计算从s2的s2_index位置开始，匹配一个s1后到达的位置"""
        if s2_index in next_index:
            return next_index[s2_index]
        
        count = 0
        j = s2_index
        for char in s1:
            if char == s2[j % len(s2)]:
                j += 1
                if j % len(s2) == 0:
                    count += 1
        
        next_index[s2_index] = (j % len(s2), count)
        return next_index[s2_index]
    
    # 计算总共能匹配多少个s2
    s2_index = 0
    total_count = 0
    
    for _ in range(n1):
        next_pos, count = get_next_index(s2_index)
        total_count += count
        s2_index = next_pos
    
    return total_count // n2


# 自动生成Solution类（无需手动编写）
Solution = create_solution(count_the_repetitions)
