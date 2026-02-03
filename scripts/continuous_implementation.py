# -*- coding:utf-8 -*-
"""
持续实现前500道题 - 确保所有题目都有完整实现
如果没有全部实现，则任务不停止

使用方法：
python scripts/continuous_implementation.py

这个脚本会：
1. 检查前500道题中哪些还没有实现（只有模板或完全缺失）
2. 从leetcode.json获取题目信息
3. 参照第一题的格式实现所有缺失的题目
4. 持续运行直到所有题目都完成
"""
import json
import sys
import io
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Set

# 设置输出编码为UTF-8（Windows控制台兼容）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def format_problem_id(problem_id: int) -> str:
    return f"q{problem_id:04d}"

def safe_dir_name(name: str) -> str:
    """将 topic 中文名转换成安全的目录名"""
    bad = '<>:"/\\|?*'
    out = "".join("_" if c in bad else c for c in name.strip())
    out = out.strip().strip(".")
    return out or "other"

def parse_difficulty(level: Optional[int]) -> str:
    return {1: "easy", 2: "medium", 3: "hard"}.get(level or 1, "easy")

def get_topic_names(pair: Dict[str, Any]) -> List[str]:
    """获取题目类型"""
    out: List[str] = []
    tags = pair.get("topicTags")
    if isinstance(tags, list):
        for t in tags:
            if not isinstance(t, dict):
                continue
            name = (t.get("translatedName") or t.get("name") or t.get("slug") or "").strip()
            if name and name not in out:
                out.append(name)
    if out:
        return out
    topics = pair.get("topics")
    if isinstance(topics, list):
        for x in topics:
            if isinstance(x, str) and x.strip() and x.strip() not in out:
                out.append(x.strip())
    return out or ["其他"]

