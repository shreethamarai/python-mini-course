### Generators 
#   - Memory Efficiency - only keep one item in memory at a time
#   - Faster startup - no need to build the full list first
#   - Can model infinite sequences


#  Large File Reading
#  Saves memory when dealing with massive files

def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("big_data.txt"):
    process(line)


# Streaming API Data
# start processing data as it arives instead of waiting for the full downlaod

import requests

def get_data(url):
    with requests.get(url, stream= True) as r:
        for chunk in r.iter_content(chunk_size=1024):
            yield chunk

for chunk in get_data("https://example.com/data"):
    print(len(chunk))

# Infinte Sequences
# Useful for simulations, IDs, or testing

def infinite_counter():
    n = 1
    while True:
        yield n
        n += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))


# Generators Expression
# same memory benefit, shorter syntax

squares = (x**2 for x in range(5))
print(next(squares)) 
print(next(squares))


