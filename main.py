import sys
import argparse
from utils.stt import SpeechToText
from utils.tts import TextToSpeech
from utils.responses import get_response
from face_detection import FaceDetector

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Hindi AI Assistant')
    parser.add_argument('--file', type=str, help='Path to audio file for processing')
    parser.add_argument('--no-face', action='store_true', help='Disable face detection')
    args = parser.parse_args()

    # Initialize components
    stt = SpeechToText()
    tts = TextToSpeech()
    face_detector = None if args.no_face else FaceDetector()

    # Check for face detection once at startup
    if not args.file and not args.no_face:
        face_detected = face_detector.detect_face()
        if not face_detected:
            print("❌ No user detected. Please face the camera.")
            return
        print("✅ User detected! Starting voice recognition...")

    try:
        print("\n💡 Hindi AI Assistant is ready!")
        print("➡️ Press Ctrl+C twice to exit the program")
        print("➡️ Press Ctrl+C once to stop listening and get response\n")

        while True:  # Main conversation loop
            try:
                if args.file:
                    # File mode
                    print("🎧 Processing audio file:", args.file)
                    text = stt.transcribe_file(args.file)
                    # Exit after processing file
                    break
                else:
                    # Microphone mode
                    print("🎤 Listening... (Press Ctrl+C to stop)")
                    text = stt.listen_microphone()

                if text:
                    print(f"🎤 User said: {text}")
                    response, should_exit = get_response(text)
                    print(f"🤖 Response: {response}")
                    print("🔊 Speaking reply...")
                    tts.speak(response)
                    
                    if should_exit:
                        print("\n👋 Goodbye!")
                        return
                    else:
                        print("\n➡️ Ready for next question! (Say 'अलविदा' or press Ctrl+C twice to exit)\n")
                else:
                    print("❌ Could not understand the speech")
                    
            except KeyboardInterrupt:
                # Inner try-catch to handle single Ctrl+C for stopping listening
                continue

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()