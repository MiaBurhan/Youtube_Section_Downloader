# Python Youtube Segment Installer for (Linux Mint)

### PreRequirments
* Python

## Main packages to install on linux(ubuntu)
* ffmpeg version 7.1.1 
* yt-dlp version 2026.08.19
* Javascript environment 

### ffmpeg install procedure

```bash
sudo add-apt-repository ppa:ubuntuhandbook1/ffmpeg7
sudo apt update
sudo apt install ffmpeg
```

### yt-dlp install procedure
```bash
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
```
```bash
sudo chmod a+rx /usr/local/bin/yt-dlp
```
```bash
yt-dlp --version
ffmpeg -version
```
### Install ffmpeg and yt-dlp from pip too
```bash
pip install ffmpeg-python

```
```bash
pip install --upgrade yt-dlp
```

### javascript runtime(deno)
```bash
sudo apt install curl
curl -fsSL https://deno.land/install.sh | sh
```
### Optional javascript runtime
**If deno doesn't work you can install node.js environment**
```bash
sudo apt update && sudo apt install nodejs npm
```
### Use Virtual Environment for python
```bash
python -m venv .venv
```
```bash
source .venv/bin/activate
```

python3 -m venv my_env
source my_env/bin/activate

deactivate