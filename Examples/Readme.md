# Examples

## Examples for "stand-alone" resources without dependencies on each other

Within each subfolder (e.g., `/Subscription`, `/Peering`, `/Database`), you'll find a `.yml` file named similarly to the folder. These files provide the most accurate examples of stand-alone resources.


## Examples for resources that depend on each other

### A subscription is needed to create a database
The `SubscriptionAndDatabase.yml` file serves as an example for this. In the `Resources` section, there are two resources: `ProSubscription` and `ProDatabase`. 

The `DependsOn` parameter is unnecessary because `ProDatabase` includes the property `SubscriptionID: !Ref ProSubscription`, which directly references the resource ID (`SubscriptionID`) of the subscription resource - which logically has to be created before.

### A subscription and a VPC are needed to create a Peering Resource
The same pattern from the previous example can be applied here. In the case of the VPC, the VPC ID can be referenced in the property of the Peering resource using `!Ref VPC`.
