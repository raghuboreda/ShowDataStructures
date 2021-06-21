from collections import deque
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.key_cache = deque()
        self.cache_size = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            l = self.cache[key]
            self.key_cache.remove(key)
            self.key_cache.append(key)
            return l
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.cache:
            if self.cache_size < self.capacity:
                self.cache[key] = value
                self.key_cache.append(key)
                self.cache_size += 1
            else:
                keyToPop = self.key_cache.popleft()
                del self.cache[keyToPop]
                self.cache[key] = value
                self.key_cache.append(key)
        return



our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.set(8,8)
our_cache.set(10,21)
our_cache.set(11,22)
print(our_cache.get(1))