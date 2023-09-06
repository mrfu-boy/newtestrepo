import os
import shutil
import cv2

filePath_1 = 'F:/Target/source/S'
targetpath_1 = 'F:/Target/target/S'


def bmp2jpg1(source,target):
    fileState_1 = os.listdir(filePath_1)
    for i in fileState_1:
        filePath_2 = filePath_1 + '/' + i
        targetpath_2 = targetpath_1 + '/' + i
        fileState_2 = os.listdir(filePath_2)
        for j in fileState_2:
            filePath_3 = filePath_2 + '/' + j
            new_path = targetpath_2 + '/' + j

            # 读取
            img = cv2.imread(filePath_3, -1)

            new_path = new_path.replace('.bmp', '.jpg')

            cv2.imwrite(new_path, img)
            print(filePath_3, ' 转换成功 ', new_path)

if __name__ == '__main__':
    bmp2jpg1(filePath_1,targetpath_1)
    # fileState_1 = os.listdir(filePath_1)
    # disadvantage = 0
    # for i in fileState_1:
    #     filePath_2 = filePath_1 + '/' + i
    #     targetpath_2 = targetpath_1 + '/' + i
    #     fileState_2 = os.listdir(filePath_2)
    #     for j in fileState_2:
    #         filePath_3 = filePath_2 + '/' + j
    #         targetpath_3 = targetpath_2 + '/' + j
    #         fileState_3 = os.listdir(filePath_3)
    #         for k in fileState_3:
    #             filePath_4 = filePath_3 + '/' + k
    #
    #             #读取
    #             img = cv2.imread(filePath_4,-1)
    #             new_path = targetpath_3 + '/' + k
    #             new_path = new_path.replace('.bmp','.jpg')
    #
    #             cv2.imwrite(new_path,img)
    #             print(filePath_4,' 转换成功 ',new_path)
    #




