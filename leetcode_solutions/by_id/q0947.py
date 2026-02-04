# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 947
标题: Online Election
难度: medium
链接: https://leetcode.cn/problems/online-election/
题目类型: 设计、数组、哈希表、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
911. 在线选举 - 给你两个整数数组 persons 和 times 。在选举中，第 i 张票是在时刻为 times[i] 时投给候选人 persons[i] 的。 对于发生在时刻 t 的每个查询，需要找出在 t 时刻在选举中领先的候选人的编号。 在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。 实现 TopVotedCandidate 类： * TopVotedCandidate(int[] persons, int[] times) 使用 persons 和 times 数组初始化对象。 * int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。 示例： 输入： ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"] [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]] 输出： [null, 0, 1, 1, 0, 0, 1] 解释： TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]); topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。 topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。 topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。 topVotedCandidate.q(15); // 返回 0 topVotedCandidate.q(24); // 返回 0 topVotedCandidate.q(8); // 返回 1 提示： * 1 <= persons.length <= 5000 * times.length == persons.length * 0 <= persons[i] < persons.length * 0 <= times[i] <= 109 * times 是一个严格递增的有序数组 * times[0] <= t <= 109 * 每个测试用例最多调用 104 次 q
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个字典来记录每个候选人的得票数，并在每次投票后更新当前领先的候选人。使用一个列表来记录每个时间点的领先候选人。

算法步骤:
1. 初始化时，遍历 persons 和 times 数组，记录每个候选人的得票数，并在每次投票后更新当前领先的候选人。
2. 查询时，使用二分查找找到小于等于 t 的最大时间点，并返回该时间点的领先候选人。

关键点:
- 使用字典记录每个候选人的得票数。
- 使用列表记录每个时间点的领先候选人。
- 使用二分查找优化查询时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + log n) - 初始化时遍历 persons 和 times 数组的时间复杂度为 O(n)，查询时使用二分查找的时间复杂度为 O(log n)。
空间复杂度: O(n) - 需要额外的空间来存储每个候选人的得票数和每个时间点的领先候选人。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        vote_counts = {}
        max_votes = 0
        current_leader = None
        
        for person, time in zip(persons, times):
            vote_counts[person] = vote_counts.get(person, 0) + 1
            if vote_counts[person] >= max_votes:
                max_votes = vote_counts[person]
                current_leader = person
            self.leaders.append(current_leader)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid - 1
        return self.leaders[right]

# 测试用例
if __name__ == "__main__":
    top_voted_candidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(top_voted_candidate.q(3))   # 输出: 0
    print(top_voted_candidate.q(12))  # 输出: 1
    print(top_voted_candidate.q(25))  # 输出: 1
    print(top_voted_candidate.q(15))  # 输出: 0
    print(top_voted_candidate.q(24))  # 输出: 0
    print(top_voted_candidate.q(8))   # 输出: 1