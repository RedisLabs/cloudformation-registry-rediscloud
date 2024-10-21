# Redis::CloudFormation::ProDatabase

CloudFormation template for Pro Database.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Redis::CloudFormation::ProDatabase",
    "Properties" : {
        "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionID">SubscriptionID</a>" : <i>String</i>,
        "<a href="#dryrun" title="DryRun">DryRun</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#datasetsizeingb" title="DatasetSizeInGb">DatasetSizeInGb</a>" : <i>String</i>,
        "<a href="#respversion" title="RespVersion">RespVersion</a>" : <i>String</i>,
        "<a href="#supportossclusterapi" title="SupportOSSClusterApi">SupportOSSClusterApi</a>" : <i>String</i>,
        "<a href="#useexternalendpointforossclusterapi" title="UseExternalEndpointForOSSClusterApi">UseExternalEndpointForOSSClusterApi</a>" : <i>String</i>,
        "<a href="#datapersistence" title="DataPersistence">DataPersistence</a>" : <i>String</i>,
        "<a href="#dataevictionpolicy" title="DataEvictionPolicy">DataEvictionPolicy</a>" : <i>String</i>,
        "<a href="#replication" title="Replication">Replication</a>" : <i>String</i>,
        "<a href="#replica" title="Replica">Replica</a>" : <i>String</i>,
        "<a href="#throughputmeasurement" title="ThroughputMeasurement">ThroughputMeasurement</a>" : <i>String</i>,
        "<a href="#localthroughputmeasurement" title="LocalThroughputMeasurement">LocalThroughputMeasurement</a>" : <i>String</i>,
        "<a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>" : <i>String</i>,
        "<a href="#remotebackup" title="RemoteBackup">RemoteBackup</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#clienttlscertificates" title="ClientTlsCertificates">ClientTlsCertificates</a>" : <i>String</i>,
        "<a href="#enabletls" title="EnableTls">EnableTls</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#saslusername" title="SaslUsername">SaslUsername</a>" : <i>String</i>,
        "<a href="#saslpassword" title="SaslPassword">SaslPassword</a>" : <i>String</i>,
        "<a href="#alerts" title="Alerts">Alerts</a>" : <i>String</i>,
        "<a href="#modules" title="Modules">Modules</a>" : <i>String</i>,
        "<a href="#queryperformancefactor" title="QueryPerformanceFactor">QueryPerformanceFactor</a>" : <i>String</i>,
        "<a href="#regexrules" title="RegexRules">RegexRules</a>" : <i>String</i>,
        "<a href="#enabledefaultuser" title="EnableDefaultUser">EnableDefaultUser</a>" : <i>String</i>,
        "<a href="#ondemandbackup" title="OnDemandBackup">OnDemandBackup</a>" : <i>String</i>,
        "<a href="#regionname" title="RegionName">RegionName</a>" : <i>String</i>,
        "<a href="#ondemandimport" title="OnDemandImport">OnDemandImport</a>" : <i>String</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
        "<a href="#importfromuri" title="ImportFromUri">ImportFromUri</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Redis::CloudFormation::ProDatabase
Properties:
    <a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionID">SubscriptionID</a>: <i>String</i>
    <a href="#dryrun" title="DryRun">DryRun</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#datasetsizeingb" title="DatasetSizeInGb">DatasetSizeInGb</a>: <i>String</i>
    <a href="#respversion" title="RespVersion">RespVersion</a>: <i>String</i>
    <a href="#supportossclusterapi" title="SupportOSSClusterApi">SupportOSSClusterApi</a>: <i>String</i>
    <a href="#useexternalendpointforossclusterapi" title="UseExternalEndpointForOSSClusterApi">UseExternalEndpointForOSSClusterApi</a>: <i>String</i>
    <a href="#datapersistence" title="DataPersistence">DataPersistence</a>: <i>String</i>
    <a href="#dataevictionpolicy" title="DataEvictionPolicy">DataEvictionPolicy</a>: <i>String</i>
    <a href="#replication" title="Replication">Replication</a>: <i>String</i>
    <a href="#replica" title="Replica">Replica</a>: <i>String</i>
    <a href="#throughputmeasurement" title="ThroughputMeasurement">ThroughputMeasurement</a>: <i>String</i>
    <a href="#localthroughputmeasurement" title="LocalThroughputMeasurement">LocalThroughputMeasurement</a>: <i>String</i>
    <a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>: <i>String</i>
    <a href="#remotebackup" title="RemoteBackup">RemoteBackup</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#clienttlscertificates" title="ClientTlsCertificates">ClientTlsCertificates</a>: <i>String</i>
    <a href="#enabletls" title="EnableTls">EnableTls</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#saslusername" title="SaslUsername">SaslUsername</a>: <i>String</i>
    <a href="#saslpassword" title="SaslPassword">SaslPassword</a>: <i>String</i>
    <a href="#alerts" title="Alerts">Alerts</a>: <i>String</i>
    <a href="#modules" title="Modules">Modules</a>: <i>String</i>
    <a href="#queryperformancefactor" title="QueryPerformanceFactor">QueryPerformanceFactor</a>: <i>String</i>
    <a href="#regexrules" title="RegexRules">RegexRules</a>: <i>String</i>
    <a href="#enabledefaultuser" title="EnableDefaultUser">EnableDefaultUser</a>: <i>String</i>
    <a href="#ondemandbackup" title="OnDemandBackup">OnDemandBackup</a>: <i>String</i>
    <a href="#regionname" title="RegionName">RegionName</a>: <i>String</i>
    <a href="#ondemandimport" title="OnDemandImport">OnDemandImport</a>: <i>String</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
    <a href="#importfromuri" title="ImportFromUri">ImportFromUri</a>: <i>String</i>
</pre>

## Properties

#### BaseUrl

[Required]. The Base URL where the API calls are sent.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SubscriptionID

[Required]. The Subscription ID under which the Database is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DryRun

[Optional]. When 'false': Creates a deployment plan and deploys it (creating any resources required by the plan). When 'true': creates a read-only deployment plan without any resource creation. Example: false. Default: 'false'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

[Required]. Database name (Database name must be up to 40 characters long, include only letters, digits, or hyphen ('-'), start with a letter, and end with a letter or digit). Example: Redis-database-example

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

[Optional]. Database protocol: either 'redis' or 'memcached'. Default: 'redis'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Port

[Optional]. TCP port on which the database is available (10000-19999). Generated automatically if omitted. Example: 10000

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DatasetSizeInGb

[Required]. The maximum amount of data in the dataset for this specific database is in GB. You can not set both datasetSizeInGb and totalMemoryInGb. if 'replication' is true, the database's total memory will be twice as large as the datasetSizeInGb.if 'replication' is false, the database's total memory of the database will be the datasetSizeInGb value. Minimum: 0.1. ExclusiveMinimum: false. Example: 1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespVersion

[Optional]. RESP version must be compatible with Redis version. Example: resp3. Allowed values: resp2/resp3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportOSSClusterApi

[Optional]. Support Redis open-source (OSS) Cluster API. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseExternalEndpointForOSSClusterApi

[Optional]. Should use external endpoint for open-source (OSS) Cluster API. Can only be enabled if OSS Cluster API support is enabled'. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataPersistence

[Optional]. Rate of database data persistence (in persistent storage). List of options: [ none, aof-every-1-second, aof-every-write, snapshot-every-1-hour, snapshot-every-6-hours, snapshot-every-12-hours ]. Example: none. Default: 'none'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataEvictionPolicy

[Optional]. Data items eviction method. List of options: [ allkeys-lru, allkeys-lfu, allkeys-random, volatile-lru, volatile-lfu, volatile-random, volatile-ttl, noeviction ]. Default: 'volatile-lru'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replication

[Optional]. Databases replication. Default: 'true'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replica

[Optional. Input as JSON]. Replica Of configuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputMeasurement

[Optional. Input as JSON]. Throughput measurement method. Default: 25000 ops/sec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalThroughputMeasurement

[Optional. Input as JSON]. Throughput measurement for an active-active subscription

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### AverageItemSizeInBytes

[Optional]. Relevant only to ram-and-flash clusters. Estimated average size (measured in bytes) of the items stored in the database. Default: 1000

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### RemoteBackup

[Optional. Input as JSON]. Database remote backup configuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

[Optional]. List of source IP addresses or subnet masks. If specified, Redis clients will be able to connect to this database only from within the specified source IP addresses ranges. Example value: '['192.168.10.0/32', '192.168.12.0/24']'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientTlsCertificates

[Optional. Input as a JSON]. A list of TLS/SSL certificates (public keys) with new line characters replaced by 
. If specified, mTLS authentication (with enableTls not specified or set to true) will be required to authenticate user connections. If empty list is received, SSL certificates will be removed and mTLS will not be required (note that TLS connection may still apply, depending on the value of the enableTls property). Default: 'null'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTls

[Optional]. When 'true', requires TLS authentication for all connections (mTLS with valid clientSslCertificate, regular TLS when the clientSslCertificate is not provided. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

[Optional]. Password to access the database. If omitted, a random 32 character long alphanumeric password will be automatically generated. Can only be set if Database Protocol is REDIS

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaslUsername

[Optional]. Memcached (SASL) Username to access the database. If omitted, the username will be set to a 'mc-' prefix followed by a random 5 character long alphanumeric. Can only be set if Database Protocol is MEMCACHED

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaslPassword

[Optional]. Memcached (SASL) Password to access the database. If omitted, a random 32 character long alphanumeric password will be automatically generated. Can only be set if Database Protocol is MEMCACHED

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alerts

[Optional. Input as JSON]. Redis database alerts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Modules

[Optional. Input as JSON]. Redis modules to be provisioned in the database.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### QueryPerformanceFactor

[Optional]. The query performance factor adds extra compute power specifically for search and query. For databases with search and query, you can increase your search queries per second by the selected factor. Example: 2x

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexRules

[Optional. Can only be modified upon Update request from a Cloud Formation stack]. Shard regex rules. Relevant only for a sharded database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDefaultUser

[Optional. Can only be modified upon Update request from a Cloud Formation stack]. When 'true', enables connecting to the database with the 'default' user. Default: 'true'. Can only be set if Database Protocol is REDIS

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandBackup

[Required to enable Backup. Can only be modified upon Update request from a Cloud Formation stack. Requires 'remoteBackup' to be active]. If 'true', creates a backup of the current database and disables all other parameters set for Update except for 'RegionName'. Default 'false'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionName

[Optional. Can only be modified upon Update request from a Cloud Formation stack. Requires 'OnDemandBackup' set to 'true']. Name of cloud provider region where the local database is located. When backing up an active-active database, backup is done separately for each local database at a specified region. Example for active-active database: 'us-east-1'. For single-region deployment, the value MUST be 'null'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandImport

[Required to enable Import. Can only be modified upon Update request from a Cloud Formation stack]. If 'true', imports the previous created backup of a database and disables all other parameters set for Update except for 'SourceType' and 'ImportFromUri'. Default 'false'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

[Required for Import. Can only be modified upon Update request from a Cloud Formation stack. Requires 'OnDemandImport' set to 'true']. Type of storage source from which to import the database file (RDB files) or data (Redis connection). List of options: [ http, redis, ftp, aws-s3, azure-blob-storage, google-blob-storage ].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportFromUri

[Required for Import. Can only be modified upon Update request from a Cloud Formation stack. Requires 'OnDemandImport' set to 'true'].  One or more URIs to source data files or Redis databases, as appropriate to specified source type (example: ['http://mydomain.com/redis-backup-file1', 'http://mydomain.com/redis-backup-file2'])

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the DatabaseID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### DatabaseID

Database ID. Populated with value within the handlers.py.

