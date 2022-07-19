import cv2

def scaling_images_equally(image, size, interpolation_algorithm = cv2.INTER_AREA):
    """等比例缩放图片

    Args:
        image (_type_): 图片
        size (_type_): 最长边大小
        interpolation_algorithm (_type_, optional): 
            如果要缩小图像，通常推荐使用# cv2.INTER_AREA 插值效果最好，
            而要放大图像，通常使用 cv2.INTER_CUBIC (速度较慢，但效果最好)，
            或者使用 cv2.INTER_LINEAR (速度较快，效果还可以)。
            至于最近邻插值 cv2.INTER_NEAREST ，一般不推荐使用

    Returns:
        _type_: new image
    """
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    width_new = size
    height_new = size
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)), interpolation_algorithm)
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new), interpolation_algorithm)
    return img_new