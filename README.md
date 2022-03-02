# NELA-GT-2020

This repository contains usage examples for the NELA-GT-2020 data set with Python 3.


## Citation
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

We release our main news dataset `NELA-GT-2020` along with two subsets,
created by doing keyword searches on the main dataset. We introduce
the `NELA-GT-ELECTIONS` dataset, containing articles related to the 
2020 U.S. Presidential Elections, and the `NELA-GT-COVID19` subset,
which contains articles related to the COVID-19 pandemic.

Metadata||||
---|---|---|---
Dataset name|`NELA-GT-2020` | `NELA-GT-ELECTIONS` | `NELA-GT-COVID19`
Formats|`Sqlite3`,`JSON` | `Sqlite3`, `JSON` | `Sqlite3`, `JSON`
No. of articles|`1779127` | `294504` | `699803`
No. of sources|`519` | `403` | `493`
No. of embedded tweets|`410784` | `107771` | `158855`
Collection period|`2020-01-01` to `2020-12-31` | `2020-01-01` to `2020-12-31` | `2020-01-01` to `2020-12-31`


### Download

- __News Data__
  - __Full dataset__ 
  [Sqlite3](https://dataverse.harvard.edu/file.xhtml?fileId=4417500&version=2.0)
  | [JSON](https://dataverse.harvard.edu/file.xhtml?fileId=4417502&version=2.0)
  - __COVID-19 subset__
  [Sqlite3](https://dataverse.harvard.edu/file.xhtml?fileId=4417498&version=2.0)
  | [JSON](https://dataverse.harvard.edu/file.xhtml?fileId=4417503&version=2.0)
  - __U.S. elections subset__
  [Sqlite3](https://dataverse.harvard.edu/file.xhtml?fileId=4417499&version=2.0)
  | [JSON](https://dataverse.harvard.edu/file.xhtml?fileId=4417504&version=2.0)

- __Source Labels__: [CSV](https://dataverse.harvard.edu/file.xhtml?fileId=4366864&version=2.0)
  - This file contains the credibility label for news sources in the dataset (reliable, unreliable, mixed).

For more details about this dataset, see the [paper](https://arxiv.org/pdf/2102.04567.pdf). 


### Limitations

Since the articles collected from news sources may be copyrighted, 
we apply a transformation to the original text so that it cannot be 
used for their originally intended purpose, i.e., that of being
read by individuals to consume journalistic information. 

We modify the text so that it cannot properly be used for news
consumption but that can still be used for text analysis via
 a [transformation](https://www.corpusdata.org/limitations.asp).

For articles with more than 200 tokens, we replace 7 tokens with `@` 
every 100 tokens. For articles with fewer than 200 tokens, we replace 5 
consecutive tokens with `@` every 20 tokens.
This transforms the articles so that it is unlikely that a user will
read NELA-GT to consume news while still keeping most of the content
that is useful for analysis (~7% for larger articles).


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
`embedded_tweet` | string | ID/URL of the embedded tweet.

### Aggregated labels

We provide aggregated labels based on Media Bias/Fact Check reports, classifying each source as:

* _Reliable_ - class 0
* _Unreliable_ - class 1
* _Mixed_ - class 2


These labels can be found in `labels.csv`

__Note__: the labels used in this aggregation were collected from Media Bias/Fact Check on Mar 20, 2020.


## Examples

Please refer to these examples for details on how to use our dataset 
using Python3 and Pandas.

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
