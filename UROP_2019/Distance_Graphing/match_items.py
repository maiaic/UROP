# Dictionary matching source numbers in 19704 to the IDs I gave them
names_19704 = {}
with open("source_names.txt", "r") as names:
    for line in names:
        info = line.split()
        number = info[0]
        name = info[1]
        names_19704[number] = name
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
    matches = {}
    with open(filename, "r") as match_data:
        for line in match_data:
            items = line.split()
            # print(items)
            if len(items) > 1 and items[1].isdigit():
                source_id = names_19704[str(int(items[0]) + 1)]
                source_no = str(int(items[1]) + 1)

                if items[7] == "Y":
                    matches[source_no] = source_id
                else:
                    if source_no in matches.keys():
                        del matches[source_no]

    return matches