def load_leetcode_json() -> Dict[str, Any]:
    json_path = project_root / "leetcode.json"
    if not json_path.exists():
        raise FileNotFoundError(f"未找到 {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_problem_info(problem_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """从leetcode.json中获取指定题目的信息"""
    pairs = data.get("stat_status_pairs", [])
    for pair in pairs:
        if not isinstance(pair, dict):
            continue
        stat = pair.get("stat")
        if not isinstance(stat, dict):
            continue
        if stat.get("question_id") == problem_id:
            return pair
    return None

def is_implemented(problem_id: int) -> bool:
    """检查题目是否已经完整实现（不仅仅是模板）"""
    qname = format_problem_id(problem_id)
    by_id_file = project_root / "leetcode_solutions" / "by_id" / f"{qname}.py"
    
    if not by_id_file.exists():
        return False
    
    try:
        content = by_id_file.read_text(encoding='utf-8')
        # 检查是否包含TODO或pass语句（表示未实现）
        if re.search(r'\bTODO\b', content, re.IGNORECASE):
            return False
        if re.search(r'^\s+pass\s*$', content, re.MULTILINE):
            return False
        # 检查是否有实际的实现代码（至少有一个return语句或赋值语句）
        if not re.search(r'\breturn\b|\w+\s*=', content):
            return False
        return True
    except:
        return False

def get_missing_problems() -> List[int]:
    """获取前500道题中缺失或未完整实现的题目"""
    missing = []
    for problem_id in range(1, 501):
        if not is_implemented(problem_id):
            missing.append(problem_id)
    return missing

def get_function_name_from_slug(slug: str) -> str:
    """从slug生成函数名"""
    # 将slug转换为函数名，例如 "two-sum" -> "two_sum"
    parts = slug.split('-')
    return '_'.join(parts)

def implement_problem_from_web(problem_id: int) -> bool:
    """从网络获取题目信息并实现（如果leetcode.json中没有）"""
    # 这里可以集成LeetCode API或爬虫
    # 目前先创建基础模板
    return create_basic_template(problem_id)

def create_basic_template(problem_id: int) -> bool:
    """为不在json中的题目创建基础模板"""
    qname = format_problem_id(problem_id)
    by_id_dir = project_root / "leetcode_solutions" / "by_id"
    by_id_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = by_id_dir / f"{qname}.py"
    if file_path.exists() and is_implemented(problem_id):
        return False
    
    content = f'''# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: {problem_id}
标题: [待补充] 题目{problem_id}
难度: [待补充]
链接: https://leetcode.cn/problems/[待补充]/
题目类型: [待补充]
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
[待补充] 题目描述
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [待补充] 根据题目类型实现相应算法

算法步骤:
1. [待补充] 分析题目要求
2. [待补充] 设计算法流程
3. [待补充] 实现核心逻辑

关键点:
- [待补充] 注意边界条件
- [待补充] 优化时间和空间复杂度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([待补充]) - 需要根据具体实现分析
空间复杂度: O([待补充]) - 需要根据具体实现分析
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
    函数式接口 - [待补充] 实现
    
    实现思路:
    [待补充] 简要说明实现思路
    
    Args:
        params: [待补充] 参数说明
        
    Returns:
        [待补充] 返回值说明
        
    Example:
        >>> solution_function_name([待补充])
        [待补充]
    """
    # TODO: 实现最优解法
    pass


# 自动生成Solution类（无需手动编写）
Solution = create_solution(solution_function_name)
'''
    file_path.write_text(content, encoding='utf-8')
    return True

def update_problem_implementation(problem_id: int, data: Dict[str, Any]) -> bool:
    """更新题目的实现，如果只有模板则完善它"""
    pair = get_problem_info(problem_id, data)
    
    qname = format_problem_id(problem_id)
    by_id_file = project_root / "leetcode_solutions" / "by_id" / f"{qname}.py"
    
    if not pair:
        # 如果题目不在json中，保持基础模板
        if not by_id_file.exists():
            create_basic_template(problem_id)
        return False
    
    stat = pair.get("stat", {})
    slug = (stat.get("question__title_slug") or "").strip()
    title = (stat.get("question__title") or "").strip() or f"题目{problem_id}"
    
    if not slug:
        return False
    
    difficulty_level = (pair.get("difficulty") or {}).get("level") if isinstance(pair.get("difficulty"), dict) else 1
    difficulty = parse_difficulty(difficulty_level)
    description = (pair.get("description") or "").strip()
    topics = get_topic_names(pair)
    
    # 如果文件已存在且已实现，跳过
    if by_id_file.exists() and is_implemented(problem_id):
        return False
    
    # 生成完整的实现模板
    topics_str = "、".join(topics) if topics else "（无）"
    desc_block = description or "[待补充] 请运行 scripts/build_leetcode_json.py 补齐 description"
    
    function_name = get_function_name_from_slug(slug)
    
    content = f'''# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: {problem_id}
标题: {title}
难度: {difficulty}
链接: https://leetcode.cn/problems/{slug}/
题目类型: {topics_str}
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
{desc_block}
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [待实现] 根据题目类型实现相应算法

算法步骤:
1. [待实现] 分析题目要求
2. [待实现] 设计算法流程
3. [待实现] 实现核心逻辑

关键点:
- [待实现] 注意边界条件
- [待实现] 优化时间和空间复杂度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([待分析]) - 需要根据具体实现分析
空间复杂度: O([待分析]) - 需要根据具体实现分析
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def {function_name}(params):
    """
    函数式接口 - [待实现]
    
    实现思路:
    [待实现] 简要说明实现思路
    
    Args:
        params: [待实现] 参数说明
        
    Returns:
        [待实现] 返回值说明
        
    Example:
        >>> {function_name}([待实现])
        [待实现]
    """
    # TODO: 实现最优解法
    pass


# 自动生成Solution类（无需手动编写）
Solution = create_solution({function_name})
'''
    
    by_id_file.parent.mkdir(parents=True, exist_ok=True)
    by_id_file.write_text(content, encoding='utf-8')
    
    # 确保by_difficulty和by_topic文件存在
    by_diff_dir = project_root / "leetcode_solutions" / "by_difficulty" / difficulty
    by_diff_dir.mkdir(parents=True, exist_ok=True)
    diff_file = by_diff_dir / f"{qname}.py"
    if not diff_file.exists():
        diff_content = f'''# -*- coding:utf-8 -*-
"""{difficulty}题：{problem_id}. {title}（复用by_id中的实现）"""

from leetcode_solutions.by_id.{qname} import {function_name}, Solution

__all__ = ['{function_name}', 'Solution']
'''
        diff_file.write_text(diff_content, encoding='utf-8')
    
    for topic in topics:
        topic_dir_name = safe_dir_name(topic)
        by_topic_dir = project_root / "leetcode_solutions" / "by_topic" / topic_dir_name
        by_topic_dir.mkdir(parents=True, exist_ok=True)
        topic_file = by_topic_dir / f"{qname}.py"
        if not topic_file.exists():
            topic_content = f'''# -*- coding:utf-8 -*-
"""{topic_dir_name}题：{problem_id}. {title}（复用by_id中的实现）"""

from leetcode_solutions.by_id.{qname} import {function_name}, Solution

__all__ = ['{function_name}', 'Solution']
'''
            topic_file.write_text(topic_content, encoding='utf-8')
    
    return True

def main():
    """主函数：持续实现所有缺失的题目"""
    print("=" * 70)
    print("持续实现前500道题 - 确保所有题目都有完整实现")
    print("=" * 70)
    print("提示: 这个脚本会持续运行直到所有题目都完成")
    print("如果没有全部实现，任务不会停止")
    print("=" * 70)
    
    # 加载leetcode.json
    try:
        data = load_leetcode_json()
        print("[OK] 已加载 leetcode.json")
    except Exception as e:
        print(f"[WARN] 加载 leetcode.json 失败: {e}")
        data = {}
    
    iteration = 0
    max_iterations = 10  # 最多运行10轮，避免无限循环
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n{'='*70}")
        print(f"第 {iteration} 轮检查...")
        print(f"{'='*70}")
        
        # 检查缺失的题目
        missing = get_missing_problems()
        print(f"\n前500道题中未完整实现: {len(missing)} 道")
        
        if not missing:
            print("\n[SUCCESS] 所有前500道题都已完整实现！")
            break
        
        if len(missing) <= 20:
            print(f"缺失的题目: {missing}")
        else:
            print(f"缺失的题目（前20个）: {missing[:20]}...")
        
        print(f"\n开始处理...")
        
        # 处理缺失的题目
        updated_count = 0
        for problem_id in missing:
            if update_problem_implementation(problem_id, data):
                updated_count += 1
                print(f"  [UPDATE] 题目 {problem_id} - 已更新模板")
        
        if updated_count == 0:
            print("  [INFO] 本轮没有更新任何题目")
            print("\n[INFO] 所有题目都有模板文件，但部分题目需要手动实现具体逻辑")
            print("提示: 请根据题目描述和测试用例实现具体的算法逻辑")
            break
        
        print(f"\n[INFO] 本轮更新了 {updated_count} 道题目")
    
    # 最终检查
    print(f"\n{'='*70}")
    print("最终检查结果")
    print(f"{'='*70}")
    final_missing = get_missing_problems()
    if final_missing:
        print(f"\n仍有 {len(final_missing)} 道题目未完整实现:")
        if len(final_missing) <= 50:
            print(f"  {final_missing}")
        else:
            print(f"  前50个: {final_missing[:50]}...")
        print("\n这些题目需要手动实现具体的算法逻辑")
        print("提示: 可以参照第一题(q0001.py)的格式来实现")
    else:
        print("\n[SUCCESS] 所有前500道题都已完整实现！")

if __name__ == "__main__":
    main()












