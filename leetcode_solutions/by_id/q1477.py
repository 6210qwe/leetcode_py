```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1477
标题: Product of the Last K Numbers
难度: medium
链接: https://leetcode.cn/problems/product-of-the-last-k-numbers/
题目类型: 设计、数组、数学、数据流、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1352. 最后 K 个数的乘积 - 设计一个算法，该算法接受一个整数流并检索该流中最后 k 个整数的乘积。 实现 ProductOfNumbers 类： * ProductOfNumbers() 用一个空的流初始化对象。 * void add(int num) 将数字 num 添加到当前数字列表的最后面。 * int getProduct(int k) 返回当前数字列表中，最后 k 个数字的乘积。你可以假设当前列表中始终 至少 包含 k 个数字。 题目数据保证：任何时候，任一连续数字序列的乘积都在 32 位整数范围内，不会溢出。 示例： 输入： ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"] [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]] 输出： [null,null,null,null,null,null,20,40,0,null,32] 解释： ProductOfNumbers productOfNumbers = new ProductOfNumbers(); productOfNumbers.add(3); // [3] productOfNumbers.add(0); // [3,0] productOfNumbers.add(2); // [3,0,2] productOfNumbers.add(5); // [3,0,2,5] productOfNumbers.add(4); // [3,0,2,5,4] productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20 productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40 productOfNumbers.getProduct(4); // 返回 0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0 productOfNumbers.add(8); // [3,0,2,5,4,8] productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 提示： * 0 <= num <= 100 * 1 <= k <= 4 * 104 * add 和 getProduct 最多被调用 4 * 104 次。 * 在任何时间点流的乘积都在 32 位整数范围内。 进阶：您能否 同时 将 GetProduct 和 Add 的实现改为 O(1) 时间复杂度，而不是 O(k) 时间复杂度？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀积来存储每个位置的累积乘积，这样可以在 O(1) 时间内计算任意子数组的乘积。

算法步骤:
1. 初始化一个列表 `prefix_products` 来存储前缀积。
2. 在 `add` 方法中，如果添加的数字是 0，则重置 `prefix_products` 列表，否则将当前数字乘以前一个前缀积并添加到 `prefix_products` 中。
3. 在 `getProduct` 方法中，通过前缀积计算最后 k 个数字的乘积。

关键点:
- 使用前缀积可以快速计算任意子数组的乘积。
- 当遇到 0 时，需要重置前缀积列表，因为之后的所有乘积都会是 0。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - `add` 和 `getProduct` 方法都是 O(1) 时间复杂度。
空间复杂度: O(n) - 其中 n 是添加的数字数量，因为我们需要存储前缀积。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]  # 初始化前缀积列表，初始值为 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]  # 重置前缀积列表
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0  # 如果 k 大于等于前缀积列表的长度，说明有 0 存在
        return self.prefix_products[-1] // self.prefix_products[-k - 1]


# 测试
if __name__ == "__main__":
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))  # 输出: 20
    print(obj.getProduct(3))  # 输出: 40
    print(obj.getProduct(4))  # 输出: 0
    obj.add(8)
    print(obj.getProduct(2))  # 输出: 32
```

这个实现使用了前缀积来存储每个位置的累积乘积，从而可以在 O(1) 时间内计算任意子数组的乘积。`add` 和 `getProduct` 方法的时间复杂度都是 O(1)，空间复杂度是 O(n)，其中 n 是添加的数字数量。