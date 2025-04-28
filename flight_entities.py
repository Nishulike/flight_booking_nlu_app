# flight_entities.py
import spacy

# Load the spaCy small English model
nlp = spacy.load("en_core_web_sm")

def extract_entities(sentence):
    """Extracts relevant entities from the sentence."""
    doc = nlp(sentence)
    entities = {}

    for ent in doc.ents:
        if ent.label_ == "GPE":  # GPE = Geo-Political Entity (cities/countries)
            if "from" in sentence.lower().split(ent.text.lower())[0]:
                entities["source_city"] = ent.text
            else:
                entities["destination_city"] = ent.text
        elif ent.label_ == "DATE":
            entities["departure_date"] = ent.text
        elif ent.label_ == "CARDINAL" or ent.label_ == "ORDINAL":
            entities["flight_number"] = ent.text  # Rough assumption

    return entities
