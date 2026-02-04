# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2647
标题: Split the Array to Make Coprime Products
难度: hard
链接: https://leetcode.cn/problems/split-the-array-to-make-coprime-products/
题目类型: 数组、哈希表、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2584. 分割数组使乘积互质 - 给你一个长度为 n 的整数数组 nums ，下标从 0 开始。 如果在下标 i 处 分割 数组，其中 0 <= i <= n - 2 ，使前 i + 1 个元素的乘积和剩余元素的乘积互质，则认为该分割 有效 。 * 例如，如果 nums = [2, 3, 3] ，那么在下标 i = 0 处的分割有效，因为 2 和 9 互质，而在下标 i = 1 处的分割无效，因为 6 和 3 不互质。在下标 i = 2 处的分割也无效，因为 i == n - 1 。 返回可以有效分割数组的最小下标 i ，如果不存在有效分割，则返回 -1 。 当且仅当 gcd(val1, val2) == 1 成立时，val1 和 val2 这两个值才是互质的，其中 gcd(val1, val2) 表示 val1 和 val2 的最大公约数。 示例 1： [https://assets.leetcode.com/uploads/2022/12/14/second.PNG] 输入：nums = [4,7,8,15,3,5] 输出：2 解释：上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。 唯一一个有效分割位于下标 2 。 示例 2： [https://assets.leetcode.com/uploads/2022/12/14/capture.PNG] 输入：nums = [4,7,15,8,3,5] 输出：-1 解释：上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。 不存在有效分割。 提示： * n == nums.length * 1 <= n <= 104 * 1 <= nums[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用埃拉托色尼筛法预处理所有数的质因数，并使用前缀和与后缀和来快速计算前缀和后缀的质因数集合。

算法步骤:
1. 预处理所有数的质因数。
2. 计算前缀和后缀的质因数集合。
3. 遍历数组，找到第一个使得前缀和后缀的质因数集合不相交的下标。

关键点:
- 使用埃拉托色尼筛法预处理质因数。
- 使用前缀和后缀的质因数集合来快速判断是否互质。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log log M)，其中 n 是数组长度，M 是数组中的最大值。
空间复杂度: O(M)，用于存储每个数的质因数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import math

def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    def prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors

    n = len(nums)
    max_num = max(nums)
    primes = [prime_factors(i) for i in range(1, max_num + 1)]

    prefix_factors = [set() for _ in range(n)]
    suffix_factors = [set() for _ in range(n)]

    for i in range(n):
        prefix_factors[i] = (prefix_factors[i-1].copy() if i > 0 else set()) | primes[nums[i]-1]
        suffix_factors[n-i-1] = (suffix_factors[n-i].copy() if i < n-1 else set()) | primes[nums[n-i-1]-1]

    for i in range(n - 1):
        if not (prefix_factors[i] & suffix_factors[i+1]):
            return i

    return -1

Solution = create_solution(solution_function_name)