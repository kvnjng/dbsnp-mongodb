#!/bin/bash
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr1.json.gz
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr2.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr3.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr4.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr5.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr6.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr7.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr8.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr9.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr10.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr11.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr12.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr13.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr14.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr15.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr16.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr17.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr18.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr19.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr20.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr21.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chr22.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chrX.json.gz
# sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 python rsjson_mongo_filter.py refsnp-chrY.json.gz