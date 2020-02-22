import sys

# cube = open("cubecheck.txt")
# cubecompare = open("sample3.txt")
cube = open(sys.argv[1])
cubecompare = open(sys.argv[2])

cubech = cube.readlines()
# print(cubech)
# print(len(cubech), end="\n")
cubecomp = cubecompare.readlines()
# print(cubecomp)
# print(len(cubecomp), end="\n")
if len(cubech) < len(cubecomp) or len(cubech) > len(cubecomp):
    print("You had one simple job, to match these files.")
    print(
        " ONE JOB. \nThe line numbers don't even compare! File 1 is {} lines while File 2 is {} lines!".format(
            len(cubech), len(cubecomp)
        )
    )
    print(" WHAT'S WRONG WITH YOU!?\n")
else:
    print("Thank God you can atleast match the file line numbers. Oh my god.\n")
i = 0
j = 0
while i < len(cubech) and j < len(cubecomp):
    if cubech[i] == cubecomp[j]:
        print("Line {} is compares!".format(i + 1))

    else:
        print(
            "Line {} doesn't compare: {} vs {}, you doodoohead.".format(
                i + 1, cubech[i], cubecomp[j]
            )
        )
        print(
            "Furthermore, File 1's Line {}'s length is {} while File 2's line length is {}. No words man. NO WORDS.".format(
                i, len(cubech[i]), (cubecomp[j])
            )
        )
    i += 1
    j += 1
