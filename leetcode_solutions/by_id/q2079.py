# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2079
标题: Delete Duplicate Folders in System
难度: hard
链接: https://leetcode.cn/problems/delete-duplicate-folders-in-system/
题目类型: 字典树、数组、哈希表、字符串、哈希函数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1948. 删除系统中的重复文件夹 - 由于一个漏洞，文件系统中存在许多重复文件夹。给你一个二维数组 paths，其中 paths[i] 是一个表示文件系统中第 i 个文件夹的绝对路径的数组。 * 例如，["one", "two", "three"] 表示路径 "/one/two/three" 。 如果两个文件夹（不需要在同一层级）包含 非空且相同的 子文件夹 集合 并具有相同的子文件夹结构，则认为这两个文件夹是相同文件夹。相同文件夹的根层级 不 需要相同。如果存在两个（或两个以上）相同 文件夹，则需要将这些文件夹和所有它们的子文件夹 标记 为待删除。 * 例如，下面文件结构中的文件夹 "/a" 和 "/b" 相同。它们（以及它们的子文件夹）应该被 全部 标记为待删除： * /a * /a/x * /a/x/y * /a/z * /b * /b/x * /b/x/y * /b/z * 然而，如果文件结构中还包含路径 "/b/w" ，那么文件夹 "/a" 和 "/b" 就不相同。注意，即便添加了新的文件夹 "/b/w" ，仍然认为 "/a/x" 和 "/b/x" 相同。 一旦所有的相同文件夹和它们的子文件夹都被标记为待删除，文件系统将会 删除 所有上述文件夹。文件系统只会执行一次删除操作。执行完这一次删除操作后，不会删除新出现的相同文件夹。 返回二维数组 ans ，该数组包含删除所有标记文件夹之后剩余文件夹的路径。路径可以按 任意顺序 返回。 示例 1： [https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder1.jpg] 输入：paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]] 输出：[["d"],["d","a"]] 解释：文件结构如上所示。 文件夹 "/a" 和 "/c"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含名为 "b" 的空文件夹。 示例 2： [https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder2.jpg] 输入：paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]] 输出：[["c"],["c","b"],["a"],["a","b"]] 解释：文件结构如上所示。 文件夹 "/a/b/x" 和 "/w"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含名为 "y" 的空文件夹。 注意，文件夹 "/a" 和 "/c" 在删除后变为相同文件夹，但这两个文件夹不会被删除，因为删除只会进行一次，且它们没有在删除前被标记。 示例 3： [https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder3.jpg] 输入：paths = [["a","b"],["c","d"],["c"],["a"]] 输出：[["c"],["c","d"],["a"],["a","b"]] 解释：文件系统中所有文件夹互不相同。 注意，返回的数组可以按不同顺序返回文件夹路径，因为题目对顺序没有要求。 示例 4： [https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder4_.jpg] 输入：paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]] 输出：[] 解释：文件结构如上所示。 文件夹 "/a/x" 和 "/b/x"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含名为 "y" 的空文件夹。 文件夹 "/a" 和 "/b"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含一个名为 "z" 的空文件夹以及上面提到的文件夹 "x" 。 示例 5： [https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder5_.jpg] 输入：paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]] 输出：[["b"],["b","w"],["b","z"],["a"],["a","z"]] 解释：本例与上例的结构基本相同，除了新增 "/b/w" 文件夹。 文件夹 "/a/x" 和 "/b/x" 仍然会被标记，但 "/a" 和 "/b" 不再被标记，因为 "/b" 中有名为 "w" 的空文件夹而 "/a" 没有。 注意，"/a/z" 和 "/b/z" 不会被标记，因为相同子文件夹的集合必须是非空集合，但这两个文件夹都是空的。 提示： * 1 <= paths.length <= 2 * 104 * 1 <= paths[i].length <= 500 * 1 <= paths[i][j].length <= 10 * 1 <= sum(paths[i][j].length) <= 2 * 105 * path[i][j] 由小写英文字母组成 * 不会存在两个路径都指向同一个文件夹的情况 * 对于不在根层级的任意文件夹，其父文件夹也会包含在输入中
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树 (Trie) 来构建文件系统的层次结构，并使用哈希表来记录每个子树的唯一标识。通过遍历 Trie 来找到并标记重复的子树。

算法步骤:
1. 构建 Trie 树，同时记录每个节点的子树的序列化形式。
2. 使用哈希表记录每个子树的序列化形式及其出现次数。
3. 再次遍历 Trie 树，标记出现次数大于 1 的子树。
4. 最后，收集未被标记的路径。

关键点:
- 使用 Trie 树来表示文件系统的层次结构。
- 使用哈希表记录每个子树的序列化形式及其出现次数。
- 通过遍历 Trie 树来标记和删除重复的子树。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N * M)，其中 N 是 paths 的长度，M 是每个路径的最大长度。
空间复杂度: O(N * M)，用于存储 Trie 树和哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_deleted = False
        self.subtree_hash = None

def build_trie(paths: List[List[str]]) -> TrieNode:
    root = TrieNode()
    for path in paths:
        node = root
        for folder in path:
            if folder not in node.children:
                node.children[folder] = TrieNode()
            node = node.children[folder]
    return root

def serialize_subtree(node: TrieNode) -> str:
    if not node.children:
        return ""
    subtree_hashes = []
    for key in sorted(node.children.keys()):
        subtree_hashes.append(f"{key}({serialize_subtree(node.children[key])})")
    return "".join(subtree_hashes)

def mark_duplicates(root: TrieNode, subtree_counts: dict):
    if not root.children:
        return
    for key in root.children:
        child = root.children[key]
        child.subtree_hash = serialize_subtree(child)
        subtree_counts[child.subtree_hash] = subtree_counts.get(child.subtree_hash, 0) + 1
        mark_duplicates(child, subtree_counts)

def collect_paths(node: TrieNode, current_path: List[str], result: List[List[str]]):
    if node.is_deleted:
        return
    if current_path:
        result.append(current_path[:])
    for key in node.children:
        current_path.append(key)
        collect_paths(node.children[key], current_path, result)
        current_path.pop()

def delete_duplicate_folders(paths: List[List[str]]) -> List[List[str]]:
    root = build_trie(paths)
    subtree_counts = {}
    mark_duplicates(root, subtree_counts)
    
    # Mark nodes with duplicate subtrees as deleted
    def mark_deleted_nodes(node: TrieNode):
        if not node.children:
            return
        for key in node.children:
            child = node.children[key]
            if subtree_counts[child.subtree_hash] > 1:
                child.is_deleted = True
            mark_deleted_nodes(child)
    
    mark_deleted_nodes(root)
    
    result = []
    collect_paths(root, [], result)
    return result

Solution = create_solution(delete_duplicate_folders)