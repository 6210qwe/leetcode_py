# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3541
标题: Report Spam Message
难度: medium
链接: https://leetcode.cn/problems/report-spam-message/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3295. 举报垃圾信息 - 给你一个字符串数组 message 和一个字符串数组 bannedWords。 如果数组中 至少 存在两个单词与 bannedWords 中的任一单词 完全相同，则该数组被视为 垃圾信息。 如果数组 message 是垃圾信息，则返回 true；否则返回 false。 示例 1： 输入： message = ["hello","world","leetcode"], bannedWords = ["world","hello"] 输出： true 解释： 数组 message 中的 "hello" 和 "world" 都出现在数组 bannedWords 中。 示例 2： 输入： message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"] 输出： false 解释： 数组 message 中只有一个单词（"programming"）出现在数组 bannedWords 中。 提示： * 1 <= message.length, bannedWords.length <= 105 * 1 <= message[i].length, bannedWords[i].length <= 15 * message[i] 和 bannedWords[i] 都只由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来存储被禁止的单词，并遍历消息数组，统计出现的次数。

算法步骤:
1. 将 `bannedWords` 转换为集合以提高查找效率。
2. 初始化一个计数器 `count` 用于记录 `message` 中出现的被禁止单词的数量。
3. 遍历 `message` 数组，如果某个单词在 `bannedWords` 集合中，增加计数器 `count`。
4. 如果 `count` 达到 2 或更多，返回 `True` 表示是垃圾信息，否则返回 `False`。

关键点:
- 使用集合来存储 `bannedWords` 以实现 O(1) 的查找时间复杂度。
- 只需要遍历一次 `message` 数组即可完成判断。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `message` 的长度，m 是 `bannedWords` 的长度。
空间复杂度: O(m)，存储 `bannedWords` 集合所需的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def solution_function_name(message: List[str], bannedWords: List[str]) -> bool:
    """
    函数式接口 - 判断给定的消息数组是否包含至少两个被禁止的单词。
    """
    # 将 bannedWords 转换为集合以提高查找效率
    banned_set = set(bannedWords)
    
    # 初始化计数器
    count = 0
    
    # 遍历 message 数组
    for word in message:
        if word in banned_set:
            count += 1
            if count >= 2:
                return True
    
    return False

Solution = create_solution(solution_function_name)