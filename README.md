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
