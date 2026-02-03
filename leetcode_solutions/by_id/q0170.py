# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 170
标题: Two Sum III - Data structure design
难度: easy
链接: https://leetcode.cn/problems/two-sum-iii-data-structure-design/
题目类型: 设计、数组、哈希表、双指针、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
170. 两数之和 III - 数据结构设计 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储数字及其出现次数，查找时遍历哈希表

算法步骤:
1. add操作：将数字加入哈希表，记录出现次数
2. find操作：遍历哈希表，查找是否存在target - num
3. 注意处理相同数字的情况（需要出现至少2次）

关键点:
- 使用哈希表实现O(1)添加，O(n)查找
- 时间复杂度：add O(1)，find O(n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: add O(1)，find O(n)
空间复杂度: O(n) - 存储数字及其出现次数
"""

# ============================================================================
# 代码实现
# ============================================================================

from collections import defaultdict
from leetcode_solutions.utils.solution import create_solution


class TwoSum:
    """
    两数之和数据结构实现类
    """
    def __init__(self):
        self.num_count = defaultdict(int)
    
    def add(self, number: int) -> None:
        """添加数字"""
        self.num_count[number] += 1
    
    def find(self, value: int) -> bool:
        """查找是否存在两个数的和等于value"""
        for num in self.num_count:
            complement = value - num
            if complement in self.num_count:
                if complement != num or self.num_count[complement] > 1:
                    return True
        return False


def two_sum_iii_data_structure_design() -> TwoSum:
    """
    函数式接口 - 创建两数之和数据结构
    
    实现思路:
    使用哈希表存储数字及其出现次数，查找时遍历哈希表。
    
    Returns:
        TwoSum实例
        
    Example:
        >>> two_sum = two_sum_iii_data_structure_design()
        >>> two_sum.add(1)
        >>> two_sum.add(3)
        >>> two_sum.add(5)
        >>> two_sum.find(4)
        True
    """
    return TwoSum()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(two_sum_iii_data_structure_design)
