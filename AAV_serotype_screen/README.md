

module load FASTX-Toolkit/0.0.14-GCCcore-10.2.0

cat aavcapsids_R1_001.fastq | /ycga-gpfs/apps/hpc/software/FASTX-Toolkit/0.0.14-GCCcore-10.2.0/bin/fastx_barcode_splitter.pl --bcfile barcode --bol --mismatches 1 --prefix R1.1X.  --suffix .fastq

grep TGCCTGACAATG R1.1X.mouse3liver.fastq | wc -l
grep GACACTATCCTA R1.1X.mouse3liver.fastq | wc -l
grep GCGATAGCGTCT R1.1X.mouse3liver.fastq | wc -l
grep TGACGTACTCAC R1.1X.mouse3liver.fastq | wc -l
grep GCTTCGCACGAG R1.1X.mouse3liver.fastq | wc -l
grep TCGGACACAACT R1.1X.mouse3liver.fastq | wc -l
grep ACAATCCTATCG R1.1X.mouse3liver.fastq | wc -l
grep CACCTAACTATC R1.1X.mouse3liver.fastq | wc -l
grep TCACACTACGCT R1.1X.mouse3liver.fastq | wc -l

**Do the same for other R1.1X.*.fastq files**
