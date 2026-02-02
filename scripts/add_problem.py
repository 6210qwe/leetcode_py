# -*- coding:utf-8 -*-
"""
辅助脚本：添加新题目时自动生成分类导入文件
使用方法: python scripts/add_problem.py <题号> <难度> <题型1,题型2,...> [周赛1,周赛2,...]
示例: python scripts/add_problem.py 10 easy "array,hash_table" "weekly_300"
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def format_problem_id(problem_id: int) -> str:
    """格式化题号为4位字符串"""
    return f"q{problem_id:04d}"


def create_by_id_file(problem_id: int, difficulty: str, topics: list, contests: list):
    """创建by_id目录下的核心实现文件（需要手动填写实现）"""
    problem_id_str = format_problem_id(problem_id)
    file_path = project_root / "leetcode_solutions" / "by_id" / f"{problem_id_str}.py"
    
    if file_path.exists():
        print(f"警告: {file_path} 已存在，跳过创建")
        return
    
    # 从metadata获取题目信息
    from leetcode_solutions.metadata import PROBLEM_METADATA
    problem_info = PROBLEM_METADATA.get(problem_id, {})
    title = problem_info.get("title", f"题目{problem_id}")
    slug = problem_info.get("slug", f"problem-{problem_id}")
    
    content = f'''# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: {problem_id}
标题: {title}
难度: {difficulty}
链接: https://leetcode.cn/problems/{slug}/
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
[TODO] 在这里详细描述题目要求

示例1:
输入: [TODO]
输出: [TODO]
解释: [TODO]

示例2:
输入: [TODO]
输出: [TODO]
解释: [TODO]

约束条件:
- [TODO]
- [TODO]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO] 简要说明核心思想

算法步骤:
1. 步骤1: [TODO]
2. 步骤2: [TODO]
3. 步骤3: [TODO]

关键点:
- [TODO] 关键点1
- [TODO] 关键点2
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO]) - [TODO] 说明原因
空间复杂度: O([TODO]) - [TODO] 说明原因
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [算法名称]实现
    
    实现思路:
    [TODO] 简要说明实现思路
    
    Args:
        params: [TODO] 参数说明
        
    Returns:
        [TODO] 返回值说明
        
    Example:
        >>> solution_function_name([TODO])
        [TODO]
    """
    # TODO: 实现最优解法
    pass


# 自动生成Solution类（无需手动编写）
Solution = create_solution(solution_function_name)
'''
    
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ 已创建: {file_path}")


def create_difficulty_file(problem_id: int, difficulty: str):
    """创建难度分类下的导入文件"""
    problem_id_str = format_problem_id(problem_id)
    
    difficulty_map = {
        "easy": "easy",
        "medium": "medium",
        "hard": "hard",
    }
    
    if difficulty not in difficulty_map:
        return
    
    dir_path = project_root / "leetcode_solutions" / "by_difficulty" / difficulty_map[difficulty]
    dir_path.mkdir(parents=True, exist_ok=True)
    
    file_path = dir_path / f"{problem_id_str}.py"
    
    if file_path.exists():
        print(f"警告: {file_path} 已存在，跳过创建")
        return
    
    content = f'''# -*- coding:utf-8 -*-
"""{difficulty_map[difficulty]}题：{problem_id}. [题目名称]（复用by_id中的实现）"""

from leetcode_solutions.by_id.{problem_id_str} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
    
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ 已创建: {file_path}")


def create_topic_file(problem_id: int, topic: str):
    """创建题型分类下的导入文件"""
    problem_id_str = format_problem_id(problem_id)
    
    dir_path = project_root / "leetcode_solutions" / "by_topic" / topic
    dir_path.mkdir(parents=True, exist_ok=True)
    
    file_path = dir_path / f"{problem_id_str}.py"
    
    if file_path.exists():
        print(f"警告: {file_path} 已存在，跳过创建")
        return
    
    content = f'''# -*- coding:utf-8 -*-
"""{topic}题：{problem_id}. [题目名称]（复用by_id中的实现）"""

from leetcode_solutions.by_id.{problem_id_str} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
    
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ 已创建: {file_path}")


def create_contest_file(problem_id: int, contest: str):
    """创建周赛分类下的导入文件"""
    problem_id_str = format_problem_id(problem_id)
    
    dir_path = project_root / "leetcode_solutions" / "by_contest" / contest
    dir_path.mkdir(parents=True, exist_ok=True)
    
    file_path = dir_path / f"{problem_id_str}.py"
    
    if file_path.exists():
        print(f"警告: {file_path} 已存在，跳过创建")
        return
    
    content = f'''# -*- coding:utf-8 -*-
