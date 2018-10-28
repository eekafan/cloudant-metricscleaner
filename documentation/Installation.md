# Installing the metricscleaner

The metricscleaner is most conveniently installed one of the two load balancers of a cloudant local cluster.  

This utility is a python tool run from the command tool. It can be run periodically (say weekly) using cron.

The metricscleaner is designed for use in RHEL7 or Centos7 hosted cloudant cluster environments. 
  
A new install requires several steps: 
  
* editing the metricscleaner configuration files  
* installing (python-based) metricscleaner software on a server

With a patch install, only the last step is necessary.


##	Installing the metricscleaner software

### Collecting software from Github

cloudant-metricsleaner is released via github. Use a github client to download the release level required.

The github repository is   
`https://github.com/rombachuk/cloudant-metricscleaner`

The releases option in Github shows the available releases.
Download from the site in either tar.gz or zip format, and place in a suitable directory, as `root` on the load-balancer eg `/root/software`


### 	Unpacking 
Then unpack the software with `tar xvf` or `unzip`, depending on the download format from github.

The software unpacks to the following directories :  
  
  * cloudant-metricscleaner (the software to be installed)
  * documentation (markdown files documenting the package)
  * deploy (installation & patch scripts for the package)

#### Example

Software release 27.0.2 is downloaded to server cl11c74lb1 directory  `/root/software/cloudant-metricscleaner-27.0.2.tar.gz` and unpacked with tar as  
  
  
```  
[root@cl11c74lb1 cloudant-metricscleaner-27.0.2]# pwd
/root/software/cloudant-metricscleaner-27.0.2
[root@cl11c74lb1 cloudant-metricscleaner-27.0.2]# ls -l
total 4
drwxrwxr-x 2 root root 275 Aug 29 17:44 cloudant-metricscleaner
drwxrwxr-x 2 root root  54 Aug 29 17:44 deploy
drwxrwxr-x 2 root root 280 Aug 29 17:44 documentation
-rw-rw-r-- 1 root root  83 Aug 29 17:44 README.md
```    

### Clean Install
This option is used when a brand new install is required, or when an existing install is to be deleted and reset.

Three steps are needed :  
  
* configure cluster access in cloudant-metricscleaner/metricscleaner_connection.info
* configure metrics db permissions in cloudant-metricscleaner/metrics-permissions.info
* configure agelimit to retain data after metrics db is shrunk in cloudant-metricscleaner/metricscleaner.conf
* run the deploy/clean_install.sh script


Do the installation as `root`

#### Configuration (metricscleaner_connection.info)
  
```
sourceurl      http://activesn.bkp.ibm.com  
sourceBase64    bWlk********3MHJk    
```   
* The sourceurl should be the vip of your cloudant local cluster.  
* The sourceBase64 credentials shoud be a base64encoding of the string `user:password` where the user is a cluster admin user, and the owner of the metrics db.  

#### Configuration (metrics_permissions.info)
  
```
{"admins":{"names":["middleamd"],"roles":[]},  
"members":{"names":["middleamd"],"roles":[]}}    
```    
* The owner of the metrics db is set here. Set the user by subsituting for middleamd in the template file provided.  

#### Configuration (metricscleaner.conf)
  
```
default_agelimit				7
default_connectioninfo        /opt/cloudant-metricscleaner/metricscleaner_connection.info
default_certificate_verification	False
default_requests_ca_bundle		/opt/cloudant-metricscleaner/ca.pem    
```   
* The default_agelimit in this file is the agelimit in days for retaining data in the metrics db. All other days data is dropped. The default is 7 days. The limit can only be set in this file. There is no command line override.

#### Installation

Once the configuration steps are done, go to `deploy` directory, and run `./clean_install.sh` 
  
This script will :  

* create a new installation in `/opt/cloudant-metricscleaner`
* backup any pre-existing `/opt/cloudant-metricscleaner` content to a new directory `opt/cloudant-metricscleaner-bkp-YYYYMMDDHHmm` where YYYYMMDDHHmm is the datetime of run of the install. You can delete this backup once you are happy with the running of the new installation


#### Patch Install
This option is used when an upgrade to an existing installation is required. No changes to the conf or info files are carried out, so cluster url and credentials are left as they are.

Do the installation as `root`

Go to `deploy` directory, and run `./patch_install.sh` 

This script will :  
  
* update the *.py files in `/opt/cloudant-metricscleaner`
* backup any pre-existing `/opt/cloudant-metricscleaner` content to a new directory `opt/cloudant-metricscleaner-bkp-YYYYMMDDHHmm` where YYYYMMDDHHmm is the datetime of run of the install. You can delete this backup once you are happy with the running of the new installation




