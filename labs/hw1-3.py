<<<<<<< Updated upstream
#1 simulation
#2 calculate

#how do we know they are next to each other
#check every year, use zero and non zero value
=======
def read_simulation_input(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    file.close()
    grid_size, num_civilizations = map(int, lines[0].split())
    birthplaces = [tuple(map(int, line.split())) for line in lines[1:num_civilizations + 1]]
    return grid_size, num_civilizations, birthplaces


def write_simulation_output(output_file, years_to_connect):
    file = open(output_file, 'w')
    file.write(str(years_to_connect) + '\n')
    file.close()


def find_root(roots, x):
    if roots[x] == x:
        return x
    else:
        roots[x] = find_root(roots, roots[x])
        return roots[x]


def union_roots(roots, ranks, x, y):
    root_x = find_root(roots, x)
    root_y = find_root(roots, y)

    if root_x != root_y:
        if ranks[root_x] > ranks[root_y]:
            roots[root_y] = root_x
        elif ranks[root_x] < ranks[root_y]:
            roots[root_x] = root_y
        else:
            roots[root_y] = root_x
            ranks[root_x] += 1


def calculate_years_to_connect(civ1, civ2):
    dx = abs(civ1[0] - civ2[0])
    dy = abs(civ1[1] - civ2[1])
    return (dx + dy + 1) // 2


def simulate_civilization_growth(grid_size, num_civilizations, birthplaces):
    if num_civilizations == 1:
        return 0

    edges = []
    for i in range(num_civilizations):
        for j in range(i + 1, num_civilizations):
            years = calculate_years_to_connect(birthplaces[i], birthplaces[j])
            edges.append((years, i, j))

    edges.sort()

    roots = list(range(num_civilizations))
    ranks = [0] * num_civilizations

    max_years = 0
    remaining_components = num_civilizations

    for years, u, v in edges:
        if find_root(roots, u) != find_root(roots, v):
            union_roots(roots, ranks, u, v)
            remaining_components -= 1
            max_years = max(max_years, years)
            if remaining_components == 1:
                break

    return max_years


input_file = '1-3input.txt'
output_file = '1-3output.txt'
grid_size, num_civilizations, birthplaces = read_simulation_input(input_file)
years_to_connect = simulate_civilization_growth(grid_size, num_civilizations, birthplaces)
write_simulation_output(output_file, years_to_connect)

print(f"Years to connect all civilizations: {years_to_connect}")
>>>>>>> Stashed changes
