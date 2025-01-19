import spacy

nlp = spacy.load("en_core_web_sm")

def get_spacy_params(text):

    words = text.split()
    updated_words = []
    for i in words:
        updated_words.append(i.capitalize())

    input  = " ".join(updated_words) 
    # print(input)

    LOCATION = []
    DATE = []
    GENDER = []
    doc = nlp(input.lower())

    tokens = []
    for token in doc:
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        #         token.shape_, token.is_alpha, token.is_stop)
        if token.is_stop == False:
            tokens.append(str(token.text))
        if token.lemma_ in  ["men","women","male",'female',"gents","ladies"]:
            if str(token.lemma_) not in GENDER:
                GENDER.append(str(token.lemma_))
        if token.text in ["men","women","male",'female',"gents","ladies"]:
            if str(token.text) not in GENDER:
                GENDER.append(str(token.text))   
        if token.text== "may":
            DATE.append("may")
    for ent in doc.ents:
        # print(ent.text, ent.label_)
        if ent.label_ == "GPE" or ent.label_ == "City" or ent.label_ == "LOC" :
            LOCATION.append(str(ent.text).lower())
        elif ent.label_ == "DATE":
            if str(ent.text).lower() not in DATE:
                DATE.append(str(ent.text).lower())
            
    mappings = {}
    if len(LOCATION)!= 0 :
        mappings.update({"LOCATION":LOCATION})    
    if len(DATE)!= 0 :
        mappings.update({"DATE":DATE})
    if len(GENDER)!= 0 :
        mappings.update({"GENDER":GENDER})

    return mappings




state_mapping = {
    "CO": "Colorado",
    "FL": "Florida",
    "IL": "Illinois",
    "OH": "Ohio",
    "PA": "Pennsylvania",
    "OR": "Oregon",
    "VA": "Virginia",
    "AL": "Alabama",
    "CA": "California",
    "NJ": "New jersey",
    "LA": "Louisiana",
    "MD": "Maryland",
    "GA": "Georgia",
    "TX": "Texas",
    "MA": "Massachusetts",
    "NY": "New york",
    "AZ": "Arizona",
    "WI": "Wisconsin",
    "MO": "Missouri",
    "KY": "Kentucky",
    "NC": "North carolina",
    "MN": "Minnesota",
    "NV": "Nevada",
    "KS": "Kansas",
    "IN": "Indiana",
    "NH": "New hampshire",
    "NE": "Nebraska",
    "HI": "Hawaii",
    "NM": "New mexico",
    "UT": "Utah",
    "CT": "Connecticut",
    "MT": "Montana",
    "IA": "Iowa",
    "AR": "Arkansas",
    "PR": "Puerto rico",
    "WA": "Washington",
    "DE": "Delaware",
    "TN": "Tennessee",
    "WV": "West virginia",
    "MI": "Michigan",
    "OK": "Oklahoma",
    "Ok": "Oklahoma",
    "SC": "South carolina",
    "MS": "Mississippi",
    "SD": "South dakota",
    "DC": "District of columbia",
    "ND": "North dakota",
    "ME": "Maine",
    "RI": "Rhode island",
    "VT": "Vermont",
    "AK": "Alaska",
    "ID": "Idaho",
    "WY": "Wyoming",
    "AB": "Alberta",
    "BC": "British Columbia",
    "ON": "Ontario",
    "QC": "Quebec",
    "NB": "New Brunswick",
    "NL": "Newfoundland and Labrador",
    "NS": "Nova Scotia",
    "PE": "Prince Edward Island",
    "MB": "Manitoba",
    "NT": "Northwest Territories",
    "NU": "Nunavut",
    "SK": "Saskatchewan",
    "YT": "Yukon",
}
# for x,y in state_mapping.items():
#     print(get_spacy_params("What are sales in "+ y))
#     print()    
    
# print(get_spacy_params(test_text))
# {"Men's Apparel": 2313798, "Men's Athletic Footwear": 2861385, "Men's Street Footwear": 3756168, "Women's Apparel": 3310075, "Women's Athletic Footwear": 2006964, "Women's Street Footwear": 2391452}
# while True:
#     text = input("Enter a question: ")
#     print(get_spacy_params(text))
#     print()
     
# months = ["january", "february" ,"march" ,"april" ,"may" ,"june", "july", "august", "september" ,"october", "november", "december"]
# for i in months:
#     text = f"Sales in {i}"
#     print(get_spacy_params(text))