import pandas as pd

{'LOCATION': ['california'], 'DATE': ['january'], 'GENDER': ['men'], 'intent': 'units_sold', 'product': 'athletic footwear'}

df = pd.read_csv("backend/dataset/nike-data-cleaned.csv")
# print(df.columns)

years = df["Year"].unique().tolist()
months = df["Month"].unique().tolist()
states = df["State"].unique().tolist()
sales_methods = df["Sales Method"].unique().tolist()
products = df["Product"].unique().tolist()
types = df["Type"].unique().tolist()
sub_types = df["SubType"].unique().tolist()


def get_response(data:dict):
    df_filter = df
    for key, values in data.items():
        if key == "DATE":
            for i in values:
                if str(i).capitalize() in months:
                    df_filter = df_filter[df_filter['Month'] == f"{str(i).capitalize()}"]
                    # print(df_filter)
        elif key == "LOCATION":
            for i in values:
                if str(i).capitalize() in states:
                    df_filter = df_filter[df_filter['State'] == f"{str(i).capitalize()}"]
                    # print(df_filter)
        elif key == "PRODUCT":
            # print(str(values).title())
            df_filter = df_filter[df_filter['SubType'] == f"{str(values).title()}"]
            # print(df_filter)
        elif key == "GENDER":
            for i in values:
                # print(str(i).title())
                df_filter = df_filter[df_filter['Gender'] == f"{str(i).title()}"]
        
        if key == "INTENT":
            val = values
            if val == "units_sold":
                return f'{df_filter["Units Sold"].sum()} UNITS'
            elif val == "revenue":
                return f'{df_filter["Revenue"].sum()} $'
            else:
                return f'{df_filter["Units Sold"].sum()} UNITS & {df_filter["Revenue"].sum()} $'

        if "INTENT" not in list(data.keys()):
            return f'{df_filter["Units Sold"].sum()} UNITS & {df_filter["Revenue"].sum()} $'
    

data = {'LOCATION': ['california'], 'DATE': ['january'], 'GENDER': ['men'], 'INTENT': 'units_sold', 'PRODUCT': 'athletic footwear'}
# print(get_response(data))