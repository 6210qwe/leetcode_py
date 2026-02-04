# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 721
标题: Accounts Merge
难度: medium
链接: https://leetcode.cn/problems/accounts-merge/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
721. 账户合并 - 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。 示例 1： 输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]] 输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]] 解释： 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']， ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。 示例 2： 输入：accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]] 输出：[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]] 提示： * 1 <= accounts.length <= 1000 * 2 <= accounts[i].length <= 10 * 1 <= accounts[i][j].length <= 30 * accounts[i][0] 由英文字母组成 * accounts[i][j] (for j > 0) 是有效的邮箱地址
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并具有相同邮箱的账户。

算法步骤:
1. 初始化并查集，用于存储每个邮箱对应的索引。
2. 遍历每个账户，将每个邮箱映射到当前账户的索引，并将所有邮箱连接起来。
3. 构建结果，将每个连通分量中的邮箱收集起来，并按字典序排序。
4. 将每个连通分量的结果添加到最终结果中。

关键点:
- 使用并查集来高效地合并和查找连通分量。
- 使用字典来存储每个邮箱对应的索引，以便快速查找。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * log(m))，其中 n 是账户数量，m 是每个账户的平均邮箱数量。排序操作的时间复杂度为 O(m * log(m))。
空间复杂度: O(n * m)，存储并查集和邮箱索引。
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


def solution_function_name(accounts: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 实现最优解法
    """
    n = len(accounts)
    uf = UnionFind(n)
    email_to_index = {}

    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_index:
                uf.union(email_to_index[email], i)
            else:
                email_to_index[email] = i

    index_to_emails = {}
    for email, index in email_to_index.items():
        root = uf.find(index)
        if root not in index_to_emails:
            index_to_emails[root] = []
        index_to_emails[root].append(email)

    result = []
    for index, emails in index_to_emails.items():
        name = accounts[index][0]
        emails.sort()
        result.append([name] + emails)

    return result


Solution = create_solution(solution_function_name)