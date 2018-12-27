import pandas as pd



google_main = pd.read_csv("./datasets/googleplaystore.csv")
print(google_main.columns)

google_app_reviews = pd.read_csv("./datasets/googleplaystore_user_reviews.csv")
print(google_app_reviews.columns)
