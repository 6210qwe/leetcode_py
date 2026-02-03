# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 17
标题: Letter Combinations of a Phone Number
难度: medium
链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
题目类型: 哈希表、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
17. 电话号码的字母组合 - 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 [https://pic.leetcode.cn/1752723054-mfIHZs-image.png] 示例 1： 输入：digits = "23" 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"] 示例 2： 输入：digits = "2" 输出：["a","b","c"] 提示： * 1 <= digits.length <= 4 * digits[i] 是范围 ['2', '9'] 的一个数字。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，递归生成所有可能的字母组合

算法步骤:
1. 创建数字到字母的映射表
2. 使用回溯函数，参数包括当前组合和剩余数字
3. 如果所有数字都处理完，将当前组合添加到结果
4. 否则，对于当前数字对应的每个字母：
   - 将字母添加到当前组合
   - 递归处理下一个数字
   - 回溯：移除刚添加的字母
5. 返回所有组合

关键点:
- 回溯算法可以系统地生成所有可能的组合
- 时间复杂度O(4^n)，其中n是数字个数，4是每个数字平均对应的字母数
- 空间复杂度O(n)，递归栈的深度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(4^n * n) - 共有4^n种组合，每种组合长度为n
空间复杂度: O(n) - 递归栈的深度为n
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def letter_combinations(digits: str) -> List[str]:
    """
    函数式接口 - 回溯算法实现
    
    实现思路:
    使用回溯算法递归生成所有可能的字母组合。
    
    Args:
        digits: 数字字符串（2-9）
        
    Returns:
        所有可能的字母组合列表
        
    Example:
        >>> letter_combinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> letter_combinations("2")
        ['a', 'b', 'c']
    """
    if not digits:
        return []
    
    # 数字到字母的映射
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(current: str, remaining_digits: str):
        if not remaining_digits:
            result.append(current)
            return
        
        digit = remaining_digits[0]
        for letter in digit_map[digit]:
            backtrack(current + letter, remaining_digits[1:])
    
    backtrack("", digits)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(letter_combinations)
