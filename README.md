# Calm proxy to launch a Market place

```
curl --location --request POST 'http://127.0.0.1:5000/api/v1/mplaunch' \
--header 'Authorization: Bearer token' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mpname" : "testmp",
    "mpversion": "0.0.1",
    "projectname": "NTXCHGR018",
    "appname" : "testmp"
}'
```
env vars
```
eval $(cat .env | sed 's/^/export /')
```

HELM installation
```
helm install -n dev --set ntx.user=$PC_USER,ntx.password=$PC_PASSWORD,ntx.prismcentralhost=$PC_HOST  launchmp launchmp-helm/.
```
