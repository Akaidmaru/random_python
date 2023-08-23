"""Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.


    *
   * *
  * * *
Height = 3 , Blocks = 6

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately."""

blocks = int(input("Enter the number of blocks: "))
height = 0

while blocks > 0:
    height += 1
    blocks -= height

print(f"The height of the pyramid: {height}")