# Unsupervised Temporal Sentiment Clustering of Skilling-J Email Data Set

## Abstract

In this notebook I explore the assigned Skilling-J email dataset. Findings include two sets of anomalies likely the result of software error, as well as several statistically and semantically distinct groupings. These findings culminate in the partitioning of the `./data/skilling-j/inbox/` directory into two distict clusters defined by the directional trend of sentiment over time. Interestingly, the temporal boundary between the upward-trending sentimental cluster-series and the subsequent downward-trending cluster-series appears to coincide within three days of when former Enron CEO Jeffrey Skilling would have given his two-week notice.

## Background & Initial Observations

Based on file contents, the `./data/skilling-j` dataset appears to be the contents of former Enron CEO and convicted felon Jeffrey Skilling. Emails contain text body and metadata and are stored in several apparently meaningfully named directories. Although this project arrives at a thematically satisfying conclusion, I did not set out to prove any specific hypothesis. Rather given limited time, I chose at every conjectural juncture to pursue the exploratory branch most likely to yield interesting results relating to clustering and anomaly detection. 