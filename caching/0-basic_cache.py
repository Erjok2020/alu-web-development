#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''



from base_caching import BaseCaching

class BaseCaching(BaseCaching):
    """ Base caching class """
    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache data """
        print("Cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
        print()

class BasicCache(BaseCaching):
    """ Basic caching system """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
