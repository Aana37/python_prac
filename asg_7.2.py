# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
avrg=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    ext=line[21:]
    tot=tot+float(ext)
avrg=float(tot/count)
print("Average spam confidence:",avrg)