# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 282
标题: Expression Add Operators
难度: hard
链接: https://leetcode.cn/problems/expression-add-operators/
题目类型: 数学、字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
282. 给表达式添加运算符 - 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回 所有 能够得到 target 的表达式。 注意，返回表达式中的操作数 不应该 包含前导零。 注意，一个数字可以包含多个数位。 示例 1: 输入: num = "123", target = 6 输出: ["1+2+3", "1*2*3"] 解释: “1*2*3” 和 “1+2+3” 的值都是6。 示例 2: 输入: num = "232", target = 8 输出: ["2*3+2", "2+3*2"] 解释: “2*3+2” 和 “2+3*2” 的值都是8。 示例 3: 输入: num = "3456237490", target = 9191 输出: [] 解释: 表达式 “3456237490” 无法得到 9191 。 提示： * 1 <= num.length <= 10 * num 仅含数字 * -231 <= target <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯，枚举所有可能的运算符组合

算法步骤:
1. 回溯枚举所有可能的运算符位置
2. 计算表达式值
3. 如果等于target，加入结果

关键点:
- 回溯枚举
- 处理乘法优先级
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(4^n) - 每个位置4种选择
空间复杂度: O(n) - 递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def add_operators(num: str, target: int) -> List[str]:
    """
    函数式接口 - 给表达式添加运算符
    
    实现思路:
    回溯：枚举所有可能的运算符组合。
    
    Args:
        num: 数字字符串
        target: 目标值
        
    Returns:
        所有能得到target的表达式
        
    Example:
        >>> add_operators("123", 6)
        ['1+2+3', '1*2*3']
    """
    result = []
    
    def backtrack(index: int, path: str, value: int, prev: int):
        """回溯函数"""
        if index == len(num):
            if value == target:
                result.append(path)
            return
        
        for i in range(index, len(num)):
            # 不能有前导0
            if i > index and num[index] == '0':
                break
            
            curr_str = num[index:i+1]
            curr_num = int(curr_str)
            
            if index == 0:
                backtrack(i + 1, curr_str, curr_num, curr_num)
            else:
                # 加法
                backtrack(i + 1, path + '+' + curr_str, value + curr_num, curr_num)
                # 减法
                backtrack(i + 1, path + '-' + curr_str, value - curr_num, -curr_num)
                # 乘法
                backtrack(i + 1, path + '*' + curr_str, value - prev + prev * curr_num, prev * curr_num)
    
    backtrack(0, "", 0, 0)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(add_operators)
