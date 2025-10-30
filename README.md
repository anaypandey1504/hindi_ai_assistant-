# Hindi AI Voice Assistant 🎤

A Python-based voice assistant that understands and responds in Hindi. It features speech recognition, text-to-speech capabilities, and optional face detection.

## Features ✨

- 🗣️ Hindi Speech Recognition using Vosk
- 🔊 Hindi Text-to-Speech using gTTS
- 👤 Optional Face Detection using OpenCV
- 🎵 Works with both microphone and audio files
- 🤖 Simple rule-based responses
- 📱 Clean and beginner-friendly code

## Installation 🚀

1. Clone this repository:
```bash
git clone https://github.com/yourusername/hindi_ai_assistant.git
cd hindi_ai_assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the Vosk Hindi model:
   - Visit [Vosk Models Page](https://alphacephei.com/vosk/models)
   - Download `vosk-model-small-hi-0.22`
   - Extract to `models/vosk-model-small-hi-0.22` folder

## Usage 💡

### Microphone Mode
```bash
python main.py
```

### Audio File Mode
```bash
python main.py --file sample_audio/record_out_16k.wav
```

### Disable Face Detection
```bash
python main.py --no-face
```

## Sample Test Prompts 🗪

Try these Hindi phrases:
- "नमस्ते" (Hello)
- "आपका नाम क्या है?" (What is your name?)
- "मौसम कैसा है?" (How's the weather?)

## Tips for Clear Hindi Audio Recording 🎯

1. Use a quiet environment
2. Speak clearly and at a moderate pace
3. Maintain consistent distance from microphone (about 6-8 inches)
4. Test microphone levels before recording
5. Avoid background noise and echo

## Future Improvements 🚀

1. Add more complex dialogue patterns
2. Implement intent recognition
3. Add Hindi language understanding (NLU)
4. Support more Indian languages
5. Add custom wake word detection
6. Implement conversation memory
7. Add GUI interface using Streamlit

## Optional: Streamlit UI

To add a web interface, create a new file `app.py`:

```python
import streamlit as st
from utils.stt import SpeechToText
from utils.tts import TextToSpeech
from utils.responses import get_response

def main():
    st.title("Hindi AI Assistant")
    st.write("Upload an audio file or use your microphone")
    
    # Add file uploader and audio recorder
    # Add response display
    # Add audio playback
    
if __name__ == "__main__":
    main()
```

Install Streamlit:
```bash
pip install streamlit
```

Run the web interface:
```bash
streamlit run app.py
```

## Contributing 🤝

Feel free to submit issues and enhancement requests!

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.