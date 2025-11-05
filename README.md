
# Roop-Cam batch 批量换脸项目(仅供学习)

> **一句话总结**：  
> 使用 **Roop-Cam + Python 脚本** 实现 **一键批量换脸**，支持文件夹内多个视频 → 输出到指定文件夹，**GPU 加速（GTX 1660 Ti）**，**永不弹 GUI**。

---

## 项目结构

```
C:\roop-cam\
│
├── roop\                   # Roop-Cam 核心代码
├── models\
│   └── inswapper_128.onnx  # 换脸模型（必须）
├── venv\                   # 虚拟环境
├── run.py                  # 主程序（命令行入口）
├── batch_headless.py       # 本项目核心：批量处理脚本
└── README.md               # 本文档
```

---

## 环境要求

| 组件 | 版本 |
|------|------|
| Python | 3.10 |
| PyTorch | `2.0.1+cu118`（支持 CUDA 11.8） |
| GPU | NVIDIA GTX 1660 Ti（6GB） |
| 显存 | ≥4GB 推荐 |
| 磁盘 | ≥10GB 空闲 |

---

## 安装步骤（已完成）

```cmd
# 1. 克隆项目（你已完成）
git clone https://github.com/eninem123/roop-cam-batch C:\roop-cam
cd C:\roop-cam

# 2. 创建虚拟环境
python -m venv venv
venv\Scripts\activate

# 3. 安装 PyTorch + CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 4. 安装其他依赖
pip install onnxruntime-gpu insightface opencv-python tqdm

# 5. 下载模型
curl -L -o models\inswapper_128.onnx https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx
```

---

## 使用方法：批量换脸

### 1. 准备文件

```
D:\Lib\
├── source_face.jpg         # 源人脸（清晰正面照）
├── input_videos\           # 输入文件夹（放多个视频）
│   ├── muban.mp4
│   └── muban2.mp4
└── output_videos\          # 输出文件夹（自动创建）
```

### 2. 修改 `batch_headless.py` 配置

```python
SOURCE_FACE = r"D:\Lib\source_face.jpg"
INPUT_DIR   = r"D:\Lib\input_videos"
OUTPUT_DIR  = r"D:\Lib\output_videos"
```

### 3. 一键运行

```cmd
cd C:\roop-cam
venv\Scripts\activate
python batch_headless.py
```

---

## 输出效果

```
找到 2 个视频，开始处理...

[1/2] 正在处理: muban.mp4
[████████████████████████████████] 100%
成功 → D:\Lib\output_videos\muban_swapped.mp4

[2/2] 正在处理: muban2.mp4
[████████████████████████████████] 100%
成功 → D:\Lib\output_videos\muban2_swapped.mp4

全部完成！输出目录：D:\Lib\output_videos
```

---

## 常见问题

| 问题                           | 解决方案                                                  |
| ------------------------------ | --------------------------------------------------------- |
| `ModuleNotFoundError: torch`   | 确保用 `venv\Scripts\python.exe` 运行                     |
| `inswapper_128.onnx not found` | 手动下载放 `models\` 目录                                 |
| 显存不足                       | 在 `cmd` 中加 `"--max-memory", "4"`                       |
| 视频无声                       | 脚本已加 `--keep-audio`                                   |
| 换脸模糊                       | 源脸需清晰正面，建议加 `--face-restoration`（需额外模型） |

---

## 高级参数（可加到 `cmd` 列表）

```python
"--video-quality", "18",      # 画质（18=高，51=低）
"--max-memory", "4",          # 限制显存 4GB
"--many-faces",               # 多人脸都替换
```

---

## 卸载

```cmd
rmdir /s C:\roop-cam
```

---

## 免责声明

> 本项目仅用于 **学习与研究**，请遵守当地法律法规，**禁止用于非法用途**。
> 我想强调，我们的交换软件仅旨在用于负责任和合乎伦理的使用。我必须重申，在使用本软件时，用户对其行为负全责。
> 预期用途:该软件旨在帮助用户创建逼真且娱乐性的内容，如电影、视觉效果、虚拟现实体验以及其他创意应用。我鼓励用户在合法、道德考量和尊重他人隐私的范围内探索这些可能性。
> 伦理准则:用户在使用我们的软件时应遵守一套伦理准则。这些准则包括但不限于:
> 不创建或分享可能伤害、诽谤或骚扰个人的内容。在使用内容中涉及的个人形象之前，应获得他们的适当同意和许可。避免出于欺骗目的使用该技术，包括传播错误信息或怀有恶意意图。尊重并遵守适用的法律、法规和版权限制。
> 隐私与同意:用户有责任确保他们已获得相关个人的必要权限和同意，这些个人形象将被用于用户的创作中。我们强烈反对在没有明确同意的情况下创建内容，特别是如果内容涉及未经同意或私人性质的信息。尊重所有相关个人的隐私和尊严至关重要。
> 法律考虑:用户必须了解和遵守与该技术相关的所有相关的地方、区域和国际法律。这包括与隐私、诽谤、知识产权相关的法律以及其他相关立法。如果用户对他们的创作所涉及的法律问题有任何疑虑，应咨询法律专业人士。
> 责任和赔偿责任:我们作为深度伪造软件的制作方和提供者，不能对使用我们的软件所导致的行为或后果承担任何责任用户需自行承担任何不当使用、意外效果或与其创建的内容相关的滥用行为所带来的全部责任和后果。
> 通过使用此软件，用户确认他们已经阅读、理解并同意遵守上述指南和免责声明。我们强烈建议用户以谨慎、正直的态度对待这项技术，并尊重他人的福祉和权利。
> 请记住，技术应用于赋能与激励，而非伤害或欺骗。让我们共同努力，以道德和负责任的方式使用深度伪造技术，为社会带来积极改善

---

**Author**: https://github.com/eninem123 老谭（2025）  

