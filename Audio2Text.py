import whisper

# Load the model — choose "base", "small", or "medium"
model = whisper.load_model("small")

# Transcribe the audio file
result = model.transcribe("LT.mp3", language="zh")

# Print the transcription
print("Transcription:", result["text"])
