# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 736
标题: Parse Lisp Expression
难度: hard
链接: https://leetcode.cn/problems/parse-lisp-expression/
题目类型: 栈、递归、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
736. Lisp 语法解析 - 给你一个类似 Lisp 语句的字符串表达式 expression，求出其计算结果。 表达式语法如下所示: * 表达式可以为整数，let 表达式，add 表达式，mult 表达式，或赋值的变量。表达式的结果总是一个整数。 * (整数可以是正整数、负整数、0) * let 表达式采用 "(let v1 e1 v2 e2 ... vn en expr)" 的形式，其中 let 总是以字符串 "let"来表示，接下来会跟随一对或多对交替的变量和表达式，也就是说，第一个变量 v1被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，依次类推；最终 let 表达式的值为 expr表达式的值。 * add 表达式表示为 "(add e1 e2)" ，其中 add 总是以字符串 "add" 来表示，该表达式总是包含两个表达式 e1、e2 ，最终结果是 e1 表达式的值与 e2 表达式的值之 和 。 * mult 表达式表示为 "(mult e1 e2)" ，其中 mult 总是以字符串 "mult" 表示，该表达式总是包含两个表达式 e1、e2，最终结果是 e1 表达式的值与 e2 表达式的值之 积 。 * 在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，"add" ，"let" ，"mult" 会被定义为 "关键字" ，不会用作变量名。 * 最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。 示例 1： 输入：expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))" 输出：14 解释： 计算表达式 (add x y), 在检查变量 x 值时， 在变量的上下文中由最内层作用域依次向外检查。 首先找到 x = 3, 所以此处的 x 值是 3 。 示例 2： 输入：expression = "(let x 3 x 2 x)" 输出：2 解释：let 语句中的赋值运算按顺序处理即可。 示例 3： 输入：expression = "(let x 1 y 2 x (add x y) (add x y))" 输出：5 解释： 第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。 第二个 (add x y) 计算结果是 3 + 2 = 5 。 提示： * 1 <= expression.length <= 2000 * exprssion 中不含前导和尾随空格 * expressoin 中的不同部分（token）之间用单个空格进行分隔 * 答案和所有中间计算结果都符合 32-bit 整数范围 * 测试用例中的表达式均为合法的且最终结果为整数
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来处理嵌套表达式，并使用哈希表来存储变量的作用域。

算法步骤:
1. 初始化一个栈，用于存储当前的作用域。
2. 定义一个辅助函数 `evaluate`，用于递归地解析和计算表达式。
3. 在 `evaluate` 函数中，根据表达式的类型（整数、变量、let、add、mult）进行相应的处理。
4. 对于 let 表达式，创建一个新的作用域，并在新作用域中处理变量赋值。
5. 对于 add 和 mult 表达式，递归计算子表达式的值并返回结果。
6. 对于变量，从当前作用域中查找其值，如果找不到则向上一层作用域查找。

关键点:
- 使用栈来管理嵌套的作用域。
- 使用哈希表来存储每个作用域中的变量值。
- 递归处理嵌套表达式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表达式的长度。每个字符最多只会被处理一次。
空间复杂度: O(n)，递归调用栈和作用域哈希表的空间消耗。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def evaluate(expression: str) -> int:
    def parse(s: str):
        res = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '(':
                balance = 1
                j = i + 1
                while j < len(s) and balance > 0:
                    if s[j] == '(':
                        balance += 1
                    elif s[j] == ')':
                        balance -= 1
                    j += 1
                res.append(s[i:j])
                i = j
            else:
                j = i
                while j < len(s) and s[j] != ' ':
                    j += 1
                res.append(s[i:j])
                i = j
        return res

    def eval_expr(expr, scope):
        if expr[0] == '(':
            return eval_nested(expr, scope)
        if expr.isdigit() or (expr.startswith('-') and expr[1:].isdigit()):
            return int(expr)
        if expr in scope[-1]:
            return scope[-1][expr]
        raise ValueError(f"Undefined variable: {expr}")

    def eval_nested(expr, scope):
        tokens = parse(expr[1:-1])
        if tokens[0] == 'let':
            new_scope = {}
            for i in range(1, len(tokens) - 2, 2):
                var = tokens[i]
                val = eval_expr(tokens[i + 1], scope + [new_scope])
                new_scope[var] = val
            return eval_expr(tokens[-1], scope + [new_scope])
        elif tokens[0] == 'add':
            return eval_expr(tokens[1], scope) + eval_expr(tokens[2], scope)
        elif tokens[0] == 'mult':
            return eval_expr(tokens[1], scope) * eval_expr(tokens[2], scope)
        else:
            raise ValueError(f"Invalid expression: {expr}")

    return eval_nested(expression, [{}])


Solution = create_solution(evaluate)