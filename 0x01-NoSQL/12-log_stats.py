#!/usr/bin/env python3
""" A module that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Prints nginx logs"""
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log = db_client.logs.nginx
    print("{} logs".format(nginx_log.estimated_document_count()))
    print("Methods:")
    for each_method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_log.count_documents({'method': each_method})
        print("\tmethod {}: {}".format(each_method, count))
    log_info = nginx_log.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(log_info)

