# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 359
标题: Logger Rate Limiter
难度: easy
链接: https://leetcode.cn/problems/logger-rate-limiter/
题目类型: 设计、哈希表、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
359. 日志速率限制器 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每条日志上次打印的时间戳，判断当前日志是否可以打印

算法步骤:
1. 设计一个 Logger 类，内部使用字典 last_time 以 message 为键，最近一次成功打印的时间戳为值。
2. 当调用 shouldPrintMessage(timestamp, message) 时：
   - 如果 message 不在字典中，说明从未打印过，可以打印，记录该时间戳并返回 True。
   - 否则取出上次打印时间 prev，若 timestamp - prev >= 10，则允许打印并更新 last_time[message]；否则返回 False。
3. 由于时间戳是单调递增的，不必考虑旧日志在时间上「回退」的情况，也可以在需要时定期清理过于久远的键值对以节省空间。

关键点:
- 每条不同的 message 独立计时，互不影响。
- 只在成功打印时更新时间戳，禁止打印时保持原有记录不变。
- 字典查询和更新都是 O(1) 平均时间，满足高频调用需求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次 shouldPrintMessage 调用只做常数次哈希表访问。
空间复杂度: O(m) - m 为出现过的不同 message 数量，需要为每个 message 存储一个时间戳。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Logger:
    """
    日志速率限制器：同一条 message 在 10 秒内只允许打印一次。

    使用哈希表记录每条 message 上次打印时间戳。
    """

    def __init__(self):
        self.last_time: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_time or timestamp - self.last_time[message] >= 10:
            self.last_time[message] = timestamp
            return True
        return False


def logger_rate_limiter() -> Logger:
    """
    函数式接口 - 返回 Logger 实例，便于在测试中进行方法调用。
    """
    return Logger()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(logger_rate_limiter)
