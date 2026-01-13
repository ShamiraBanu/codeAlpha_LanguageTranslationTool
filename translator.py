# Make sure to install the library first:
# pip install deep-translator

from deep_translator import GoogleTranslator

# Ask user for input text
text = input("Enter the text you want to translate: ")

# Ask user for target language code (e.g., 'ta' for Tamil, 'hi' for Hindi, 'fr' for French)
target_language = input("Enter the target language code (e.g., ta, hi, fr): ")

try:
    # Translate the text
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    
    # Show results
    print("\nOriginal Text:", text)
    print("Translated Text:", translated)

except Exception as e:
    print("Error occurred:", e)
    print("Make sure the language code is correct and you have an internet connection.")
