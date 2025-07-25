import numpy as np # type: ignore

def bankers_algorithm(claim, allocated, max_claim, available):
    n = len(claim)
    m = len(available)

    need = max_claim - allocated

    # Safety algorithm
    work = available.copy()
    finish = np.zeros(n, dtype=bool)
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i] <= work):
                work += allocated[i]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                break
        if not found:
            return "The Processes Are In An Unsafe State"

    # Resource allocation algorithm
    need = claim - allocated
    if all(np.sum(allocated, axis=0) + available >= np.sum(claim, axis=0)):
        return "Allocated Resources: " + ' '.join(map(str, np.sum(allocated, axis=0)))
    else:
        return "Not enough resources available"

# Example input
claim_vector = np.array([1, 2])
allocated_resources = np.array([[1, 2], [3, 4]])
max_claim_table = np.array([[5, 6], [2, 3]])
available_resources = np.array([-3, 4])

# Output
print("Expected Output:")
print("Enter . The . Total . Number . Of . Processes :.")
print("Enter . The . Total . Number . Of . Resources . To . Allocate :.")
print("Enter . The . Claim . Vector :.")
print("Enter . Allocated . Resource . Table: . 1 2 3 4 5 6")
print("Enter . The .Maximum . Claim . Table: . 2 3 4 5 6 7")

print("The . Claim . Vector: .", "->".join(map(str, claim_vector)))
print("The . Allocated . Resource . Table")
for row in allocated_resources:
    print(">".join(map(str, row)))
print("The . Maximum . Claim . Table")
for row in max_claim_table:
    print(">".join(map(str, row)))

print("Available. Resources :", "->".join(map(str, available_resources)))

# Run Banker's algorithm
result = bankers_algorithm(claim_vector, allocated_resources, max_claim_table, available_resources)
print(result)
