# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1097
标题: Stream of Characters
难度: hard
链接: https://leetcode.cn/problems/stream-of-characters/
题目类型: 设计、字典树、数组、字符串、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1032. 字符流 - 设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 words 中的一个字符串。 例如，words = ["abc", "xyz"] 且字符流中逐个依次加入 4 个字符 'a'、'x'、'y' 和 'z' ，你所设计的算法应当可以检测到 "axyz" 的后缀 "xyz" 与 words 中的字符串 "xyz" 匹配。 按下述要求实现 StreamChecker 类： * StreamChecker(String[] words) ：构造函数，用字符串数组 words 初始化数据结构。 * boolean query(char letter)：从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 words 中的某一字符串，返回 true ；否则，返回 false。 示例： 输入： ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"] [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]] 输出： [null, false, false, false, true, false, true, false, false, false, false, false, true] 解释： StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]); streamChecker.query("a"); // 返回 False streamChecker.query("b"); // 返回 False streamChecker.query("c"); // 返回n False streamChecker.query("d"); // 返回 True ，因为 'cd' 在 words 中 streamChecker.query("e"); // 返回 False streamChecker.query("f"); // 返回 True ，因为 'f' 在 words 中 streamChecker.query("g"); // 返回 False streamChecker.query("h"); // 返回 False streamChecker.query("i"); // 返回 False streamChecker.query("j"); // 返回 False streamChecker.query("k"); // 返回 False streamChecker.query("l"); // 返回 True ，因为 'kl' 在 words 中 提示： * 1 <= words.length <= 2000 * 1 <= words[i].length <= 200 * words[i] 由小写英文字母组成 * letter 是一个小写英文字母 * 最多调用查询 4 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储所有单词的逆序形式，然后在查询时从当前字符流的末尾开始匹配。

算法步骤:
1. 构造 Trie 树，将每个单词的逆序形式插入到 Trie 中。
2. 在每次查询时，从当前字符流的末尾开始，逐步向前匹配 Trie 树中的节点。
3. 如果匹配到一个完整的单词，则返回 True；否则，继续匹配直到字符流的开头或匹配失败。

关键点:
- 使用 Trie 树来高效地存储和查询单词的逆序形式。
- 在查询时从字符流的末尾开始匹配，确保匹配到的是后缀。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是 words 的长度，n 是 words 中最长单词的长度。构建 Trie 树的时间复杂度为 O(m * n)，每次查询的时间复杂度为 O(n)。
空间复杂度: O(m * n)，Trie 树的空间复杂度取决于所有单词的总长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie_root = TrieNode()
        self.stream = []
        
        # 将每个单词的逆序形式插入到 Trie 树中
        for word in words:
            node = self.trie_root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie_root
        
        # 从字符流的末尾开始匹配
        for char in reversed(self.stream):
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end_of_word:
                return True
        return False


# 测试用例
if __name__ == "__main__":
    stream_checker = StreamChecker(["cd", "f", "kl"])
    print(stream_checker.query("a"))  # False
    print(stream_checker.query("b"))  # False
    print(stream_checker.query("c"))  # False
    print(stream_checker.query("d"))  # True
    print(stream_checker.query("e"))  # False
    print(stream_checker.query("f"))  # True
    print(stream_checker.query("g"))  # False
    print(stream_checker.query("h"))  # False
    print(stream_checker.query("i"))  # False
    print(stream_checker.query("j"))  # False
    print(stream_checker.query("k"))  # False
    print(stream_checker.query("l"))  # True