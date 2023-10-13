import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image

# 加载预训练的 InceptionV3 模型
model = InceptionV3(weights='imagenet')

# 加载要识别的图像
img_path = 'fyp.jpg'  # 替换为你的图像文件路径
img = image.load_img(img_path, target_size=(299, 299))

# 将图像转换为 numpy 数组，并增加一个维度
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# 预处理图像以符合模型的输入要求
x = preprocess_input(x)

# 使用模型进行图像分类
predictions = model.predict(x)

# 解码预测结果
labels = decode_predictions(predictions)

# 打印识别结果
for label in labels[0]:
    print(f"{label[1]}: {label[2]:.2f}%")

# 自动标注示例：选择置信度最高的类别作为标注
top_prediction = labels[0][0]
annotation = f"这是 {top_prediction[1]}, 置信度: {top_prediction[2]:.2f}%"

# 在图像上添加自动标注
from PIL import Image, ImageDraw, ImageFont

# 打开图像文件
image = Image.open(img_path)

# 创建 ImageDraw 对象，以便在图像上绘制文本
draw = ImageDraw.Draw(image)

# 指定字体和文本颜色
font = ImageFont.truetype("simsun.ttc", 16)  # 使用合适的字体文件路径
text_color = (255, 255, 255)

# 获取文本的大小
# text_width, text_height = draw.textsize(annotation, font)

# draw.textbbox((0, 0), annotation, font) 方法返回一个四元组 (x0, y0, x1, y1)，表示绘制文本的边界框。其中 (x0, y0) 是左上角坐标，(x1, y1) 是右下角坐标。
text_bbox = draw.textbbox((0, 0), annotation, font)

# 指定文本的位置（居中）
image_width, image_height = image.size
x = (image_width - (text_bbox[2] - text_bbox[0])) // 2
y = image_height - (text_bbox[3] - text_bbox[1]) - 20  # 文本距离底部的距离

# 在图像上添加自动标注
draw.text((x, y), annotation, fill=text_color, font=font)

# 保存标注后的图像
image.save("annotated_image.jpg")

# 显示标注后的图像（可选）
image.show()
