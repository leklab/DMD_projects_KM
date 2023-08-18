# open file

import sys
inFile=open(sys.argv[1],'rt')
outFile=open(sys.argv[2],'wt')

sp=33357446
#reference sequence

reference="TGCAAAACAGCATCTTTCTCCTGATTCTGTCATCTTCCTGAAAGCATTCTATTACTGCCGACTGCTGGGAACCAGAAAGTCTATTTGAATTCCAACAGCTCCCCTTTCGCATGATTCAAGTTAGGTTAGGTGGGCATGCCTA"


#write a header

outFile.write("chr"+'\t'+"pos"+'\t'+"A"+'\t'+"C"+'\t'+"G"+'\t'+"T"+'\t'+"transition"+'\t'+"transversion"+'\n')

# read the file

SITES= [line.rstrip('\n') for line in inFile]

for i in range(1,len(SITES)):
    NT=SITES[i].split("\t")
    if reference[i-1]=="A":
        NTA=0
        NTC=NT[3]
        NTG=NT[4]
        NTT=NT[5]
        transition=NTG
        transversion=int(NTC)+int(NTT)
    if reference[i-1]=="C":
        NTA=NT[2]
        NTC=0
        NTG=NT[4]
        NTT=NT[5]
        transition=NTT
        transversion=int(NTG)+int(NTA)
    if reference[i-1]=="G":
        NTA=NT[2]
        NTC=NT[3]
        NTG=0
        NTT=NT[5]
        transition=NTA
        transversion=int(NTC)+int(NTT)
    if reference[i-1]=="T":
        NTA=NT[2]
        NTC=NT[3]
        NTG=NT[4]
        NTT=0
        transition=NTC
        transversion=int(NTA)+int(NTG)

    outFile.write("X"+'\t'+str(i+sp)+'\t'+str(NTA)+'\t'+str(NTC)+'\t'+str(NTG)+'\t'+str(NTT)+'\t'+str(transition)+'\t'+str(transversion)+'\n')

inFile.close()
outFile.close()
