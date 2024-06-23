# Huffman Algorithm With Python

## How it works

### Encryption

#### Step-1
        After running the python file. Write the name of your file, such as for this project I used few 
        input files i.e. input1.txt. The encrypted .bin file and decrypted .txt file will be created 
        automatically. After you start the file compression it will enter the encoding() function.

#### Step-2
        Let us use input1.txt file as Example. This file contains the following text.
![Image of text](/Pics/text.png)

        We run a frequency_count() function to find the total frequency of each character in the text.
![Image of text](/Pics/text2.png)

#### Step-3
        Next we run the huffman_tree() function and make a binary huffman tree. Where the left node 
        contains smaller value and right node contains the larger value.
![Image of graph](/Pics/graph.png)

#### Step-4
        Next we run the traverse() function and set value of 0 to the left node and 1 to the right node.
![Image of graph](/Pics/graph2.png)

        So we get a new value for each of the character by the Huffman Tree
![Image of text](/Pics/text3.png)

        So we get the huffman code which is
![Image of text](/Pics/text4.png)

#### Step-5
        Now we need to pad the huffman code. So, We can divide the code into groups of 8 bits. If the 
        total number of bit in huffman code is not a perfectly divided by 8 we will not be able to 
        group the huffman code into groups of 8. So, we need to add a layer of padding at the end 
        which contains only 0s so that it will be perfectly divided by 8.

```python
    padded_value = 8 - len(huffman_code) % 8

    for i in range(padded_value):
        huffman_code += "0"

```

        We will also keep a record of how my extra 0s we put at the end of the huffman code and store 
        it in padded_info so that we can remove them to decrypt the code perfectly. We convert the 
        total number of 0s into binary and format it into 8 bit number. Then we add it in the beginning 
        of the huffman code.

```python
    padded_info = "{0:08b}".format(padded_value)
    padded_text = padded_info + huffman_code
```

#### Step-6
        Next we divide the padded huffman code into groups of 8 bit and convert it into binary array.

```python
    def byte_array_creation(self, padded_text):
        array = []

        for i in range(0, len(padded_text), 8):
            byte = padded_text[i:i + 8]
            array.append(int(byte, 2))

        final_byte = bytes(array)
        return final_byte
```
#### Step-7
        Finally, we write the binary array into the input1.bin file.


### Observations
        By applying the Huffman Encryption we can reduce the file size also keep the data secured.
![Image of siza](/Pics/size.png)


### Decryption

#### Step-1
        After you start the file decryption it will enter the decoding() function and start the process.

#### Step-2
        First we reconvert the binary array into padded huffman code.

```python
    bit_string = ""
    byte = r.read(1)
    while byte:
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, "0")
        bit_string += bits
        byte = r.read(1)
```

#### Step-3
        Next we run the depadding() function to start the depadding process. We group the whole padded 
        huffman code into groups of 8 bits and store it in array. We pop the first index of the array 
        and reconvert it into integer which contains the number of extra padding we added at the end 
        of the huffman code. Then we remove the extra 0s at the end.

#### Step-4
        Then we compare the huffman code with the value of each characters we got from the huffman tree 
        which is
![Image of text](/Pics/text3.png)
        
        Then we replace the huffman code with the text.
![Image of text](/Pics/text5.png)
