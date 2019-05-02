
#### To run it Locally please have Docker Compose installed !

#### Build images - docker-compose up --build 
Also for more testing you good add Selenium to your docker-compose.yml 
So you could extend your testing cases in your app when spining up.

#### Also in Kubernetes with minikube
Please install Helm Chart :
For locally testing with minikube
`brew install kubernetes-helm`
`helm create myhelm`
`helm init `
and deploy your charts!

### View your app  browser http://0.0.0.0:8000/

#### If you want to run the project on the cloud follow the next steps
Ofcourse if you are going to host your registry you will need to auth your registry for the images.
       gcloud auth configure-docker
#### On the home page on GCP :
#### IN Tools
Tools:
  --- Container Registry to start

#### then:
docker tag octapp-image gcr.io/[PROJECT-ID]/octapp-image:tag1

docker push gcr.io/[PROJECT-ID]/octapp:tag1
docker pull gcr.io/[PROJECT-ID]/octapp:tag1

#### for your latest images of your app.
Also for your secrets use :
`$ echo mysecretpassword | base64`

#### Then create your Helm chart with :
`$ helm create myhelm`
`$ helm install --name myapp ./mychart --set service.type=NodePort`

`$ kubectl create -f tiller-rbac-config.yaml`
`helm init --service-account tiller`

To intall memcahce to your cluster with helm:
`helm install stable/memcached --name mycache --set replicaCount=2`

Verify that exist :
`kubectl get service mycache-memcached -o jsonpath="{.spec.clusterIP}"`


#### For Load balancing
orizontalpodautoscaler autoscaling nginx hpa
kube-dns-autoscaler

####For Monitoring using Prometheus
`helm install --name prometheus stable/prometheus`

`helm ls` to list what is deployed!

THEN

`export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")`

`$ kubectl --namespace default port-forward $POD_NAME 9090`
Also for scraping into prometheus :
prometheus-to-sd is a simple component that can scrape metrics stored in prometheus text format from one or multiple components and push them to the Stackdriver. Main requirement: k8s cluster should run on GCE or GKE.

For most our services you can use help to deploy it an configure it to the GKE cluster you have created.

#### For your Secrets please do
Create storage in google cloud.

gcloud-mysql-sqlproxy PASSWORD=$(kubectl get secret --namespace databases -gcloud-mysql-sqlproxy -o jsonpath="{.data.gcloud-mysql-sqlproxy-password}" | base64 --decode; echo)


# Let's first convert our password into base64 encoding.

`echo -n $PASSWORD | base64`

#### MUST DO : Copy the generated value and replace it with `YOUR_ENCODED_PASSWORD` in the `password-secret.yml`. Then create the secret.

`kubectl create -f db-password-secret.yml`

#### Now that the secret has been setup, lets migrate the data.
`kubectl create -f migration.yml`

#### Wait for a minute and check the status of the migration using folling commands.
`kubectl get jobs`

#### In order to check the logs, identify the pod running the pod running migration.
`kubectl get pods --show-all`

#### Check the logs of the pod
#### kubectl logs POD_NAME
`kubectl logs `

#### We can just delete the jobs using
`kubectl delete -f migration.yml`

`kubectl create -f cloud-storage-secrets.yml`

#### For Kubernetes cluster (GKE):

From command line :  ` gcloud beta container --project "rock-dragon-239409" clusters create "octapp-cluster-1" --zone "us-central1-a" --username "admin" --cluster-version "1.11.8-gke.6" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-cloud-logging --enable-cloud-monitoring --no-enable-ip-alias --network "projects/rock-dragon-239409/global/networks/default" --subnetwork "projects/rock-dragon-239409/regions/us-central1/subnetworks/default" --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair` 

#### For Docker

Build a Docker image, replacing <your-project-id> with your project ID.

docker build -t gcr.io/<your-project-id>/polls .
Configure docker to use gcloud as a credential helper, so that you can push the image to Google Container Registry:

`gcloud auth configure-docker`

Connect to the cluster in my example `gcloud container clusters get-credentials octapp-cluster-1 --zone us-central1-a --project rock-dragon-239409`
then
`docker push gcr.io/rock-dragon-239409/5289fa94d757:tag1`

