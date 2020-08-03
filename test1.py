# Downroad
/BiO/Install/sratoolkit.2.9.6-ubuntu64/bin/fastq-dump --gzip --split-3 SRR1002940
# 40000 cut
head -n 40000 SRR1533627_1.fastq > SRR1533627_1.temp.fastq
# QC
/BiO/Install/FastQC_0.10.1/fastqc -t 4 --nogroup SRR1002940.r1.temp.fastq
# Trimmomatic 
java -jar /BiO/Install/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads 4 -phred33  SRR1002940.r1.temp.fq SRR1002940.r2.temp.fq SRR1002940.r1.trim.fq SRR1002940.r1.unpair.fq SRR1002940.r2.trim.fq SRR1002940.r2.unpair.fq ILLUMINACLIP:/BiO/Install/Trimmomatic-0.38/adapters/TruSeq3-PE-2.fa:2:151:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
# QC
/BiO/Install/FastQC_0.10.1/fastqc -t 4 --nogroup SRR1533627_1.trim.fq
# Map
bwa mem -t 4 -R ‘@RG\tPL:Illumina\tID:Song\tSM:SRR1002940\tLB:HiSeq’ /BiO/Education/WGS/REF/hg19.fa SRR1002940.r1.trim.fq SRR1002940.r2.trim.fq > SRR1002940.sam















