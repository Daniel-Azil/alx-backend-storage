#!/usr/bin/env python3
""" A module that creates new document within the collection. """
import pymongo


def  insert_school(mongo_collection, **kwargs):
    """ A function thats inserts new document and attribute"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)

