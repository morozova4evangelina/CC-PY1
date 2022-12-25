import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file: str, delimiter: str = ",") -> list[dict]:
    result = []
    with open(input_file) as f:
        keys = f.readline().split(delimiter)
        for line in f:
            value = line.split(delimiter)
            row = {keys[i]: value[i] for i in range(len(keys))}
            result.append(row)
    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
