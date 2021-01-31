# NELA-GT-2020

This repository contains usage examples for the NELA-GT-2020 data set with Python 3.

__Download the dataset here__:

__For more details about this dataset, check the paper__:


If you use this dataset in your work, please cite us as follows: <br>
```
@misc{
    gruppi2020nelagt2020,
    title={NELA-GT-2020: A Large Multi-Labelled News Dataset for The Study of Misinformation in News Articles},
    author={Maurício Gruppi and Benjamin D. Horne and Sibel Adalı},
    year={2021},
    eprint={---},
    archivePrefix={arXiv},
    primaryClass={cs.CY}
}
```
## Data

Metadata||
---|---
Dataset name|`NELA-GT-2020`
Formats|`Sqlite3`,`JSON`
No. of articles|`1731634`
No. of sources|`519`
Collection period|`2020-01-01` to `2021-01-01`

### Tables

#### Table: Newsdata

Each data point collected corresponds to an article and contains the fields described below.

|Field | Type | Description|
---|---|---
`id` | string | ID of the article.
`date` | string | date of publication (`YYYY-MM-DD`).
`source` | string | name of the source.
`title` | string | article's headline.
`content` | string | article's body text.
`author` | string | author who signed the article.
`published` | string | date time string as provided by source.
`published_utc` | integer | unix timestamp of publication.
`collection_utc` | integer | unix timestamp of collection date.
`url` | string  | url of the paper.


#### Table: Tweet

Each entry corresponds to an embedded tweet observed in the article with id `article_id`.

|Field| Type| Description|
---|---|---
`id` | string | ID of the embedded tweet.
`article_id` | string | ID of the article that contains the embedded tweet.
`embedded_tweet` | string | Raw HTML of the embedded tweet.

### Aggregated labels

We provide aggregated labels based on Media Bias/Fact Check reports, classifying each source as:

* _Reliable_ - class 0
* _Mixed_ - class 1
* _Unreliable_ - class 2

These labels can be found in `labels.csv`

__Note__: the labels used in this aggregation were collected from Media Bias/Fact Check on Mar 20, 2020.


## Examples
###  load-sqlite3.py

* How to load the data from the Sqlite3 database using SQL queries.
  + Loading data from single or multiple sources from the database
  + Loading data from the database into a Pandas dataframe

Usage:
```
python3 load-sqlite3.py <path-to-database>
```

###  load-json.py

* How to load NELA in JSON format with Python 3.
  + Loading a single source's JSON
  + Loading a directory of NELA JSON files - **WARNING**: this consumes a lot of memory

Usage:
```
python3 load-json.py <path-to-file>
```
