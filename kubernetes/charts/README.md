Please to deploy the chart of the gcloudDB 

You can use the helm command :

`helm upgrade mysql-sqlproxy stable/gcloud-mysql-sqlproxy --namespace mysql-sqlproxy \ --set serviceAccountKey="$(cat service-account.json | base64)" \ --set cloudsql.instances[0].instance=INSTANCE \  --set cloudsql.instances[0].project=PROJECT \ --set cloudsql.instances[0].region=REGION \ --set cloudsql.instances[0].port=3306 -i`

OR

the chart inside :
`kubernetes/charts/gcloudmysql.yaml`