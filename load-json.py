import argparse
import json
import os

# This script shows how to load NELA-GT-2019 JSON files


# Start here
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to NELA JSON file")

    args = parser.parse_args()

    # Loading a single file
    print("- Loading file", args.path)
    with open(args.path) as fin:
        data = json.load(fin)

    # Display fields
    print("-> Loaded %d articles" % len(data))
    print("- Data fields:")
    for field in data[0]:
        print("    +", field)

    # Loading a directory of NELA JSON files
    # Uses the input directory path to search for other json files
    # WARNING: this may take up LOTS OF RAM if loading the entire data set
    # and may cause your computer to freeze

    path = os.path.dirname(args.path)
    print(" - Loading directory", path)
    decision = input("! WARNING: loading large JSON data sets may take a lot of memory and slow down/freeze your system. \
                     \nDo you wish to continue? Type 'yes' to load directory.\n")

    if decision == "yes":
        src_data = dict()
        for root, dirs, files in os.walk(path):
            for f in sorted(files):  # sort files alphabetically
                print("+ Reading", f)
                with open(os.path.join(root, f)) as fin:
                    src_data[f] = json.load(fin)

        print("- %d files read" % len(src_data))

    print("ALL DONE.")


if __name__ == "__main__":
    main()
