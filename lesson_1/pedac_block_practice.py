#Understand the problem
"""
input: integer
output: integer (return a different object)

questions:
-How should I deal with input that isn't an integer?
-Can I assume all inputs are integers?
-what does the structure look like?
-How many upper blocks can a lower level block support if more than 1?
- Is a lower layer valid if it has more blocks than it needs?
- Will there always be left-over blocks?

explicit rules:
-cubes have 6 sides!
-The top layer is a single cube!
-structure built in layers
-A block in an upper layer must be supported by four blocks in a lower layer.
-A block in a lower layer can support more than one block in an upper layer.
-You cannot leave gaps between blocks.
-leftover blocks after building the tallest structure possible.

implicit rules:
-input must be an integer
- Layer number correlates with blocks in a layer:
- The number of blocks in a layer is layer number * layer number.
"""
#Examples and Test Cases
# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

#Data Structure
# - Perhaps we can use a nested list to represent the structure?
#     - Each sublist could represent a layer.
# [
#     ['x'],
#     ['x', 'x', 'x', 'x'],
#     ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#       ...
# ]

#Algorithm
"""
-Start with blocks remaining being the integer from the user
-build one layer at a time
-if there is enough blocks to build the next layer, subtract the amount of blocks
in that layer from the total blocks remaining.
-repeat those two steps over and over
-return left over blocks from building structure

1. Start with:
     - The "number of blocks remaining" is equal to the input.
     - The "current layer number" is layer 0.

2. Calculate the "current layer number" for the next layer by
   adding 1 to the "current layer number".

3. Using the new "current layer number", calculate the "number of
   blocks required in this layer" by multiplying the "current
   layer number" by itself.

4. Determine whether the "number of blocks remaining" is greater
   than or equal to the "number of blocks required in this layer".
     - If there are enough blocks:
         - Subtract the "number of blocks required in this layer"
           from the "number of blocks remaining".
         - Go to step 2.
     - If there aren't enough blocks:
         - Return the "number of blocks remaining".
"""
def calculate_leftover_blocks(n):
    current_layer_number = 0
    blocks_remaining = n
    blocks_required_for_layer = (current_layer_number + 1) ** 2

    while blocks_remaining >= blocks_required_for_layer:
        blocks_remaining -= blocks_required_for_layer
        current_layer_number += 1
        blocks_required_for_layer = (current_layer_number + 1) ** 2
    return blocks_remaining

print(calculate_leftover_blocks(0) == 0)
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True