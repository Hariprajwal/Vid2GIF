import os
import math
import subprocess

def video_to_gifs(video_path, output_dir="gifs", clip_length=3, fps=15):
    # Ensure output folder exists
    os.makedirs(output_dir, exist_ok=True)

    # Get video duration using ffprobe
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", video_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    try:
        duration = float(result.stdout.strip())
    except ValueError:
        print("❌ Could not read video duration. Check ffmpeg installation.")
        return

    print(f"Video length: {duration:.2f} seconds")

    # Number of GIFs to create
    num_clips = math.ceil(duration / clip_length)

    for i in range(num_clips):
        start = i * clip_length
        output_path = os.path.join(output_dir, f"output_{i+1}.gif")

        # ffmpeg command
        command = [
            "ffmpeg", "-y",             # overwrite
            "-ss", str(start),          # start time
            "-t", str(clip_length),     # duration
            "-i", video_path,           # input file
            "-vf", f"fps={fps},scale=480:-1:flags=lanczos", # resize + fps
            output_path
        ]

        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"✅ Saved: {output_path}")

# --- Hardcoded path ---
# Replace this with the actual path to your video file
video_path = "D:\\downloads\\namo\\1.mp4" # Change this to your actual file path

# Check if file exists
if os.path.exists(video_path):
    print(f"Processing: {video_path}")
    video_to_gifs(video_path)
else:
    print(f"❌ File not found: {video_path}")
    print("Please make sure to:")
    print("1. Replace the video_path with your actual file path")
    print("2. Use the correct file extension (.mp4, .mov, etc.)")
    print("3. Use the full path if the file isn't in the same directory")
