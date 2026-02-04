# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1751
标题: Slowest Key
难度: easy
链接: https://leetcode.cn/problems/slowest-key/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1629. 按键持续时间最长的键 - LeetCode 设计了一款新式键盘，正在测试其可用性。测试人员将会点击一系列键（总计 n 个），每次一个。 给你一个长度为 n 的字符串 keysPressed ，其中 keysPressed[i] 表示测试序列中第 i 个被按下的键。releaseTimes 是一个升序排列的列表，其中 releaseTimes[i] 表示松开第 i 个键的时间。字符串和数组的 下标都从 0 开始 。第 0 个键在时间为 0 时被按下，接下来每个键都 恰好 在前一个键松开时被按下。 测试人员想要找出按键 持续时间最长 的键。第 i 次按键的持续时间为 releaseTimes[i] - releaseTimes[i - 1] ，第 0 次按键的持续时间为 releaseTimes[0] 。 注意，测试期间，同一个键可以在不同时刻被多次按下，而每次的持续时间都可能不同。 请返回单次按键 持续时间最长 的键，如果有多个这样的键，则返回 按字母顺序排列最大 的那个键。 示例 1： 输入：releaseTimes = [9,29,49,50], keysPressed = "cbcd" 输出：'c' 解释：按键顺序和持续时间如下： 按下 'c' ，持续时间 9（时间 0 按下，时间 9 松开） 按下 'b' ，持续时间 29 - 9 = 20（松开上一个键的时间 9 按下，时间 29 松开） 按下 'c' ，持续时间 49 - 29 = 20（松开上一个键的时间 29 按下，时间 49 松开） 按下 'd' ，持续时间 50 - 49 = 1（松开上一个键的时间 49 按下，时间 50 松开） 按键持续时间最长的键是 'b' 和 'c'（第二次按下时），持续时间都是 20 'c' 按字母顺序排列比 'b' 大，所以答案是 'c' 示例 2： 输入：releaseTimes = [12,23,36,46,62], keysPressed = "spuda" 输出：'a' 解释：按键顺序和持续时间如下： 按下 's' ，持续时间 12 按下 'p' ，持续时间 23 - 12 = 11 按下 'u' ，持续时间 36 - 23 = 13 按下 'd' ，持续时间 46 - 36 = 10 按下 'a' ，持续时间 62 - 46 = 16 按键持续时间最长的键是 'a' ，持续时间 16 提示： * releaseTimes.length == n * keysPressed.length == n * 2 <= n <= 1000 * 1 <= releaseTimes[i] <= 109 * releaseTimes[i] < releaseTimes[i+1] * keysPressed 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过一次遍历找到按键持续时间最长的键，并在有多个键持续时间相同的情况下选择字母顺序最大的键。

算法步骤:
1. 初始化变量 `max_duration` 为 0，用于记录当前最长的按键持续时间。
2. 初始化变量 `result` 为第一个按键，用于记录当前持续时间最长的键。
3. 遍历 `releaseTimes` 和 `keysPressed`，计算每个按键的持续时间。
4. 如果当前按键的持续时间大于 `max_duration`，更新 `max_duration` 和 `result`。
5. 如果当前按键的持续时间等于 `max_duration`，但按键的字母顺序更大，则更新 `result`。
6. 返回 `result`。

关键点:
- 一次遍历即可完成，时间复杂度为 O(n)。
- 使用常数空间存储中间结果，空间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def slowest_key(release_times: List[int], keys_pressed: str) -> str:
    """
    函数式接口 - 找出按键持续时间最长的键
    """
    max_duration = 0
    result = keys_pressed[0]
    
    for i in range(len(keys_pressed)):
        if i == 0:
            duration = release_times[i]
        else:
            duration = release_times[i] - release_times[i - 1]
        
        if duration > max_duration or (duration == max_duration and keys_pressed[i] > result):
            max_duration = duration
            result = keys_pressed[i]
    
    return result


Solution = create_solution(slowest_key)