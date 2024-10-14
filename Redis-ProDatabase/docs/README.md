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
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>String</i>,
        "<a href="#servercert" title="ServerCert">ServerCert</a>" : <i>String</i>,
        "<a href="#by" title="By">By</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#localthroughputmeasurementregion" title="LocalThroughputMeasurementRegion">LocalThroughputMeasurementRegion</a>" : <i>String</i>,
        "<a href="#writeoperationspersecond" title="WriteOperationsPerSecond">WriteOperationsPerSecond</a>" : <i>String</i>,
        "<a href="#readoperationspersecond" title="ReadOperationsPerSecond">ReadOperationsPerSecond</a>" : <i>String</i>,
        "<a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>" : <i>String</i>,
        "<a href="#active" title="Active">Active</a>" : <i>String</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>String</i>,
        "<a href="#timeutc" title="TimeUTC">TimeUTC</a>" : <i>String</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#storagepath" title="StoragePath">StoragePath</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#publiccertificatepemstring" title="PublicCertificatePEMString">PublicCertificatePEMString</a>" : <i>String</i>,
        "<a href="#enabletls" title="EnableTls">EnableTls</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#saslusername" title="SaslUsername">SaslUsername</a>" : <i>String</i>,
        "<a href="#saslpassword" title="SaslPassword">SaslPassword</a>" : <i>String</i>,
        "<a href="#alertname" title="AlertName">AlertName</a>" : <i>String</i>,
        "<a href="#alertvalue" title="AlertValue">AlertValue</a>" : <i>String</i>,
        "<a href="#modulename" title="ModuleName">ModuleName</a>" : <i>String</i>,
        "<a href="#moduleparameters" title="ModuleParameters">ModuleParameters</a>" : <i>String</i>,
        "<a href="#queryperformancefactor" title="QueryPerformanceFactor">QueryPerformanceFactor</a>" : <i>String</i>
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
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>String</i>
    <a href="#servercert" title="ServerCert">ServerCert</a>: <i>String</i>
    <a href="#by" title="By">By</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#localthroughputmeasurementregion" title="LocalThroughputMeasurementRegion">LocalThroughputMeasurementRegion</a>: <i>String</i>
    <a href="#writeoperationspersecond" title="WriteOperationsPerSecond">WriteOperationsPerSecond</a>: <i>String</i>
    <a href="#readoperationspersecond" title="ReadOperationsPerSecond">ReadOperationsPerSecond</a>: <i>String</i>
    <a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>: <i>String</i>
    <a href="#active" title="Active">Active</a>: <i>String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>String</i>
    <a href="#timeutc" title="TimeUTC">TimeUTC</a>: <i>String</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#storagepath" title="StoragePath">StoragePath</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#publiccertificatepemstring" title="PublicCertificatePEMString">PublicCertificatePEMString</a>: <i>String</i>
    <a href="#enabletls" title="EnableTls">EnableTls</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#saslusername" title="SaslUsername">SaslUsername</a>: <i>String</i>
    <a href="#saslpassword" title="SaslPassword">SaslPassword</a>: <i>String</i>
    <a href="#alertname" title="AlertName">AlertName</a>: <i>String</i>
    <a href="#alertvalue" title="AlertValue">AlertValue</a>: <i>String</i>
    <a href="#modulename" title="ModuleName">ModuleName</a>: <i>String</i>
    <a href="#moduleparameters" title="ModuleParameters">ModuleParameters</a>: <i>String</i>
    <a href="#queryperformancefactor" title="QueryPerformanceFactor">QueryPerformanceFactor</a>: <i>String</i>
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

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

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

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SupportOSSClusterApi

[Optional]. Support Redis open-source (OSS) Cluster API. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### UseExternalEndpointForOSSClusterApi

[Optional]. Should use external endpoint for open-source (OSS) Cluster API. Can only be enabled if OSS Cluster API support is enabled'. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DataPersistence

[Optional]. Rate of database data persistence (in persistent storage). List of options: [ none, aof-every-1-second, aof-every-write, snapshot-every-1-hour, snapshot-every-6-hours, snapshot-every-12-hours ]. Example: none. Default: 'none'.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DataEvictionPolicy

