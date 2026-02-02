# -*- coding:utf-8 -*-
"""
Solution类生成工具
用于自动将函数式实现转换为LeetCode标准的Solution类
"""

from typing import Callable, Any


def create_solution(func: Callable) -> type:
    """
    将函数式实现自动转换为LeetCode标准的Solution类
    
    Args:
        func: 函数式实现
        
    Returns:
        Solution类
        
    Example:
        >>> def two_sum(nums, target):
        ...     return [0, 1]
        >>> Solution = create_solution(two_sum)
        >>> s = Solution()
        >>> s.twoSum([2, 7, 11, 15], 9)
        [0, 1]
    """
    # 获取函数名，转换为驼峰命名（LeetCode标准格式）
    func_name = func.__name__
    method_name = _to_camel_case(func_name)
    
    # 创建Solution类
    class Solution:
        """LeetCode提交格式的类（自动生成）"""
        
        def __init__(self):
            self._func = func
        
        def __call__(self, *args, **kwargs):
            """支持直接调用Solution实例"""
            return func(*args, **kwargs)
    
    # 动态添加方法
    def method_wrapper(self, *args, **kwargs):
        """方法包装器"""
        return func(*args, **kwargs)
    
    # 设置方法名和文档
    method_wrapper.__name__ = method_name
    method_wrapper.__doc__ = f"LeetCode标准接口\n\n{func.__doc__ or ''}"
    
    # 绑定方法到类
    setattr(Solution, method_name, method_wrapper)
    
    # 设置类的文档
    Solution.__doc__ = f"LeetCode提交格式的类（自动生成）\n\n原函数: {func_name}"
    
    return Solution


def _to_camel_case(snake_str: str) -> str:
    """
    将蛇形命名转换为驼峰命名
    
    Args:
        snake_str: 蛇形命名字符串（如 two_sum）
        
    Returns:
        驼峰命名字符串（如 twoSum）
        
    Example:
        >>> _to_camel_case("two_sum")
        'twoSum'
        >>> _to_camel_case("add_two_numbers")
        'addTwoNumbers'
    """
    components = snake_str.split('_')
    # 第一个单词小写，后续单词首字母大写
    return components[0] + ''.join(x.capitalize() for x in components[1:])


# 提供一个装饰器版本，更简洁
def solution_class(func: Callable) -> type:
    """
    装饰器版本：将函数装饰为Solution类
    
    Usage:
        @solution_class
        def two_sum(nums, target):
            return [0, 1]
        
        # 使用
        s = two_sum.Solution()  # 注意：函数名变成了类
        s.twoSum([2, 7, 11, 15], 9)
    """
    return create_solution(func)

