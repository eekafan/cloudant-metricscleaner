#!/bin/bash
now=`date +%Y%m%d%H%M`
cp -r /opt/cloudant-metricscleaner /opt/cloudant-metricscleaner-bkp-$now
cp ../cloudant-metricscleaner/*.py /opt/cloudant-metricscleaner