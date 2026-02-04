# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1834
标题: Minimum Number of People to Teach
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-people-to-teach/
题目类型: 贪心、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1733. 需要教语言的最少人数 - 在一个由 m 个用户组成的社交网络里，我们获取到一些用户之间的好友关系。两个用户之间可以相互沟通的条件是他们都掌握同一门语言。 给你一个整数 n ，数组 languages 和数组 friendships ，它们的含义如下： * 总共有 n 种语言，编号从 1 到 n 。 * languages[i] 是第 i 位用户掌握的语言集合。 * friendships[i] = [u i , v i] 表示 u i 和 vi 为好友关系。 你可以选择 一门 语言并教会一些用户，使得所有好友之间都可以相互沟通。请返回你 最少 需要教会多少名用户。 请注意，好友关系没有传递性，也就是说如果 x 和 y 是好友，且 y 和 z 是好友， x 和 z 不一定是好友。 示例 1： 输入：n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]] 输出：1 解释：你可以选择教用户 1 第二门语言，也可以选择教用户 2 第一门语言。 示例 2： 输入：n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]] 输出：2 解释：教用户 1 和用户 3 第三门语言，需要教 2 名用户。 提示： * 2 <= n <= 500 * languages.length == m * 1 <= m <= 500 * 1 <= languages[i].length <= n * 1 <= languages[i][j] <= n * 1 <= u i < v i <= languages.length * 1 <= friendships.length <= 500 * 所有的好友关系 (u i, v i) 都是唯一的。 * languages[i] 中包含的值互不相同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法来找到最少需要教会的语言数量。首先找出所有无法沟通的好友对，然后统计每种语言在这些好友对中的出现频率，最后选择出现频率最高的语言进行教学。

算法步骤:
1. 初始化一个集合 `cannot_communicate` 来存储无法沟通的好友对。
2. 遍历所有好友对，检查他们是否有共同语言。如果没有，将这对好友加入 `cannot_communicate` 集合。
3. 初始化一个字典 `language_count` 来统计每种语言在 `cannot_communicate` 好友对中的出现频率。
4. 遍历 `cannot_communicate` 集合中的每个好友对，更新 `language_count`。
5. 找出 `language_count` 中出现频率最高的语言，并计算需要教会的用户数量。

关键点:
- 使用集合来存储无法沟通的好友对，避免重复计算。
- 使用字典来统计每种语言的出现频率，方便找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m + f * n)，其中 m 是用户的数量，f 是好友对的数量，n 是语言的数量。
空间复杂度: O(m + f)，用于存储无法沟通的好友对和语言计数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def minimum_teachings(n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
    # 将语言列表转换为集合，方便查找
    languages = [set(langs) for langs in languages]
    
    # 存储无法沟通的好友对
    cannot_communicate = set()
    
    # 检查每对好友是否可以沟通
    for u, v in friendships:
        if not (languages[u-1] & languages[v-1]):
            cannot_communicate.add(u)
            cannot_communicate.add(v)
    
    # 统计每种语言在无法沟通的好友对中的出现频率
    language_count = {}
    for user in cannot_communicate:
        for lang in languages[user-1]:
            if lang not in language_count:
                language_count[lang] = 0
            language_count[lang] += 1
    
    # 找出出现频率最高的语言
    max_count = 0
    best_language = None
    for lang, count in language_count.items():
        if count > max_count:
            max_count = count
            best_language = lang
    
    # 计算需要教会的用户数量
    if best_language is None:
        return 0
    return len(cannot_communicate) - max_count

Solution = create_solution(minimum_teachings)