# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2827
标题: Greatest Common Divisor Traversal
难度: hard
链接: https://leetcode.cn/problems/greatest-common-divisor-traversal/
题目类型: 并查集、数组、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2709. 最大公约数遍历 - 给你一个下标从 0 开始的整数数组 nums ，你可以在一些下标之间遍历。对于两个下标 i 和 j（i != j），当且仅当 gcd(nums[i], nums[j]) > 1 时，我们可以在两个下标之间通行，其中 gcd 是两个数的 最大公约数 。 你需要判断 nums 数组中 任意 两个满足 i < j 的下标 i 和 j ，是否存在若干次通行可以从 i 遍历到 j 。 如果任意满足条件的下标对都可以遍历，那么返回 true ，否则返回 false 。 示例 1： 输入：nums = [2,3,6] 输出：true 解释：这个例子中，总共有 3 个下标对：(0, 1) ，(0, 2) 和 (1, 2) 。 从下标 0 到下标 1 ，我们可以遍历 0 -> 2 -> 1 ，我们可以从下标 0 到 2 是因为 gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1 ，从下标 2 到 1 是因为 gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1 。 从下标 0 到下标 2 ，我们可以直接遍历，因为 gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1 。同理，我们也可以从下标 1 到 2 因为 gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1 。 示例 2： 输入：nums = [3,9,5] 输出：false 解释：我们没法从下标 0 到 2 ，所以返回 false 。 示例 3： 输入：nums = [4,3,12,8] 输出：true 解释：总共有 6 个下标对：(0, 1) ，(0, 2) ，(0, 3) ，(1, 2) ，(1, 3) 和 (2, 3) 。所有下标对之间都存在可行的遍历，所以返回 true 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并具有公共质因数的元素，并检查最终是否只有一个连通分量。

算法步骤:
1. 初始化并查集。
2. 对于每个数，找到其所有质因数，并将这些质因数映射到当前数的索引。
3. 如果某个质因数已经在并查集中存在，则将当前数的索引与该质因数对应的索引进行合并。
4. 最后检查并查集中连通分量的数量，如果只有一个连通分量，则返回 True，否则返回 False。

关键点:
- 使用埃拉托斯特尼筛法预处理质因数。
- 使用并查集高效地合并和查找连通分量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums 的长度。预处理质因数的时间复杂度是 O(n log n)，并查集操作的时间复杂度接近 O(1)。
空间复杂度: O(n)，用于存储并查集和质因数映射。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def solution_function_name(nums: List[int]) -> bool:
    """
    函数式接口 - 判断 nums 数组中任意两个满足 i < j 的下标 i 和 j 是否可以通过 gcd > 1 的路径遍历。
    """
    n = len(nums)
    if n == 1:
        return True

    # 埃拉托斯特尼筛法预处理质因数
    max_num = max(nums)
    primes = []
    is_prime = [True] * (max_num + 1)
    for i in range(2, max_num + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # 并查集初始化
    uf = UnionFind(n)

    # 质因数映射
    prime_to_index = {}
    for i, num in enumerate(nums):
        for prime in primes:
            if prime > num:
                break
            if num % prime == 0:
                if prime in prime_to_index:
                    uf.union(i, prime_to_index[prime])
                else:
                    prime_to_index[prime] = i

    # 检查连通分量数量
    return len(set(uf.find(i) for i in range(n))) == 1

Solution = create_solution(solution_function_name)