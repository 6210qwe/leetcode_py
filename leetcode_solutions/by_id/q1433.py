# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1433
标题: Encrypt and Decrypt Strings
难度: hard
链接: https://leetcode.cn/problems/encrypt-and-decrypt-strings/
题目类型: 设计、字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2227. 加密解密字符串 - 给你一个字符数组 keys ，由若干 互不相同 的字符组成。还有一个字符串数组 values ，内含若干长度为 2 的字符串。另给你一个字符串数组 dictionary ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 0 开始字符串的数据结构。 字符串 加密 按下述步骤进行： 1. 对字符串中的每个字符 c ，先从 keys 中找出满足 keys[i] == c 的下标 i 。 2. 在字符串中，用 values[i] 替换字符 c 。 请注意，如果 keys 中不存在字符串中的字符，则无法执行加密过程，返回空字符串 ""。 字符串 解密 按下述步骤进行： 1. 将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。如果存在多个有效的 i ，从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。 2. 在字符串中，用 keys[i] 替换 s 。 实现 Encrypter 类： * Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和 dictionary 初始化 Encrypter 类。 * String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。 * int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。 示例： 输入： ["Encrypter", "encrypt", "decrypt"] [[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]] 输出： [null, "eizfeiam", 2] 解释： Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]); encrypter.encrypt("abcd"); // 返回 "eizfeiam"。 // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。 encrypter.decrypt("eizfeiam"); // return 2. // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为 'd'。 // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和 "cbcd"。 // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary 中出现，所以答案是 2 。 提示： * 1 <= keys.length == values.length <= 26 * values[i].length == 2 * 1 <= dictionary.length <= 100 * 1 <= dictionary[i].length <= 100 * 所有 keys[i] 和 dictionary[i] 互不相同 * 1 <= word1.length <= 2000 * 1 <= word2.length <= 200 * 所有 word1[i] 都出现在 keys 中 * word2.length 是偶数 * keys、values[i]、dictionary[i]、word1 和 word2 只含小写英文字母 * 至多调用 encrypt 和 decrypt 总计 200 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用两个字典来存储加密和解密的映射关系。
- 对于加密，直接通过字符查找对应的值。
- 对于解密，使用深度优先搜索（DFS）来生成所有可能的解密字符串，并检查它们是否在字典中。

算法步骤:
1. 初始化时，构建加密和解密的映射字典。
2. 加密时，遍历输入字符串，根据加密字典替换每个字符。
3. 解密时，使用DFS生成所有可能的解密字符串，并统计在字典中的数量。

关键点:
- 使用字典来快速查找加密和解密的映射。
- 使用DFS生成所有可能的解密字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * 2^k)，其中 n 是输入字符串的长度，m 是字典的长度，k 是解密字符串的长度的一半。
空间复杂度: O(m + k)，其中 m 是字典的长度，k 是解密字符串的长度的一半。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encrypt_map = {key: value for key, value in zip(keys, values)}
        self.decrypt_map = {}
        for key, value in zip(keys, values):
            if value not in self.decrypt_map:
                self.decrypt_map[value] = []
            self.decrypt_map[value].append(key)
        self.dictionary = set(dictionary)

    def encrypt(self, word1: str) -> str:
        encrypted = ""
        for char in word1:
            if char in self.encrypt_map:
                encrypted += self.encrypt_map[char]
            else:
                return ""
        return encrypted

    def decrypt(self, word2: str) -> int:
        def dfs(index, current):
            if index == len(word2):
                if current in self.dictionary:
                    self.count += 1
                return
            if word2[index:index+2] in self.decrypt_map:
                for char in self.decrypt_map[word2[index:index+2]]:
                    dfs(index + 2, current + char)

        self.count = 0
        dfs(0, "")
        return self.count


Solution = create_solution(Encrypter)