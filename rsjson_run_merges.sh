#!/bin/sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 scripts/merges/rsjson_merged_merges.sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 scripts/merges/rsjson_nosnppos_merges.sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 scripts/merges/rsjson_other_merges.sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 scripts/merges/rsjson_unsupported_merges.sh