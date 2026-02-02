# leetcode-solutions

一个自定义的LeetCode题解PyPI包，包含最优Python解法，支持按**题号、难度、题型、周赛**等多维度导入使用。

## 特性

- ✅ **多维度分类**：支持按题号、难度（简单/中等/困难/会员/面试）、题型、周赛分类
- ✅ **最优解法**：每道题只保留最高效的算法实现
- ✅ **灵活导入**：支持多种导入方式，使用便捷
- ✅ **元数据查询**：提供题目信息查询功能
- ✅ **代码复用**：核心实现只写一次，各分类通过导入复用

## 安装

```bash
pip install leetcode-solutions
```

## 使用示例

### 1. 按题号导入（最常用）

```python
from leetcode_solutions.by_id import q0001

# 使用函数式接口
result = q0001.two_sum([2, 7, 11, 15], 9)
print(result)  # [0, 1]

# 使用类式接口（兼容LeetCode提交格式）
solution = q0001.Solution()
result = solution.twoSum([3, 2, 4], 6)
print(result)  # [1, 2]
```

### 2. 按难度导入

```python
from leetcode_solutions.by_difficulty.easy import q0001
from leetcode_solutions.by_difficulty.medium import q0002
from leetcode_solutions.by_difficulty.hard import q0003
from leetcode_solutions.by_difficulty.premium import q0004
from leetcode_solutions.by_difficulty.interview import q0001

# 使用方式相同
result = q0001.two_sum([2, 7, 11, 15], 9)
```

### 3. 按题型导入

```python
from leetcode_solutions.by_topic.array import q0001
from leetcode_solutions.by_topic.linked_list import q0002
from leetcode_solutions.by_topic.dp import q0005

# 使用方式相同
result = q0001.two_sum([2, 7, 11, 15], 9)
```

### 4. 按周赛导入

```python
from leetcode_solutions.by_contest.weekly_300 import q0001
from leetcode_solutions.by_contest.biweekly_100 import q0002

# 使用方式相同
result = q0001.two_sum([2, 7, 11, 15], 9)
```

### 5. 查询题目信息

```python
from leetcode_solutions import (
    get_problems_by_difficulty,
    get_problems_by_topic,
    get_problems_by_contest,
    get_problem_info,
    PROBLEM_METADATA
)

# 查询所有简单题
easy_problems = get_problems_by_difficulty("easy")
print(easy_problems)  # [1, ...]

# 查询所有数组题
array_problems = get_problems_by_topic("array")
print(array_problems)  # [1, ...]

# 查询所有周赛题
contest_problems = get_problems_by_contest("weekly_300")
print(contest_problems)  # [1, ...]

# 查询题目详细信息
info = get_problem_info(1)
print(info)
# {
#     "id": 1,
#     "title": "两数之和",
#     "slug": "two-sum",
#     "difficulty": "easy",
#     "topics": ["array", "hash_table"],
#     "is_premium": False,
#     "is_interview": True,
#     "contests": ["weekly_300"]
# }
```

### 6. 使用工具类

```python
from leetcode_solutions.utils import ListNode, TreeNode

# 创建链表
head = ListNode.from_list([1, 2, 3, 4])
print(head.to_list())  # [1, 2, 3, 4]

# 创建树
root = TreeNode.from_list([1, 2, 3, None, 5])
```

## 项目结构

```
leetcode_solutions/
├── __init__.py          # 核心导出文件
├── by_id/               # 按题号分类（核心实现层）
│   ├── __init__.py
│   ├── q0001.py
│   ├── q0002.py
│   └── ...
├── by_difficulty/       # 按难度分类（复用by_id）
│   ├── easy/
│   ├── medium/
│   ├── hard/
│   ├── premium/
│   └── interview/
├── by_topic/            # 按题型分类（复用by_id）
│   ├── array/
│   ├── linked_list/
│   ├── dp/
│   └── ...
├── by_contest/          # 按周赛分类（复用by_id）
│   ├── weekly_300/
│   ├── biweekly_100/
│   └── ...
├── utils/               # 通用工具类
│   ├── linked_list.py
│   ├── tree.py
│   └── common.py
└── metadata.py          # 元数据映射
```

## 开发指南

### 添加新题目

1. 在 `leetcode_solutions/by_id/` 下创建 `qXXXX.py`（4位题号，不足补0）
2. 实现最优解法（函数式 + 类式）
3. 在 `metadata.py` 中添加题目元数据
4. 在对应的 `by_difficulty/`、`by_topic/`、`by_contest/` 目录下创建导入文件

### 更新版本

修改 `setup.py` 中的 `__version__`，然后重新打包发布。

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

