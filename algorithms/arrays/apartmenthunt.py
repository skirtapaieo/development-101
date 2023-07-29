# Apartment Hunting Problem Solution

# Function to calculate the minimum distances to the nearest facility for each block
def getMinDistances(blocks, req):
    # Initialize minDistances with 0 if the facility is present at the block, otherwise with infinity
    minDistances = [0 if block[req] else float('inf') for block in blocks]
    
    # First pass: from left to right
    for i in range(1, len(blocks)):
        # If the facility is not present at the current block
        if minDistances[i] == float('inf'):
            # The minimum distance is one more than the minimum distance at the previous block
            minDistances[i] = minDistances[i - 1] + 1
            
    # Second pass: from right to left
    for i in reversed(range(len(blocks) - 1)):
        # The minimum distance is the minimum of the current minimum distance and
        # one more than the minimum distance at the next block
        minDistances[i] = min(minDistances[i], minDistances[i + 1] + 1)
    
    return minDistances

# Function to calculate the maximum of the minimum distances to each facility for each block
def getMaxDistances(blocks, reqs):
    # Initialize maxDistances with zeros
    maxDistances = [0] * len(blocks)
    
    # For each facility
    for req in reqs:
        # Get the minimum distances to this facility
        minDistances = getMinDistances(blocks, req)
        
        # For each block
        for i in range(len(blocks)):
            # The maximum distance is the maximum of the current maximum distance and
            # the minimum distance to the current facility
            maxDistances[i] = max(maxDistances[i], minDistances[i])
    
    return maxDistances

# Main function to solve the apartment hunting problem
def apartmentHunting(blocks, reqs):
    # Get the maximum of the minimum distances to each facility for each block
    maxDistances = getMaxDistances(blocks, reqs)
    
    # Return the index of the block with the minimum maximum distance
    return maxDistances.index(min(maxDistances))
