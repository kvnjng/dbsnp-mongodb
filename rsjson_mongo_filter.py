import json
import gzip
import os
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
import time
start_time = time.time()  # measure script's run time


# find merged rs numbers
def getRSIDs(primary_refsnp):
    rsids = []
    # append rsid reference
    rsids.append(primary_refsnp['refsnp_id'])
    # append rsid merges
    for i in primary_refsnp['dbsnp1_merges']:
        rsids.append(i['merged_rsid'])
    return rsids


# find chromosome
def getChromosome(f_in):
    return f_in.name.split('.')[0].split('-')[1][3:]


# find GRCh37 genomic position
def getPosition(primary_refsnp):
    position = ''
    for i in primary_refsnp['primary_snapshot_data']['placements_with_allele']:
        if len(i['placement_annot']['seq_id_traits_by_assembly']) > 0:
            assembly = i['placement_annot']['seq_id_traits_by_assembly'][0]['assembly_name']
            is_chrom = i['placement_annot']['seq_id_traits_by_assembly'][0]['is_chromosome']
            pos = i['alleles'][0]['allele']['spdi']['position']
            # only choose bp from GRCh37.p13
            if is_chrom == True and assembly == "GRCh37.p13":
                position = str(pos)
    return position


# find sequence change annotations
def getAnnotations(primary_refsnp):
    annotations = []
    for i in primary_refsnp['allele_annotations']:
        try:
            a = i['assembly_annotation'][0]['genes'][0]['rnas'][0]['protein']['sequence_ontology'][0]['name']
            # clean up text by trimming off '_variant'
            annotations.append(a.replace('_variant', ''))
        except:
            continue
    return list(set(annotations))


# find variant type
def getVariantType(primary_refsnp):
    variant_type = 'NA'
    try:
        variant_type = primary_refsnp['primary_snapshot_data']['variant_type']
    except:
        pass
    return variant_type


# write output from parsing json files
def createRecord(rsids, chromosome, position, annotations, variant_type):
    if len(rsids) > 0:
        for rsid in rsids:
            if len(rsid) > 0 and len(chromosome) > 0 and len(position) > 0 and len(annotations) > 0 and len(variant_type) > 0:
                writeJSON(rsid, chromosome, position, ','.join(annotations), variant_type)
                # insertMongoDB(rsid, chromosome, position, ','.join(annotations), variant_type)
            elif len(rsid) > 0 and len(chromosome) > 0 and len(position) > 0 and len(annotations) == 0 and len(variant_type) > 0:
                # if no annotations, insert NA
                writeJSON(rsid, chromosome, position, 'NA', variant_type)
                # insertMongoDB(rsid, chromosome, position, 'NA', variant_type)
            else:
                pass

def writeJSON(rsid, chromosome, position, annotations, variant_type):
    record = {
        "id": rsid,
        "chromosome": chromosome,
        "position": position,
        "function": annotations,
        "type": variant_type
    }
    with open('chr_' + chromosome + '_filtered.json', 'a') as outfile:
        json.dump(record, outfile)
        outfile.write('\n')


# def insertMongoDB(rsid, chromosome, position, annotations, variant_type):
#     client = MongoClient('localhost', 27017)
#     db = client["LDLink"]
#     record = {
#         "id": rsid,
#         "chromosome": chromosome,
#         "position": position,
#         "function": annotations,
#         "type": variant_type
#     }
#     dbsnp = db.dbsnp151
#     dbsnp.insert_one(record).inserted_id

# def createIndexes():
#     client = MongoClient('localhost', 27017)
#     db = client["LDLink"]
#     print "Drop indexes on ID and Genomic Coordinates if exist."
#     try:
#         db.dbsnp151.drop_index( "id_1" )
#         db.dbsnp151.drop_index( "chromosome_1_position_1" )
#     except:
#         pass
#     print "Indexes dropped."
#     print "Create index on RSID."
#     db.dbsnp151.create_index('id')
#     print "RSID indexing completed."
#     print "Create index on genomic coordinates"
#     db.dbsnp151.create_index([("chromosome", ASCENDING), ("position", ASCENDING)])
#     print "Genomic coordinates indexing completed."


def main():
    print "Start creating json file(s) with filtered records. db: LDLink, collection: dbsnp151"
    # iterate through each file in directory
    input_dir = 'json_refsnp/'
    for filename in os.listdir(input_dir):
        if "refsnp" in filename:
            print filename
            with gzip.open(input_dir + filename, 'rb') as f_in:
                # limit lines read per file
                # cnt = 0
                for line in f_in:
                    # try:
                    rs_obj = json.loads(line.decode('utf-8'))
                    # last_line = json.dumps(rs_obj)
                    if 'primary_snapshot_data' in rs_obj:
                        rsids = getRSIDs(rs_obj)
                        # print rsids
                        chromosome = getChromosome(f_in)
                        position = getPosition(rs_obj)
                        annotations = getAnnotations(rs_obj['primary_snapshot_data'])
                        variant_type = getVariantType(rs_obj)
                        # create and insert row into sqlite database
                        createRecord(rsids, chromosome, position, annotations, variant_type)
                        # limit lines read per file
                        # cnt = cnt + 1
                        # if (cnt > 50000):
                        #     break
    print "JSON file(s) completed."

    # print "Start indexing MongoDB."
    # createIndexes()
    # print "Indexing completed."


    # print script's run time when finshed
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
