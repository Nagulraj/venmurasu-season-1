import requests

from indicnlp import common
from indicnlp import loader
from urllib.parse import quote
from indicnlp.transliterate.unicode_transliterate import ItransTransliterator

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES = r"F:\University\Final_Year\FYP\Resources\indic_nlp_resources-master\indic_nlp_resources-master"

# Export the path to the Indic NLP Resources directory programmatically
common.set_resources_path(INDIC_NLP_RESOURCES)

# Initialize the Indic NLP library
loader.load()

# Transliteration
input_text = 'புத்துணர்ச்சியான சுவாசம் மற்றும் பளபளப்பான பற்கள் தங்களின் தோற்றத்தை நிர்ணயிக்கிறது'
lang = 'ta'
print('iTrans transliteration: ')
print(ItransTransliterator.to_itrans(input_text, lang))

# transliteration with brahmi api
text = quote('புத்துணர்ச்சியான சுவாசம் மற்றும் பளபளப்பான பற்கள் தங்களின் தோற்றத்தை நிர்ணயிக்கிறது')
url = 'http://www.cfilt.iitb.ac.in/indicnlpweb/indicnlpws/transliterate_bulk/ta/en/{}/rule'.format(textsponse = requests.get(url)
print('Brahmi-net transliterations: ')
print(response.json())