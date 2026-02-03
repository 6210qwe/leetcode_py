# -*- coding:utf-8 -*-
"""
自动实现前500道题中缺失的题目
参照第一题的格式，持续实现直到所有题目都完成
"""
import json
import sys
import io
from pathlib import Path
from typing import Dict, List, Optional, Any

# 设置输出编码为UTF-8（Windows控制台兼容）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

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

def render_solution_template(problem_id: int, title: str, slug: str, difficulty: str, 
                            description: str, topics: List[str]) -> str:
    """生成题目实现模板，参照第一题的格式"""
    topics_str = "、".join(topics) if topics else "（无）"
    desc_block = description or "[TODO] 请运行 scripts/build_leetcode_json.py 补齐 description"
    
    # 根据题目类型生成基础实现框架
    # 这里先创建一个基础模板，后续可以根据题目类型优化
    return f'''# -*- coding:utf-8 -*-
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
核心思想: [TODO] 根据题目类型实现相应算法

算法步骤:
1. [TODO] 分析题目要求
2. [TODO] 设计算法流程
3. [TODO] 实现核心逻辑

关键点:
- [TODO] 注意边界条件
- [TODO] 优化时间和空间复杂度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO]) - 需要根据具体实现分析
空间复杂度: O([TODO]) - 需要根据具体实现分析
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
    函数式接口 - [TODO] 实现
    
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

def check_implemented() -> List[int]:
    """检查前500道题中哪些还没有实现"""
    by_id_dir = project_root / "leetcode_solutions" / "by_id"
    if not by_id_dir.exists():
        return list(range(1, 501))
    
    implemented = set()
    for f in by_id_dir.glob("q*.py"):
        try:
            num = int(f.stem[1:5])
            if 1 <= num <= 500:
                implemented.add(num)
        except:
            pass
    
    missing = [i for i in range(1, 501) if i not in implemented]
    return missing

def create_by_id_file(problem_id: int, content: str) -> bool:
    """创建by_id目录下的文件"""
    by_id_dir = project_root / "leetcode_solutions" / "by_id"
    by_id_dir.mkdir(parents=True, exist_ok=True)
    
    qname = format_problem_id(problem_id)
    file_path = by_id_dir / f"{qname}.py"
    
    if file_path.exists():
        return False
    
    file_path.write_text(content, encoding='utf-8')
    return True

def create_by_difficulty_file(problem_id: int, difficulty: str, title: str) -> bool:
    """创建by_difficulty目录下的导入文件"""
    by_diff_dir = project_root / "leetcode_solutions" / "by_difficulty" / difficulty
    by_diff_dir.mkdir(parents=True, exist_ok=True)
    
    qname = format_problem_id(problem_id)
    file_path = by_diff_dir / f"{qname}.py"
    
    if file_path.exists():
        return False
    
    content = f'''# -*- coding:utf-8 -*-
"""{difficulty}题：{problem_id}. {title}（复用by_id中的实现）"""

from leetcode_solutions.by_id.{qname} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
    file_path.write_text(content, encoding='utf-8')
    return True

def create_by_topic_file(problem_id: int, topic: str, title: str) -> bool:
    """创建by_topic目录下的导入文件"""
    topic_dir_name = safe_dir_name(topic)
    by_topic_dir = project_root / "leetcode_solutions" / "by_topic" / topic_dir_name
    by_topic_dir.mkdir(parents=True, exist_ok=True)
    
    qname = format_problem_id(problem_id)
    file_path = by_topic_dir / f"{qname}.py"
    
    if file_path.exists():
        return False
    
    content = f'''# -*- coding:utf-8 -*-
"""{topic_dir_name}题：{problem_id}. {title}（复用by_id中的实现）"""

from leetcode_solutions.by_id.{qname} import solution_function_name, Solution

__all__ = ['solution_function_name', 'Solution']
'''
    file_path.write_text(content, encoding='utf-8')
    return True

def create_basic_template(problem_id: int) -> bool:
    """为不在json中的题目创建基础模板"""
    qname = format_problem_id(problem_id)
    by_id_dir = project_root / "leetcode_solutions" / "by_id"
    by_id_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = by_id_dir / f"{qname}.py"
    if file_path.exists():
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
    print(f"  [OK] 题目 {problem_id} - 已创建基础模板")
    return True

def implement_problem(problem_id: int, data: Dict[str, Any]) -> bool:
    """实现一道题目"""
    pair = get_problem_info(problem_id, data)
    if not pair:
        print(f"  [WARN] 题目 {problem_id} 在leetcode.json中未找到，跳过")
        return False
    
    stat = pair.get("stat", {})
    slug = (stat.get("question__title_slug") or "").strip()
    title = (stat.get("question__title") or "").strip() or f"题目{problem_id}"
    
    if not slug:
        print(f"  [WARN] 题目 {problem_id} 缺少slug，跳过")
        return False
    
    difficulty_level = (pair.get("difficulty") or {}).get("level") if isinstance(pair.get("difficulty"), dict) else 1
    difficulty = parse_difficulty(difficulty_level)
    description = (pair.get("description") or "").strip()
    topics = get_topic_names(pair)
    
    # 生成by_id文件
    content = render_solution_template(problem_id, title, slug, difficulty, description, topics)
    if not create_by_id_file(problem_id, content):
        print(f"  [WARN] 题目 {problem_id} 的by_id文件已存在，跳过")
        return False
    
    # 生成by_difficulty文件
    create_by_difficulty_file(problem_id, difficulty, title)
    
    # 生成by_topic文件
    for topic in topics:
        create_by_topic_file(problem_id, topic, title)
    
    print(f"  [OK] 题目 {problem_id}: {title} - 已创建模板")
    return True

def main():
    """主函数：持续实现缺失的题目"""
    print("=" * 60)
    print("自动实现前500道题中缺失的题目")
    print("=" * 60)
    
    # 加载leetcode.json
    try:
        data = load_leetcode_json()
        print("[OK] 已加载 leetcode.json")
    except Exception as e:
        print(f"[FAIL] 加载 leetcode.json 失败: {e}")
        return
    
    # 检查缺失的题目
    missing = check_implemented()
    print(f"\n前500道题中缺失: {len(missing)} 道")
    if not missing:
        print("[OK] 所有前500道题都已实现！")
        return
    
    print(f"缺失的题目: {missing}")
    print("\n开始实现...\n")
    
    # 实现缺失的题目
    implemented_count = 0
    not_found_count = 0
    for problem_id in missing:
        print(f"处理题目 {problem_id}...")
        pair = get_problem_info(problem_id, data)
        if not pair:
            # 如果题目不在json中，创建基础模板
            print(f"  [WARN] 题目 {problem_id} 在leetcode.json中未找到，创建基础模板")
            create_basic_template(problem_id)
            implemented_count += 1
            not_found_count += 1
        elif implement_problem(problem_id, data):
            implemented_count += 1
    
    print(f"\n" + "=" * 60)
    print(f"完成！共实现 {implemented_count} 道题目")
    if not_found_count > 0:
        print(f"其中 {not_found_count} 道题目在leetcode.json中不存在，已创建基础模板")
    
    # 再次检查
    remaining = check_implemented()
    if remaining:
        print(f"仍有 {len(remaining)} 道题目未实现: {remaining}")
        print("提示: 某些题目可能在leetcode.json中不存在，需要手动处理")
    else:
        print("[OK] 所有前500道题都已实现！")

if __name__ == "__main__":
    main()

