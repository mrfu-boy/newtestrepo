import cv2

if __name__ == '__main__':
    filePath_1 = 'F:/Target/source/B/ng/MER-131-210U3C(KE0210070522)_2023-08-04_15_16_06_790-359.bmp'
    targetpath_1 = 'F:/Target/target/MER-131-210U3C(KE0210070522)_2023-08-04_15_16_06_790-359.jpg'

    img = cv2.imread(filePath_1,-1)
    cv2.imwrite(targetpath_1,img)

