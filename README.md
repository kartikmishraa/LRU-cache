# LRU Cache

This is a Python-based implementation of LRU Cache, a data structure used to store a limited number of items and improve performance by reducing the number of costly operations needed to retrieve data.

> It works on the principle that the items that have been used recently are more likely to be used again, while the items that have not been used recently are less likely to be used again.

LRU cache is commonly used in applications where there is a high frequency of reads and a low frequency of writes.

## How LRU Cache works

The LRU cache is implemented using a combination of hash tables and doubly linked lists. Each node in the linked list represents an item in the cache, and the hash table maps the keys to the corresponding nodes in the list. When an item is accessed, it is moved to the front of the list, and when the cache is full, the item at the end of the list (i.e., the least recently used item) is removed.

## Requirements

This project requires Python 3.7 or later.

## Usage

To use the LRU Cache, import the **'LRU'** class from the **'cache'** module:

```python
from cache import LRU

c1 = LRU(50)  # create a cache with a limit of 100 items

c1.set("India", "+91")  # add an item to the cache
c1.set("UK", "+44")

print(c1.get("India"))  # retrieve an item from the cache
```

> The Cache class has two methods:
>
> - set(key, value): Adds an item to the cache with the given key and value. If the cache is full, the least recently used item is removed.
> - get(key): Retrieves the value of the item with the given key from the cache. If the item is not in the cache, None is returned.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions to this project are welcome. To contribute, fork the repository, create a new branch, and submit a pull request. Please include tests for any new functionality.
