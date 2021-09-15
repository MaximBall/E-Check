PASSWORD = 'asqw'
DB='name-db'

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://mks:{PASSWORD}@cluster0.qvwnv.mongodb.net/{DB}?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[DB]
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    print("Try connect")
    dbname = get_database()
    print("Connect")

    collection_name = dbname["user_1_items"]


    item_2 = {
        "item_name" : "NEW_OKI",
        "price" : 342,
        "category" : "kitchen appliance"
    }

    collection_name.insert_one(item_2)