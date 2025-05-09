# 📄 ID & Bank Card PDF Generator

使用 Python 脚本将身份证正反面或银行卡正面图像，**以真实尺寸**（85.6mm × 54mm）排版到 A4 页面，并输出 PDF，方便打印用于开户、办事等需求。

---

## 📁 文件说明

### ✅ `idcard_dual_side.py`

- 功能：将身份证正反面图像上下排列、居中对齐，排版成 A4 PDF。
- 输出：身份证两面以真实尺寸（85.6mm × 54mm）出现在 A4 页面中。
- 适用：开户、身份认证等需要身份证复印件的场景。

### ✅ `bankcard_single_center.py`

- 功能：将银行卡正面图像居中排版到 A4 页面。
- 输出：单张卡片以实际尺寸出现在页面中央。
- 适用：银行业务、资料提交等场景。

---

## 📦 使用依赖

确保安装以下 Python 库：

```bash
pip install Pillow reportlab
```
---

## 🚀 使用方式

将身份证或银行卡图像放入与脚本相同的目录，运行如下命令：
```
# 生成身份证双面 PDF
python idcard_dual_side.py

# 生成银行卡 PDF
python bankcard_single_center.py
```
输出的 PDF 文件默认保存在脚本目录下。

---

## 📌 注意事项

输出尺寸精确为卡片实际大小（标准：85.6mm × 54mm）
打印时请设置为「实际大小」（100% 缩放）避免图像被放大或缩小

---

## 🧑‍💻 作者

本项目由 Python 编写，欢迎改进建议和 PR！
