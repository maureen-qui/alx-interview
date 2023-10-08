def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = set()
    # Stack for DFS
    stack = [0]  # Start with the first box (index 0)

    while stack:
        current_box = stack.pop()

        # Check if the current box is already opened
        if current_box not in opened_boxes:
            opened_boxes.add(current_box)

            # Add keys from the current box to the stack
            stack.extend(boxes[current_box])

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
