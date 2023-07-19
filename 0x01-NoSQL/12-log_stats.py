#!/usr/bin/env python3
""" 12. Log stats
"""


from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Access the "logs" database and "nginx" collection
db = client['logs']
collection = db['nginx']

# Get the total number of documents in the collection
total_logs = collection.count_documents({})

print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this collection")

# Define the list of HTTP methods to check
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Display the count of each HTTP method in the collection
print("second line: Methods:")
for method in http_methods:
    count = collection.count_documents({"method": method})
    print(f"\t{method}: {count}")

# Display the count of documents with method=GET and path=/status
count_status_path = collection.count_documents({"method": "GET", "path": "/status"})
print(f"one line with the number of documents with:\nmethod=GET\npath=/status: {count_status_path}")