[Optional]. Data items eviction method. List of options: [ allkeys-lru, allkeys-lfu, allkeys-random, volatile-lru, volatile-lfu, volatile-random, volatile-ttl, noeviction ]. Default: 'volatile-lru'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Replication

[Optional]. Databases replication. Default: 'true'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Endpoint

[Required for replica]. A Redis URI (sample format: 'redis://user:password@host:port)'. If the URI provided is Redis Cloud instance, only host and port should be provided (using the format: ['redis://endpoint1:6379', 'redis://endpoint2:6380'] ).

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Encryption

[Optional]. Defines if encryption should be used to connect to the sync source. If left null and if the source is a Redis Cloud instance, it will automatically detect if the source uses encryption.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ServerCert

[Optional]. TLS/SSL certificate chain of the sync source. If left null and if the source is a Redis Cloud instance, it will automatically detect the certificate to use.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### By

[Required to enable throughputMeasurement]. Throughput measurement method. Either 'number-of-shards' or 'operations-per-second'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Value

[Required to enable throughputMeasurement]. Throughput value (as applies to selected measurement method). Example: 10000. Default: 25000 ops/sec

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### LocalThroughputMeasurementRegion

[Optional]. Local throughput for the regional instance of an Active-Active database

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### WriteOperationsPerSecond

[Optional]. Example: 1000. Default: 1000 ops/sec

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ReadOperationsPerSecond

[Optional]. Example: 1000. Default: 1000 ops/sec

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### AverageItemSizeInBytes

[Optional]. Relevant only to ram-and-flash clusters. Estimated average size (measured in bytes) of the items stored in the database. Default: 1000

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Active

[Optional]. Determine whether backup should be active or not. Default: null

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Interval

[Required when active is true]. Represent the interval between backups, should be in the following format every-x-hours where x is one of (24,12,6,4,2,1). for example: 'every-4-hours'.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### TimeUTC

[Optional]. State the hour which the backup will take place. Available only for 12 or 24 hours backup interval. Should be specified an hour for example 2 PM as 14:00

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### StorageType

[Required when active is true]. Type of storage source from which to import the database file (RDB files) or data (Redis connection)

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### StoragePath

[Required when active is true]. Path for backup

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SourceIp

[Optional]. List of source IP addresses or subnet masks. If specified, Redis clients will be able to connect to this database only from within the specified source IP addresses ranges. example value: '['192.168.10.0/32', '192.168.12.0/24']'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### PublicCertificatePEMString

[Required for clientTlsCertificates]. Public key certificate (PEM format)

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### EnableTls

[Optional]. When 'true', requires TLS authentication for all connections (mTLS with valid clientSslCertificate, regular TLS when the clientSslCertificate is not provided. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Password

[Optional]. Password to access the database. If omitted, a random 32 character long alphanumeric password will be automatically generated. Can only be set if Database Protocol is REDIS

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SaslUsername

[Optional]. Memcached (SASL) Username to access the database. If omitted, the username will be set to a 'mc-' prefix followed by a random 5 character long alphanumeric. Can only be set if Database Protocol is MEMCACHED

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SaslPassword

[Optional]. Memcached (SASL) Password to access the database. If omitted, a random 32 character long alphanumeric password will be automatically generated. Can only be set if Database Protocol is MEMCACHED

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### AlertName

[Required to enable alerts]. Alert name. List of options: [ dataset-size, datasets-size, throughput-higher-than, throughput-lower-than, latency, syncsource-error, syncsource-lag, connections-limit ]. Example: dataset-size

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### AlertValue

[Required to enable alerts]. Alert value. Example: 80

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ModuleName

[Required only to enable modules]. Redis module Id

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ModuleParameters

[Optional]. Redis database module parameters (name and value), as relevant to the specific module (see modules parameters specification). Example: OrderedMap {}

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### QueryPerformanceFactor

[Optional]. The query performance factor adds extra compute power specifically for search and query. For databases with search and query, you can increase your search queries per second by the selected factor. Example: 2x

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the DatabaseID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### DatabaseID

Database ID. Populated with value within the handlers.py.

