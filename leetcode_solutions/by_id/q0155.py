# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 155
标题: Min Stack
难度: medium
链接: https://leetcode.cn/problems/min-stack/
题目类型: 栈、设计
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
155. 最小栈 - 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 实现 MinStack 类: * MinStack() 初始化堆栈对象。 * void push(int val) 将元素val推入堆栈。 * void pop() 删除堆栈顶部的元素。 * int top() 获取堆栈顶部的元素。 * int getMin() 获取堆栈中的最小元素。 示例 1: 输入： ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]] 输出： [null,null,null,null,-3,null,0,-2] 解释： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop(); minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2. 提示： * -231 <= val <= 231 - 1 * pop、top 和 getMin 操作总是在 非空栈 上调用 * push, pop, top, and getMin最多被调用 3 * 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用辅助栈存储每个状态下的最小值

算法步骤:
1. 使用两个栈：一个存储元素，一个存储最小值
2. push时，同时更新最小值栈
3. pop时，同时弹出最小值栈
4. getMin直接返回最小值栈顶

关键点:
- 使用辅助栈实现O(1)获取最小值
- 时间复杂度O(1)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 所有操作都是O(1)
空间复杂度: O(n) - 需要存储n个元素
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


class MinStack:
    """
    最小栈实现类
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]


def min_stack() -> MinStack:
    """
    函数式接口 - 创建最小栈
    
    实现思路:
    使用辅助栈存储每个状态下的最小值。
    
    Returns:
        最小栈实例
        
    Example:
        >>> stack = min_stack()
        >>> stack.push(-2)
        >>> stack.push(0)
        >>> stack.push(-3)
        >>> stack.getMin()
        -3
    """
    return MinStack()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(min_stack)
