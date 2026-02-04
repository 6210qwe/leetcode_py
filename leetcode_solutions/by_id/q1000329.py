# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000329
标题: 单词的压缩编码
难度: medium
链接: https://leetcode.cn/problems/iSwD2y/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 065. 单词的压缩编码 - 单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足： * words.length == indices.length * 助记字符串 s 以 '#' 字符结尾 * 对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等 给定一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。 示例 1： 输入：words = ["time", "me", "bell"] 输出：10 解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。 words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#" words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#" words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#" 示例 2： 输入：words = ["t"] 输出：2 解释：一组有效编码为 s = "t#" 和 indices = [0] 。 提示： * 1 <= words.length <= 2000 * 1 <= words[i].length <= 7 * words[i] 仅由小写字母组成 注意：本题与主站 820 题相同： https://leetcode.cn/problems/short-encoding-of-words/ [https://leetcode.cn/problems/short-encoding-of-words/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储单词的反序，这样可以有效地找到所有后缀相同的单词，并将其合并。

算法步骤:
1. 反转每个单词并存入集合中。
2. 将反转后的单词插入字典树。
3. 遍历字典树，计算每个叶子节点的深度，累加这些深度得到最终结果。

关键点:
- 反转单词以便处理后缀。
- 使用字典树来存储和查找单词。
- 计算每个叶子节点的深度并累加。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是单词的数量，m 是单词的最大长度。
空间复杂度: O(n * m)，存储所有单词的反转和字典树的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_leaf_depths(self) -> int:
        def dfs(node, depth):
            if not node.children:
                return depth + 1
            total_depth = 0
            for child in node.children.values():
                total_depth += dfs(child, depth + 1)
            return total_depth

        return dfs(self.root, 0)

def solution_function_name(words: List[str]) -> int:
    """
    函数式接口 - 返回成功对 words 进行编码的最小助记字符串 s 的长度
    """
    # 反转每个单词并去重
    reversed_words = set(word[::-1] for word in words)
    
    # 创建字典树
    trie = Trie()
    
    # 插入反转后的单词
    for word in reversed_words:
        trie.insert(word)
    
    # 计算每个叶子节点的深度并累加
    return trie.get_leaf_depths()

Solution = create_solution(solution_function_name)