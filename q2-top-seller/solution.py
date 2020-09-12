import pandas as pd
import sys

df_names = [
    "product",
    "sales",
    "store"
]

dfs = {}

def get_inputs(argv):
    inputs = {}

    for i in range(1, len(argv), 2):
       inputs[argv[i-1]] = argv[i]
    return inputs

def parse_inputs(inputs):
    min_date = "2020-01-01"
    max_date = "2020-06-30"
    top = 3
    try:
        min_date = inputs["--min-date"]
        pass
    except Exception as e:
        print(f"[INFO] You did not set {e}. It will be used {min_date}")
        pass

    try:
        max_date = inputs["--max-date"]
        pass
    except Exception as e:
        print(f"[INFO] You did not set {e}. It will be used {max_date}")
        pass

    try:
        top = int(inputs["--top"])
        pass
    except Exception as e:
        print(f"[INFO] You did not set {e}. It will be used {top}")
        pass

    return min_date, max_date, top

def find_top_sellers(join_ds_name, att_name):
    top_sellers_df = pd.merge(dfs["sales"], 
                             dfs[join_ds_name], 
                             left_on=join_ds_name, right_on="id")\
                        .loc[:, [att_name, "quantity"]]

    top_sellers_df = top_sellers_df.groupby(att_name)\
                .sum()\
                .nlargest(top, 'quantity', keep="all")
    return top_sellers_df

inputs = get_inputs(sys.argv[1:])
min_date, max_date, top = parse_inputs(inputs)

product_fname = "product.csv"
sales_fname = "sales.csv"
store_fname = "store.csv"

for df_name in df_names:
    dfs[df_name] = pd.read_csv(df_name + ".csv")

date_mask = ((dfs["sales"]["date"] >= min_date) &
             (dfs["sales"]["date"] <= max_date))

dfs["sales"] = dfs["sales"][date_mask]


# -- top seller product --
top_seller_product_df = find_top_sellers("product", "name")

# -- top seller store --
top_seller_store_df = find_top_sellers("store", "name")
 
#-- top seller brand --
top_seller_brand_df = find_top_sellers("product", "brand")

# -- top seller city --
top_seller_city_df = find_top_sellers("store", "city")

# print results
print("-- top seller product --")
print(top_seller_product_df)

print("-- top seller store --")
print(top_seller_store_df)

print("-- top seller brand --")
print(top_seller_brand_df)

print("-- top seller city --")
print(top_seller_city_df)