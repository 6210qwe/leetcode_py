# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 873
标题: Guess the Word
难度: hard
链接: https://leetcode.cn/problems/guess-the-word/
题目类型: 数组、数学、字符串、博弈、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
843. 猜猜这个单词 - 给你一个由 不同 字符串组成的单词列表 words ，其中 words[i] 长度均为 6 。words 中的一个单词将被选作秘密单词 secret 。 另给你一个辅助对象 Master ，你可以调用 Master.guess(word) 来猜单词，其中参数 word 长度为 6 且必须是 words 中的字符串。 Master.guess(word) 将会返回如下结果： * 如果 word 不是 words 中的字符串，返回 -1 ，或者 * 一个整数，表示你所猜测的单词 word 与 秘密单词 secret 的准确匹配（值和位置同时匹配）的数目。 每组测试用例都会包含一个参数 allowedGuesses ，其中 allowedGuesses 是你可以调用 Master.guess(word) 的最大次数。 对于每组测试用例，在不超过允许猜测的次数的前提下，你应该调用 Master.guess 来猜出秘密单词。最终，你将会得到以下结果： * 如果你调用 Master.guess 的次数大于 allowedGuesses 所限定的次数或者你没有用 Master.guess 猜到秘密单词，则得到 "Either you took too many guesses, or you did not find the secret word." 。 * 如果你调用 Master.guess 猜到秘密单词，且调用 Master.guess 的次数小于或等于 allowedGuesses ，则得到 "You guessed the secret word correctly." 。 生成的测试用例保证你可以利用某种合理的策略（而不是暴力）猜到秘密单词。 示例 1： 输入：secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10 输出：You guessed the secret word correctly. 解释： master.guess("aaaaaa") 返回 -1 ，因为 "aaaaaa" 不在 words 中。 master.guess("acckzz") 返回 6 ，因为 "acckzz" 是秘密单词 secret ，共有 6 个字母匹配。 master.guess("ccbazz") 返回 3 ，因为 "ccbazz" 共有 3 个字母匹配。 master.guess("eiowzz") 返回 2 ，因为 "eiowzz" 共有 2 个字母匹配。 master.guess("abcczz") 返回 4 ，因为 "abcczz" 共有 4 个字母匹配。 一共调用 5 次 master.guess ，其中一个为秘密单词，所以通过测试用例。 示例 2： 输入：secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10 输出：You guessed the secret word correctly. 解释：共有 2 个单词，且其中一个为秘密单词，可以通过测试用例。 提示： * 1 <= words.length <= 100 * words[i].length == 6 * words[i] 仅由小写英文字母组成 * words 中所有字符串 互不相同 * secret 存在于 words 中 * 10 <= allowedGuesses <= 30
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Minimax 策略来选择最优的猜测单词，以最小化最坏情况下的剩余可能单词数量。

算法步骤:
1. 定义一个函数 `match_count` 来计算两个单词之间的匹配字符数。
2. 定义一个函数 `minimax_score` 来计算每个单词的 Minimax 分数。
3. 在每次猜测时，选择具有最小 Minimax 分数的单词进行猜测。
4. 根据 Master.guess 的返回值更新剩余可能的单词列表。
5. 重复上述步骤直到找到秘密单词或达到最大猜测次数。

关键点:
- 使用 Minimax 策略来选择最优的猜测单词。
- 通过匹配字符数来更新剩余可能的单词列表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是 words 的长度，m 是单词的长度（固定为 6）。
空间复杂度: O(n)，用于存储剩余可能的单词列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def match_count(word1: str, word2: str) -> int:
            """计算两个单词之间的匹配字符数。"""
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        def minimax_score(word: str, possible_words: List[str]) -> int:
            """计算单词的 Minimax 分数。"""
            score_distribution = [0] * 7
            for p_word in possible_words:
                if p_word != word:
                    score_distribution[match_count(word, p_word)] += 1
            return max(score_distribution)

        possible_words = wordlist[:]
        while possible_words:
            # 选择具有最小 Minimax 分数的单词进行猜测
            best_guess = min(possible_words, key=lambda word: minimax_score(word, possible_words))
            match_num = master.guess(best_guess)
            if match_num == 6:
                return
            # 更新剩余可能的单词列表
            possible_words = [word for word in possible_words if match_count(word, best_guess) == match_num]

Solution = create_solution(Solution)