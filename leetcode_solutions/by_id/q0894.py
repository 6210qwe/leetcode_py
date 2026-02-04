# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 894
标题: Random Pick with Blacklist
难度: hard
链接: https://leetcode.cn/problems/random-pick-with-blacklist/
题目类型: 数组、哈希表、数学、二分查找、排序、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
710. 黑名单中的随机数 - 给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。 优化你的算法，使它最小化调用语言 内置 随机函数的次数。 实现 Solution 类: * Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数 * int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数 示例 1： 输入 ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"] [[7, [2, 3, 5]], [], [], [], [], [], [], []] 输出 [null, 0, 4, 1, 6, 1, 0, 4] 解释 Solution solution = new Solution(7, [2, 3, 5]); solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用， // 0、1、4和6的返回概率必须相等(即概率为1/4)。 solution.pick(); // 返回 4 solution.pick(); // 返回 1 solution.pick(); // 返回 6 solution.pick(); // 返回 1 solution.pick(); // 返回 0 solution.pick(); // 返回 4 提示: * 1 <= n <= 109 * 0 <= blacklist.length <= min(105, n - 1) * 0 <= blacklist[i] < n * blacklist 中所有值都 不同 * pick 最多被调用 2 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希映射将黑名单中的数字映射到非黑名单的数字上，从而实现 O(1) 时间复杂度的 pick 操作。

算法步骤:
1. 计算有效数字的数量 size = n - len(blacklist)。
2. 将黑名单中的数字分成两部分：小于 size 的部分和大于等于 size 的部分。
3. 对于小于 size 的黑名单数字，找到一个大于等于 size 且不在黑名单中的数字进行映射。
4. 在 pick 操作中，生成一个 [0, size) 范围内的随机数，如果该数在映射中，则返回映射后的值，否则直接返回该数。

关键点:
- 通过哈希映射将黑名单中的数字映射到非黑名单的数字上。
- 生成随机数时只考虑 [0, size) 范围内的数字，确保每个数字都有同等的概率被选中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 初始化时需要遍历黑名单并进行映射。
空间复杂度: O(b) - 需要存储黑名单中的映射关系，其中 b 是黑名单的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist)
        self.mapping = {}
        
        # 将黑名单中的数字分成两部分
        black_set = set(blacklist)
        last = n - 1
        
        for b in blacklist:
            if b < self.size:
                while last in black_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        index = random.randint(0, self.size - 1)
        return self.mapping.get(index, index)

# 工厂函数
def create_solution(n: int, blacklist: List[int]) -> Solution:
    return Solution(n, blacklist)

# 测试
if __name__ == "__main__":
    solution = create_solution(7, [2, 3, 5])
    print(solution.pick())  # 可能输出 0, 1, 4, 6
    print(solution.pick())  # 可能输出 0, 1, 4, 6
    print(solution.pick())  # 可能输出 0, 1, 4, 6