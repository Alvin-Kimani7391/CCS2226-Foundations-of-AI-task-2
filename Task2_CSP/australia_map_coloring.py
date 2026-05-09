# australia_map_coloring.py

# Regions of Australia
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Available colours
colors = ['Red', 'Green', 'Blue']

# Adjacency relationships
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Store assigned colours
solution = {}

# Check if colour assignment is valid
def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def solve(region_index=0):
    if region_index == len(regions):
        return True

    region = regions[region_index]

    for color in colors:
        if is_valid(region, color):
            solution[region] = color

            if solve(region_index + 1):
                return True

            del solution[region]

    return False

# Solve CSP
if solve():
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(region, "->", color)
else:
    print("No solution found.")