"""{contest}：{problem_id}. [题目名称]（复用by_id中的实现）"""

from leetcode_solutions.by_id.{problem_id_str} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
    
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ 已创建: {file_path}")


def update_metadata(problem_id: int, difficulty: str, topics: list, contests: list, 
                   title: str = "", slug: str = "", is_premium: bool = False, 
                   is_interview: bool = False):
    """更新metadata.py文件"""
    metadata_path = project_root / "leetcode_solutions" / "metadata.py"
    
    # 读取现有内容
    content = metadata_path.read_text(encoding='utf-8')
    
    # 生成新的条目
    if not title:
        title = f"题目{problem_id}"
    if not slug:
        slug = f"problem-{problem_id}"
    
    new_entry = f'''    {problem_id}: {{
        "id": {problem_id},
        "title": "{title}",
        "slug": "{slug}",
        "difficulty": "{difficulty.lower()}",
        "topics": {topics},
        "is_premium": {is_premium},
        "is_interview": {is_interview},
        "contests": {contests},
    }},'''
    
    # 找到PROBLEM_METADATA字典的结束位置
    if f'    {problem_id}:' in content:
        print(f"警告: metadata.py中已存在题目{problem_id}的条目，请手动更新")
        return
    
    # 在字典末尾（最后一个}之前）插入新条目
    lines = content.split('\n')
    insert_pos = None
    for i, line in enumerate(lines):
        if 'PROBLEM_METADATA: Dict[int, Dict] = {' in line:
            # 找到字典开始
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == '}' and lines[j-1].strip().endswith(','):
                    insert_pos = j
                    break
            break
    
    if insert_pos:
        lines.insert(insert_pos, new_entry)
        metadata_path.write_text('\n'.join(lines), encoding='utf-8')
        print(f"✓ 已更新: {metadata_path}")
    else:
        print(f"警告: 无法自动更新metadata.py，请手动添加以下内容：")
        print(new_entry)


def main():
    if len(sys.argv) < 4:
        print("使用方法: python scripts/add_problem.py <题号> <难度> <题型1,题型2,...> [周赛1,周赛2,...]")
        print("示例: python scripts/add_problem.py 10 easy \"array,hash_table\" \"weekly_300\"")
        sys.exit(1)
    
    problem_id = int(sys.argv[1])
    difficulty = sys.argv[2].lower()
    topics = [t.strip() for t in sys.argv[3].split(',')]
    contests = [c.strip() for c in sys.argv[4].split(',')] if len(sys.argv) > 4 else []
    
    print(f"添加题目 {problem_id}:")
    print(f"  难度: {difficulty}")
    print(f"  题型: {topics}")
    print(f"  周赛: {contests}")
    print()
    
    # 创建文件
    create_by_id_file(problem_id, difficulty, topics, contests)
    create_difficulty_file(problem_id, difficulty)
    
    for topic in topics:
        create_topic_file(problem_id, topic)
    
    for contest in contests:
        create_contest_file(problem_id, contest)
    
    # 更新metadata（需要手动填写title和slug）
    update_metadata(problem_id, difficulty, topics, contests)
    
    print()
    print("✓ 文件创建完成！")
    print("⚠ 请手动完成以下步骤：")
    print("  1. 在 by_id/qXXXX.py 中实现最优解法")
    print("  2. 在 metadata.py 中补充题目的 title 和 slug")
    print("  3. 更新各分类文件中的函数名和类名")


if __name__ == "__main__":
    main()

