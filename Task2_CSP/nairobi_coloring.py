# nairobi_coloring.py

subcounties = [
    'Westlands', 'Dagoretti North', 'Dagoretti South',
    'Langata', 'Kibra', 'Roysambu',
    'Kasarani', 'Ruaraka', 'Embakasi South',
    'Embakasi North', 'Embakasi Central',
    'Embakasi East', 'Embakasi West',
    'Makadara', 'Kamukunji',
    'Starehe', 'Mathare'
]

colors = ['Red', 'Green', 'Blue', 'Yellow']

# Simplified neighboring relationships
neighbors = {
    'Westlands': ['Dagoretti North', 'Starehe'],
    'Dagoretti North': ['Westlands', 'Dagoretti South'],
    'Dagoretti South': ['Dagoretti North', 'Langata'],
    'Langata': ['Dagoretti South', 'Kibra'],
    'Kibra': ['Langata', 'Starehe'],
    'Roysambu': ['Kasarani'],
    'Kasarani': ['Roysambu', 'Ruaraka'],
    'Ruaraka': ['Kasarani', 'Mathare'],
    'Embakasi South': ['Embakasi East'],
    'Embakasi North': ['Embakasi Central'],
    'Embakasi Central': ['Embakasi North', 'Embakasi East'],
    'Embakasi East': ['Embakasi Central', 'Embakasi South'],
    'Embakasi West': ['Makadara'],
    'Makadara': ['Embakasi West', 'Kamukunji'],
    'Kamukunji': ['Makadara', 'Starehe'],
    'Starehe': ['Westlands', 'Kamukunji', 'Kibra'],
    'Mathare': ['Ruaraka']
}

solution = {}

def is_valid(area, color):
    for neighbor in neighbors.get(area, []):
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def solve(index=0):
    if index == len(subcounties):
        return True

    area = subcounties[index]

    for color in colors:
        if is_valid(area, color):
            solution[area] = color

            if solve(index + 1):
                return True

            del solution[area]

    return False

if solve():
    print("Nairobi Map Coloring:")
    for area, color in solution.items():
        print(area, "->", color)
else:
    print("No solution found.")