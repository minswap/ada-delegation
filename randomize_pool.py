import json
import random

# First block of epoch 427: https://cexplorer.io/block/895af0e01d05998358cda4f8ef6868f8d75eccc36f67c731357a1d82a8e2a5ed
SEED = "895af0e01d05998358cda4f8ef6868f8d75eccc36f67c731357a1d82a8e2a5ed"

with open('filtered-pool-list.json') as file:
    data = json.load(file)

random.seed(SEED)
# Number of pools needs to be <= 2080 in order to fit within Python's Mersenne Twister implemetation's period
random.shuffle(data)

with open('randomize-pool-list.json', 'w') as file:
    json.dump(data, file, indent=2)
