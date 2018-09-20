import datetime
import string
import sys
import base64
import os
import re
from optparse import OptionParser

def process_defaults_config(cfile):
    default_agelimit = 7
    default_connectioninfo = '/opt/cloudant-metricscleaner/metricscleaner_connection.info'
    default_certificate_verification = False
    default_requests_ca_bundle = '/opt/cloudant-metricscleaner/ca.pem'
    default_inputlogfile = '/var/log/haproxy.log'

    if cfile and os.path.isfile(cfile):
      cf = open(cfile,'r')
      cflines = cf.readlines()
      for cfline in cflines:
          cflineparts = cfline.split()
          if len(cflineparts) == 2 and cflineparts[0] == 'default_connectioninfo':
             default_connectioninfo = cflineparts[1] 
          elif len(cflineparts) == 2 and cflineparts[0] == 'default_agelimit':
             default_age_limit = cflineparts[1] 
          elif len(cflineparts) == 2 and cflineparts[0] == 'default_certificate_verification':
             default_certificate_verification = cflineparts[1] 
          elif len(cflineparts) == 2 and cflineparts[0] == 'default_requests_ca_bundle':
             default_requests_ca_bundle = cflineparts[1]  
          else:
 	     pass
      cf.close()
    return default_connectioninfo, default_certificate_verification,default_requests_ca_bundle


def process_connection_info(cinfo):
    source_url = None
    source_credentials = None
    source_username = None
    source_password = None
    proxy_url = None
    if cinfo and os.path.isfile(cinfo):
      cf = open(cinfo,'r')
      cflines = cf.readlines()
      for cfline in cflines:
          cflineparts = cfline.split()
          if len(cflineparts) == 2 and cflineparts[0] == 'sourceurl':
             source_url = cflineparts[1] 
          if len(cflineparts) == 2 and cflineparts[0] == 'sourceBase64':
             source_credentials = cflineparts[1] 
             src_credparts = str(base64.urlsafe_b64decode(source_credentials)).split(':')
             if len(src_credparts) == 2:
                source_username = src_credparts[0]
                source_password = src_credparts[1]
          elif len(cflineparts) == 2 and cflineparts[0] == 'proxyurl':
             proxy_url = cflineparts[1] 
          else:
 	     pass
      cf.close()
    return source_url,source_credentials,source_username,source_password,proxy_url


def options():
    parser = OptionParser()
    parser.add_option("-x",
                      "--connectioninfo",
                      help="file containing source and destination info [default none]")
    opts, args = parser.parse_args()
    return opts, args


