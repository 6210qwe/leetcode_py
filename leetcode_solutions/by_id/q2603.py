# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2603
标题: Reward Top K Students
难度: medium
链接: https://leetcode.cn/problems/reward-top-k-students/
题目类型: 数组、哈希表、字符串、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2512. 奖励最顶尖的 K 名学生 - 给你两个字符串数组 positive_feedback 和 negative_feedback ，分别包含表示正面的和负面的词汇。不会 有单词同时是正面的和负面的。 一开始，每位学生分数为 0 。每个正面的单词会给学生的分数 加 3 分，每个负面的词会给学生的分数 减 1 分。 给你 n 个学生的评语，用一个下标从 0 开始的字符串数组 report 和一个下标从 0 开始的整数数组 student_id 表示，其中 student_id[i] 表示这名学生的 ID ，这名学生的评语是 report[i] 。每名学生的 ID 互不相同。 给你一个整数 k ，请你返回按照得分 从高到低 最顶尖的 k 名学生。如果有多名学生分数相同，ID 越小排名越前。 示例 1： 输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2 输出：[1,2] 解释： 两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。 示例 2： 输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2 输出：[2,1] 解释： - ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。 - ID 为 2 的学生有 1 个正面词汇，得分为 3 分。 学生 2 分数更高，所以返回 [2,1] 。 提示： * 1 <= positive_feedback.length, negative_feedback.length <= 104 * 1 <= positive_feedback[i].length, negative_feedback[j].length <= 100 * positive_feedback[i] 和 negative_feedback[j] 都只包含小写英文字母。 * positive_feedback 和 negative_feedback 中不会有相同单词。 * n == report.length == student_id.length * 1 <= n <= 104 * report[i] 只包含小写英文字母和空格 ' ' 。 * report[i] 中连续单词之间有单个空格隔开。 * 1 <= report[i].length <= 100 * 1 <= student_id[i] <= 109 * student_id[i] 的值 互不相同 。 * 1 <= k <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希集合来存储正面和负面词汇，然后遍历每个学生的报告，计算每个学生的分数，并使用堆来获取前 k 名学生。

算法步骤:
1. 将正面和负面词汇分别存储在哈希集合中。
2. 初始化一个列表来存储每个学生的分数和 ID。
3. 遍历每个学生的报告，计算其分数，并将其分数和 ID 存储在列表中。
4. 使用堆来获取分数最高的前 k 名学生。如果分数相同，ID 较小的学生排名靠前。

关键点:
- 使用哈希集合来快速查找正面和负面词汇。
- 使用堆来高效地获取前 k 名学生。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k + m)，其中 n 是学生数量，m 是正面和负面词汇的总长度。遍历学生报告的时间复杂度是 O(n)，使用堆的时间复杂度是 O(n log k)。
空间复杂度: O(m + n)，其中 m 是正面和负面词汇的总长度，n 是学生数量。存储词汇和学生信息的空间复杂度是 O(m + n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def top_k_students(positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
    # 将正面和负面词汇存储在哈希集合中
    positive_set = set(positive_feedback)
    negative_set = set(negative_feedback)

    # 计算每个学生的分数
    scores = []
    for i, r in enumerate(report):
        score = 0
        words = r.split()
        for word in words:
            if word in positive_set:
                score += 3
            elif word in negative_set:
                score -= 1
        scores.append((-score, student_id[i]))

    # 使用堆来获取前 k 名学生
    heapq.heapify(scores)
    result = [heapq.heappop(scores)[1] for _ in range(k)]
    return result

Solution = create_solution(top_k_students)