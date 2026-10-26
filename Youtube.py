import subprocess

url = "https://youtu.be/vmpMvS6EOBw"

# Download and trim directly using yt-dlp's built-in section feature
subprocess.run([
    "yt-dlp",
    "-S", "res:1080",
    "--download-sections",
    "*00:03:43-00:05:44",
    "-o", "newcodeccheck",
    url
])