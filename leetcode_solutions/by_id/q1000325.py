# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000325
标题: 实现 Trie (前缀树)
难度: medium
链接: https://leetcode.cn/problems/QC3q1f/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 062. 实现 Trie (前缀树) - Trie [https://baike.baidu.com/item/字典树/9825209?fr=aladdin]（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。 请你实现 Trie 类： * Trie() 初始化前缀树对象。 * void insert(String word) 向前缀树中插入字符串 word 。 * boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。 * boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。 示例： 输入 inputs = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"] inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]] 输出 [null, null, true, false, true, null, true] 解释 Trie trie = new Trie(); trie.insert("apple"); trie.search("apple"); // 返回 True trie.search("app"); // 返回 False trie.startsWith("app"); // 返回 True trie.insert("app"); trie.search("app"); // 返回 True 提示： * 1 <= word.length, prefix.length <= 2000 * word 和 prefix 仅由小写英文字母组成 * insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次 注意：本题与主站 208 题相同：https://leetcode.cn/problems/implement-trie-prefix-tree/ [https://leetcode.cn/problems/implement-trie-prefix-tree/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
