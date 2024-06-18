#!/usr/bin/env python3
""" A module that returns the lists of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ A function that  returns list of school with specific topic"""
    return [t for t in mongo_collection.find({"topics": topic})]

