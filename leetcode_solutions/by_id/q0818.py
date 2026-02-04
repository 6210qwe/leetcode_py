# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 818
标题: Similar RGB Color
难度: easy
链接: https://leetcode.cn/problems/similar-rgb-color/
题目类型: 数学、字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
800. 相似 RGB 颜色 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将每个颜色分量的两位十六进制数转换为最接近的单个十六进制字符表示的颜色。

算法步骤:
1. 将输入的颜色字符串按每两个字符一组分割成三个部分，分别对应红色、绿色和蓝色分量。
2. 对于每个颜色分量，找到最接近的单个十六进制字符表示的颜色。
3. 将处理后的三个颜色分量重新组合成新的颜色字符串。

关键点:
- 使用预定义的十六进制字符列表来简化查找最接近的颜色。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个颜色分量的处理都是常数时间操作。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def find_closest_hex(hex_val: str) -> str:
    """
    找到最接近给定两位十六进制值的单个十六进制字符。
    """
    hex_chars = "0123456789abcdef"
    int_val = int(hex_val, 16)
    closest_hex = min(hex_chars, key=lambda x: abs(int(x, 16) * 17 - int_val))
    return closest_hex + closest_hex

def solution_function_name(color: str) -> str:
    """
    函数式接口 - 实现最优解法
    """
    # 将颜色字符串按每两个字符一组分割成三个部分
    red, green, blue = color[1:3], color[3:5], color[5:7]
    
    # 找到每个颜色分量最接近的单个十六进制字符
    new_red = find_closest_hex(red)
    new_green = find_closest_hex(green)
    new_blue = find_closest_hex(blue)
    
    # 重新组合成新的颜色字符串
    return f"#{new_red}{new_green}{new_blue}"

Solution = create_solution(solution_function_name)