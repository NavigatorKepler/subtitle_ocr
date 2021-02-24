import cv2
import string
import random
import os

from tqdm import tqdm


def divide(video_name=None):
    assert isinstance(video_name, str), '请传入有效的视频文件路径'
    imagepath = ''.join(random.sample(string.ascii_letters + string.digits, 12))
    try:
        os.mkdir('__tmp'+imagepath)
    except:
        raise BaseException('文件夹已存在, 请重试')

    cap = cv2.VideoCapture(video_name)
    fps = float(cap.get(cv2.CAP_PROP_FPS))
    tqdm.write(str(fps))
    totalframe = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    pbar = tqdm(range(totalframe), ascii=True, ncols=90)

    while(cap.isOpened()):
        ret, frame = cap.read()
        timestamp = '%012d' % int(cap.get(cv2.CAP_PROP_POS_MSEC))
        image_name = '__tmp' + imagepath + '/' + timestamp + '.jpg'
        pbar.set_description(timestamp)

        if ret == True:
            cv2.imwrite(image_name, frame)
        else:
            break
        pbar.update(1)

    pbar.close()
    cap.release()

    return imagepath

# devide('第43集 勇闯黑龙堡.mp4')
