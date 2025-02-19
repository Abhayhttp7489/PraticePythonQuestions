def merge_dicts_with_overlapping_keys(dicts):
    merged_dict = {}

    for d in dicts:
        for key, value in d.items():
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value
    return merged_dict
print(merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]))