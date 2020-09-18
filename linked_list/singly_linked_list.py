"""
description: 单向链表的实现
author: Eileen
data: 2020/9/18
"""

class Node:
    def __init__(self, index, value=None):
        self.value = value
        self.index = index
        self.next_node = None


class LinkList:
    def __init__(self):
        self.length = 0
        self.next_node = None


    def add(self, value):
        """
        向链表后插入元素
        :param value: 元素值
        :return:None
        """
        node = self.next_node
        if node:  # "存在下一节点"
            last_node = node
            while node:
                node = node.next_node
                if node:
                    last_node = node
                else:
                    break
            last_node.next_node = Node(last_node.index+1, value)
        else:  # "不存在下一节点"
            next_node = Node(1, value)
            self.next_node = next_node
        self.length += 1

    def get(self, index):
        """
        获取指定索引的节点值
        :param index:索引
        :return:value
        """
        current_node = self.next_node
        while current_node:
            if getattr(current_node, "index") == index:
                return current_node.value
            else:
                current_node = current_node.next_node


    def set(self, index, value):
        """
        给指定索引的节点设置值
        :param index:索引
        :param value:设置的值
        :return:None
        """
        current_node = self.next_node
        while current_node:
            if getattr(current_node, "index") == index:
                current_node.value = value
                break
            else:
                current_node = current_node.next_node

    def size(self):
        """
        返回链表长度
        :return: length
        """
        return self.length

    def delete(self, value=None, index=None):
        """
        删除元素, 可根据索引或者指定值
        :param index:索引
        :param value:元素值
        :return:None
        """
        if bool(value) ^ bool(index):
            if self.next_node:
                last_node = self.next_node
                current_node = self.next_node
                if getattr(current_node, "value") == value or getattr(current_node, "index") == index:  # 要删除第一个
                    self.next_node = self.next_node.next_node
                else:
                    last_node = self.next_node
                    current_node = self.next_node
                while current_node:
                    if getattr(current_node, "value") == value or getattr(current_node, "index") == index:
                        last_node.next_node = current_node.next_node if current_node else None
                        self.length -= 1
                        # 更新索引
                        self._update_index(last_node)
                        break
                    else:
                        last_node = current_node
                        current_node = current_node.next_node

    def _update_index(self, node):
        """
        删除元素后更新索引
        :param node:删除节点的上一个节点
        :return:None
        """
        index = node.index
        while node:
            node = node.next_node
            if node:
                index += 1
                node.index = index
            else:
                break

link_list = LinkList()
link_list.add(5)
link_list.add(6)
link_list.add(7)
link_list.add(8)
link_list.add(9)
link_list.add(10)
link_list.delete(value=6)
link_list.delete(index=3)
print(link_list.size())
print(link_list.get(4))
link_list.set(4, 11)
print(link_list.get(4))
print(help(LinkList))

