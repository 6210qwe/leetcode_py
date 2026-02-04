# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1125
标题: Design File System
难度: medium
链接: https://leetcode.cn/problems/design-file-system/
题目类型: 设计、字典树、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1166. 设计文件系统 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储文件路径，并使用哈希表来存储每个路径的值。

算法步骤:
1. 初始化一个根节点和一个哈希表来存储路径值。
2. 创建 `createPath` 方法：如果路径不存在且父路径存在，则创建新路径并存储其值；否则返回错误。
3. 创建 `get` 方法：如果路径存在，则返回其值；否则返回 -1。
4. 创建 `set` 方法：如果路径存在，则更新其值；否则返回错误。

关键点:
- 使用字典树来高效地存储和查找路径。
- 使用哈希表来存储路径的值，以实现快速访问和更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(L) - 其中 L 是路径的长度。
空间复杂度: O(NL) - 其中 N 是路径的数量，L 是路径的平均长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional


class FileSystem:
    def __init__(self):
        self.root = {}
        self.values = {}

    def createPath(self, path: str, value: int) -> bool:
        # 检查路径是否已经存在
        if path in self.values:
            return False

        # 检查父路径是否存在
        parent_path = '/'.join(path.split('/')[:-1])
        if parent_path and parent_path not in self.values:
            return False

        # 创建新路径
        current = self.root
        for directory in path.split('/')[1:]:
            if directory not in current:
                current[directory] = {}
            current = current[directory]

        # 存储路径值
        self.values[path] = value
        return True

    def get(self, path: str) -> int:
        # 返回路径的值，如果路径不存在则返回 -1
        return self.values.get(path, -1)

    def set(self, path: str, value: int) -> bool:
        # 更新路径的值，如果路径不存在则返回 False
        if path not in self.values:
            return False
        self.values[path] = value
        return True


# 示例用法
if __name__ == "__main__":
    fs = FileSystem()
    print(fs.createPath("/a", 1))  # 输出: True
    print(fs.get("/a"))  # 输出: 1
    print(fs.set("/a", 2))  # 输出: True
    print(fs.get("/a"))  # 输出: 2
    print(fs.createPath("/a/b", 3))  # 输出: True
    print(fs.get("/a/b"))  # 输出: 3
    print(fs.createPath("/c", 4))  # 输出: True
    print(fs.get("/c"))  # 输出: 4