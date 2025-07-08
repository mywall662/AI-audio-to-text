# AI-audio-to-text
**Requirement**
1. Install Whisper and Dependencies
pip install git+https://github.com/openai/whisper.git 

2. Install ffmpeg
Windows: Download from https://ffmpeg.org/download.html and add to PATH.
https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip

**🧠 Whisper Model Sizes:**
Model	Size	Speed	Accuracy
tiny	~39 MB	Fast	Low
base	~74 MB	Fast	Decent
small	~244 MB	OK	Good
medium	~769 MB	Slower	Very Good
large	~1.5 GB	Slow	Best

**Step-by-Step: Set Up ffmpeg on Windows**
1. Extract the ZIP
a. Right-click the ZIP file ffmpeg-master-latest-win64-gpl-shared.zip.
b. Extract it using “Extract All...” or 7-Zip/WinRAR.

You’ll get a folder like:
ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe

2. Move Folder
a. C:\ffmpeg\
b. C:\ffmpeg\bin\ffmpeg.exe

3. Add ffmpeg to System PATH
a. open Edit the system environment variables.
b. Click Environment Variables at the bottom.
c. Under System variables, find and select Path → click Edit.
d. Click New, and paste this path:
- C:\ffmpeg\bin


