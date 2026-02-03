# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 299
标题: Bulls and Cows
难度: medium
链接: https://leetcode.cn/problems/bulls-and-cows/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
299. 猜数字游戏 - 你在和朋友一起玩 猜数字（Bulls and Cows） [https://baike.baidu.com/item/%E7%8C%9C%E6%95%B0%E5%AD%97/83200?fromtitle=Bulls+and+Cows&fromid=12003488&fr=aladdin]游戏，该游戏规则如下： 写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示： * 猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛）， * 有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。 给你一个秘密数字 secret 和朋友猜测的数字 guess ，请你返回对朋友这次猜测的提示。 提示的格式为 "xAyB" ，x 是公牛个数， y 是奶牛个数，A 表示公牛，B 表示奶牛。 请注意秘密数字和朋友猜测的数字都可能含有重复数字。 示例 1： 输入：secret = "1807", guess = "7810" 输出："1A3B" 解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。 "1807" | "7810" 示例 2： 输入：secret = "1123", guess = "0111" 输出："1A1B" 解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。 "1123" "1123" | or | "0111" "0111" 注意，两个不匹配的 1 中，只有一个会算作奶牛（数字猜对位置不对）。通过重新排列非公牛数字，其中仅有一个 1 可以成为公牛数字。 提示： * 1 <= secret.length, guess.length <= 1000 * secret.length == guess.length * secret 和 guess 仅由数字组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 先统计Bulls，再统计Cows

算法步骤:
1. 遍历统计Bulls（位置和数字都相同）
2. 统计secret和guess中每个数字的出现次数
3. Cows = min(secret[i], guess[i])的总和 - Bulls

关键点:
- 先统计Bulls
- 再统计Cows
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为字符串长度
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def get_hint(secret: str, guess: str) -> str:
    """
    函数式接口 - 猜数字游戏
    
    实现思路:
    先统计Bulls，再统计Cows。
    
    Args:
        secret: 秘密数字
        guess: 猜测数字
        
    Returns:
        提示字符串
        
    Example:
        >>> get_hint("1807", "7810")
        '1A3B'
    """
    bulls = 0
    secret_count = Counter()
    guess_count = Counter()
    
    # 统计Bulls和数字出现次数
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_count[secret[i]] += 1
            guess_count[guess[i]] += 1
    
    # 统计Cows
    cows = 0
    for digit in secret_count:
        cows += min(secret_count[digit], guess_count[digit])
    
    return f"{bulls}A{cows}B"


# 自动生成Solution类（无需手动编写）
Solution = create_solution(get_hint)
