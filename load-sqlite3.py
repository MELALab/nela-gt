import argparse
import sqlite3
import pandas as pd
# This script shows an example of how to use NELA-GT-2019 with sqlite3
# For more info, see: https://github.com/mgruppi/nela-gt


# Execute a given SQL query on the database and return values
def execute_query(path, query):
    conn = sqlite3.connect(path)
    # execute query on database and retrieve them with fetchall
    results = conn.cursor().execute(query).fetchall()
    return results


# Execute query and load results into pandas dataframe
def execute_query_pandas(path, query):
    conn = sqlite3.connect(path)
    df = pd.read_sql_query(query, conn)
    return df


# Start here
def main():
    # Make input command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to NELA database file.")
    args = parser.parse_args()

    # Query 1: select all articles from a specific source
    source = "thenewyorktimes"
    query = "SELECT * FROM newsdata WHERE source='%s'" % source

    data = execute_query(args.path, query)

    print("-> Found %d articles from %s" % (len(data), source))

    # Query 2: select articles from multiple sources
    sources = ['thenewyorktimes', 'cnn', 'foxnews']
    # Note that we need to add extra quotes around each source's name
    # for the query to work properly e.g.: "'thenewyorktimes'"
    sources_str = ["'%s'" % s for s in sources]
    query = "SELECT * FROM newsdata WHERE source IN (%s)" % ",".join(sources_str)
    data = execute_query(args.path, query)

    print("-> Found %d articles from %s." % (len(data), ",".join(sources)))

    # Alternatively, one can fetch queries into a pandas dataframe:
    df = execute_query_pandas(args.path, query)

    print("-- Same results but in a Pandas dataframe.")
    print(df)

    # Query 3: fetch all embedded tweets and the respective article_ids
    query = "SELECT id, article_id, embedded_tweet FROM tweet"
    df_tweet = execute_query_pandas(args.path, query)
    print(df_tweet)
    print("-- Embedded tweets stored in Pandas dataframe.")

    print("- ALL DONE.")


if __name__ == "__main__":
    main()
