from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 输入图像路径
front_img_path = '2-1.jpg'
back_img_path = '2-2.jpg'
output_pdf_path = '2.pdf'

# 身份证尺寸（mm 转换为 points，1 mm ≈ 2.83465 points）
id_width_mm = 85.6
id_height_mm = 54
id_width_pt = id_width_mm * 2.83465
id_height_pt = id_height_mm * 2.83465

# A4 尺寸
a4_width, a4_height = A4

# 创建 PDF 画布
c = canvas.Canvas(output_pdf_path, pagesize=A4)

# 计算摆放位置（居中、上下排列）
x_pos = (a4_width - id_width_pt) / 2
y_pos_top = (a4_height + id_height_pt) / 2 + 30  # 上方多一些距离
y_pos_bottom = (a4_height - id_height_pt) / 2 - 30

# 添加正面
c.drawImage(front_img_path, x_pos, y_pos_top, width=id_width_pt, height=id_height_pt)

# 添加反面
c.drawImage(back_img_path, x_pos, y_pos_bottom, width=id_width_pt, height=id_height_pt)

# 保存 PDF
c.save()
print("✅ 已生成 PDF 文件：", output_pdf_path)
