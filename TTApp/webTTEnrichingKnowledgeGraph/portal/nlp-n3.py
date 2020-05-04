import spacy
# Word tokenization
from spacy.lang.en import English
from spacy.lang.es import Spanish
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
import en_core_web_sm

# Load English tokenizer, tagger, parser, NER and word vectors
# nlp = English()
nlp = spacy.load("en_core_web_sm")


#text2 = '<http://opendata.org/resource/Waste_incineration_of_ferro_metals_average_european_waste_to_energy_plant_without_collection_transport_and_pre_treatment_at_plant_location_eu_27_catalog><http://purl.org/dc/terms/description><"The European average Waste">.'


text = 'New York_City on Tuesday declared a public health emergency and ordered mandatory measles vaccinations amid an outbreak, becoming the latest national flash point over refusals to inoculate against dangerous diseases. At least 285 people have contracted measles in the city since September, mostly in Brooklyn’s Williamsburg neighborhood. The order covers four Zip codes there, Mayor Bill de Blasio (D) said Tuesday. The mandate orders all unvaccinated people in the area, including a concentration of Orthodox Jews, to receive inoculations, including for children as young as 6 months old. Anyone who resists could be fined up to $1,000.'

textSplit = text.split('/')
text2 = ''
text2 = textSplit

print("split text", textSplit)
#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)


# my_doc = nlp("""New York City on Tuesday declared a public health emergency and ordered mandatory measles vaccinations amid an outbreak, becoming the latest national flash point over refusals to inoculate against dangerous diseases.
# At least 285 people have contracted measles in the city since September, mostly in Brooklyn’s Williamsburg neighborhood. The order covers four Zip codes there, Mayor Bill de Blasio (D) said Tuesday.
# The mandate orders all unvaccinated people in the area, including a concentration of Orthodox Jews, to receive inoculations, including for children as young as 6 months old. Anyone who resists could be fined up to $1,000.""")


# Create list of word tokens
token_list = []

#Implementation of stop words:
filtered_sent = []

for token in my_doc:
    token_list.append(token.text)
print(token_list, token.text)

for token2 in my_doc.ents:
    print([token2.text, token2.label_])

# filtering stop words
for word in my_doc:
    if word.is_stop==False:
        filtered_sent.append(word)
print("\n Filtered Sentence:", filtered_sent)

print("entitys: ", [(X.text, X.label_) for X in my_doc.ents])
