# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2202
标题: Sum of k-Mirror Numbers
难度: hard
链接: https://leetcode.cn/problems/sum-of-k-mirror-numbers/
题目类型: 数学、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2081. k 镜像数字的和 - 一个 k 镜像数字 指的是一个在十进制和 k 进制下从前往后读和从后往前读都一样的 没有前导 0 的 正 整数。 * 比方说，9 是一个 2 镜像数字。9 在十进制下为 9 ，二进制下为 1001 ，两者从前往后读和从后往前读都一样。 * 相反地，4 不是一个 2 镜像数字。4 在二进制下为 100 ，从前往后和从后往前读不相同。 给你进制 k 和一个数字 n ，请你返回 k 镜像数字中 最小 的 n 个数 之和 。 示例 1： 输入：k = 2, n = 5 输出：25 解释： 最小的 5 个 2 镜像数字和它们的二进制表示如下： 十进制 二进制 1 1 3 11 5 101 7 111 9 1001 它们的和为 1 + 3 + 5 + 7 + 9 = 25 。 示例 2： 输入：k = 3, n = 7 输出：499 解释： 7 个最小的 3 镜像数字和它们的三进制表示如下： 十进制 三进制 1 1 2 2 4 11 8 22 121 11111 151 12121 212 21212 它们的和为 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499 。 示例 3： 输入：k = 7, n = 17 输出：20379000 解释：17 个最小的 7 镜像数字分别为： 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596 提示： * 2 <= k <= 9 * 1 <= n <= 30
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过生成所有可能的回文数并检查其在 k 进制下的表示是否也是回文数来找到 k 镜像数字。

算法步骤:
1. 生成所有可能的回文数。
2. 检查每个回文数在 k 进制下的表示是否也是回文数。
3. 收集前 n 个满足条件的 k 镜像数字并计算它们的和。

关键点:
- 生成回文数时，可以利用对称性减少生成的数量。
- 使用字符串反转来检查回文性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是需要找到的 k 镜像数字的数量，m 是生成的回文数的长度。
空间复杂度: O(n * m)，用于存储生成的回文数及其 k 进制表示。
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


def generate_palindromes(length: int) -> List[int]:
    if length == 1:
        return [i for i in range(1, 10)]
    if length == 2:
        return [i * 11 for i in range(1, 10)]
    
    half_length = (length + 1) // 2
    palindromes = []
    
    def build_palindrome(prefix: str):
        if len(prefix) == half_length:
            if length % 2 == 0:
                palindrome = prefix + prefix[::-1]
            else:
                palindrome = prefix[:-1] + prefix[-1] + prefix[:-1][::-1]
            palindromes.append(int(palindrome))
            return
        for digit in range(10):
            build_palindrome(prefix + str(digit))
    
    build_palindrome("")
    return palindromes


def to_k_base(num: int, k: int) -> str:
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(str(num % k))
        num //= k
    return ''.join(digits[::-1])


def sum_of_k_mirror_numbers(k: int, n: int) -> int:
    count = 0
    total_sum = 0
    length = 1
    
    while count < n:
        palindromes = generate_palindromes(length)
        for num in palindromes:
            k_base = to_k_base(num, k)
            if is_palindrome(k_base):
                total_sum += num
                count += 1
                if count == n:
                    return total_sum
        length += 1


Solution = create_solution(sum_of_k_mirror_numbers)