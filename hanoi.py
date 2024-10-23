def hanoi(n, origin, destination, auxiliary):
    if n == 1:
        print(f"Move disc 1 of {origin} to {destination}")
        return
    
    hanoi(n-1, origin, auxiliary, destination)

    print(f"Move disc {n} of {origin} to {destination}")

    hanoi(n-1, auxiliary, destination, origin)

hanoi(3, 'A', 'C', 'B')