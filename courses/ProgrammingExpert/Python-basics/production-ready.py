import logging
from typing import List, Optional


def compare_lists(
    lst1: Optional[List] = None,
    lst2: Optional[List] = None
) -> int:
    """
    Return the number of unique elements common to two lists.

    Args:
        lst1: The first list. If not provided, an empty list will be used.
        lst2: The second list. If not provided, an empty list will be used.

    Returns:
        The number of unique elements that are common to `lst1` and `lst2`.

    Raises:
        TypeError: If either argument is not a list or contains unhashable
        types.
    """

    # Ensure input arguments are of correct type
    if lst1 is None:
        lst1 = []
    if lst2 is None:
        lst2 = []

    if not isinstance(lst1, list):
        raise TypeError(
            f'Expected lst1 to be a list, got {type(lst1).__name__}')
    if not isinstance(lst2, list):
        raise TypeError(
            f'Expected lst2 to be a list, got {type(lst2).__name__}')

    # Convert to sets and find intersection
    try:
        lst1_set = set(lst1)
        lst2_set = set(lst2)
    except TypeError as e:
        raise TypeError('Both lists should contain only hashable items') from e

    set_intersection = lst1_set.intersection(lst2_set)

    # Log the result
    logging.info("Lists compared. Found %d common unique elements.",
                 len(set_intersection))

    return len(set_intersection)
