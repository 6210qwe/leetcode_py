# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 942
标题: Super Palindromes
难度: hard
链接: https://leetcode.cn/problems/super-palindromes/
题目类型: 数学、字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
906. 超级回文数 - 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为 超级回文数 。 现在，给你两个以字符串形式表示的正整数 left 和 right ，统计并返回区间 [left, right] 中的 超级回文数 的数目。 示例 1： 输入：left = "4", right = "1000" 输出：4 解释：4、9、121 和 484 都是超级回文数。 注意 676 不是超级回文数：26 * 26 = 676 ，但是 26 不是回文数。 示例 2： 输入：left = "1", right = "2" 输出：1 提示： * 1 <= left.length, right.length <= 18 * left 和 right 仅由数字（0 - 9）组成。 * left 和 right 不含前导零。 * left 和 right 表示的整数在区间 [1, 1018 - 1] 内。 * left 小于等于 right 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过生成所有可能的回文数，并检查它们的平方是否也在给定范围内且是回文数。

算法步骤:
1. 生成所有长度不超过 9 的回文数。
2. 对每个回文数，计算其平方。
3. 检查平方是否在给定范围内且是回文数。
4. 统计满足条件的超级回文数的数量。

关键点:
- 生成回文数时，只需生成一半的数字，然后镜像生成另一半。
- 使用字符串操作来检查回文性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 生成和检查的回文数数量是常数级别的。
空间复杂度: O(1) - 只使用了常数级别的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def generate_palindromes(n: int) -> List[int]:
    palindromes = []
    for i in range(1, n + 1):
        for j in range(10 ** (i - 1), 10 ** i):
            half = str(j)
            palindromes.append(int(half + half[::-1]))
            if i > 1:
                palindromes.append(int(half + half[-2::-1]))
    return palindromes


def superpalindromesInRange(left: str, right: str) -> int:
    l, r = int(left), int(right)
    count = 0
    palindromes = generate_palindromes(9)
    
    for p in palindromes:
        square = p * p
        if l <= square <= r and is_palindrome(str(square)):
            count += 1
    
    return count


Solution = create_solution(superpalindromesInRange)