

module load FASTX-Toolkit/0.0.14-GCCcore-10.2.0

cat C7_R1_001.fastq| /ycga-gpfs/apps/hpc/software/FASTX-Toolkit/0.0.14-GCCcore-10.2.0/bin/fastx_barcode_splitter.pl --bcfile barcode --bol --mismatches 3 --prefix R1fix.  --suffix .fastq

tar -xvzf BBMap_38.91.tar.gz

/home/km2286/scratch60/00_fastq/bbmap/repair.sh in1="R1fix.F1R1.fastq" in2="C7_R2_001.fastq" out1="R1.primers1.fastq" out2="R2.primers1.fastq" outs="primers1.fq repair"
/home/km2286/scratch60/00_fastq/bbmap/repair.sh in1="R1fix.F2R2.fastq" in2="C7_R2_001.fastq" out1="R1.primers2.fastq" out2="R2.primers2.fastq" outs="primers2.fq repair"
/home/km2286/scratch60/00_fastq/bbmap/repair.sh in1="R1fix.F3R3.fastq" in2="C7_R2_001.fastq" out1="R1.primers3.fastq" out2="R2.primers3.fastq" outs="primers3.fq repair"
/home/km2286/scratch60/00_fastq/bbmap/repair.sh in1="R1fix.F4R4.fastq" in2="C7_R2_001.fastq" out1="R1.primers4.fastq" out2="R2.primers4.fastq" outs="primers4.fq repair"

module load BWA/0.7.15-foss-2016a

bwa mem -M -t 8 -R "@RG\tID:c7\tPL:ILLUMINA\tSM:c7" /ycga-gpfs/project/ysm/lek/ml2529/reference/Homo_sapiens_assembly19.fasta R1.primers1.fastq R2.primers1.fastq >1.sam 2> 1.bwa.sterr.log
bwa mem -M -t 8 -R "@RG\tID:c7\tPL:ILLUMINA\tSM:c7" /ycga-gpfs/project/ysm/lek/ml2529/reference/Homo_sapiens_assembly19.fasta R1.primers2.fastq R2.primers2.fastq >2.sam 2> 2.bwa.sterr.log
bwa mem -M -t 8 -R "@RG\tID:c7\tPL:ILLUMINA\tSM:c7" /ycga-gpfs/project/ysm/lek/ml2529/reference/Homo_sapiens_assembly19.fasta R1.primers3.fastq R2.primers3.fastq >3.sam 2> 3.bwa.sterr.log
bwa mem -M -t 8 -R "@RG\tID:c7\tPL:ILLUMINA\tSM:c7" /ycga-gpfs/project/ysm/lek/ml2529/reference/Homo_sapiens_assembly19.fasta R1.primers4.fastq R2.primers4.fastq >4.sam 2> 4.bwa.sterr.log

module load picard/2.9.0-Java-1.8.0_121

java -Xmx14G -jar $EBROOTPICARD/picard.jar SortSam INPUT=1.sam OUTPUT=1.bam SORT_ORDER=coordinate
java -Xmx14G -jar $EBROOTPICARD/picard.jar SortSam INPUT=2.sam OUTPUT=2.bam SORT_ORDER=coordinate
java -Xmx14G -jar $EBROOTPICARD/picard.jar SortSam INPUT=3.sam OUTPUT=3.bam SORT_ORDER=coordinate
java -Xmx14G -jar $EBROOTPICARD/picard.jar SortSam INPUT=4.sam OUTPUT=4.bam SORT_ORDER=coordinate

module load SAMtools
samtools index 1.bam
samtools index 2.bam
samtools index 3.bam
samtools index 4.bam

./site_metrics -r X:33357447-33357588 -s -d 0 -q 37 1.bam>1.out1
python site_metrics_mut.py 1.out1 1.out2
./site_metrics -r X:33357447-33357588 -s -d 0 -q 37 2.bam>2.out1
python site_metrics_mut.py 2.out1 2.out2
./site_metrics -r X:33357447-33357588 -s -d 0 -q 37 3.bam>3.out1
python site_metrics_mut.py 3.out1 3.out2
./site_metrics -r X:33357447-33357588 -s -d 0 -q 37 4.bam>4.out1
python site_metrics_mut.py 4.out1 4.out2

python distribution_his.py 1.out2 1.out1 1out_his
python distribution_his.py 2.out2 2.out1 2out_his
python distribution_his.py 3.out2 3.out1 3out_his
python distribution_his.py 4.out2 4.out1 4out_his
