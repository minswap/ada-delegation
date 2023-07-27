import json
import random

# First block of epoch 426: https://cexplorer.io/block/74ccbf93c3f546dafe5e8e93448c567b8122603e87b9f6909ba3fdae89792ba4
SEED = "74ccbf93c3f546dafe5e8e93448c567b8122603e87b9f6909ba3fdae89792ba4"

with open('filtered-pool-list.json') as file:
    data = json.load(file)

random.seed(SEED)
# Number of pools needs to be <= 2080 in order to fit within Python's Mersenne Twister implemetation's period
random.shuffle(data)

with open('randomize-pool-list.json', 'w') as file:
    json.dump(data, file, indent=2)
