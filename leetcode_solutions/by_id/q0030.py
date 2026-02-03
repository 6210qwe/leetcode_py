# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 30
标题: Substring with Concatenation of All Words
难度: hard
链接: https://leetcode.cn/problems/substring-with-concatenation-of-all-words/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
30. 串联所有单词的子串 - 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。 s 中的 串联子串 是指一个包含 words 中所有字符串以任意顺序排列连接起来的子串。 * 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。 示例 1： 输入：s = "barfoothefoobarman", words = ["foo","bar"] 输出：[0,9] 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。 输出顺序无关紧要。返回 [9,0] 也是可以的。 示例 2： 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"] 输出：[] 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。 s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。 所以我们返回一个空数组。 示例 3： 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"] 输出：[6,9,12] 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。 提示： * 1 <= s.length <= 104 * 1 <= words.length <= 5000 * 1 <= words[i].length <= 30 * words[i] 和 s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口 + 哈希表，使用滑动窗口检查每个可能的起始位置

算法步骤:
1. 计算目标长度：word_len * words数量
2. 创建words的计数哈希表word_count
3. 对于每个可能的起始位置i（0到word_len-1）：
   - 使用滑动窗口，窗口大小为word_len
   - 维护当前窗口的单词计数current_count
   - 当窗口大小等于目标长度时，检查是否匹配
   - 如果匹配，添加起始位置到结果
4. 返回所有匹配的起始位置

关键点:
- 由于words中所有字符串长度相同，可以按word_len为单位滑动窗口
- 需要从0到word_len-1的每个起始位置开始，确保不遗漏
- 使用哈希表记录words中每个单词的出现次数
- 时间复杂度O(n*m)，n为s长度，m为words长度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*m) - n为s长度，m为words长度，需要检查n个起始位置，每个位置需要O(m)时间
空间复杂度: O(m) - 需要存储words的哈希表，m为words长度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter
from leetcode_solutions.utils.solution import create_solution


def find_substring(s: str, words: List[str]) -> List[int]:
    """
    函数式接口 - 滑动窗口 + 哈希表实现
    
    实现思路:
    使用滑动窗口检查每个可能的起始位置，使用哈希表记录words中每个单词的出现次数。
    
    Args:
        s: 主字符串
        words: 单词数组
        
    Returns:
        所有串联子串在s中的开始索引列表
        
    Example:
        >>> find_substring("barfoothefoobarman", ["foo","bar"])
        [0, 9]
        >>> find_substring("wordgoodgoodgoodbestword", ["word","good","best","word"])
        []
    """
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = Counter(words)
    result = []
    
    # 对于每个可能的起始位置（0到word_len-1）
    for start in range(word_len):
        left = start
        current_count = Counter()
        
        # 滑动窗口
        for right in range(start, len(s) - word_len + 1, word_len):
            word = s[right:right + word_len]
            
            # 如果word不在words中，重置窗口
            if word not in word_count:
                current_count.clear()
                left = right + word_len
                continue
            
            # 添加当前单词到计数
            current_count[word] += 1
            
            # 如果当前单词出现次数超过words中的次数，移动左边界
            while current_count[word] > word_count[word]:
                left_word = s[left:left + word_len]
                current_count[left_word] -= 1
                left += word_len
            
            # 如果窗口大小等于目标长度，找到匹配
            if right - left + word_len == total_len:
                result.append(left)
                # 移动左边界
                left_word = s[left:left + word_len]
                current_count[left_word] -= 1
                left += word_len
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_substring)
