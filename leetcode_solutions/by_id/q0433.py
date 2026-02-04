# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 433
标题: Minimum Genetic Mutation
难度: medium
链接: https://leetcode.cn/problems/minimum-genetic-mutation/
题目类型: 广度优先搜索、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
433. 最小基因变化 - 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。 * 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中） 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。 示例 1： 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"] 输出：1 示例 2： 输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"] 输出：2 示例 3： 输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"] 输出：3 提示： * start.length == 8 * end.length == 8 * 0 <= bank.length <= 10 * bank[i].length == 8 * start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从 start 到 end 的最短路径。

算法步骤:
1. 初始化一个队列，将 start 加入队列，并设置初始步数为 0。
2. 使用一个集合来记录已经访问过的基因序列，避免重复访问。
3. 开始 BFS 循环：
   - 从队列中取出当前基因序列和当前步数。
   - 如果当前基因序列等于 end，则返回当前步数。
   - 否则，生成所有可能的单字符变化后的基因序列。
   - 对于每个新生成的基因序列，如果它在基因库中且未被访问过，则将其加入队列并标记为已访问。
4. 如果遍历完所有可能的基因序列仍未找到 end，则返回 -1。

关键点:
- 使用 BFS 保证找到的路径是最短的。
- 使用集合来记录已访问的基因序列，避免重复计算。
- 优化时间和空间复杂度，确保每次只处理必要的基因序列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m) - n 是基因库的长度，m 是基因序列的长度（固定为 8）。
空间复杂度: O(n) - 主要用于存储队列和已访问的基因序列。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_genetic_mutation(start: str, end: str, bank: List[str]) -> int:
    """
    函数式接口 - 使用广度优先搜索 (BFS) 来找到从 start 到 end 的最短路径。
    
    实现思路:
    使用 BFS 保证找到的路径是最短的，使用集合来记录已访问的基因序列，避免重复计算。
    
    Args:
        start: 起始基因序列
        end: 目标基因序列
        bank: 基因库
        
    Returns:
        返回从 start 变化到 end 所需的最少变化次数，如果无法完成则返回 -1。
        
    Example:
        >>> minimum_genetic_mutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
        1
    """
    if end not in bank:
        return -1

    from collections import deque
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps

        for i in range(8):
            for char in "ACGT":
                next_gene = current[:i] + char + current[i+1:]
                if next_gene in bank and next_gene not in visited:
                    visited.add(next_gene)
                    queue.append((next_gene, steps + 1))

    return -1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(minimum_genetic_mutation)