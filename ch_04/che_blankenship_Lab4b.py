base_size = 10

# Number of rows.
for i in range(base_size, -1, -1):
    row = ""
    # Number of stars.
    # j it's unnecessary. better replacing with "_".
    # for _ in range(i):
    for j in range(i):
        row = row + "*"

    print(row)
