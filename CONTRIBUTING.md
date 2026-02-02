# 贡献指南

## 添加新题目

### 方法1：使用辅助脚本（推荐）

```bash
python scripts/add_problem.py <题号> <难度> <题型1,题型2,...> [周赛1,周赛2,...]
```

示例：
```bash
python scripts/add_problem.py 10 easy "array,hash_table" "weekly_300"
```

脚本会自动：
1. 在 `by_id/` 下创建核心实现文件模板
2. 在对应的 `by_difficulty/` 目录下创建导入文件
3. 在对应的 `by_topic/` 目录下创建导入文件
4. 在对应的 `by_contest/` 目录下创建导入文件
5. 在 `metadata.py` 中添加元数据条目

然后你需要：
1. 在 `by_id/qXXXX.py` 中实现最优解法
2. 在 `metadata.py` 中补充题目的 `title` 和 `slug`
3. 更新各分类文件中的函数名和类名（如果与模板不同）

### 方法2：手动添加

#### 步骤1：在 `by_id/` 下创建核心实现

创建文件 `leetcode_solutions/by_id/qXXXX.py`（4位题号，不足补0）：

```python
# -*- coding:utf-8 -*-
"""
题号. 题目名称（难度）
LeetCode链接：https://leetcode.cn/problems/slug/
最优解法：算法名称
时间复杂度：O(?), 空间复杂度：O(?)
"""

from typing import List

def solution_function(nums: List[int]) -> int:
    """函数式接口"""
    # 实现最优解法
    pass

class Solution:
    """LeetCode提交格式的类"""
    def solutionMethod(self, nums: List[int]) -> int:
        return solution_function(nums)
```

#### 步骤2：在 `metadata.py` 中添加元数据

在 `PROBLEM_METADATA` 字典中添加条目：

```python
题号: {
    "id": 题号,
    "title": "题目名称",
    "slug": "题目slug",
    "difficulty": "easy/medium/hard",
    "topics": ["题型1", "题型2"],
    "is_premium": False,
    "is_interview": False,
    "contests": ["周赛名称"],
},
```

#### 步骤3：在分类目录下创建导入文件

根据题目的难度、题型、周赛，在对应目录下创建导入文件：

- `by_difficulty/<难度>/qXXXX.py`
- `by_topic/<题型>/qXXXX.py`
- `by_contest/<周赛>/qXXXX.py`

这些文件只需要导入 `by_id` 中的实现：

```python
from leetcode_solutions.by_id.qXXXX import solution_function, Solution
```

## 代码规范

1. **函数命名**：使用小写字母和下划线，如 `two_sum`
2. **类命名**：使用大驼峰，如 `Solution`
3. **注释**：每个文件顶部包含题目信息，函数包含docstring
4. **时间复杂度**：在文件顶部注释中说明
5. **最优解法**：只保留最高效的算法实现

## 测试

添加新题目后，建议测试：

```python
from leetcode_solutions.by_id import qXXXX
# 测试函数式接口
result = qXXXX.solution_function([...])
# 测试类式接口
solution = qXXXX.Solution()
result = solution.solutionMethod([...])
```

## 提交

1. 确保代码通过lint检查
2. 更新版本号（如果需要）
3. 提交Pull Request

