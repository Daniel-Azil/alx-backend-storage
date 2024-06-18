#!/usr/bin/env python3
"""A python module that lists all document in a collection."""
import pymongo


def list_all(mongo_collection):
    """A function that lists all document in the given collection."""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())

