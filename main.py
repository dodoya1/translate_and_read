from deep_translator import GoogleTranslator
from gtts import gTTS

# text to speech
def text_to_speech(text, lang):    
    text2speech = gTTS(text, lang=lang)
    text2speech.save("outputs/speech.mp3")
    return True

# Use GoogleTranslator module to translate text into Japanese
def translate(text, translated_lang):
    translated = GoogleTranslator(source = 'auto',target = translated_lang).translate(text)
    return translated

# Separate sentences and translate them.
def separate_translate(text, translated_lang):
    MAX_LENGTH = 4500
    # Splits the text into chunks of the specified maximum length.
    chunks = [text[i:i+MAX_LENGTH] for i in range(0, len(text), MAX_LENGTH)]

    translated_chunks = []
    for chunk in chunks:
        translated_chunk = translate(chunk, translated_lang)
        translated_chunks.append(translated_chunk)

    translated_text = ''.join(translated_chunks)

    # Writes the translated text to a text file.
    with open("outputs/translated.txt", mode = "w") as f:
        f.write(translated_text)
    
    text_to_speech(translated_text, translated_lang)

def main():
    translated_lang = input("Please enter the subtitle language (language after translation):")

    with open("input/transcript.txt", 'r') as f:
        text = f.read()

    separate_translate(text, translated_lang)

if __name__ == "__main__":
    main()
