# 25. Climbing Stairs

# Write a function solve that calculates how many distinct ways you can climb a staircase of n steps, taking 1 or 2 steps at a time.

def solve(n):
    if n == 0:
      return 1
    if n < 0:
      return 0

    return solve(n - 1) + solve(n - 2)

# This function recursively walks up the stairs, constantly detecting if the step it took is valid.
# If it is, it will return 1, and if it isn't, it will return 0.
# It will then add all valid results together to get the total possible number of ways to climb the stairs.

# There is likely a better way to do this based on the reccurence relation, but I'm not sure what that would look like.