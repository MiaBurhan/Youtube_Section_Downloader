
import subprocess

url = "https://youtu.be/vmpMvS6EOBw"

subprocess.run([
    "yt-dlp",
    "-f", "bv*[height<=1080]+ba/b[height<=1080]",
    "--merge-output-format", "mp4",
    "--download-sections", "*00:03:43-00:05:44",
    "--force-keyframes-at-cuts",
    "-o", "NewCodecCheck.%(ext)s",
    url
], check=True)
