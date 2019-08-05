from source_items import Source,load_sources_list,find_distance
from match_items import load_matches_dict, names_19704
import os
import itertools

obsids = open("obsids.txt", "r")

# Step 1: Load sources
sources = os.listdir("sources/")
source_data = {}
for filename in sources:
    source_data[filename[0:5]] = load_sources_list("sources/" + filename)

# Step 2: Load matches
matches = os.listdir("matches/")
match_data = {}
for filename in matches:
    match_data[filename[0:5]] = load_matches_dict("matches/" + filename)

# Step 3: Add source names to all the sources
# Step 4: Make a dictionary for a given obsid that calculates the distances between all of the sources
distances_dict = {}
for obsid in obsids:
    obsid_sources = source_data[obsid]
    obsid_matches = match_data[obsid]
    source_pairs = list(itertools.combinations(obsid_sources, 2))
    distances = {}

    for source in obsid_sources:
        source.sourcematch(obsid_matches[source.get_row()])

    for pair in source_pairs:
        source1 = pair[0]
        source2 = pair[1]
        distances[(source1.get_match(), source2.get_match())] = find_distance(source1, source2)

    distances_dict[obsid] = distances
