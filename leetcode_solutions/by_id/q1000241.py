# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000241
标题: 复原 IP 地址
难度: medium
链接: https://leetcode.cn/problems/0on3uN/
题目类型: 字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 087. 复原 IP 地址 - 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。 示例 1： 输入：s = "25525511135" 输出：["255.255.11.135","255.255.111.35"] 示例 2： 输入：s = "0000" 输出：["0.0.0.0"] 示例 3： 输入：s = "1111" 输出：["1.1.1.1"] 示例 4： 输入：s = "010010" 输出：["0.10.0.10","0.100.1.0"] 示例 5： 输入：s = "10203040" 输出：["10.20.30.40","102.0.30.40","10.203.0.40"] 提示： * 0 <= s.length <= 3000 * s 仅由数字组成 注意：本题与主站 93 题相同：https://leetcode.cn/problems/restore-ip-addresses/ [https://leetcode.cn/problems/restore-ip-addresses/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯枚举 4 段，每段长度 1~3，检查合法性

算法步骤:
1. 定义函数 valid(segment) 判断一段字符串是否是合法 IP 段：
   - 长度 1~3
   - 若长度>1，则不能以 '0' 开头
   - 数值在 0~255 之间
2. 回溯函数 dfs(start, parts)：
   - 若已经取了 4 段：
       * 若 start == len(s)，将用 '.' 连接 parts 加入结果
       * 否则直接返回
   - 从 end = start 到 min(start+3, len(s))：
       * 取当前段 seg = s[start:end]
       * 若 seg 不合法则 continue
       * 将 seg 加入 parts，递归 dfs(end, parts)，回溯时弹出
3. 初始调用 dfs(0, [])

关键点:
- 精确地分成 4 段，不能多也不能少
- 处理前导零和数值范围限制
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^4) 上界常数，对每个起点最多尝试 3 种长度，共 4 段
空间复杂度: O(1) 额外空间（不计结果）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def restore_ip_addresses(s: str) -> List[str]:
    """
    函数式接口 - 复原 IP 地址
    """
    res: List[str] = []
    n = len(s)

    def valid(seg: str) -> bool:
        if not seg or len(seg) > 3:
            return False
        if len(seg) > 1 and seg[0] == '0':
            return False
        return int(seg) <= 255

    def dfs(start: int, parts: List[str]) -> None:
        if len(parts) == 4:
            if start == n:
                res.append(".".join(parts))
            return
        # 剩余字符数剪枝
        remaining = n - start
        remaining_slots = 4 - len(parts)
        if remaining < remaining_slots or remaining > 3 * remaining_slots:
            return

        for end in range(start + 1, min(start + 4, n + 1)):
            seg = s[start:end]
            if not valid(seg):
                continue
            parts.append(seg)
            dfs(end, parts)
            parts.pop()

    dfs(0, [])
    return res


Solution = create_solution(restore_ip_addresses)
