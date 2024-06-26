def count_infected_computers(n, edges, initial):
    nearby_list = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        nearby_list[edge[0]].append(edge[1])
        nearby_list[edge[1]].append(edge[0])

    visited = set()

    def dfs(computer):
        if computer in visited:
            return 0
        visited.add(computer)
        infected_count = 1  # Count this computer as infected
        for neighbor in nearby_list[computer]:
            infected_count += dfs(neighbor)
        return infected_count

    total_infected = dfs(initial) - 1
    return total_infected


def read_input(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    file.close()
    n = int(lines[0].strip())
    m = int(lines[1].strip())
    edges = [tuple(map(int, line.strip().split())) for line in lines[2:2 + m]]
    initial = int(lines[2 + m].strip())
    return n, edges, initial


def write_output(output_file, result):
    file = open(output_file, 'w')
    file.write(str(result) + '\n')
    file.close()


input_file = '1-2input.txt'
output_file = '1-2output.txt'
n, edges, initial = read_input(input_file)
result = count_infected_computers(n, edges, initial)
write_output(output_file, result)

print(f"There are {result} infected computers")
