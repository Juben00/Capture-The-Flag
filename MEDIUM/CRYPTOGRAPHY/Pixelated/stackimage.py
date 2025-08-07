import numpy as np
from PIL import Image

img1 = Image.open("scrambled1.png")
img2 = Image.open("scrambled2.png")

# Convert to larger type BEFORE multiplication
im1input = np.array(img1, dtype=np.uint16) * 1079
im2input = np.array(img2, dtype=np.uint16) * 1079

# XOR operation, then cast back to uint8
bitwise_xor = np.bitwise_xor(im1input, im2input).astype(np.uint8)

# Save result
Image.fromarray(bitwise_xor).save("flag.png")