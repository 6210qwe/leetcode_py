# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1728
标题: Fancy Sequence
难度: hard
链接: https://leetcode.cn/problems/fancy-sequence/
题目类型: 设计、线段树、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1622. 奇妙序列 - 请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。 请实现 Fancy 类 ： * Fancy() 初始化一个空序列对象。 * void append(val) 将整数 val 添加在序列末尾。 * void addAll(inc) 将所有序列中的现有数值都增加 inc 。 * void multAll(m) 将序列中的所有现有数值都乘以整数 m 。 * int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 109 + 7 取余。如果下标大于等于序列的长度，请返回 -1 。 示例： 输入： ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"] [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]] 输出： [null, null, null, null, null, 10, null, null, null, 26, 34, 20] 解释： Fancy fancy = new Fancy(); fancy.append(2); // 奇妙序列：[2] fancy.addAll(3); // 奇妙序列：[2+3] -> [5] fancy.append(7); // 奇妙序列：[5, 7] fancy.multAll(2); // 奇妙序列：[5*2, 7*2] -> [10, 14] fancy.getIndex(0); // 返回 10 fancy.addAll(3); // 奇妙序列：[10+3, 14+3] -> [13, 17] fancy.append(10); // 奇妙序列：[13, 17, 10] fancy.multAll(2); // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20] fancy.getIndex(0); // 返回 26 fancy.getIndex(1); // 返回 34 fancy.getIndex(2); // 返回 20 提示： * 1 <= val, inc, m <= 100 * 0 <= idx <= 105 * 总共最多会有 105 次对 append，addAll，multAll 和 getIndex 的调用。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用懒惰更新和逆元来高效处理批量操作。

算法步骤:
1. 初始化时，维护一个序列 `seq` 和两个变量 `add` 和 `mul` 来记录当前的加法和乘法操作。
2. 在 `append` 操作时，将值添加到序列中，并记录当前的 `add` 和 `mul`。
3. 在 `addAll` 操作时，更新 `add`。
4. 在 `multAll` 操作时，更新 `mul` 和 `add`。
5. 在 `getIndex` 操作时，根据记录的 `add` 和 `mul` 计算出正确的值。

关键点:
- 使用逆元来处理乘法操作的撤销。
- 通过懒惰更新来减少不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) 对于每个操作（append, addAll, multAll, getIndex）。
空间复杂度: O(n) 其中 n 是序列的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1
        self.inv = 1

    def append(self, val: int) -> None:
        # 记录当前的 add 和 mul，并将值添加到序列中
        self.seq.append((val - self.add) * pow(self.mul, MOD - 2, MOD) % MOD)

    def addAll(self, inc: int) -> None:
        # 更新 add
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        # 更新 mul 和 add
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD
        self.inv = (self.inv * pow(m, MOD - 2, MOD)) % MOD

    def getIndex(self, idx: int) -> int:
        # 如果索引超出范围，返回 -1
        if idx >= len(self.seq):
            return -1
        # 根据记录的 add 和 mul 计算出正确的值
        return (self.seq[idx] * self.mul + self.add) % MOD


Solution = create_solution(Fancy)