import string
import random

from cnstd import CnStd
from cnocr import CnOcr

from divide import divide

__std = CnStd(model_name='resnet50_v1b',context='cpu')
__ocr = CnOcr(model_name='densenet-lite-gru',context='cpu')

def OCRProcess(image_name=None):
    assert isinstance(image_name, str), '请输入有效的图片路径'
    box_info_list = __std.detect(image_name)

    for box_info in box_info_list:
        cropped_img = box_info['cropped_img']
        ocr_res = __ocr.ocr_for_single_line(cropped_img)
        print(ocr_res)
        # print('ocr result: %s' % ''.join(ocr_res))
    pass

OCRProcess('000000001960.jpg')
OCRProcess('000000002000.jpg')
OCRProcess('000000002040.jpg')
OCRProcess('000000002080.jpg')
OCRProcess('000000002120.jpg')