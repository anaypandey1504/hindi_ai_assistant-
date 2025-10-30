import os
from gtts import gTTS
from playsound import playsound
import tempfile

class TextToSpeech:
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
        self.temp_file = os.path.join(self.temp_dir, "response.mp3")

    def speak(self, text):
        """
        Convert text to speech and play it
        """
        try:
            # Create gTTS object
            tts = gTTS(text=text, lang='hi', slow=False)
            
            # Save to temporary file
            tts.save(self.temp_file)
            
            # Play the audio
            playsound(self.temp_file)
            
            # Clean up
            try:
                os.remove(self.temp_file)
            except:
                pass  # Ignore cleanup errors
                
        except Exception as e:
            print(f"❌ Error in text-to-speech: {str(e)}")
            raise