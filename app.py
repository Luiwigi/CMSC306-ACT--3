import time
from collections import deque

print(' ')
print("====== Campus Search System ======")

def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    operations = 0

    while queue:
        operations += 1
        node = queue.popleft()
        if node == target:
            return True, operations
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    return False, operations


def dfs(graph, start, target):
    visited = set()
    stack = [start]
    operations = 0

    while stack:
        operations += 1
        node = stack.pop()
        if node == target:
            return True, operations
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return False, operations


def campus_system():
    students = [
        {"ID": 1, "student_id": "0424-3492", "veg": False, "review": []},
        {"ID": 2, "student_id": "0424-5324", "veg": False, "review": []},
        {"ID": 3, "student_id": "0424-7643", "veg": False, "review": []},
        {"ID": 4, "student_id": "0424-0901", "veg": False, "review": []}
    ]

    buildings_graph = {
        "Registrar": ["B.A.O", "OSAS"],
        "B.A.O": ["Registrar", "CCS DEAN's OFFICE"],
        "OSAS": ["Registrar", "Cafeteria"],
        "CCS DEAN's OFFICE": ["B.A.O", "Cafeteria"],
        "Cafeteria": ["OSAS", "CCS DEAN's OFFICE"]
    }

    while True:
        print("1. Search Student ID")
        print("2. Search Building")
        print("3. Exit")

        choose = input("Choose an Option: ")

        if choose == "1":
            print("\nSTUDENT IDs")
            print('='*30)
            for s in students:
                print(s["student_id"])

            target = input("\nEnter Student ID to search: ")

            dataset_size = len(students)
            operations = 0
            found = False

            start_time = time.time()

            for s in students:
                operations += 1
                if s["student_id"] == target:
                    found = True
                    break

            end_time = time.time()

            print("\nResult:", "Found" if found else "Not Found")
            print("Dataset Size:", dataset_size)
            print("Operations:", operations)
            print("Execution Time:", f"{end_time - start_time:.6f} seconds")
            print('-'*30)

        elif choose == "2":
            print("\nList of Buildings:")
            print("="*30)
            for b in buildings_graph.keys():
                print("-", b)

            start_building = input("Enter Starting Building: ")
            target_building = input("Enter Target Building: ")
            algorithm = input("Choose Algorithm (BFS/DFS): ").upper()

            dataset_size = len(buildings_graph)

            start_time = time.time()

            if algorithm == "BFS":
                found, operations = bfs(buildings_graph, start_building, target_building)
            elif algorithm == "DFS":
                found, operations = dfs(buildings_graph, start_building, target_building)
            else:
                print("Invalid algorithm choice")
                continue

            end_time = time.time()

            print("\nResult:", "Found" if found else "Not Found")
            print("Dataset Size:", dataset_size)
            print("Operations:", operations)
            print("Execution Time:", f"{end_time - start_time:.6f} seconds")
            print('-'*30)

        elif choose == "3":
            print("DONE")
            break

        else:
            print("Invalid choice. Choose Again")


campus_system()
