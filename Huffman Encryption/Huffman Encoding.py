from heapq import heapify, heappop
import os


class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None


class Huffman:
    def __init__(self, text):
        self.text = text

    def frequency_count(self, text_from_input):
        dict = {}

        for x in text_from_input:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1

        return dict

    def traverse(self, node, target, total=""):
        if node is not None:
            if node.elem[1] == target:
                return total

            left = self.traverse(node.left, target, total+"0")
            if left:
                return left

            right = self.traverse(node.right, target, total+"1")
            if right:
                return right

    def min_obj(self, obj):
        array = []
        for x in range(len(obj)):
            array.append((obj[x].elem, x))

        heapify(array)
        vertex = heappop(array)
        min = obj.pop(vertex[1])

        return min, obj


    def huffman_tree(self):
        frequency_list = []

        for x, y in self.frequency_dict.items():
            frequency_list.append((y, x))
        nodes = []

        while len(frequency_list) != 1:
            node = []
            for z in range(2):
                heapify(frequency_list)
                vertex = heappop(frequency_list)
                if vertex[1] != "":
                    node.append(BTNode(vertex))
                else:
                    vertex, nodes = self.min_obj(nodes)
                    node.append(vertex)

            total_sum = node[0].elem[0] + node[1].elem[0]
            new = (total_sum, "")
            frequency_list.append(new)
            new_node = BTNode(new)
            new_node.left = node[0]
            new_node.right = node[1]
            nodes.append(new_node)

        return nodes[-1]

    def padding(self, huffman_code):
        padded_value = 8 - len(huffman_code) % 8

        for i in range(padded_value):
            huffman_code += "0"

        padded_info = "{0:08b}".format(padded_value)
        padded_text = padded_info + huffman_code

        return padded_text

    def byte_array_creation(self, padded_text):
        array = []

        for i in range(0, len(padded_text), 8):
            byte = padded_text[i:i + 8]
            array.append(int(byte, 2))

        final_byte = bytes(array)
        return final_byte

    def depadding(self, padded_text):
        array = []

        for i in range(0, len(padded_text), 8):
            array.append(padded_text[i:i + 8])

        padded_value = int(array.pop(0), 2)

        bit_string = ""
        for x in array:
            bit_string += f"{x}"

        final_bit = bit_string[:-padded_value]

        return final_bit

    def decrypt(self, node, target, total=""):
        if node is not None:
            if node.elem[1] == target:
                return total

            left = self.decrypt(node.left, target, total+"0")
            if left:
                return left

            right = self.decrypt(node.right, target, total+"1")
            if right:
                return right

    def encoding(self):
        print("File Compression Started....")
        print("..........")
        print(".....")
        filename, file_extension = os.path.splitext(self.text)
        output_path = filename + ".bin"
        with open(self.text, "r+") as r, open(output_path, "wb") as w:
            text_from_input = r.read()
            text_from_input = text_from_input.rstrip()

            self.frequency_dict = self.frequency_count(text_from_input)
            self.node = self.huffman_tree()

            for z in self.frequency_dict:
                self.frequency_dict[z] = self.traverse(self.node, z)

            huffman_code = ""
            for i in text_from_input:
                huffman_code += f"{self.frequency_dict[i]}"

            padded_text = self.padding(huffman_code)
            byte_Array = self.byte_array_creation(padded_text)

            print("File Compression Successful")
            w.write(byte_Array)
            w.close()

    def decoding(self):
        print("File Decompression Started....")
        print("..........")
        print(".....")
        filename, file_extension = os.path.splitext(self.text)
        file_input = filename + ".bin"
        output_path = filename + "_decrypted" + ".txt"
        with open(file_input, "rb") as r, open(output_path, "w") as w:
            bit_string = ""
            byte = r.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, "0")
                bit_string += bits
                byte = r.read(1)

            original_bits = self.depadding(bit_string)

            original_text = ""
            stored = ""
            counter = 0
            while len(original_bits) != 0:
                stored += original_bits[counter]
                for x, y in self.frequency_dict.items():
                    if stored == y:
                        original_text += x
                        original_bits = original_bits[len(stored):]
                        counter -= len(stored)
                        stored = ""
                counter += 1

            print("File Decompression Successful")
            w.write(original_text)
            w.close()


path = input("Write the name of your file: ")
print("Do You Want To Start The File Compression")
huffman_obj = Huffman(path)
flag = True
while flag:
    process = input("Yes/No: ")
    if process == "Yes":
        huffman_obj.encoding()
        print("Do You Want To Decompress")
        next_step = input("Yes/No: ")
        if next_step == "Yes":
            huffman_obj.decoding()
            print("Thank You For Your Time")
            break
        else:
            print("Thank You For Your Time")
            break
    elif process == "No":
        print("Thank You For Your Time")
        break
    else:
        print("Did Not Choose Any Valid Process Try Again")