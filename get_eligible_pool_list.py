import json

# Load the JSON file
with open('all-pool-list.json') as file:
    data = json.load(file)

# Define the conditions for pool removal
def should_remove(pool):
    stake = int(pool['stake'])
    tax_fix = int(pool['tax_fix'])
    pledge = int(pool['pledge'])
    tax_ratio = float(pool['tax_ratio'])
    blocks_lifetime = int(pool['blocks_lifetime'])

    if 200_000_000_000 <= stake <= 5_000_000_000_000 and \
       tax_fix <= 340_000_000 and \
       pledge >= 20_000_000_000 and \
       tax_ratio <= 3 and \
       blocks_lifetime >= 1:
        return False

    return True

# Filter the pools based on the conditions
filtered_pools = [pool for pool in data if not should_remove(pool)]

# Save the filtered pools to a new JSON file
with open('filtered-pool-list.json', 'w') as file:
    json.dump(filtered_pools, file, indent=2)

# Save the ineligible pools to a separate JSON file
unfiltered_pools = [pool for pool in data if should_remove(pool)]
with open('unfiltered-pool-list.json', 'w') as file:
    json.dump(unfiltered_pools, file, indent=2)

print("Filtered pools saved to filtered-pool-list.json.")
print("Ineligible pools saved to unfiltered-pool-list.json.")
