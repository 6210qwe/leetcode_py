# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 676
标题: Implement Magic Dictionary
难度: medium
链接: https://leetcode.cn/problems/implement-magic-dictionary/
题目类型: 深度优先搜索、设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
676. 实现一个魔法字典 - 设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。 实现 MagicDictionary 类： * MagicDictionary() 初始化对象 * void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同 * bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。 示例： 输入 ["MagicDictionary", "buildDict", "search", "search", "search", "search"] [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]] 输出 [null, null, false, true, false, false] 解释 MagicDictionary magicDictionary = new MagicDictionary(); magicDictionary.buildDict(["hello", "leetcode"]); magicDictionary.search("hello"); // 返回 False magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True magicDictionary.search("hell"); // 返回 False magicDictionary.search("leetcoded"); // 返回 False 提示： * 1 <= dictionary.length <= 100 * 1 <= dictionary[i].length <= 100 * dictionary[i] 仅由小写英文字母组成 * dictionary 中的所有字符串 互不相同 * 1 <= searchWord.length <= 100 * searchWord 仅由小写英文字母组成 * buildDict 仅在 search 之前调用一次 * 最多调用 100 次 search
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 按长度分组 + 暴力比较差异位置

算法步骤:
1. 使用字典按单词长度分组存储所有单词，例如 buckets[len(word)] 存放所有该长度的单词
2. buildDict(dictionary):
   - 遍历字典中的每个单词，按长度加入对应分组
3. search(searchWord):
   - 若 searchWord 的长度在 buckets 中不存在，直接返回 False
   - 否则遍历该长度分组中的每个单词 word：
       统计与 searchWord 不同的字符个数 diff
       若 diff 恰好为 1，则返回 True
   - 遍历结束未找到则返回 False

关键点:
- 题目数据范围很小（最多 100 个单词，长度最多 100），直接暴力比较即可
- 需要保证“恰好一个字符不同”
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度:
- buildDict: O(N * L) - N 为单词数，L 为平均长度
- search: O(M * L) - M 为同长度单词数
空间复杂度: O(N * L) - 存储所有单词
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode


class MagicDictionary:
    """
    实现一个魔法字典
    """

    def __init__(self):
        # 按长度分组存储单词
        self.buckets: dict[int, List[str]] = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            length = len(word)
            if length not in self.buckets:
                self.buckets[length] = []
            self.buckets[length].append(word)

    def search(self, searchWord: str) -> bool:
        length = len(searchWord)
        if length not in self.buckets:
            return False

        for word in self.buckets[length]:
            diff = 0
            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False


# 注意：本题在 LeetCode 上直接使用 MagicDictionary 类，不通过 create_solution
