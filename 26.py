#  26. Merge Intervals
# 15:49
# Write a function solve that merges overlapping intervals and returns the merged list. Intervals are represented as lists of two integers: start and end.

def solve(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged

# This function first checks if the list of intervals is empty, and if it is, it returns an empty list.
# It then sorts the intervals based on the first element of each interval.
# It then iterates through the rest of the intervals, and compares the current interval with the last interval in the merged list.
# If the current interval overlaps with the last interval, the last interval is updated to include the current interval.
# If the current interval does not overlap with the last interval, the current interval is added to the merged list.

# This challenge was easy to understand, but difficult to implement nicely