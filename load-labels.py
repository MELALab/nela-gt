import argparse


# Load NELA-GT-2019 ground truth label file
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to label file")

    args = parser.parse_args()

    labels = dict()
    with open(args.path) as fin:
        # Read out the header line from label file
        fin.readline()
        # Iterate over lines, taking the value from first column after name
        # i.e., aggregated label
        for line in fin:
            l = line.strip().split(",")
            source = l[0]
            if l[1] == "":  # NODATA for this entry, skip it
                continue
            labels[source] = int(l[1])  # get value from last column (label)

    print("- Read labels for %d sources" % len(labels))

    print("- Labels")

    print("source, label\n")
    for s in sorted(labels):
        print(s,labels[s])

    print("ALL DONE.")


if __name__ == "__main__":
    main()
