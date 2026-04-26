# Vid2GIF
Vid2GIF is a lightweight Python tool that converts any video file into a high-quality GIF using FFmpeg. It supports MP4, AVI, MKV, MOV, and more, making it an easy solution for creating shareable GIFs from movies, clips, or screen recordings.
<img width="1008" height="448" alt="image" src="https://github.com/user-attachments/assets/4ea07bd0-4142-49c2-b123-93a229e346fb" />
 example gif : baktha prahalada
![output_23](https://github.com/user-attachments/assets/d0767005-7b61-4536-a689-6591306f33ed)
# 🎬 Vid2GIF: Local Media Conversion Engine

**Vid2GIF** is a lightweight, high-speed Python utility designed to convert local video files into high-quality GIFs. Perfect for developers, designers, and content creators, it provides a command-line interface to bypass slow web-converters and maintain full control over the output quality.

## ✨ Why Vid2GIF?
* **Privacy First:** All processing happens locally on your machine—no data is uploaded.
* **Format Flexibility:** Supports all major video formats (MP4, MKV, MOV, etc.).
* **Custom Resolution:** Easily scale down 4K or 1080p footage for web-friendly GIFs.
* **Performance:** Optimized for speed using the `MoviePy` and `FFmpeg` backends.

## 🛠 Tech Stack
* **Language:** Python 3.12
* **Processing:** MoviePy / FFmpeg
* **Environment:** Works seamlessly on Windows, macOS, and Linux (WSL/Ubuntu).

## 📦 Usage
Convert any video in your current directory with a single command:
```bash
python main.py --input video.mp4 --output animation.gif --fps 15
