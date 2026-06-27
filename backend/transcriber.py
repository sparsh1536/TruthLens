from faster_whisper import WhisperModel
import os

# Tiny model for faster inference
model = WhisperModel("tiny", device="cpu", compute_type="int8")


def transcribe_audio(audio_path):

    transcript_path = audio_path + ".txt"

    # Use cached transcript if available
    if os.path.exists(transcript_path):
        print("⚡ Using cached transcript...")
        with open(transcript_path, "r", encoding="utf-8") as f:
            return f.read()

    print("🎙️ Transcribing audio...")

    segments, info = model.transcribe(audio_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + "\n"

    # Save transcript for future runs
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript