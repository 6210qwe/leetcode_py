# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2134
标题: Maximize the Confusion of an Exam
难度: medium
链接: https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/
题目类型: 字符串、二分查找、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2024. 考试的最大困扰度 - 一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。 给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数： * 每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。 请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。 示例 1： 输入：answerKey = "TTFF", k = 2 输出：4 解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。 总共有四个连续的 'T' 。 示例 2： 输入：answerKey = "TFFT", k = 1 输出：3 解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。 或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。 两种情况下，都有三个连续的 'F' 。 示例 3： 输入：answerKey = "TTFTTFTT", k = 1 输出：5 解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。 或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。 两种情况下，都有五个连续的 'T' 。 提示： * n == answerKey.length * 1 <= n <= 5 * 104 * answerKey[i] 要么是 'T' ，要么是 'F' * 1 <= k <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最长的连续子数组，使得在不超过 k 次操作的情况下，可以将所有字符变为相同的字符。

算法步骤:
1. 初始化两个指针 left 和 right 来表示滑动窗口的左右边界。
2. 遍历字符串，扩展右边界 right，并记录当前窗口内的 'T' 和 'F' 的数量。
3. 如果当前窗口内需要的操作次数超过 k，则移动左边界 left，直到操作次数不超过 k。
4. 记录最大窗口长度。

关键点:
- 使用滑动窗口来维护一个满足条件的子数组。
- 通过移动左右指针来动态调整窗口大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 answerKey 的长度。每个字符最多被访问两次（一次作为右边界，一次作为左边界）。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_consecutive_answers(answer_key: str, k: int) -> int:
    """
    函数式接口 - 返回在不超过 k 次操作的情况下，最大连续 'T' 或者 'F' 的数目。
    """
    def max_consecutive_char(char: str) -> int:
        left, max_length, count = 0, 0, 0
        for right in range(len(answer_key)):
            if answer_key[right] != char:
                count += 1
            while count > k:
                if answer_key[left] != char:
                    count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

    return max(max_consecutive_char('T'), max_consecutive_char('F'))


Solution = create_solution(max_consecutive_answers)