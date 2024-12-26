# 2.1. Кодирование строки по алгоритму Хаффмана
from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(string):
    freq = Counter(string)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(tree, prefix="", codes={}):
    if tree.char is not None:
        codes[tree.char] = prefix
    else:
        generate_huffman_codes(tree.left, prefix + "0", codes)
        generate_huffman_codes(tree.right, prefix + "1", codes)
    return codes

def huffman_encode(string):
    tree = build_huffman_tree(string)

    codes = generate_huffman_codes(tree)

    encoded_text = "".join(codes[char] for char in string)

    print(len(codes), len(encoded_text))
    for char, code in codes.items():
        print(f"'{char}': {code}")
    print(encoded_text)

string = "Errare humanum est."
huffman_encode(string)
