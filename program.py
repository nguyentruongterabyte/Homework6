"""
    MSSV     : N20DCCN083
    Họ và tên: Nguyễn Thái Trưởng
"""

import numpy as np
import matplotlib.pyplot as plt

def read_bin(fn, xsize):
    fid = open(fn, 'rb')
    if fid == -1:
        raise Exception(f'Could not open {fn}')
    x = np.fromfile(fid, dtype='uint8', count=xsize * xsize)
    x = x.reshape((xsize, xsize))
    fid.close()
    return x

def show_byte_image(x, fig_num):
    plt.subplot(2, 4, fig_num)
    plt.imshow(x, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')


def main():
    size = 256  # number of rows/cols in the image
    wsize = 3  # for 3x3 filter windows
    wsizeo2 = wsize // 2  # window half-size ( =1 for 3x3)

    # camera99.bin
    print("Doing camera99.bin...")
    plt.figure(figsize=(14, 6))
    # Read and display the image
    x = read_bin('camera99.bin', size)
    show_byte_image(x, 1)
    plt.title('camera99.bin', fontsize=12)
    plt.savefig('camera99.png', bbox_inches='tight')
    # Apply median, erode, and dilate
    yMF = np.zeros_like(x)
    yE = np.zeros_like(x)
    yD = np.zeros_like(x)
    yO = np.zeros_like(x)
    yC = np.zeros_like(x)

    for row in range(wsizeo2, size - wsizeo2):
        for col in range(wsizeo2, size - wsizeo2):
            W = x[row - wsizeo2:row + wsizeo2 + 1, col - wsizeo2:col + wsizeo2 + 1]
            yMF[row, col] = np.median(W)
            yE[row, col] = np.min(W)
            yD[row, col] = np.max(W)

    # Apply dilate to yE and erode to yD to finish the open and close
    for row in range(wsizeo2 + 1, size - wsizeo2 - 1):
        for col in range(wsizeo2 + 1, size - wsizeo2 - 1):
            W = yE[row - wsizeo2:row + wsizeo2 + 1, col - wsizeo2:col + wsizeo2 + 1]
            yO[row, col] = np.max(W)
            W = yD[row - wsizeo2:row + wsizeo2 + 1, col - wsizeo2:col + wsizeo2 + 1]
            yC[row, col] = np.min(W)

    # Display the output images
    show_byte_image(yMF, 2)
    plt.title('3x3 Median Filter (99)', fontsize=12)
    plt.savefig('camera99MF.png', )

    show_byte_image(yO, 3)
    plt.title('3x3 Morphological Opening (99)', fontsize=12)
    plt.savefig('camera99O.png', bbox_inches='tight')

    show_byte_image(yC, 4)
    plt.title('3x3 Morphological Closing (99)', fontsize=12)
    plt.savefig('camera99C.png', bbox_inches='tight')

    # Reset variables for the next image
    size = 256
    W = np.zeros((wsize, wsize), dtype=np.uint8)
    yMF = np.zeros((size, size), dtype=np.uint8)
    yE = np.zeros((size, size), dtype=np.uint8)
    yD = np.zeros((size, size), dtype=np.uint8)
    yO = np.zeros((size, size), dtype=np.uint8)
    yC = np.zeros((size, size), dtype=np.uint8)

    # Read and display the image
    x = read_bin('camera9.bin', size)
    show_byte_image(x, 5)
    plt.title('camera9.bin', fontsize=12)
    plt.savefig('camera9.png', bbox_inches='tight')

    # Apply median, erode, and dilate
    for row in range(wsizeo2, size - wsizeo2):
        for col in range(wsizeo2, size - wsizeo2):
            W = x[row - wsizeo2:row + wsizeo2 + 1, col - wsizeo2:col + wsizeo2 + 1]
            yMF[row, col] = np.median(W)
            yE[row, col] = np.min(W)
            yD[row, col] = np.max(W)

    # Apply dilate to yE and erode to yD to finish the open and close
    for row in range(wsizeo2 + 1, size - wsizeo2 - 1):
        for col in range(wsizeo2 + 1, size - wsizeo2 - 1):
            W = yE[row - wsizeo2:row + wsizeo2 + 1, col - wsizeo2:col + wsizeo2 + 1]
            yO[row, col] = np.max(W)
            W = yD[row - wsizeo2:row + wsizeo2 + 1, col - wsizeo2:col + wsizeo2 + 1]
            yC[row, col] = np.min(W)

    # Display the output images
    show_byte_image(yMF, 6)
    plt.title('3x3 Median Filter (9)', fontsize=12)
    plt.savefig('camera9MF.png', bbox_inches='tight')

    show_byte_image(yO, 7)
    plt.title('3x3 Morphological Opening (9)', fontsize=12)
    plt.savefig('camera9O.png', bbox_inches='tight')

    show_byte_image(yC, 8)
    plt.title('3x3 Morphological Closing (9)', fontsize=12)
    plt.savefig('camera9C.png', bbox_inches='tight')
    plt.show()
    print("\n")

if __name__ == "__main__":
    main()
