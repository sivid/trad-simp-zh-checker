# This script attempts to obtain phrases used exclusively in Simplified
# Chinese, by eliminating a phrase when it's the same in Traditional Chinese.
# Unfortunately, it has false positives.  example:
# 趟

# data file downloaded from http://cc-cedict.org/wiki/


cedict_file = "cedict_ts.u8"

count = 0
content = []
with open(cedict_file, "r") as f:
    for line in f:
        if (line.startswith("#")):
            continue
        splits = line.split()
        tw_phrase = splits[0]
        cn_phrase = splits[1]
        if (tw_phrase == cn_phrase):
            # print("skipping {:s} {:s}".format(tw_phrase, cn_phrase))
            continue
        content.append([tw_phrase, cn_phrase])
        count += 1
        if count > 100:
            break

content.sort(key=lambda ele: len(ele[1]))

line_count = 0
for pair in content:
    print("{:d}\t{:s}".format(line_count, pair[1]))
    line_count += 1