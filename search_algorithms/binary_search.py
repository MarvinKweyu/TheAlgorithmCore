# assumptions: smallest item is 0

"""
Binary search
An implementation of the binary search algorithm

contributors: Marvin Kweyu (twitter: @marvinus_j)
"""


def binarySearch(array_to_search: list = [], search_item: int = 0) -> int:
    """
    Given a sorted array, return the position of the item to be searched
    """

    high = array_to_search[-1]
    low = 0

    while low <= high:
        middle = (high + low) // 2

        if search_item == array_to_search[middle]:
            return middle

        elif array_to_search[middle] > search_item:
            high = array_to_search[middle]

        elif array_to_search[middle] < search_item:
            low = array_to_search[middle]
        # item does not exist. Return -1
        return -1


my_array = [x for x in range(10)]

search_item = 2

if __name__ == "__main__":
    print(f"Item is at index {binarySearch(my_array, search_item)}")
