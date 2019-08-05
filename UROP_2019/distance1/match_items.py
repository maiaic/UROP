# Dictionary matching source numbers in 19704 to the IDs I gave them
names_19704 = {}
names = open("source_names.txt", "r")
for line in names:
    info = line.split()
    number = info[0]
    name = info[1]
    names_19704[number] = [name]
    # if len(info) == 3:
        # names_19704[number].append(info[2])

# -------------------------------------------------------------------------- #

def load_matches_dict(filename):
    """
    :Parameters:
    filename - a string of the filename containing match data

    :return:
    => dictionary assigning the pre-existing source IDs to the matches in a given file
    """
    match_data = open(filename, "r")
    matches = {}

    for line in match_data:
        items = line.split()
        source_id = names_19704[str(int(items[0]) + 1)]
        if items[7] == "Y":
            matches[str(int(items[1]) + 1)] = source_id

    return matches
