# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 460
标题: LFU Cache
难度: hard
链接: https://leetcode.cn/problems/lfu-cache/
题目类型: 设计、哈希表、链表、双向链表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
460. LFU 缓存 - 请你为 最不经常使用（LFU） [https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95]缓存算法设计并实现数据结构。 实现 LFUCache 类： * LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象 * int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。 * void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 示例： 输入： ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]] 输出： [null, null, null, 1, null, -1, 3, null, -1, 3, 4] 解释： // cnt(x) = 键 x 的使用计数 // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的） LFUCache lfu = new LFUCache(2); lfu.put(1, 1); // cache=[1,_], cnt(1)=1 lfu.put(2, 2); // cache=[2,1], cnt(2)=1, cnt(1)=1 lfu.get(1); // 返回 1 // cache=[1,2], cnt(2)=1, cnt(1)=2 lfu.put(3, 3); // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小 // cache=[3,1], cnt(3)=1, cnt(1)=2 lfu.get(2); // 返回 -1（未找到） lfu.get(3); // 返回 3 // cache=[3,1], cnt(3)=2, cnt(1)=2 lfu.put(4, 4); // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用 // cache=[4,3], cnt(4)=1, cnt(3)=2 lfu.get(1); // 返回 -1（未找到） lfu.get(3); // 返回 3 // cache=[3,4], cnt(4)=1, cnt(3)=3 lfu.get(4); // 返回 4 // cache=[3,4], cnt(4)=2, cnt(3)=3 提示： * 1 <= capacity <= 104 * 0 <= key <= 105 * 0 <= value <= 109 * 最多调用 2 * 105 次 get 和 put 方法
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表+双向链表实现LFU缓存

算法步骤:
1. 使用两个哈希表：key_to_node存储key到节点的映射，freq_to_dll存储频率到双向链表的映射
2. get操作：如果key存在，更新频率，返回value
3. put操作：如果key存在，更新value和频率；否则插入新节点，如果容量满则删除最少使用的节点

关键点:
- 使用双向链表维护相同频率的节点（LRU顺序）
- 使用哈希表实现O(1)访问
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

from typing import List, Optional
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class LFUNode:
    """LFU节点"""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoubleLinkedList:
    """双向链表"""
    def __init__(self):
        self.head = LFUNode(0, 0)
        self.tail = LFUNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_to_head(self, node: LFUNode):
        """添加到头部"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove_node(self, node: LFUNode):
        """删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_tail(self) -> Optional[LFUNode]:
        """删除尾部节点"""
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node


def lfu_cache(capacity: int):
    """
    函数式接口 - LFU缓存
    
    实现思路:
    使用哈希表+双向链表实现LFU缓存，支持O(1)的get和put操作。
    
    Args:
        capacity: 缓存容量
        
    Returns:
        LFUCache类
        
    Example:
        >>> cache = lfu_cache(2)
        >>> cache.put(1, 1)
        >>> cache.put(2, 2)
        >>> cache.get(1)
        1
    """
    class LFUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.key_to_node = {}
            self.freq_to_dll = defaultdict(DoubleLinkedList)
            self.min_freq = 0
        
        def get(self, key: int) -> int:
            if key not in self.key_to_node:
                return -1
            
            node = self.key_to_node[key]
            self._update_freq(node)
            return node.value
        
        def put(self, key: int, value: int):
            if self.capacity == 0:
                return
            
            if key in self.key_to_node:
                node = self.key_to_node[key]
                node.value = value
                self._update_freq(node)
            else:
                if len(self.key_to_node) >= self.capacity:
                    self._remove_lfu()
                
                node = LFUNode(key, value)
                self.key_to_node[key] = node
                self.freq_to_dll[1].add_to_head(node)
                self.min_freq = 1
        
        def _update_freq(self, node: LFUNode):
            """更新节点频率"""
            old_freq = node.freq
            self.freq_to_dll[old_freq].remove_node(node)
            
            if old_freq == self.min_freq and self.freq_to_dll[old_freq].size == 0:
                self.min_freq += 1
            
            node.freq += 1
            self.freq_to_dll[node.freq].add_to_head(node)
        
        def _remove_lfu(self):
            """删除最少使用的节点"""
            dll = self.freq_to_dll[self.min_freq]
            node = dll.remove_tail()
            if node:
                del self.key_to_node[node.key]
    
    return LFUCache(capacity)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(lfu_cache)
