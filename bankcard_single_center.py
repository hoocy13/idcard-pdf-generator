from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 输入图像路径
card_img_path = '3.jpg'
output_pdf_path = '银行卡3.pdf'

# 银行卡/身份证标准尺寸：85.6mm x 54mm
mm_to_pt = 2.83465  # mm -> points
card_width_pt = 85.6 * mm_to_pt
card_height_pt = 54 * mm_to_pt

# A4 纸尺寸（单位：points）
a4_width, a4_height = A4

# 创建 PDF 画布
c = canvas.Canvas(output_pdf_path, pagesize=A4)

# 计算居中位置
x_pos = (a4_width - card_width_pt) / 2
y_pos = (a4_height - card_height_pt) / 2

# 添加银行卡图像到画布
c.drawImage(card_img_path, x_pos, y_pos, width=card_width_pt, height=card_height_pt)

# 保存 PDF
c.save()
print("✅ 已生成居中银行卡 PDF：", output_pdf_path)
