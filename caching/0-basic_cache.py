#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''



class BaseCaching:
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

# Example usage:
if __name__ == "__main__":
    # Create an instance of BasicCache
    basic_cache = BasicCache()

    # Add items to the cache
    basic_cache.put("key1", "value1")
    basic_cache.put("key2", "value2")
    basic_cache.put("key3", "value3")

    # Print the cache
    basic_cache.print_cache()

    # Retrieve items from the cache
    print("Get key1:", basic_cache.get("key1"))  # Output: value1
    print("Get key4:", basic_cache.get("key4"))  # Output: None
    print("Get None:", basic_cache.get(None))    # Output: None
