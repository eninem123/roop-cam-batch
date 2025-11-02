# 文件：C:\roop-cam\batch_headless.py
import os
import glob
import subprocess
from pathlib import Path

# ================== 配置区 ===================
SOURCE_FACE = r"D:\Lib\source_face.jpg"
INPUT_DIR   = r"D:\Lib\input_videos"
OUTPUT_DIR  = r"D:\Lib\output_videos"
# ============================================

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

video_files = []
for ext in ('*.mp4', '*.avi', '*.mov', '*.mkv', '*.webm'):
    video_files.extend(glob.glob(os.path.join(INPUT_DIR, ext)))
    video_files.extend(glob.glob(os.path.join(INPUT_DIR, ext.upper())))

print(f"找到 {len(video_files)} 个视频，开始处理...\n")

# 强制使用 venv 的 python
PYTHON_VENV = r"C:\roop-cam\venv\Scripts\python.exe"

for idx, video in enumerate(video_files, 1):
    name = os.path.basename(video)
    output = os.path.join(OUTPUT_DIR, Path(name).stem + "_swapped.mp4")
    
    # 只用你版本支持的参数
    cmd = [
        PYTHON_VENV, "run.py",
        "--target", video,
        "--source", SOURCE_FACE,
        "--output", output,
        "--execution-provider", "cuda",
        "--keep-fps",
        "--keep-audio"
        # 去掉 --headless 和 --skip-download
    ]
    
    print(f"[{idx}/{len(video_files)}] 正在处理: {name}")
    
    result = subprocess.run(cmd, cwd=r"C:\roop-cam", capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"成功 → {output}\n")
    else:
        print(f"失败 → {name}")
        print("错误：")
        print(result.stderr.strip() if result.stderr else "无输出")
        print("-" * 60 + "\n")

print(f"全部完成！输出目录：{OUTPUT_DIR}")