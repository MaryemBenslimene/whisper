import whisper

model = whisper.load_model("large")
result = model.transcribe("Recording-_43_.wav")
print(result["text"])