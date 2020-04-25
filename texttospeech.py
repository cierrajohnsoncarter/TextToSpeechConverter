from newspaper import Article  # Extracting and parsing articles
import nltk  # Work with human language data
from gtts import gTTS  # text to speech conversion
import os  # Interacting with operating system
from io import BytesIO
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

# Get the article
article = Article(
    'https://hackernoon.com/how-to-launch-your-own-blockchain-choosing-the-right-consensus-part-ii-y07y32tv')

article.download()  # Download the article
article.parse()  # Parse the article
nltk.download('punkt')  # Download 'punkt' package
article.nlp()  # Apply nlp (Natural Language Processing)

# Get the article text
my_text = article.text

# Print the text
print(my_text)

# Choose language for tts
language = 'en'  # English
language2 = 'fr'

# Convert text to speech
my_obj = gTTS(text=my_text, lang=language, slow=False)
my_obj2 = gTTS(text=my_text, lang=language2, slow=False)

# Save the converted audio to a file
my_obj.save('read_article_english.mp3')
my_obj2.save('read_article_french.mp3')

# Play the file
os.system('start read_article_english.mp3')
os.system('start read_article_french.mp3')
