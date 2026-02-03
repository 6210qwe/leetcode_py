# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 6
标题: Zigzag Conversion
难度: medium
链接: https://leetcode.cn/problems/zigzag-conversion/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
6. Z 字形变换 - 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下： P A H N A P L S I I G Y I R 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。 请你实现这个将字符串进行指定行数变换的函数： string convert(string s, int numRows); 示例 1： 输入：s = "PAYPALISHIRING", numRows = 3 输出："PAHNAPLSIIGYIR" 示例 2： 输入：s = "PAYPALISHIRING", numRows = 4 输出："PINALSIGYAHRPI" 解释： P I N A L S I G Y A H R P I 示例 3： 输入：s = "A", numRows = 1 输出："A" 提示： * 1 <= s.length <= 1000 * s 由英文字母（小写和大写）、',' 和 '.' 组成 * 1 <= numRows <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 模拟Z字形排列，按行存储字符，然后按行读取

算法步骤:
1. 创建numRows个字符串列表，用于存储每一行的字符
2. 使用方向标志direction控制当前是向下还是向上移动
3. 遍历字符串，将每个字符放入对应的行
4. 当到达第一行或最后一行时，改变方向
5. 将所有行的字符串连接起来

关键点:
- 使用方向标志简化代码，避免复杂的索引计算
- 当numRows=1时，直接返回原字符串
- 时间复杂度O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历字符串一次，n为字符串长度
空间复杂度: O(n) - 需要存储所有字符
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


def convert(s: str, num_rows: int) -> str:
    """
    函数式接口 - 模拟Z字形排列实现
    
    实现思路:
    模拟Z字形排列过程，按行存储字符，然后按行读取。
    
    Args:
        s: 输入字符串
        num_rows: Z字形排列的行数
        
    Returns:
        按行读取后的字符串
        
    Example:
        >>> convert("PAYPALISHIRING", 3)
        'PAHNAPLSIIGYIR'
        >>> convert("PAYPALISHIRING", 4)
        'PINALSIGYAHRPI'
    """
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [''] * num_rows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        # 到达第一行或最后一行时，改变方向
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1
    
    return ''.join(rows)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(convert)
