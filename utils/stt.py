import os
import json
import wave
import time
import msvcrt
import sounddevice as sd
import numpy as np
from vosk import Model, KaldiRecognizer

class SpeechToText:
    def __init__(self, model_path="models/vosk-model-small-hi-0.22"):
        if not os.path.exists(model_path):
            raise Exception(
                "❌ Hindi model not found. Please download from https://alphacephei.com/vosk/models"
                " and extract to models/vosk-model-small-hi-0.22"
            )
        self.model = Model(model_path)
        self.sample_rate = 16000

    def listen_microphone(self, duration=None):
        """
        Listen to microphone input and convert to text
        duration: Optional recording duration in seconds
        """
        rec = KaldiRecognizer(self.model, self.sample_rate)
        
        print("🎤 Listening... (Say something in Hindi)")
        print("Press Ctrl+C to stop listening")
        
        try:
            # Record audio in chunks
            with sd.InputStream(samplerate=self.sample_rate, 
                              channels=1,
                              dtype=np.int16,
                              blocksize=4000) as stream:
                
                while True:
                    # Read chunk of audio data
                    data, _ = stream.read(4000)
                    data = data.flatten()  # Convert to 1D array if needed
                    
                    # Process the audio chunk
                    if rec.AcceptWaveform(data.tobytes()):
                        result = json.loads(rec.Result())
                        text = result.get('text', '').strip()
                        if text:  # If we got some text, return it
                            return text
                    
                    # Show partial results
                    partial = json.loads(rec.PartialResult())
                    if partial.get('partial'):
                        print(f"Hearing: {partial['partial']}", end='\r')
                        
        except KeyboardInterrupt:
            print("\n⏹️ Stopped listening")
            # Get final results before stopping
            result = json.loads(rec.FinalResult())
            return result.get('text', '').strip()
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            return None
                            
        except KeyboardInterrupt:
            print("\n⏹️ Stopped listening")
        except Exception as e:
            print(f"❌ Error recording audio: {str(e)}")
            return None

        result = json.loads(rec.FinalResult())
        return result.get('text', '')

    def transcribe_file(self, audio_path):
        """
        Transcribe audio from a WAV file
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"❌ Audio file not found: {audio_path}")

        wf = wave.open(audio_path, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())
        
        result = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                part_result = json.loads(rec.Result())
                result += part_result.get('text', '') + " "

        final_result = json.loads(rec.FinalResult())
        result += final_result.get('text', '')
        return result.strip()