# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2285
标题: Design Bitset
难度: medium
链接: https://leetcode.cn/problems/design-bitset/
题目类型: 设计、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2166. 设计位集 - 位集 Bitset 是一种能以紧凑形式存储位的数据结构。 请你实现 Bitset 类。 * Bitset(int size) 用 size 个位初始化 Bitset ，所有位都是 0 。 * void fix(int idx) 将下标为 idx 的位上的值更新为 1 。如果值已经是 1 ，则不会发生任何改变。 * void unfix(int idx) 将下标为 idx 的位上的值更新为 0 。如果值已经是 0 ，则不会发生任何改变。 * void flip() 翻转 Bitset 中每一位上的值。换句话说，所有值为 0 的位将会变成 1 ，反之亦然。 * boolean all() 检查 Bitset 中 每一位 的值是否都是 1 。如果满足此条件，返回 true ；否则，返回 false 。 * boolean one() 检查 Bitset 中 是否 至少一位 的值是 1 。如果满足此条件，返回 true ；否则，返回 false 。 * int count() 返回 Bitset 中值为 1 的位的 总数 。 * String toString() 返回 Bitset 的当前组成情况。注意，在结果字符串中，第 i 个下标处的字符应该与 Bitset 中的第 i 位一致。 示例： 输入 ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"] [[5], [3], [1], [], [], [0], [], [], [0], [], []] 输出 [null, null, null, null, false, null, null, true, null, 2, "01010"] 解释 Bitset bs = new Bitset(5); // bitset = "00000". bs.fix(3); // 将 idx = 3 处的值更新为 1 ，此时 bitset = "00010" 。 bs.fix(1); // 将 idx = 1 处的值更新为 1 ，此时 bitset = "01010" 。 bs.flip(); // 翻转每一位上的值，此时 bitset = "10101" 。 bs.all(); // 返回 False ，bitset 中的值不全为 1 。 bs.unfix(0); // 将 idx = 0 处的值更新为 0 ，此时 bitset = "00101" 。 bs.flip(); // 翻转每一位上的值，此时 bitset = "11010" 。 bs.one(); // 返回 True ，至少存在一位的值为 1 。 bs.unfix(0); // 将 idx = 0 处的值更新为 0 ，此时 bitset = "01010" 。 bs.count(); // 返回 2 ，当前有 2 位的值为 1 。 bs.toString(); // 返回 "01010" ，即 bitset 的当前组成情况。 提示： * 1 <= size <= 105 * 0 <= idx <= size - 1 * 至多调用 fix、unfix、flip、all、one、count 和 toString 方法 总共 105 次 * 至少调用 all、one、count 或 toString 方法一次 * 至多调用 toString 方法 5 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储位，并使用一个标志变量来记录是否翻转过。

算法步骤:
1. 初始化时，创建一个大小为 size 的列表，所有位初始化为 0。
2. fix 和 unfix 操作直接修改列表中的值。
3. flip 操作通过翻转标志变量来实现，避免实际翻转列表。
4. all 和 one 操作根据翻转标志和当前的 1 的数量来判断。
5. count 操作返回 1 的数量。
6. toString 操作根据翻转标志生成字符串。

关键点:
- 使用一个标志变量来记录是否翻转过，避免实际翻转列表。
- 维护一个 1 的数量计数器，用于快速计算 count、all 和 one。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作的时间复杂度均为 O(1)。
空间复杂度: O(n) - 使用一个大小为 n 的列表来存储位。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.ones_count = 0

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones_count += 1
        else:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones_count += 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones_count -= 1
        else:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones_count -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones_count = self.size - self.ones_count

    def all(self) -> bool:
        return self.ones_count == self.size

    def one(self) -> bool:
        return self.ones_count > 0

    def count(self) -> int:
        return self.ones_count

    def toString(self) -> str:
        if self.flipped:
            return ''.join('1' if bit == 0 else '0' for bit in self.bits)
        else:
            return ''.join(str(bit) for bit in self.bits)


Solution = create_solution(Bitset)