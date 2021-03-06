#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import hashlib as hasher
import datetime as date

"""
比特币的区域链的简单实现
"""

class Block:
    """
    散列块 = 块索引 + 时间戳 + 数据 + 前块hash的加密hash
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash =previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(
            (str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash)).encode("utf-8")
        )
        return sha.hexdigest()

# b = Block()
#起源块
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

#后续块
def next_block(last_block):
    this_index = last_block.index+1
    this_timestamp = date.datetime.now()
    this_data = "Vic faith block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

if __name__ == "__main__":

    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    num = 20#只添加20块
    for i in range(0, num):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print(block_to_add.index)
        print("Hash: {}\n".format(block_to_add.hash))