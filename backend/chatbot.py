from spacy_main import get_spacy_params
from intent_model.intent_fetch import detect_intent
from product_model.product_fetch import detect_product
from fetch_response import get_response


def filter_params(input):
    intent = detect_intent(input)
    product = detect_product(input)
    params = get_spacy_params(input)
    if len(intent)!=0:
        params.update({"INTENT":intent})
    if len(product)!=0:
        params.update({"PRODUCT":product})
    
    return params
    
def generate_reponse(text):
    final = filter_params(text)
    
    reply = get_response(final)
    return reply







"""
What are the sales of mens athletic footwear in California in January
----->{'LOCATION': ['california'], 'DATE': ['january'], 'GENDER': ['men'], 'intent': 'units_sold', 'product': 'athletic footwear'}

What is the revenue of mens street footwear in Texas in November
----->{'LOCATION': ['texas'], 'DATE': ['november'], 'GENDER': ['men'], 'intent': 'revenue', 'product': 'street footwear'}

Sales and revenue for Men in May
----->{'DATE': ['may'], 'GENDER': ['men'], 'intent': 'sales_revenue'}
"""    

# questions = ["What are the sales of mens athletic footwear in California in January", "What is the revenue of mens street footwear in Texas in November","Sales and revenue for Men in May"]
# for i in questions:
#     print(i)
#     print(f"----->{filter_params(i)}\n")

# while True:
#     text = input("Enter a question: ")
#     print(filter_params(text))    
    