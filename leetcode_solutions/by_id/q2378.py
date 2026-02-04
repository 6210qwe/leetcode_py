# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2378
标题: Sender With Largest Word Count
难度: medium
链接: https://leetcode.cn/problems/sender-with-largest-word-count/
题目类型: 数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2284. 最多单词数的发件人 - 给你一个聊天记录，共包含 n 条信息。给你两个字符串数组 messages 和 senders ，其中 messages[i] 是 senders[i] 发出的一条 信息 。 一条 信息 是若干用单个空格连接的 单词 ，信息开头和结尾不会有多余空格。发件人的 单词计数 是这个发件人总共发出的 单词数 。注意，一个发件人可能会发出多于一条信息。 请你返回发出单词数 最多 的发件人名字。如果有多个发件人发出最多单词数，请你返回 字典序 最大的名字。 注意： * 字典序里，大写字母小于小写字母。 * "Alice" 和 "alice" 是不同的名字。 示例 1： 输入：messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"] 输出："Alice" 解释：Alice 总共发出了 2 + 3 = 5 个单词。 userTwo 发出了 2 个单词。 userThree 发出了 3 个单词。 由于 Alice 发出单词数最多，所以我们返回 "Alice" 。 示例 2： 输入：messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"] 输出："Charlie" 解释：Bob 总共发出了 5 个单词。 Charlie 总共发出了 5 个单词。 由于最多单词数打平，返回字典序最大的名字，也就是 Charlie 。 提示： * n == messages.length == senders.length * 1 <= n <= 104 * 1 <= messages[i].length <= 100 * 1 <= senders[i].length <= 10 * messages[i] 包含大写字母、小写字母和 ' ' 。 * messages[i] 中所有单词都由 单个空格 隔开。 * messages[i] 不包含前导和后缀空格。 * senders[i] 只包含大写英文字母和小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个发件人的单词总数，然后找到单词总数最多的发件人。如果有多个发件人单词总数相同，则返回字典序最大的发件人。

算法步骤:
1. 初始化一个哈希表 `word_count`，用于记录每个发件人的单词总数。
2. 遍历 `messages` 和 `senders` 数组，对于每条消息，计算其单词数并更新对应发件人的单词总数。
3. 找到单词总数最多的发件人。如果有多个发件人单词总数相同，则返回字典序最大的发件人。

关键点:
- 使用哈希表记录每个发件人的单词总数。
- 使用 `split` 方法来计算每条消息的单词数。
- 使用 `max` 函数结合自定义键函数来找到单词总数最多的发件人。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 messages 的长度，m 是每条消息的平均长度。
空间复杂度: O(n)，哈希表的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(messages: List[str], senders: List[str]) -> str:
    """
    函数式接口 - 返回发出单词数最多的发件人名字
    """
    word_count = {}
    
    # 计算每个发件人的单词总数
    for i in range(len(messages)):
        sender = senders[i]
        message = messages[i]
        if sender not in word_count:
            word_count[sender] = 0
        word_count[sender] += len(message.split())
    
    # 找到单词总数最多的发件人
    max_sender = max(word_count.items(), key=lambda x: (x[1], x[0]))
    
    return max_sender[0]


Solution = create_solution(solution_function_name)