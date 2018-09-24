# Metricscleaner User Guide

The metrics database can grow to large size as rows are collected for cluster nodes for many metrics each minute. It is useful to truncate the content to a set age limit (default is 7 days).

This tool supports this truncating. It uses Cloudant map-reduce views and replication to achieve this.

The metricscleaner is run from the command line, once configured.

It can be run any number of times.

The sequence of cleaning is :  

* if daily_stats view not present in metrics database, add it. For a large database, this stage can take some time, and will increase cpu usage on the cluster. It will need to happen only once.
* if metrics_tmp database does not exist, create it with defined permissions. It will need to happen only once.
* extract documents, including views, from metrics database into metrics_tmp up to age limit
* drop the metrics db and recreate it with defined permissions
* replicate metrics_tmp content to metrics db

The tool creates a replication labelled 'metricscleaner' and a datetimestamp. Only once this replication is complete, is the cleaning/shrinking completed.


##	Running the metricscleaner 

As `root` on the server you have installed and configured the tool (usually a load-balancer), go to `opt/metricscleaner` and type  
`$ python metricsshrinker.py`

The tool provides a commentary of its activity.  
The tool script finishes once the replication is submitted.  
The task is complete once the replication is completed (check the Cloudant dashboard tool -> completed replications).