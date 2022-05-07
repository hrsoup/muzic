import os
from mido import MidiFile
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict

rootdir = './data_midi'
l = []
n = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fPath = os.path.join(subdir, file)
        mid = MidiFile(fPath)
        if mid.length < 10:
            print(fPath)
            os.remove(fPath)
            n += 1
        else:
            l.append(mid.length)

print("%i files have midi length less than 10" % (n))

sns.set()
sns.displot(l, color='#99CCFF')
plt.show()
