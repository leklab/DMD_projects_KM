# open file

import sys
inFile=open(sys.argv[1],'rt')
inFiletotal=open(sys.argv[2],'rt')
outFile=open(sys.argv[3],'wt')


outFile.write("chr"+'\t'+"pos"+'\t'+"var_freq"+'\t'+'\n')


# read the file
NUMBERStotal= [line.rstrip('\n') for line in inFiletotal]
NUMBERS= [line.rstrip('\n') for line in inFile]
for i in range(1,len(NUMBERS)):
    NUMBER=NUMBERS[i].split("\t")
    NUMBERtotal=NUMBERStotal[i].split("\t")
    ttreads=int(NUMBERtotal[2])+int(NUMBERtotal[3])+int(NUMBERtotal[4])+int(NUMBERtotal[5])
    for j in range(2,6):
        if float(NUMBER[j])/float(ttreads)!=0:
            outFile.write(NUMBER[0]+"\t"+NUMBER[1]+"\t"+str(float(NUMBER[j])/float(ttreads))+'\n')

inFile.close()
inFiletotal.close()
outFile.close()
