import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convert_to_month(int):
  months = {
      1: "January",
      2: "February",
      3: "March",
      4: "April",
      5: "May",
      6: "June",
      7: "July",
      8: "August",
      9: "September",
      10: "October",
      11: "November",
      12: "December"
  }
  if 1 <= int <= 12:
    return months[int]
  else:
    return "NA"

df = pd.read_csv('backend/dataset/nike-new-data.csv')

def extract_gender(product_type):
    if str(product_type).startswith('Men'):
        return 'Men'
    elif str(product_type).startswith('Women'):
        return 'Women'

def extract_category(product):
    product_type = str(product.lower())
    if 'footwear' in product_type:
        return 'Footwear'
    elif 'apparel' in product_type:
        return 'Apparel'
    
def extract_product(product):
    if "street" in product.lower():
        return "Street Footwear"
    elif "athletic" in product.lower():
        return "Athletic Footwear"
    elif "apparel" in product.lower():
        return "Apparel"


# DATA CLEANING, DATA PREPROCESSING, DATA TRANSFORMATION, DATA WRANGLING
df.drop_duplicates()
df.fillna("NA")
df["Date"]= pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month.apply(convert_to_month)
df['Gender'] = df['Product'].apply(extract_gender)
df['Type'] = df['Product'].apply(extract_category)
df["SubType"] = df['Product'].apply(extract_product)

new = df.groupby(["Date","Year","Month","State","Sales Method","Product","Gender","Type","SubType"])[['Price per Unit','Units Sold']].sum().reset_index()

new["Revenue"] = new["Price per Unit"] * new["Units Sold"]

new.to_csv("backend/dataset/nike-data-cleaned.csv", index=False)

df20 = new[new["Year"] == 2020]
df21 = new[new["Year"] == 2021]

yoy_revenue_df = new.groupby(["Year"])[['Revenue']].sum().reset_index()
yoy_sales_df = new.groupby(["Year"])[['Units Sold']].sum().reset_index()

mom_revenue_df = new.groupby(["Month"])[['Revenue']].sum().reset_index()
mom_sales_df = new.groupby(["Month"])[['Units Sold']].sum().reset_index()

gender_revenue_df = new.groupby(["Gender"])[['Revenue']].sum().reset_index()
gender_sales_df = new.groupby(["Gender"])[['Units Sold']].sum().reset_index()

product_revenue_df = new.groupby(["Product"])[['Revenue']].sum().reset_index()
product_sales_df = new.groupby(["Product"])[['Units Sold']].sum().reset_index()

type_revenue_df = new.groupby(["Type"])[['Revenue']].sum().reset_index()
type_sales_df = new.groupby(["Type"])[['Units Sold']].sum().reset_index()

sub_type_revenue_df = new.groupby(["SubType"])[['Revenue']].sum().reset_index()
sub_type_sales_df = new.groupby(["SubType"])[['Units Sold']].sum().reset_index()


yoy_revenue = {}
yoy_sales = {}
gender_revenue = {}
gender_sales = {}
type_revenue = {}
type_sales = {}
product_revenue = {}
product_sales = {}
mom_revenue = {}
mom_sales = {}
sub_type_revenue = {}
sub_type_sales = {}

# Year on year data aggregation
for index, row in yoy_revenue_df.iterrows():
    key = row['Year']
    value = row['Revenue']
    yoy_revenue.update({int(key):int(value)})
    
for index, row in yoy_sales_df.iterrows():
    year = row['Year']
    value = row['Units Sold']
    yoy_sales.update({int(year):int(value)})        

# Month on month data aggregation
for index, row in mom_revenue_df.iterrows():
    key = row['Month']
    value = row['Revenue']
    mom_revenue.update({key:value})

for index, row in mom_sales_df.iterrows():
    key = row['Month']
    value = row['Units Sold']
    mom_sales.update({key:value})
        
# Gender data aggregation
for index, row in gender_revenue_df.iterrows():
    key = row['Gender']
    value = row['Revenue']
    gender_revenue.update({key:value})

for index, row in gender_sales_df.iterrows():
    key = row['Gender']
    value = row['Units Sold']
    gender_sales.update({key:value})
    
# Product data aggregation    
for index, row in product_revenue_df.iterrows():
    key = row['Product']
    value = row['Revenue']
    product_revenue.update({key:value})

for index, row in product_sales_df.iterrows():
    key = row['Product']
    value = row['Units Sold']
    product_sales.update({key:value})    

