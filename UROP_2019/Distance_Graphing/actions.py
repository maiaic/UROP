from source_items import Source,load_sources_list,find_distance
from match_items import load_matches_dict, names_19704
import os
import itertools

with open("obsid_all.txt", "r") as obsids_file:
    obsids = [line[0:-1] for line in obsids_file if len(line) > 0]

# Step 1: Load sources
sources = os.listdir("sources/")
source_data = {}
for filename in sources:
    source_data[filename[0:-12]] = load_sources_list("sources/" + filename)

# Step 2: Load matches
matches = os.listdir("matches/")
match_data = {}
for filename in matches:
    match_data[filename[0:-10]] = load_matches_dict("matches/" + filename)

# Step 3: Add source names to all the sources
# Step 4: Make a dictionary for a given obsid that calculates the distances between all of the sources
# Step 5: Iterate thru dictionary to make a list of data points for given source source_pairs
    # dict[(A, B)] = [(obsid, (dist, err)), ... ]
def to_graph():
    to_graph = {}

    for obsid in obsids:
        if obsid in match_data.keys():
            obsid_sources = source_data[obsid]
            obsid_matches = match_data[obsid]
            source_pairs = list(itertools.combinations(obsid_sources, 2))

            for pair in source_pairs:
                source1 = pair[0]
                source2 = pair[1]

                if source1.get_row() in obsid_matches.keys() and source2.get_row() in obsid_matches.keys():
                    source1.source_match(obsid_matches[source1.get_row()])
                    id1 = source1.get_match()

                    source2.source_match(obsid_matches[source2.get_row()])
                    id2 = source2.get_match()

                    datapoint = (obsid, find_distance(source1, source2))


                    if (id1, id2) in to_graph.keys():
                        to_graph[(id1, id2)].append(datapoint)
                    elif (id2, id1) in to_graph.keys():
                        to_graph[(id2, id1)].append(datapoint)
                    else:
                        to_graph[(id1, id2)] = [datapoint]

    return to_graph

def dates_dict():
    """
    Creates a dictionary matching obsids to dates
    """
    some_files = ["obslog_acis-i.txt", "obslog_acis-s.txt"]
    dates_dict = {}

    for filename in some_files:
        with open(filename, "r") as dates_file:
            for line in dates_file:
                items = line.split()
                if len(items) > 0 and items[0].isdigit():
                    dates_dict[items[1]] = items[2][0:10]
    return dates_dict

def reverse_dates_dict():
    """
    Creates a dictionary matching dates to obsids
    """
    some_files = ["obslog_acis-i.txt", "obslog_acis-s.txt"]
    dates_dict = {}

    for filename in some_files:
        with open(filename, "r") as dates_file:
            for line in dates_file:
                items = line.split()
                if len(items) > 0 and items[0].isdigit():
                    dates_dict[items[2][0:10]] = items[1]

    return dates_dict
