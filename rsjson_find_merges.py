import sys
import json
import gzip
import os
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
import time
start_time = time.time()  # measure script's run time


# find merged rs numbers
def getRSID(primary_refsnp):
    rsid = primary_refsnp['refsnp_id']
    return rsid


# find sequence change annotations
def getMerges(primary_refsnp):
    merges = primary_refsnp['merged_into']
    return merges

# find chromosome
def getName(f_in):
    return f_in.name.split('.')[0].split('-')[1]


# write output from parsing json files
# def createRecord(rsid, merges, chromosome):
#     if len(rsid) > 0:
#         if len(rsid) > 0 and len(merges) > 0:
#             writeJSON(rsid, merges, chromosome)
#         else:
#             pass


def writeJSON(rsid, merges, name):
    record = {
        "id": rsid,
        "merged_into": merges
    }
    with open('refsnp-' + name + '_merges.json', 'a') as outfile:
        json.dump(record, outfile)
        outfile.write('\n')


def main():
    print "Start creating json file(s) with rsIDs of possible missing merges"
    filename = sys.argv[1]
    print filename
    input_dir = 'json_refsnp/'
    with gzip.open(input_dir + filename, 'rb') as f_in:
        # limit lines read per file
        # cnt = 0
        for line in f_in:
            rs_obj = json.loads(line.decode('utf-8'))
            if 'merged_snapshot_data' in rs_obj:
                # print "found one!!!", line
                rsid = getRSID(rs_obj)
                merges = getMerges(rs_obj['merged_snapshot_data'])
                name = getName(f_in)
                writeJSON(rsid, merges, name)
                # limit lines read per file
                # cnt = cnt + 1
                # if (cnt > 10):
                #     break
    print "JSON file(s) completed."

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
