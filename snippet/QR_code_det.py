from PIL import Image
import cv2
import numpy as np

# Reference https://github.com/WeChatCV/opencv_3rdparty

class QrcodeDetor:
    def __init__(self):
        self.detector = cv2.wechat_qrcode_WeChatQRCode(
        "wechat_qrcodedet/detect.prototxt", "wechat_qrcodedet/detect.caffemodel", 
        "wechat_qrcodedet/sr.prototxt", "wechat_qrcodedet/sr.caffemodel")

    def __call__(self, image):
        # image 为 Image
        res, points = self.detector.detectAndDecode(np.array(image))
       
        QRcode = []
        # 如果检测到任何二维码
        if points is not None:
            for point in points:
                x_min = round(np.min(point[:, 0]))
                x_max = round(np.max(point[:, 0]))
                y_min = round(np.min(point[:, 1]))
                y_max = round(np.max(point[:, 1]))
                QRcode.append([x_min, y_min, x_max, y_max])

        return QRcode


if __name__ == "__main__":
    qrcode = QrcodeDetor()
    print(qrcode(Image.open("test.jpg")))