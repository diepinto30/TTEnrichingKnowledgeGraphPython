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
nlpPredicate = spacy.load("en_core_web_sm")
nlpObjectEntity = spacy.load("en_core_web_sm")


subjectEntity = 'The decline of global extreme poverty continues, but has slowed. The deceleration indicates that the world' \
                ' is not on track to achieve the target of less than 3 per cent of the world living in extreme poverty by 2030. ' \
                'People who continue to live in extreme poverty face deep, entrenched deprivation often exacerbated by violent conflicts ' \
                'and vulnerability to disasters. Strong social protection systems and government spending on key services often help ' \
                'those left behind get back on their feet and escape poverty, but these services need to be brought to scale.' \
                'The share of the world population living in extreme poverty declined to 10 per cent in 2015, down from 16 per cent ' \
                'in 2010 and 36 per cent in 1990. However, the pace of poverty reduction is decelerating, with a “nowcast” of 8.6 per ' \
                'cent in 2018. Moreover, baseline projections suggest that 6 per cent of the world population will still be living in ' \
                'extreme poverty in 2030, missing the target of ending poverty.' \
                'Despite having a job, 8 per cent of the world’s workers and their families still lived in extreme poverty in 2018. ' \
                'The situation remains particularly alarming in sub-Saharan Africa, where the share of working poor stood at 38 per cent in 2018.' \
                'Social protection systems help prevent and reduce poverty and provide a safety net for the vulnerable. However, social ' \
                'protection is not a reality for a large majority of the world’s population. In 2016, 55 per cent – as many as 4 billion ' \
                'people – were not covered by any social protection cash benefits, with large variations across regions: from 87 per' \
                ' cent without coverage in sub-Saharan Africa to 14 per cent in Europe and Northern America.' \
                'Only 22 percent of unemployed persons receive unemployment cash benefits, only 28 per cent of persons with severe ' \
                'disabilities receive disability cash benefits, only 35 per cent of children worldwide enjoy effective access to social protection and only 41 per cent of women giving birth receive maternity cash benefits.' \
                'Disasters often lead to a downturn in the trajectory of socioeconomic development and exacerbate poverty. From 1998 to 2017, direct economic losses from disasters were estimated at almost $3 trillion, of which climate - related disasters accounted for 77 per cent of the total – a rise of 151 per cent compared with the period from 1978 to 1997 – and climate-related and geophysical disasters claimed an estimated 1.3 million lives. More than 90 per cent of deaths reported internationally were due to disaster events in low- and middle-income countries, and economic losses from disasters as a percentage of gross domestic product (GDP) were also much higher in these countries.' \
                'Countries have reported progress in the development and implementation of national and local disaster risk reduction strategies in line with the Sendai Framework for Disaster Risk Reduction 2015–2030. As at 31 March 2019, 67 countries had reported progress in such alignment and 24 countries reported that their respective local governments had developed local strategies consistent with national strategies and plans.' \
                'Only one third of all countries spend between 15 per cent and 20 per cent of total government expenditure on education, as recommended in the Education 2030 Framework for Action'

predicate = ' city'

objectEntity = 'The European average Waste.'


# text = "New York City on Tuesday declared a public health emergency and ordered mandatory measles vaccinations amid an outbreak, becoming the latest national flash point over refusals to inoculate against dangerous diseases. At least 285 people have contracted measles in the city since September, mostly in Brooklyn’s Williamsburg neighborhood. The order covers four Zip codes there, Mayor Bill de Blasio (D) said Tuesday. The mandate orders all unvaccinated people in the area, including a concentration of Orthodox Jews, to receive inoculations, including for children as young as 6 months old. Anyone who resists could be fined up to $1,000."

# split text to character
textSplit = subjectEntity.split('_')
text2 = ''
text2 = textSplit
print("split text", textSplit)


#  "nlp" Object is used to create documents with linguistic annotations.
my_docSubjectEntity = nlp(subjectEntity)
my_docPredicate = nlpPredicate(predicate)
my_docObjectEntity = nlpObjectEntity(objectEntity)

# Create list of word tokens
token_list = []

for token2 in my_docSubjectEntity:
    print(token2.text)

for token in my_docPredicate:
    print(token.text, token.lemma_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

for ent in my_docSubjectEntity.ents:
    print("Entitys: ", [ent.text, ent.label_])

# for ent in my_docPredicate:
    # print("Predicate: ", [ent.text, ent.label_, ent.tag_])

for ent in my_docObjectEntity.ents:
    object3 = ''
    print("Object: ", [ent.text, ent.label_])
    object3 = ent.text + " " + ent.label_
    print(object3)

for ent2 in my_docPredicate:
    print("Object: ", token.text, token.lemma_, token.tag_, token.dep_)


