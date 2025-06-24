from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import json
import pandas as pd


def main():
    # Połączenie z MongoDB
    client = MongoClient("mongodb://localhost:27017/?replication=true")

    db = client["moviesDB"]
    collection = db["moviesCollection"]

    projection = {"title": 1, "revenue.Amount": 1, "budget.Amount":1}  # wyłącznie pola title, revenue i budget
    documents = collection.find({}, projection)
    df = pd.DataFrame(list(documents))

    df['budget_amount'] = df['budget'].apply(lambda x: x['Amount'])
    df['revenue_amount'] = df['revenue'].apply(lambda x: x['Amount'])
    df['profit'] = df['revenue_amount'] - df['budget_amount']
    top3 = df.nlargest(3, 'profit')
    print("Top 3 movies with the highest profit:")
    print(top3[['title', 'profit']]) # top 3 filmy z największym przychodem
    average_profit = df['profit'].mean()
    print(f"Average profit of all movies: {average_profit}") # średni przychód
    
    ### ilość wystąpień aktorów...
    actors_list = {"title": 1, "starring": 1}  # wyłącznie pola title i starring
    df2 = pd.DataFrame(list(collection.find({}, actors_list)))
    exploded = df2.explode('starring')
    # Wyciągamy nazwiska aktorów z kolumny 'starring'
    exploded['actor'] = exploded['starring'].apply(lambda x: x['Actor'] if isinstance(x, dict) else None)
    # Liczymy wystąpienia każdego aktora
    actor_counts = exploded['actor'].value_counts().sort_values(ascending=True)
    # Wyświetlamy posortowaną listę
    print(actor_counts)

    ### wyszukiwanie filmów o frazach "war", "wars", "come"
    search_terms = ["war", "wars", "come"]
    search_results = []

    # Zamknij połączenie
    client.close()

if __name__ == "__main__":
    main()