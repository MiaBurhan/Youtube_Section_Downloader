import subprocess

url = "https://youtu.be/mfv0V1SxbNA"

# Step 1: get direct stream URL
stream_url = subprocess.check_output([
    "yt-dlp", "-f", "bv*+ba", "-g", url
]).decode().strip()

# Step 2: trim with ffmpeg
subprocess.run([
    "ffmpeg",
    "-ss", "00:32:13",
    "-to", "00:34:34",
    "-i", stream_url,
    "-c", "copy",
    "clip.mp4"
])