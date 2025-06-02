import logging

def print_state(state):
    print(f"Current state: {state}")

def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        logging.info(f"Move disk 1 from {source} to {target}")
        print_state(state)
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        disk = state[source].pop()
        state[target].append(disk)
        logging.info(f"Move disk {n} from {source} to {target}")
        print_state(state)
        hanoi(n - 1, auxiliary, target, source, state)

def main():
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            raise ValueError("The number of disks must be a positive integer.")
    except ValueError as e:
        print(f"\033[91m Invalid input: {e} \033[0m Please enter a valid data.")
        return

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    state = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }

    print(f"Initial state: {state}")
    hanoi(n, "A", "C", "B", state)
    print(f"Final state: {state}")
    print("All disks have been moved successfully!")

if __name__ == "__main__":
    main()
