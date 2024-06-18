#!/usr/bin/env python3
""" A module that returns chaneges on all topics of a school document based on the name"""
import pymongo

def update_topics(mongo_collection, name, topics):
    """A function that returns changes all topics of a school document
        based on the name"""
     mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

