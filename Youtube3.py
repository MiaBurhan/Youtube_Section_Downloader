import subprocess

url = "https://youtu.be/vmpMvS6EOBw"

subprocess.run([
    "yt-dlp",
    "-f", "bv*[height=1080][vcodec^=vp09]+ba/bv*[height=1080][vcodec^=av01]+ba/bv*[height<=1080]+ba",
    "--merge-output-format", "mkv",
    "--download-sections", "*00:03:43-00:05:44",
    "-o", "newcodecChecking.mkv",
    url,
], check=True)