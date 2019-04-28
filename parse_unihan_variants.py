# This script attempts to parse Unihan_Variants.txt to extract known characters
# that are specific to Simplified Chinese.
# Unfortunately, it has false positives.  example:
# 猪 内

# data file is from http://www.unicode.org/Public/UNIDATA/Unihan.zip
# original webpage  http://unicode.org/charts/unihan.html

filepath = "Unihan/Unihan_Variants.txt"

def get_char(code_point):
    if not code_point.startswith("U+"):
        print("weird code_point: >>>{:s}<<<".format(code_point))
        exit(1)
    hex_str = "0x" + code_point[2:]
    hex_int = int(hex_str, 16)
    return chr(hex_int)

count = 0
tw_set = set()
cn_set = set()
with open(filepath, "r") as f:
    for line in f:
        if (line.startswith("#") or line.strip() == ""):
            continue
        splits = line.split()
        if (splits[1] == "kZVariant" or splits[1] == "kSemanticVariant"):
            continue
        if (splits[1] == "kTraditionalVariant"):
            tw_set.add(get_char(splits[2]))
            cn_set.add(get_char(splits[0]))
            continue
        if (splits[1] == "kSimplifiedVariant"):
            tw_set.add(get_char(splits[0]))
            cn_set.add(get_char(splits[2]))
            continue
        # count += 1
        # if count > 100:
        #     break

cn_set.difference_update(tw_set)

print("tw_set: {:s}".format(",".join(e for e in tw_set)))
print("cn_set: {:s}".format(",".join(e for e in cn_set)))

