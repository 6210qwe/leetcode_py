# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2813
标题: To Be Or Not To Be
难度: easy
链接: https://leetcode.cn/problems/to-be-or-not-to-be/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2704. 相等还是不相等 - 请你编写一个名为 expect 的函数，用于帮助开发人员测试他们的代码。它应该接受任何值 val 并返回一个包含以下两个函数的对象。 * toBe(val) 接受另一个值并在两个值相等（ === ）时返回 true 。如果它们不相等，则应抛出错误 "Not Equal" 。 * notToBe(val) 接受另一个值并在两个值不相等（ !== ）时返回 true 。如果它们相等，则应抛出错误 "Equal" 。 示例 1： 输入：func = () => expect(5).toBe(5) 输出：{"value": true} 解释：5 === 5 因此该表达式返回 true。 示例 2： 输入：func = () => expect(5).toBe(null) 输出：{"error": "Not Equal"} 解释：5 !== null 因此抛出错误 "Not Equal". 示例 3： 输入：func = () => expect(5).notToBe(null) 输出：{"value": true} 解释：5 !== null 因此该表达式返回 true.
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用闭包来创建 `toBe` 和 `notToBe` 函数，并在这些函数中进行值的比较。

算法步骤:
1. 定义 `expect` 函数，接受一个值 `val`。
2. 返回一个对象，该对象包含 `toBe` 和 `notToBe` 两个方法。
3. `toBe` 方法接受一个值 `other_val`，如果 `val` 和 `other_val` 相等则返回 `True`，否则抛出 "Not Equal" 错误。
4. `notToBe` 方法接受一个值 `other_val`，如果 `val` 和 `other_val` 不相等则返回 `True`，否则抛出 "Equal" 错误。

关键点:
- 使用闭包来捕获 `expect` 函数中的 `val` 值。
- 在 `toBe` 和 `notToBe` 方法中进行值的比较并抛出相应的错误。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Any

def expect(val: Any):
    """
    创建一个包含 toBe 和 notToBe 方法的对象，用于比较值。
    """
    def toBe(other_val: Any) -> bool:
        if val == other_val:
            return True
        else:
            raise AssertionError("Not Equal")

    def notToBe(other_val: Any) -> bool:
        if val != other_val:
            return True
        else:
            raise AssertionError("Equal")

    return {"toBe": toBe, "notToBe": notToBe}

# 测试示例
if __name__ == "__main__":
    # 示例 1
    assert expect(5).toBe(5) is True
    # 示例 2
    try:
        expect(5).toBe(None)
    except AssertionError as e:
        assert str(e) == "Not Equal"
    # 示例 3
    assert expect(5).notToBe(None) is True