# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3721
标题: Count Mentions Per User
难度: medium
链接: https://leetcode.cn/problems/count-mentions-per-user/
题目类型: 数组、数学、排序、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3433. 统计用户被提及情况 - 给你一个整数 numberOfUsers 表示用户总数，另有一个大小为 n x 3 的数组 events 。 每个 events[i] 都属于下述两种类型之一： 1. 消息事件（Message Event）：["MESSAGE", "timestampi", "mentions_stringi"] * 事件表示在 timestampi 时，一组用户被消息提及。 * mentions_stringi 字符串包含下述标识符之一： * id<number>：其中 <number> 是一个区间 [0,numberOfUsers - 1] 内的整数。可以用单个空格分隔 多个 id ，并且 id 可能重复。此外，这种形式可以提及离线用户。 * ALL：提及 所有 用户。 * HERE：提及所有 在线 用户。 2. 离线事件（Offline Event）：["OFFLINE", "timestampi", "idi"] * 事件表示用户 idi 在 timestampi 时变为离线状态 60 个单位时间。用户会在 timestampi + 60 时自动再次上线。 返回数组 mentions ，其中 mentions[i] 表示 id 为 i 的用户在所有 MESSAGE 事件中被提及的次数。 最初所有用户都处于在线状态，并且如果某个用户离线或者重新上线，其对应的状态变更将会在所有相同时间发生的消息事件之前进行处理和同步。 注意 在单条消息中，同一个用户可能会被提及多次。每次提及都需要被 分别 统计。 示例 1： 输入：numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]] 输出：[2,2] 解释： 最初，所有用户都在线。 时间戳 10 ，id1 和 id0 被提及，mentions = [1,1] 时间戳 11 ，id0 离线 。 时间戳 71 ，id0 再次 上线 并且 "HERE" 被提及，mentions = [2,2] 示例 2： 输入：numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]] 输出：[2,2] 解释： 最初，所有用户都在线。 时间戳 10 ，id1 和 id0 被提及，mentions = [1,1] 时间戳 11 ，id0 离线 。 时间戳 12 ，"ALL" 被提及。这种方式将会包括所有离线用户，所以 id0 和 id1 都被提及，mentions = [2,2] 示例 3： 输入：numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]] 输出：[0,1] 解释： 最初，所有用户都在线。 时间戳 10 ，id0 离线 。 时间戳 12 ，"HERE" 被提及。由于 id0 仍处于离线状态，其将不会被提及，mentions = [0,1] 提示： * 1 <= numberOfUsers <= 100 * 1 <= events.length <= 100 * events[i].length == 3 * events[i][0] 的值为 MESSAGE 或 OFFLINE 。 * 1 <= int(events[i][1]) <= 105 * 在任意 "MESSAGE" 事件中，以 id<number> 形式提及的用户数目介于 1 和 100 之间。 * 0 <= <number> <= numberOfUsers - 1 * 题目保证 OFFLINE 引用的用户 id 在事件发生时处于 在线 状态。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个字典来记录每个用户的在线状态，并使用一个列表来记录每个用户的提及次数。

算法步骤:
1. 初始化所有用户的在线状态为 True，并初始化提及次数为 0。
2. 对事件按时间戳排序。
3. 遍历事件：
   - 如果是离线事件，更新用户的在线状态。
   - 如果是消息事件，根据提及字符串更新用户的提及次数。

关键点:
- 使用字典来高效地管理用户的在线状态。
- 使用列表来记录每个用户的提及次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 events 的长度。排序操作的时间复杂度为 O(n log n)，遍历操作的时间复杂度为 O(n)。
空间复杂度: O(n + m)，其中 n 是 events 的长度，m 是 numberOfUsers 的数量。需要额外的空间来存储用户的在线状态和提及次数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_mentions_per_user(number_of_users: int, events: List[List[str]]) -> List[int]:
    """
    统计用户被提及情况
    :param number_of_users: 用户总数
    :param events: 事件列表
    :return: 每个用户的提及次数
    """
    # 初始化用户的在线状态和提及次数
    online_status = {i: True for i in range(number_of_users)}
    mentions = [0] * number_of_users
    
    # 对事件按时间戳排序
    events.sort(key=lambda x: int(x[1]))
    
    # 遍历事件
    for event in events:
        event_type, timestamp, details = event
        timestamp = int(timestamp)
        
        if event_type == "OFFLINE":
            user_id = int(details)
            online_status[user_id] = False
            # 设置用户在 60 个单位时间后重新上线
            events.append(["ONLINE", str(timestamp + 60), str(user_id)])
            events.sort(key=lambda x: int(x[1]))  # 重新排序事件
        
        elif event_type == "MESSAGE":
            if details == "ALL":
                for user_id in range(number_of_users):
                    mentions[user_id] += 1
            elif details == "HERE":
                for user_id, is_online in online_status.items():
                    if is_online:
                        mentions[user_id] += 1
            else:
                for mention in details.split():
                    if mention.startswith("id"):
                        user_id = int(mention[2:])
                        mentions[user_id] += 1
    
    return mentions


Solution = create_solution(count_mentions_per_user)