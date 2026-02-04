# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1747
标题: Lexicographically Smallest String After Applying Operations
难度: medium
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/
题目类型: 深度优先搜索、广度优先搜索、字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1625. 执行操作后字典序最小的字符串 - 给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。 你可以在 s 上按任意顺序多次执行下面两个操作之一： * 累加：将 a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。当数字超过 9 时，从 0 重新循环计算。例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。 * 轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。 请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。 如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。 示例 1： 输入：s = "5525", a = 9, b = 2 输出："2050" 解释：执行操作如下： 初态："5525" 轮转："2555" 累加："2454" 累加："2353" 轮转："5323" 累加："5222" 累加："5121" 轮转："2151" 累加："2050"​​​​​ 无法获得字典序小于 "2050" 的字符串。 示例 2： 输入：s = "74", a = 5, b = 1 输出："24" 解释：执行操作如下： 初态："74" 轮转："47" 累加："42" 轮转："24"​​​​​ 无法获得字典序小于 "24" 的字符串。 示例 3： 输入：s = "0011", a = 4, b = 2 输出："0011" 解释：无法获得字典序小于 "0011" 的字符串。 提示： * 2 <= s.length <= 100 * s.length 是偶数 * s 仅由数字 0 到 9 组成 * 1 <= a <= 9 * 1 <= b <= s.length - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来遍历所有可能的操作序列，并记录每个状态的最小字典序。

算法步骤:
1. 初始化一个集合 `visited` 来记录已经访问过的状态。
2. 使用一个队列 `queue` 来进行 BFS，初始状态是输入字符串 `s`。
3. 在 BFS 过程中，对于每个状态，分别尝试两种操作：累加和轮转。
4. 对于每种操作生成的新状态，如果未访问过，则将其加入队列并更新最小字典序。
5. 最终返回记录的最小字典序字符串。

关键点:
- 使用集合 `visited` 来避免重复访问同一个状态。
- 使用 BFS 来遍历所有可能的操作序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 其中 n 是字符串的长度。最坏情况下，需要遍历所有可能的状态。
空间复杂度: O(n^2) - 最坏情况下，队列和集合中可能存储所有可能的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_lexicographically_smallest_string(s: str, a: int, b: int) -> str:
    from collections import deque
    
    def add_a_to_odd_indices(s: str, a: int) -> str:
        return ''.join([str((int(c) + a) % 10) if i % 2 == 1 else c for i, c in enumerate(s)])
    
    def rotate_right(s: str, b: int) -> str:
        n = len(s)
        b %= n
        return s[-b:] + s[:-b]
    
    visited = set()
    queue = deque([s])
    min_lexico = s
    
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        min_lexico = min(min_lexico, current)
        
        # Apply the two operations
        new_state_add = add_a_to_odd_indices(current, a)
        new_state_rotate = rotate_right(current, b)
        
        if new_state_add not in visited:
            queue.append(new_state_add)
        if new_state_rotate not in visited:
            queue.append(new_state_rotate)
    
    return min_lexico


Solution = create_solution(find_lexicographically_smallest_string)