
from deepmerge import Merger

# Define a merger instance with strategies
merger = Merger(
    # Overwrite with latest non None value.
    [(dict, ["merge"])],
    # Apply each dict-based strategy.
    ["override"],
    # Overwrite values.
    ["override"]
)

dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
dict2 = {'a': 2, 'b': {'y': 25, 'z': 30}, 'c': 3}

merged_dict = merger.merge(dict1, dict2)
print(merged_dict)
