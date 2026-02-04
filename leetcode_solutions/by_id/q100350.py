# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100350
标题: Operations LCCI
难度: medium
链接: https://leetcode.cn/problems/operations-lcci/
题目类型: 设计、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.09. 运算 - 请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。 你的实现应该支持如下操作： * Operations() 构造函数 * minus(a, b) 减法，返回a - b * multiply(a, b) 乘法，返回a * b * divide(a, b) 除法，返回a / b 示例： Operations operations = new Operations(); operations.minus(1, 2); //返回-1 operations.multiply(3, 4); //返回12 operations.divide(5, -2); //返回-2 提示： * 你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况 * 单个用例的函数调用次数不会超过1000次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用加法和逻辑运算符实现基本的算术运算。

算法步骤:
1. 减法: 通过将b取反并加到a上来实现。
2. 乘法: 通过累加a多次来实现。
3. 除法: 通过不断减去b并计数来实现。

关键点:
- 使用递归或循环来实现乘法和除法。
- 处理负数情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中n是乘法或除法中的较小值。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

class Operations:
    def __init__(self):
        pass

    def negate(self, a: int) -> int:
        """将a取反"""
        negated = 0
        while a != 0:
            negated += 1
            a += 1
        return negated

    def minus(self, a: int, b: int) -> int:
        """减法，返回a - b"""
        return a + self.negate(b)

    def multiply(self, a: int, b: int) -> int:
        """乘法，返回a * b"""
        if a == 0 or b == 0:
            return 0
        result = 0
        positive = True
        if a < 0:
            a = self.negate(a)
            positive = not positive
        if b < 0:
            b = self.negate(b)
            positive = not positive
        
        for _ in range(b):
            result += a
        
        return result if positive else self.negate(result)

    def divide(self, a: int, b: int) -> int:
        """除法，返回a / b"""
        if b == 0:
            raise ValueError("除数不能为0")
        
        result = 0
        positive = (a > 0 and b > 0) or (a < 0 and b < 0)
        a = self.negate(a) if a < 0 else a
        b = self.negate(b) if b < 0 else b
        
        while a >= b:
            a = self.minus(a, b)
            result += 1
        
        return result if positive else self.negate(result)

# 工厂函数
def create_solution():
    return Operations()

# 示例
if __name__ == "__main__":
    operations = create_solution()
    print(operations.minus(1, 2))  # 返回-1
    print(operations.multiply(3, 4))  # 返回12
    print(operations.divide(5, -2))  # 返回-2