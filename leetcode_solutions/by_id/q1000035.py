# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000035
标题: Baby Names LCCI
难度: medium
链接: https://leetcode.cn/problems/baby-names-lcci/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.07. 婴儿名字 - 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。 在结果列表中，选择 字典序最小 的名字作为真实名字。 示例： 输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"] 输出：["John(27)","Chris(36)"] 提示： * names.length <= 100000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理名字的合并，并在合并时选择字典序最小的名字。

算法步骤:
1. 初始化并查集，将每个名字初始化为其自身的父节点。
2. 遍历同义词对，使用并查集将同义词合并，并在合并时选择字典序最小的名字作为根节点。
3. 遍历名字及其频率，使用并查集找到每个名字的根节点，并累加频率到根节点。
4. 构建结果列表，输出每个根节点及其累计频率。

关键点:
- 使用并查集来处理名字的合并。
- 在合并时选择字典序最小的名字作为根节点。
- 使用字典来存储名字及其频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log* n)，其中 n 是名字的数量，m 是同义词对的数量。并查集的操作几乎是常数时间复杂度，log* n 是阿克曼函数的反函数，增长极其缓慢。
空间复杂度: O(n)，需要存储每个名字及其频率。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY

def solution_function_name(names: List[str], synonyms: List[str]) -> List[str]:
    """
    函数式接口 - 实现最优解法
    """
    # 解析同义词对
    synonym_pairs = [s[1:-1].split(',') for s in synonyms]
    
    # 初始化并查集
    uf = UnionFind()
    
    # 合并同义词
    for a, b in synonym_pairs:
        uf.union(a, b)
    
    # 解析名字及其频率
    name_freq = {}
    for name in names:
        name, freq = name.split('(')
        freq = int(freq[:-1])
        name_freq[name] = freq
    
    # 累加频率到根节点
    real_names = {}
    for name, freq in name_freq.items():
        root = uf.find(name)
        if root not in real_names:
            real_names[root] = (name, freq)
        else:
            current_name, current_freq = real_names[root]
            if name < current_name:
                real_names[root] = (name, current_freq + freq)
            else:
                real_names[root] = (current_name, current_freq + freq)
    
    # 构建结果列表
    result = [f"{name}({freq})" for name, freq in real_names.values()]
    return result

Solution = create_solution(solution_function_name)