# Product sub type data aggregation
for index, row in type_revenue_df.iterrows():
    key = row['Type']
    value = row['Revenue']
    type_revenue.update({key:value})

for index, row in type_sales_df.iterrows():
    key = row['Type']
    value = row['Units Sold']
    type_sales.update({key:value})

# Product sub type data aggregation
for index, row in sub_type_revenue_df.iterrows():
    key = row['SubType']
    value = row['Revenue']
    sub_type_revenue.update({key:value})

for index, row in sub_type_sales_df.iterrows():
    key = row['SubType']
    value = row['Units Sold']
    sub_type_sales.update({key:value})
    

# print(yoy_revenue)
# print(yoy_sales)
# print(mom_revenue)
# print(mom_sales)
# print(gender_revenue)
# print(gender_sales)
# print(type_revenue)
# print(type_sales)
# print(product_revenue)
# print(product_sales)

# {2020: 3348615, 2021: 13291227}
# {2020: 46405, 2021: 195579}
# {'April': 1475253, 'August': 1705552, 'December': 1580985, 'February': 1119642, 'January': 1412190, 'July': 1612631, 'June': 1234661, 'March': 1069808, 'May': 1500912, 'November': 1234626, 'October': 1203945, 'September': 1489637}
# {'April': 21312, 'August': 25151, 'December': 18719, 'February': 18820, 'January': 22301, 'July': 21173, 'June': 17451, 'March': 18750, 'May': 21016, 'November': 16935, 'October': 17947, 'September': 22409}
# {'Men': 8931351, 'Women': 7708491}
# {'Men': 130251, 'Women': 111733}
# {'Apparel': 5623873, 'Footwear': 11015969}
# {'Apparel': 72441, 'Footwear': 169543}
# {"Men's Apparel": 2313798, "Men's Athletic Footwear": 2861385, "Men's Street Footwear": 3756168, "Women's Apparel": 3310075, "Women's Athletic Footwear": 2006964, "Women's Street Footwear": 2391452}
# {"Men's Apparel": 30085, "Men's Athletic Footwear": 42429, "Men's Street Footwear": 57737, "Women's Apparel": 42356, "Women's Athletic Footwear": 31068, "Women's Street Footwear": 38309}

def get_best(data):
    key = max(data, key=data.get)
    value = data[key]
    return [key, value]

def get_least(data):
    key = min(data, key=data.get)
    value = data[key]
    return [key, value]

data = {
    "units_2021": f"{yoy_sales.get(2021)} UNITS".upper(),
    "revenue_2021":f"{yoy_revenue.get(2021)} $".upper(),
    "units_2021": f"{yoy_sales.get(2020)} UNITS".upper(),
    "revenue_2021":f"{yoy_revenue.get(2020)} $".upper(),
    "top_month_sales":f"{get_best(mom_sales)[0]} - {get_best(mom_sales)[1]} UNITS".upper(),
    "top_month_revenue":f"{get_best(mom_revenue)[0]} - {get_best(mom_revenue)[1]} $".upper(),
    "least_month_sales":f"{get_least(mom_sales)[0]} - {get_least(mom_sales)[1]} UNITS".upper(),
    "least_month_revenue":f"{get_least(mom_revenue)[0]} - {get_least(mom_revenue)[1]} $".upper(),
    "top_revenue_product":f"{get_best(product_revenue)[0]} - {get_best(product_revenue)[1]} $".upper(),
    "top_sold_product":f"{get_best(product_sales)[0]} - {get_best(product_sales)[1]} $".upper(),
    "men_sales":f"{gender_sales.get('Men')} UNITS".upper(),
    "men_revenue":f"{gender_revenue.get('Men')} $".upper(),
    "women_sales":f"{gender_sales.get('Women')} UNITS".upper(),
    "women_revenue":f"{gender_revenue.get('Women')} $".upper(),
    "top_sold_type":f"{get_best(type_sales)[0]} - {get_best(type_sales)[1]} $".upper(),
    "top_revenue_type":f"{get_best(type_revenue)[0]} - {get_best(type_revenue)[1]} $".upper(),
    "top_sold_sub_type":f"{get_best(sub_type_sales)[0]} - {get_best(sub_type_sales)[1]} $".upper(),
    "top_revenue_sub_type":f"{get_best(sub_type_revenue)[0]} - {get_best(sub_type_revenue)[1]} $".upper(),
}   
