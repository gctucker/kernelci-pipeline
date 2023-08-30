```
$ kubectl create namespace kernelci-pipeline
$ kubectl create secret generic \
    kernelci-api-token \
    --namespace=kernelci-pipeline \
    --from-literal="token=12345678990abcdef"
secret/kernelci-api-token created
$ kubectl apply -f monitor.yaml
#$ kubectl create secret generic \
#    kernelci-api-system-token \
#    --namespace=kernelci-pipeline \
#    --from-literal="token=12345678990abcdef"
#secret/kernelci-api-system-token created
$ kubectl create secret generic \
    azure-files-token \
    --namespace=kernelci-pipeline \
    --from-literal="token=the-token-string"
$ kubectl create secret generic \
    lava-collabora-token \
    --namespace=kernelci-pipeline \
    --from-literal="token=the-lava-token-string"
secret/lava-collabora-token created
$ kubectl wait \
    --namespace=kernelci-pipeline
    --for=condition=ready
    --timeout=600s
    pod tarball
pod/tarball condition met
```
In the Kubernetes runtimes:
```
$ kubectl create secret generic \
    kci-api-jwt-early-access \
    --context=gke_android-kernelci-external_europe-west4-c_kci-eu-west4 \
    --namespace=default \
    --from-literal="token=12345678990abcdef"
secret/kci-api-jwt-early-access created
```
