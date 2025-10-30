def get_response(text):
    """
    Get appropriate response based on input text
    Returns: (response_text, should_exit)
    """
    text = text.lower()
    
    # Check for exit commands
    if any(word in text for word in ["बाय", "अलविदा", "फिर मिलेंगे", "बाई", "गुड बाय"]):
        return "अलविदा! फिर मिलेंगे। 👋", True
    
    # Simple rule-based responses
    if "नाम" in text:
        return "मुझे आपका नाम नहीं पता।", False
    elif "नमस्ते" in text:
        return "नमस्ते! कैसे हैं आप?", False
    elif "मौसम" in text:
        return "क्षमा करें, मैं मौसम की जानकारी नहीं दे सकता।", False
    
    # Default response
    return "मैं समझ नहीं पाया, कृपया दोबारा बोलें।", False