Once connected run the command `kubectl get all`

Also

for DB's

#### Prerequisites CloudSQL(MSQL)
 Kubernetes cluster on Google Container Engine (GKE)
 Kubernetes cluster on Google Compute Engine (GCE)
 Cloud SQL Administration API enabled
 GCP Service account for the proxy.
With HELM deployment (as google made it easy): 

`helm upgrade pg-sqlproxy stable/gcloud-mysql-sqlproxy --namespace sqlproxy \ --set serviceAccountKey="$(cat service-account.json | base64)" \ --set cloudsql.instances[0].instance=INSTANCE \  --set cloudsql.instances[0].project=PROJECT \ --set cloudsql.instances[0].region=REGION \ --set cloudsql.instances[0].port=3306 -i`


#### Jekins CI/CD

For the Deployment Pipeline you can you the `Jenkinsfile`
and by having deployed the Jenkins inside your cluster with Helm.

See the usage:
`jenkins/values.yaml`

Deploy :
`./helm install -n cd stable/jenkins -f jenkins/values.yaml --version 0.16.6 --wait`

Also you will need to use the Kubernetes Plugin:
https://wiki.jenkins.io/display/JENKINS/Kubernetes+Plugin


#### Deployment look like

When you will run `$ kubectl get pods --all-namespaces` you will get everything that you deployed!
etc.
```
NAMESPACE     NAME                                                         READY     STATUS    RESTARTS   AGE
default       nginx-1-6644d9f968-n2xhr                                     1/1       Running   0          2h
default       prometheus-alertmanager-7494bbff5f-vfm2w                     2/2       Running   0          14m
default       prometheus-kube-state-metrics-7d6bdbc649-gdfbh               1/1       Running   0          14m
default       prometheus-node-exporter-5dzpp                               1/1       Running   0          14m
default       prometheus-node-exporter-72jz2                               1/1       Running   0          14m
default       prometheus-node-exporter-n7k8v                               1/1       Running   0          14m
default       prometheus-pushgateway-55b8b7cb74-jn6fc                      1/1       Running   0          14m
default       prometheus-server-7fb4d789df-nhc4l                           2/2       Running   0          14m
kube-system   event-exporter-v0.2.3-85644fcdf-8nxww                        2/2       Running   0          4h
kube-system   fluentd-gcp-scaler-8b674f786-t6pb7                           1/1       Running   0          4h
kube-system   fluentd-gcp-v3.2.0-b2wt6                                     2/2       Running   0          4h
kube-system   fluentd-gcp-v3.2.0-hcw6d                                     2/2       Running   0          4h
kube-system   fluentd-gcp-v3.2.0-nk7b8                                     2/2       Running   0          4h
kube-system   heapster-v1.6.0-beta.1-84544f7756-rjgtv                      3/3       Running   0          4h
kube-system   kube-dns-76dbb796c5-9bwbk                                    4/4       Running   0          4h
kube-system   kube-dns-76dbb796c5-rkf2k                                    4/4       Running   0          4h
kube-system   kube-dns-autoscaler-67c97c87fb-64l86                         1/1       Running   0          4h
kube-system   kube-proxy-gke-octapp-cluster-1-default-pool-d6ad528a-4nwd   1/1       Running   0          4h
kube-system   kube-proxy-gke-octapp-cluster-1-default-pool-d6ad528a-bk3v   1/1       Running   0          4h
kube-system   kube-proxy-gke-octapp-cluster-1-default-pool-d6ad528a-r8xd   1/1       Running   0          4h
kube-system   kubernetes-dashboard-69db8c7745-q6kc4                        1/1       Running   0          4h
kube-system   l7-default-backend-7ff48cffd7-rmd56                          1/1       Running   0          4h
kube-system   metrics-server-v0.2.1-fd596d746-wfk98                        2/2       Running   0          4h
kube-system   prometheus-to-sd-d4j52                                       1/1       Running   0          4h
kube-system   prometheus-to-sd-grbcc                                       1/1       Running   0          4h
kube-system   prometheus-to-sd-qk267                                       1/1       Running   0          4h
kube-system   tiller-deploy-54fc6d9ccc-n7n88                               1/1       Running   0          3h ```
