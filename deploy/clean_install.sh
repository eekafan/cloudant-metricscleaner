#!/bin/bash
now=`date +%Y%m%d%H%M`
cp -r /opt/cloudant-metricscleaner /opt/cloudant-metricscleaner-bkp-$now
rm -rf /opt/cloudant-metricscleaner
cp -r ../cloudant-metricscleaner /opt