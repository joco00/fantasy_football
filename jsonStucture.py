def pullStructure(data):
    """
    :description: obtains the structure of the json data
    :params:
        data -> dict

    :return: dict

    :example:
        input -> {'p1' [1,2,3], 'p2': {'q1' : 1, 'q2': []}, 'p3': 1}
        output -> {'p1': [], 'p2': {'q1' : 1, 'q2': []}, 'p3': 1}


    :notes:
        dictionaries are not changed but lists are reduced to a single entry
    """

    def helper(i):
        if type(i) == dict:
            return pullStructure(i)
        elif type(i) == list and len(i) > 0:
            if type(i[0]) == dict:
                return [pullStructure(i[0])]
            return []

        return i

    return {k: helper(i) for k, i in data.items()}


if __name__ == "__main__":
    test1 = {"p1": [1, 2, 3], "p2": {"q1": 1, "q2": []}, "p3": 1}
    print(pullStructure(test1))

    test2 = {
        "p1": [1, 2, 3],
        "p2": [
            {"q1": 1, "q2": []},
            {"q1": 1, "q2": []},
            {"q1": 1, "q2": []},
            {"q1": 1, "q2": []},
        ],
        "p3": 1,
    }
    print(pullStructure(test2))

    import json

    with open("mBoxscore.json", "r") as f:
        data = pullStructure(json.load(f))

    with open(f"test.json", "w") as f:
        f.write(json.dumps(data))
