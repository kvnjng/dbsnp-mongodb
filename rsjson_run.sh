#!/bin/sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 rsjson_chr_1.sh
sbatch --time=48:00:00 --mail-type=ALL,TIME_LIMIT_80 rsjson_chr_2.sh