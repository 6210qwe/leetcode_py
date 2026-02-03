# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 158
标题: Read N Characters Given read4 II - Call Multiple Times
难度: hard
链接: https://leetcode.cn/problems/read-n-characters-given-read4-ii-call-multiple-times/
题目类型: 数组、交互、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
158. 用 Read4 读取 N 个字符 II - 多次调用 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用缓冲区存储read4读取的剩余字符，支持多次调用

算法步骤:
1. 维护一个内部缓冲区存储上次read4读取的剩余字符
2. 先使用缓冲区中的字符
3. 缓冲区用完后，调用read4读取新字符
4. 将多余的字符存入缓冲区供下次使用

关键点:
- 使用缓冲区处理多次调用的情况
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要读取n个字符
空间复杂度: O(1) - 缓冲区大小固定为4
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


class Solution:
    """
    用Read4读取N个字符II（多次调用）实现类
    """
    def __init__(self):
        self.buffer = [''] * 4
        self.buffer_size = 0
        self.buffer_index = 0
    
    def read(self, buf: List[str], n: int) -> int:
        """
        读取n个字符到buf
        
        Args:
            buf: 目标缓冲区
            n: 要读取的字符数
            
        Returns:
            实际读取的字符数
        """
        total = 0
        
        while total < n:
            # 如果缓冲区有剩余字符，先使用
            if self.buffer_index < self.buffer_size:
                buf[total] = self.buffer[self.buffer_index]
                total += 1
                self.buffer_index += 1
            else:
                # 缓冲区用完了，重新读取
                self.buffer_size = read4(self.buffer)
                self.buffer_index = 0
                
                if self.buffer_size == 0:
                    break
        
        return total


def read_n_characters_given_read4_ii_call_multiple_times() -> Solution:
    """
    函数式接口 - 创建Read4读取器（支持多次调用）
    
    实现思路:
    使用缓冲区存储read4读取的剩余字符，支持多次调用。
    
    Returns:
        Solution实例
        
    Example:
        >>> reader = read_n_characters_given_read4_ii_call_multiple_times()
        >>> buf = [''] * 100
        >>> reader.read(buf, 5)
        5
    """
    return Solution()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(read_n_characters_given_read4_ii_call_multiple_times)
