
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
git clone https://github.com/s0md3v/roop.git C:\roop-cam
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

## 声明

> 本项目仅用于 **学习与研究**，请遵守当地法律法规，**禁止用于非法用途**。

---

**Author**: 你（2025）  
**GPU**: GTX 1660 Ti + CUDA 11.8  
**状态**: 批量换脸 100% 成功
```

---

**保存为 `C:\roop-cam\README.md`**，打开即看！  
**你的项目已完整文档化**，可分享、可复现、可扩展！
```