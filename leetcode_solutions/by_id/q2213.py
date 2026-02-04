# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2213
标题: Find All People With Secret
难度: hard
链接: https://leetcode.cn/problems/find-all-people-with-secret/
题目类型: 深度优先搜索、广度优先搜索、并查集、图、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2092. 找出知晓秘密的所有专家 - 给你一个整数 n ，表示有 n 个专家从 0 到 n - 1 编号。另外给你一个下标从 0 开始的二维整数数组 meetings ，其中 meetings[i] = [xi, yi, timei] 表示专家 xi 和专家 yi 在时间 timei 要开一场会。一个专家可以同时参加 多场会议 。最后，给你一个整数 firstPerson 。 专家 0 有一个 秘密 ，最初，他在时间 0 将这个秘密分享给了专家 firstPerson 。接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播。更正式的表达是，每次会议，如果专家 xi 在时间 timei 时知晓这个秘密，那么他将会与专家 yi 分享这个秘密，反之亦然。 秘密共享是 瞬时发生 的。也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享。 在所有会议都结束之后，返回所有知晓这个秘密的专家列表。你可以按 任何顺序 返回答案。 示例 1： 输入：n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1 输出：[0,1,2,3,5] 解释： 时间 0 ，专家 0 将秘密与专家 1 共享。 时间 5 ，专家 1 将秘密与专家 2 共享。 时间 8 ，专家 2 将秘密与专家 3 共享。 时间 10 ，专家 1 将秘密与专家 5 共享。 因此，在所有会议结束后，专家 0、1、2、3 和 5 都将知晓这个秘密。 示例 2： 输入：n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3 输出：[0,1,3] 解释： 时间 0 ，专家 0 将秘密与专家 3 共享。 时间 2 ，专家 1 与专家 2 都不知晓这个秘密。 时间 3 ，专家 3 将秘密与专家 0 和专家 1 共享。 因此，在所有会议结束后，专家 0、1 和 3 都将知晓这个秘密。 示例 3： 输入：n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1 输出：[0,1,2,3,4] 解释： 时间 0 ，专家 0 将秘密与专家 1 共享。 时间 1 ，专家 1 将秘密与专家 2 共享，专家 2 将秘密与专家 3 共享。 注意，专家 2 可以在收到秘密的同一时间分享此秘密。 时间 2 ，专家 3 将秘密与专家 4 共享。 因此，在所有会议结束后，专家 0、1、2、3 和 4 都将知晓这个秘密。 提示： * 2 <= n <= 105 * 1 <= meetings.length <= 105 * meetings[i].length == 3 * 0 <= xi, yi <= n - 1 * xi != yi * 1 <= timei <= 105 * 1 <= firstPerson <= n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来追踪每个专家是否知晓秘密，并使用广度优先搜索（BFS）来处理同一时间的会议。

算法步骤:
1. 初始化并查集，将专家 0 和 firstPerson 连接。
2. 按时间对会议进行排序。
3. 对于每个时间点，使用 BFS 处理该时间点的所有会议，更新并查集。
4. 最后，通过并查集找出所有知晓秘密的专家。

关键点:
- 使用并查集来高效管理专家之间的连接关系。
- 使用 BFS 来处理同一时间的会议，确保秘密在同一时间点内传播。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m log m + n + m)，其中 m 是 meetings 的长度，n 是专家的数量。排序操作的时间复杂度为 O(m log m)，并查集和 BFS 的操作总时间为 O(n + m)。
空间复杂度: O(n + m)，并查集需要 O(n) 的空间，存储会议需要 O(m) 的空间。
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
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def solution_function_name(n: int, meetings: List[List[int]], first_person: int) -> List[int]:
    # 初始化并查集
    uf = UnionFind(n)
    uf.union(0, first_person)
    
    # 按时间对会议进行排序
    meetings.sort(key=lambda x: x[2])
    
    # 处理每个时间点的会议
    i = 0
    while i < len(meetings):
        current_time = meetings[i][2]
        groups = {}
        
        # 处理当前时间点的所有会议
        while i < len(meetings) and meetings[i][2] == current_time:
            x, y, _ = meetings[i]
            root_x = uf.find(x)
            root_y = uf.find(y)
            
            if root_x not in groups:
                groups[root_x] = set()
            if root_y not in groups:
                groups[root_y] = set()
            
            groups[root_x].add(x)
            groups[root_y].add(y)
            
            i += 1
        
        # 合并当前时间点的所有组
        for group in groups.values():
            if any(uf.find(expert) == uf.find(0) for expert in group):
                for expert in group:
                    uf.union(expert, 0)
    
    # 返回所有知晓秘密的专家
    return [i for i in range(n) if uf.find(i) == uf.find(0)]


Solution = create_solution(solution_function_name)