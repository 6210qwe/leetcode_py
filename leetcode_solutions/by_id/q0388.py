# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 388
标题: Longest Absolute File Path
难度: medium
链接: https://leetcode.cn/problems/longest-absolute-file-path/
题目类型: 栈、深度优先搜索、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
388. 文件的最长绝对路径 - 假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例： [https://assets.leetcode.com/uploads/2020/08/28/mdir.jpg] 这里将 dir 作为根目录中的唯一目录。dir 包含两个子目录 subdir1 和 subdir2 。subdir1 包含文件 file1.ext 和子目录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。 在文本格式中，如下所示(⟶表示制表符)： dir ⟶ subdir1 ⟶ ⟶ file1.ext ⟶ ⟶ subsubdir1 ⟶ subdir2 ⟶ ⟶ subsubdir2 ⟶ ⟶ ⟶ file2.ext 如果是代码表示，上面的文件系统可以写为 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 。'\n' 和 '\t' 分别是换行符和制表符。 文件系统中的每个文件和文件夹都有一个唯一的 绝对路径 ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 '/' 连接。上面例子中，指向 file2.ext 的 绝对路径 是 "dir/subdir2/subsubdir2/file2.ext" 。每个目录名由字母、数字和/或空格组成，每个文件名遵循 name.extension 的格式，其中 name 和 extension由字母、数字和/或空格组成。 给定一个以上述格式表示文件系统的字符串 input ，返回文件系统中 指向 文件 的 最长绝对路径 的长度 。 如果系统中没有文件，返回 0。 示例 1： [https://assets.leetcode.com/uploads/2020/08/28/dir1.jpg] 输入：input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" 输出：20 解释：只有一个文件，绝对路径为 "dir/subdir2/file.ext" ，路径长度 20 示例 2： [https://assets.leetcode.com/uploads/2020/08/28/dir2.jpg] 输入：input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 输出：32 解释：存在两个文件： "dir/subdir1/file1.ext" ，路径长度 21 "dir/subdir2/subsubdir2/file2.ext" ，路径长度 32 返回 32 ，因为这是最长的路径 示例 3： 输入：input = "a" 输出：0 解释：不存在任何文件 示例 4： 输入：input = "file1.txt\nfile2.txt\nlongfile.txt" 输出：12 解释：根目录下有 3 个文件。 因为根目录中任何东西的绝对路径只是名称本身，所以答案是 "longfile.txt" ，路径长度为 12 提示： * 1 <= input.length <= 104 * input 可能包含小写或大写的英文字母，一个换行符 '\n'，一个制表符 '\t'，一个点 '.'，一个空格 ' '，和数字。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 按行解析带有 '\n' 和 '\t' 的文本，利用栈或数组记录每一层目录的当前路径长度，遇到文件时更新最长绝对路径

算法步骤:
1. 先按 '\n' 将整个字符串分割成多行，每一行代表一个文件或目录。
2. 对于每一行，统计其开头连续 '\t' 的个数 depth，表示当前节点的层级（根目录为 0）。
3. 取出该行除去 '\t' 后的名字 name：
   - 使用一个数组或字典 len\_at\_depth，其中 len\_at\_depth[d] 表示深度 d 目录的「绝对路径长度」（不含末尾的 '/'）。
   - 当前节点的完整路径长度为：curLen = (depth == 0 ? 0 : len\_at\_depth[depth-1] + 1) + len(name)，其中加 1 是中间的 '/'。
4. 如果 name 中包含 '.'，说明这是一个文件，则用 curLen 更新答案 maxLen；否则这是目录，记录 len\_at\_depth[depth] = curLen。
5. 遍历所有行后返回 maxLen，若始终未遇到文件则返回 0。

关键点:
- 深度 depth 可以直接由 '\t' 个数得到，不需要显式维护树结构。
- 目录的路径长度会被后代复用，因此要存入 len\_at\_depth，用于下一层计算。
- 注意区分文件和目录：简单地用是否包含 '.' 判断即可（题目保证格式合法）。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n 为字符串长度，每个字符最多被扫描常数次。
空间复杂度: O(d) - d 为最大目录深度，len\_at\_depth 数组大小与之同阶，通常远小于 n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_absolute_file_path(input: str) -> int:
    """
    给定文件系统字符串，返回最长文件绝对路径的长度。
    """
    if not input:
        return 0

    max_len = 0
    # depth -> 当前目录绝对路径长度（不含末尾的 '/'）
    depth_len: dict[int, int] = {0: 0}

    for line in input.split("\n"):
        # 统计前导 '\t' 个数作为深度
        depth = 0
        while depth < len(line) and line.startswith("\t", depth):
            depth += 1
        name = line[depth:]
        # 当前节点完整路径长度
        cur_len = depth_len[depth] = depth_len.get(depth - 1, 0) + (1 if depth > 0 else 0) + len(name)
        if "." in name:  # 文件
            max_len = max(max_len, cur_len)

    return max_len


# 自动生成Solution类（无需手动编写）
Solution = create_solution(longest_absolute_file_path)
