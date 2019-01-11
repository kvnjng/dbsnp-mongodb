#!/bin/sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr1.json.gz
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr2.json.gz