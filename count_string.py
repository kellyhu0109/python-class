import sys
q = sys.stdin.read()

# q = '''7
# Hi!
# Hello World!!
# The Little Prince
# Bigtable timestamps are integers.
# This is a sample file.
# Each cell in a Bigtable can contain multiple versions of the same data; these versions are indexed by timestamp.
# It stood on a hill overlooking the village, some of its windows boarded, tiles missing from its roof, and ivy spreaDitng unchecked over its face.'''

q_list = q.splitlines()
num = q_list[0]

for x in range(1, len(q_list)):
    split_list = q_list[x].split(' ')
    print(len(split_list))
