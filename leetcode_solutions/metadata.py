# -*- coding:utf-8 -*-
"""
LeetCode题目元数据（从 leetcode.json 动态加载）
用于按条件查询题号、难度、题型、周赛等信息

数据源：项目根目录的 leetcode.json（由 scripts/build_leetcode_json.py 生成/更新）
"""

import json
from pathlib import Path
from typing import List, Dict, Optional, Set

# 项目根目录
_project_root = Path(__file__).parent.parent
_json_path = _project_root / "leetcode.json"

# 缓存：避免重复加载
_cached_metadata: Optional[Dict[int, Dict]] = None
_cached_json_mtime: Optional[float] = None


def _load_metadata() -> Dict[int, Dict]:
    """
    从 leetcode.json 加载并转换为 PROBLEM_METADATA 格式
    只在文件修改时重新加载（基于 mtime）
    """
    global _cached_metadata, _cached_json_mtime
    
    if not _json_path.exists():
        return {}
    
    # 检查文件是否修改
    current_mtime = _json_path.stat().st_mtime
    if _cached_metadata is not None and _cached_json_mtime == current_mtime:
        return _cached_metadata
    
    # 加载 JSON
    try:
        with open(_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        return {}
    
    # 转换为 PROBLEM_METADATA 格式
    metadata: Dict[int, Dict] = {}
    pairs = data.get("stat_status_pairs", [])
    
    for pair in pairs:
        if not isinstance(pair, dict):
            continue
        
        stat = pair.get("stat", {})
        if not isinstance(stat, dict):
            continue
        
        problem_id = stat.get("question_id")
        if not isinstance(problem_id, int):
            continue
        
        # 解析难度
        difficulty_map = {1: 'easy', 2: 'medium', 3: 'hard'}
        difficulty_level = pair.get("difficulty", {}).get("level", 1) if isinstance(pair.get("difficulty"), dict) else 1
        difficulty = difficulty_map.get(difficulty_level, 'easy')
        
        # 解析 topics（从 topicTags 或 topics 字段）
        topics: List[str] = []
        topic_tags = pair.get("topicTags")
        if isinstance(topic_tags, list):
            for tag in topic_tags:
                if isinstance(tag, dict):
                    name = tag.get("translatedName") or tag.get("name") or tag.get("slug") or ""
                    if name and name not in topics:
                        topics.append(name)
        
        if not topics:
            topics_list = pair.get("topics")
            if isinstance(topics_list, list):
                for t in topics_list:
                    if isinstance(t, str) and t.strip() and t.strip() not in topics:
                        topics.append(t.strip())
        
        if not topics:
            topics = ['other']
        
        # 构建元数据条目
        metadata[problem_id] = {
            "id": problem_id,
            "title": stat.get("question__title", ""),
            "slug": stat.get("question__title_slug", ""),
            "difficulty": difficulty,
            "topics": topics,
            "is_premium": pair.get("paid_only", False),
            "is_interview": pair.get("is_interview", False),
            "description": pair.get("description", ""),
            "contests": pair.get("contests", []),
        }
    
    # 更新缓存
    _cached_metadata = metadata
    _cached_json_mtime = current_mtime
    
    return metadata


# 核心映射字典：题号 → 详细信息（动态加载）
def _get_problem_metadata() -> Dict[int, Dict]:
    """获取 PROBLEM_METADATA（延迟加载）"""
    return _load_metadata()


# 为了兼容性，提供一个属性访问方式
class _MetadataProxy:
    """代理类，让 PROBLEM_METADATA 看起来像字典"""
    
    def items(self):
        return _get_problem_metadata().items()
    
    def keys(self):
        return _get_problem_metadata().keys()
    
    def values(self):
        return _get_problem_metadata().values()
    
    def get(self, key, default=None):
        return _get_problem_metadata().get(key, default)
    
    def __getitem__(self, key):
        return _get_problem_metadata()[key]
    
    def __contains__(self, key):
        return key in _get_problem_metadata()
    
    def __len__(self):
        return len(_get_problem_metadata())
    
    def __iter__(self):
        return iter(_get_problem_metadata())


# 导出 PROBLEM_METADATA（兼容原有代码）
PROBLEM_METADATA: Dict[int, Dict] = _MetadataProxy()  # type: ignore


def get_problems_by_difficulty(difficulty: str) -> List[int]:
    """
    按难度查询题号列表
    
    Args:
        difficulty: 难度级别，可选值: "easy", "medium", "hard"
        
    Returns:
        题号列表
        
    Example:
        >>> get_problems_by_difficulty("easy")
        [1, 2, ...]
    """
    difficulty = difficulty.lower()
    valid_difficulties = {"easy", "medium", "hard"}
    if difficulty not in valid_difficulties:
        return []
    
    metadata = _get_problem_metadata()
    return [k for k, v in metadata.items() if v["difficulty"] == difficulty]


def get_problems_by_topic(topic: str) -> List[int]:
    """
    按题型查询题号列表
    
    Args:
        topic: 题型，如 "数组", "链表", "动态规划" 等（支持中文标签名）
        
    Returns:
        题号列表
        
    Example:
        >>> get_problems_by_topic("数组")
        [1, 2, ...]
    """
    topic = topic.lower()
    metadata = _get_problem_metadata()
    return [
        k for k, v in metadata.items()
        if topic in [t.lower() for t in v.get("topics", [])]
    ]


def get_problems_by_contest(contest: str) -> List[int]:
    """
    按周赛查询题号列表
    
    Args:
        contest: 周赛名称，如 "weekly_300", "biweekly_100" 等
        
    Returns:
        题号列表
        
    Example:
        >>> get_problems_by_contest("weekly_300")
        [1, 2, ...]
    """
    contest = contest.lower()
    metadata = _get_problem_metadata()
    return [
        k for k, v in metadata.items()
        if contest in [c.lower() for c in v.get("contests", [])]
    ]


def get_premium_problems() -> List[int]:
    """
    获取所有会员题题号列表
    
    Returns:
        题号列表
    """
    metadata = _get_problem_metadata()
    return [k for k, v in metadata.items() if v.get("is_premium", False)]


def get_interview_problems() -> List[int]:
    """
    获取所有面试高频题题号列表
    
    Returns:
        题号列表
    """
    metadata = _get_problem_metadata()
    return [k for k, v in metadata.items() if v.get("is_interview", False)]


def get_problem_info(problem_id: int) -> Optional[Dict]:
    """
    获取指定题号的详细信息
    
    Args:
        problem_id: 题号
        
    Returns:
        题目信息字典，如果不存在返回None
        
    Example:
        >>> get_problem_info(1)
        {'id': 1, 'title': '两数之和', ...}
    """
    metadata = _get_problem_metadata()
    return metadata.get(problem_id)


def get_all_topics() -> Set[str]:
    """
    获取所有题型列表
    
    Returns:
        题型集合
    """
    metadata = _get_problem_metadata()
    topics = set()
    for v in metadata.values():
        topics.update(v.get("topics", []))
    return topics


def get_all_contests() -> Set[str]:
    """
    获取所有周赛列表
    
    Returns:
        周赛名称集合
    """
    metadata = _get_problem_metadata()
    contests = set()
    for v in metadata.values():
        contests.update(v.get("contests", []))
    return contests
