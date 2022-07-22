import speech_recognition
import subprocess


class GoogleAPI:
    @staticmethod
    def recognize(filepath: str):
        file_path = GoogleAPI.ogg_to_wav(filepath)

        recognizer = speech_recognition.Recognizer()

        audio_data = speech_recognition.AudioFile(file_path)
        with audio_data as source:
            # TODO: make asynchronous
            return recognizer.recognize_google(recognizer.record(source), language="ru-RU").lower()

    @staticmethod
    def ogg_to_wav(file_path: str) -> str:
        new_file_path = file_path.replace(".ogg", ".flac")

        subprocess.run(f"ffmpeg -i {file_path} -c:a flac {new_file_path}".split(" "))

        return new_file_path
