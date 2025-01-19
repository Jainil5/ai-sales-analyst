import json

products = ["units_sold","revenue"]
final_list = []

for value in products:
    product_list = []
    product_list.append(f"What are the sales of {value}?".lower())
    product_list.append(f"What is the revenue of {value}?".lower())
    product_list.append(f"Units sold of {value} in California?".lower())
    product_list.append(f"Sales of {value} in Texas?".lower())
    product_list.append(f"How many units of {value} sold in Atlanta?".lower())

    value = {"tag":value.lower(),"patterns":product_list,"responses":[value.lower()]}
    
    final_list.append(value)  

# print(final_list)

output_dict = {"intents":final_list}

with open("backend/intent_model/intent_intents.json", "w") as file:
    json.dump(output_dict, file, indent=2)

