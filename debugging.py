def total_steps(steps):
    return sum(steps)


def average_steps(steps):
    return sum(steps) // len(steps)


def max_steps(steps):
    return max(steps)


def min_steps(steps):
    return min(steps)


def goal_met(steps):
    return [step >= 10000 for step in steps]


# Programa principal
user_input = input()
steps = list(map(int, user_input.split()))

print(f"Total steps: {total_steps(steps)}")
print(f"Average daily steps: {average_steps(steps)}")
print(f"Highest steps in a day: {max_steps(steps)}")
print(f"Lowest steps in a day: {min_steps(steps)}")
print(f"Goal met each day: {goal_met(steps)}")