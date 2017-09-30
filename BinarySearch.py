# This is a Python script that performs a binary search on a list
# @TODO: Let it take in a random list
# @TODO: Give more elegant solution that prevents walking off list

# List: [0, 2, 24, 28, 32, 95, 100]

sorted_list = [0, 2, 24, 28, 32, 95, 100, 200, 1809]
target = 1000


def solution(sorted_list, target):
    """
    :param sorted_list: The list we're performing the search on
    :param target: The element we are trying to find
    :return: None
    """
    left = 0
    right = (len(sorted_list) - 1)
    binarySearch(sorted_list, left, right, target)


def binarySearch(sorted_list, left, right, target):
    """
    :param sorted_list: The list we're performing the search on
    :param left: The left index of the current chunk
    :param right: The right index of the current chunk
    :param target: The element we are trying to find
    :return: None
    """
    mid = int(((left + right) / 2))
    print("mid: %s" % (mid))
    print("array: %s" % (sorted_list[left:(right+1)]))
    if sorted_list[mid] == target:
        print("%s found at index %s" % (target, mid))
    elif ((mid == 0) or ( mid == len(sorted_list) - 1))\
            and target != sorted_list[mid]:
        print("%s not found in list" % (target))
    elif target < sorted_list[mid]:
        new_right = (mid - 1)
        binarySearch(sorted_list, left, new_right, target)
    elif target > sorted_list[mid]:
        new_left = (mid + 1)
        binarySearch(sorted_list, new_left, right, target)


if __name__ == "__main__":
    solution(sorted_list, target)
