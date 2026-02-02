# -*- coding:utf-8 -*-
"""
LeetCode题目元数据
用于按条件查询题号、难度、题型、周赛等信息
"""

from typing import List, Dict, Optional, Set

# 核心映射字典：题号 → 详细信息
PROBLEM_METADATA: Dict[int, Dict] = {
    1: {
        "id": 1,
        "title": "两数之和",
        "slug": "two-sum",
        "difficulty": "easy",
        "topics": ["array", "hash_table"],
        "is_premium": False,
        "is_interview": True,
        "contests": ["weekly_300"],  # 所属周赛列表
    },
    2: {
        "id": 2,
        "title": "两数相加",
        "slug": "add-two-numbers",
        "difficulty": "medium",
        "topics": ["linked_list", "math"],
        "is_premium": False,
        "is_interview": True,
        "contests": [],
    },
    3: {
        "id": 3,
        "title": "无重复字符的最长子串",
        "slug": "longest-substring-without-repeating-characters",
        "difficulty": "medium",
        "topics": ["hash_table", "string", "sliding_window"],
        "is_premium": False,
        "is_interview": True,
        "contests": [],
    },
    5: {
        "id": 5,
        "title": "最长回文子串",
        "slug": "longest-palindromic-substring",
        "difficulty": "medium",
        "topics": ["string", "dp"],
        "is_premium": False,
        "is_interview": True,
        "contests": [],
    },
    # 新增题目时，只需在这里添加条目即可
}


def get_problems_by_difficulty(difficulty: str) -> List[int]:
    """
    按难度查询题号列表
    
    Args:
        difficulty: 难度级别，可选值: "easy", "medium", "hard"
        
    Returns:
        题号列表
        
    Example:
        >>> get_problems_by_difficulty("easy")
        [1, ...]
    """
    difficulty = difficulty.lower()
    valid_difficulties = {"easy", "medium", "hard"}
    if difficulty not in valid_difficulties:
        return []
    
    return [k for k, v in PROBLEM_METADATA.items() if v["difficulty"] == difficulty]


def get_problems_by_topic(topic: str) -> List[int]:
    """
    按题型查询题号列表
    
    Args:
        topic: 题型，如 "array", "linked_list", "dp" 等
        
    Returns:
        题号列表
        
    Example:
        >>> get_problems_by_topic("array")
        [1, ...]
    """
    topic = topic.lower()
    return [k for k, v in PROBLEM_METADATA.items() if topic in [t.lower() for t in v["topics"]]]


def get_problems_by_contest(contest: str) -> List[int]:
    """
    按周赛查询题号列表
    
    Args:
        contest: 周赛名称，如 "weekly_300", "biweekly_100" 等
        
    Returns:
        题号列表
        
    Example:
        >>> get_problems_by_contest("weekly_300")
        [1, ...]
    """
    contest = contest.lower()
    return [k for k, v in PROBLEM_METADATA.items() if contest in [c.lower() for c in v.get("contests", [])]]


def get_premium_problems() -> List[int]:
    """
    获取所有会员题题号列表
    
    Returns:
        题号列表
    """
    return [k for k, v in PROBLEM_METADATA.items() if v.get("is_premium", False)]


def get_interview_problems() -> List[int]:
    """
    获取所有面试高频题题号列表
    
    Returns:
        题号列表
    """
    return [k for k, v in PROBLEM_METADATA.items() if v.get("is_interview", False)]


def get_problem_info(problem_id: int) -> Optional[Dict]:
    """
    获取指定题号的详细信息
    
    Args:
        problem_id: 题号
        
    Returns:
        题目信息字典，如果不存在返回None
        
    Example:
        >>> get_problem_info(1)
        {
            "id": 1,
            "title": "两数之和",
            "slug": "two-sum",
            "difficulty": "easy",
            "topics": ["array", "hash_table"],
            "is_premium": False,
            "is_interview": True,
            "contests": ["weekly_300"]
        }
    """
    return PROBLEM_METADATA.get(problem_id)


def get_all_topics() -> Set[str]:
    """
    获取所有题型列表
    
    Returns:
        题型集合
    """
    topics = set()
    for v in PROBLEM_METADATA.values():
        topics.update(v.get("topics", []))
    return topics


def get_all_contests() -> Set[str]:
    """
    获取所有周赛列表
    
    Returns:
        周赛名称集合
    """
    contests = set()
    for v in PROBLEM_METADATA.values():
        contests.update(v.get("contests", []))
    return contests

