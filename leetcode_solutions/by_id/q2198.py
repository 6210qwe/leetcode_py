# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2198
标题: Process Restricted Friend Requests
难度: hard
链接: https://leetcode.cn/problems/process-restricted-friend-requests/
题目类型: 并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2076. 处理含限制条件的好友请求 - 给你一个整数 n ，表示网络上的用户数目。每个用户按从 0 到 n - 1 进行编号。 给你一个下标从 0 开始的二维整数数组 restrictions ，其中 restrictions[i] = [xi, yi] 意味着用户 xi 和用户 yi 不能 成为 朋友 ，不管是 直接 还是通过其他用户 间接 。 最初，用户里没有人是其他用户的朋友。给你一个下标从 0 开始的二维整数数组 requests 表示好友请求的列表，其中 requests[j] = [uj, vj] 是用户 uj 和用户 vj 之间的一条好友请求。 如果 uj 和 vj 可以成为 朋友 ，那么好友请求将会 成功 。每个好友请求都会按列表中给出的顺序进行处理（即，requests[j] 会在 requests[j + 1] 前）。一旦请求成功，那么对所有未来的好友请求而言， uj 和 vj 将会 成为直接朋友 。 返回一个 布尔数组 result ，其中元素遵循此规则：如果第 j 个好友请求 成功 ，那么 result[j] 就是 true ；否则，为 false 。 注意：如果 uj 和 vj 已经是直接朋友，那么他们之间的请求将仍然 成功 。 示例 1： 输入：n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]] 输出：[true,false] 解释： 请求 0 ：用户 0 和 用户 2 可以成为朋友，所以他们成为直接朋友。 请求 1 ：用户 2 和 用户 1 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (1--2--0) 。 示例 2： 输入：n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]] 输出：[true,false] 解释： 请求 0 ：用户 1 和 用户 2 可以成为朋友，所以他们成为直接朋友。 请求 1 ：用户 0 和 用户 2 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (0--2--1) 。 示例 3： 输入：n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]] 输出：[true,false,true,false] 解释： 请求 0 ：用户 0 和 用户 4 可以成为朋友，所以他们成为直接朋友。 请求 1 ：用户 1 和 用户 2 不能成为朋友，因为他们之间存在限制。 请求 2 ：用户 3 和 用户 1 可以成为朋友，所以他们成为直接朋友。 请求 3 ：用户 3 和 用户 4 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (0--4--3--1) 。 提示： * 2 <= n <= 1000 * 0 <= restrictions.length <= 1000 * restrictions[i].length == 2 * 0 <= xi, yi <= n - 1 * xi != yi * 1 <= requests.length <= 1000 * requests[j].length == 2 * 0 <= uj, vj <= n - 1 * uj != vj
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来管理用户之间的关系，并在处理每个请求时检查是否违反了限制条件。

算法步骤:
1. 初始化并查集，每个用户的父节点指向自己。
2. 对于每个好友请求，找到两个用户所在的集合。
3. 检查这两个集合中的任意一对用户是否在限制条件中，如果在则拒绝该请求。
4. 如果没有违反限制条件，则合并这两个集合。
5. 记录每个请求的结果。

关键点:
- 使用路径压缩和按秩合并来优化并查集的操作。
- 在处理每个请求时，需要检查两个集合中的所有用户对是否在限制条件中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * α(n))，其中 n 是用户数量，m 是请求数量，α 是反阿克曼函数。
空间复杂度: O(n + k)，其中 n 是用户数量，k 是限制条件的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def process_friend_requests(n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
    uf = UnionFind(n)
    restriction_set = {tuple(sorted(pair)) for pair in restrictions}
    results = []
    
    for u, v in requests:
        root_u = uf.find(u)
        root_v = uf.find(v)
        
        if root_u == root_v:
            results.append(True)
            continue
        
        # Check if the union of the two sets would violate any restrictions
        for i in range(n):
            if uf.find(i) == root_u:
                for j in range(n):
                    if uf.find(j) == root_v and (i, j) in restriction_set:
                        results.append(False)
                        break
                else:
                    continue
                break
        else:
            uf.union(root_u, root_v)
            results.append(True)
    
    return results

Solution = create_solution(process_friend_requests)