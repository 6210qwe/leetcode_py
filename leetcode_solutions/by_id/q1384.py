# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1384
标题: Maximum Font to Fit a Sentence in a Screen
难度: medium
链接: https://leetcode.cn/problems/maximum-font-to-fit-a-sentence-in-a-screen/
题目类型: 数组、字符串、二分查找、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1618. 找出适应屏幕的最大字号 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定最大字体大小。

算法步骤:
1. 定义一个辅助函数 `can_fit`，用于判断给定的字体大小是否可以适应屏幕。
2. 初始化二分查找的左右边界。
3. 在二分查找过程中，使用 `can_fit` 函数来调整左右边界，直到找到最大的适应屏幕的字体大小。

关键点:
- 使用二分查找来优化时间复杂度。
- 辅助函数 `can_fit` 用于判断当前字体大小是否适合屏幕。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log m)，其中 n 是句子中字符的数量，m 是字体大小的范围。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional

def can_fit(sentence: str, screen_width: int, screen_height: int, font_size: int) -> bool:
    """
    判断给定的字体大小是否可以适应屏幕。
    """
    words = sentence.split()
    max_width = 0
    current_width = 0
    lines = 1
    
    for word in words:
        word_width = len(word) * font_size
        if current_width + word_width > screen_width:
            lines += 1
            current_width = word_width
            max_width = max(max_width, current_width)
        else:
            current_width += word_width + font_size  # 空格宽度
    
    return lines * font_size <= screen_height and max_width <= screen_width

def max_font_to_fit_sentence(sentence: str, screen_width: int, screen_height: int, fonts: List[int]) -> int:
    """
    找出适应屏幕的最大字号。
    """
    left, right = 0, len(fonts) - 1
    
    while left < right:
        mid = (left + right + 1) // 2
        if can_fit(sentence, screen_width, screen_height, fonts[mid]):
            left = mid
        else:
            right = mid - 1
    
    return fonts[left] if can_fit(sentence, screen_width, screen_height, fonts[left]) else -1

Solution = create_solution(max_font_to_fit_sentence)