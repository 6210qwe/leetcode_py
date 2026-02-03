# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 146
标题: LRU Cache
难度: medium
链接: https://leetcode.cn/problems/lru-cache/
题目类型: 设计、哈希表、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
146. LRU 缓存 - 请你设计并实现一个满足 LRU (最近最少使用) 缓存 [https://baike.baidu.com/item/LRU] 约束的数据结构。 实现 LRUCache 类： * LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 * void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 示例： 输入 ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] 输出 [null, null, null, 1, null, -1, null, -1, 3, 4] 解释 LRUCache lRUCache = new LRUCache(2); lRUCache.put(1, 1); // 缓存是 {1=1} lRUCache.put(2, 2); // 缓存是 {1=1, 2=2} lRUCache.get(1); // 返回 1 lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3} lRUCache.get(2); // 返回 -1 (未找到) lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3} lRUCache.get(1); // 返回 -1 (未找到) lRUCache.get(3); // 返回 3 lRUCache.get(4); // 返回 4 提示： * 1 <= capacity <= 3000 * 0 <= key <= 10000 * 0 <= value <= 105 * 最多调用 2 * 105 次 get 和 put
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表+双向链表实现LRU缓存

算法步骤:
1. 定义双向链表节点
2. 使用哈希表存储key到节点的映射
3. get操作：如果存在，移动到头部
4. put操作：如果存在更新值并移动，否则插入新节点，如果超过容量删除尾部

关键点:
- 双向链表支持O(1)删除
- 时间复杂度O(1)，空间复杂度O(capacity)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - get和put操作都是O(1)
空间复杂度: O(capacity) - 存储capacity个节点
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Optional
from leetcode_solutions.utils.solution import create_solution


class LRUNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional['LRUNode'] = None
        self.next: Optional['LRUNode'] = None


class LRUCache:
    """
    LRU缓存实现类
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, LRUNode] = {}
        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: LRUNode):
        """在头部添加节点"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: LRUNode):
        """删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node: LRUNode):
        """移动节点到头部"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self) -> LRUNode:
        """删除尾部节点"""
        last = self.tail.prev
        self._remove_node(last)
        return last
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)
        return node.value
    
    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            new_node = LRUNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)


def lru_cache(capacity: int) -> LRUCache:
    """
    函数式接口 - 创建LRU缓存
    
    实现思路:
    使用哈希表+双向链表实现LRU缓存。
    
    Args:
        capacity: 缓存容量
        
    Returns:
        LRU缓存实例
        
    Example:
        >>> cache = lru_cache(2)
        >>> cache.put(1, 1)
        >>> cache.put(2, 2)
        >>> cache.get(1)
        1
    """
    return LRUCache(capacity)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(lru_cache)
