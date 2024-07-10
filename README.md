# case-study

## Step 1: Install kops and kubectl
To set up your Kubernetes cluster, you need to install kops and kubectl on your local machine. Follow the steps below:

Install kops
Download the kops binary:
```bash
curl -LO https://github.com/kubernetes/kops/releases/download/v1.21.0/kops-linux-amd64
Make the kops binary executable:
chmod +x kops-linux-amd64
Move the kops binary to a directory in your PATH:
sudo mv kops-linux-amd64 /usr/local/bin/kops
```
Install kubectl
```bash
Download the kubectl binary:
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
Make the kubectl binary executable:
chmod +x kubectl
Move the kubectl binary to a directory in your PATH:
sudo mv kubectl /usr/local/bin/kubectl
```
By following these steps, you will have kops and kubectl installed on your local machine, ready to manage your Kubernetes cluster.

## Create an S3 bucket for kops state store
```bash
aws s3api create-bucket --bucket my-kops-state-store --region us-east-
```
## Create the cluster command
```bash
kops create -f cluster.yaml
kops update cluster mycluster.k8s.local --yes
kops validate cluster
```
## Apply the Kubernetes Objects
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
## Apply the Horizontal Pod Autoscaler
```bash
kubectl apply -f hpa.yaml
```

## Create Docker Images
    - Build and push the Docker image

    docker build -t my-web-app:latest .
    docker tag my-web-app:latest <dockerhub-username>/my-web-app:latest
    docker push <dockerhub-username>/my-web-app:latest
    

## Apply the Deployment
```bash
kubectl apply -f deployment.yaml
```

## Setting up S3 Lifecycle Policies
```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-s3-bucket --lifecycle-configuration file://lifecycle.json
```

## Using Helm for Reusability

```helm
my-helm-chart/
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
├── Chart.yaml
└── values.yaml
```

## Deploy Helm Chart

```bash
helm install my-web-app ./my-helm-chart
```


## Run the Ansible playbook
```bash
cd ansible
ansible-playbook deploy.yml
```


## Creating and Managing Secrets
    - Encode your AWS access key and secret key in base64
        echo -n 'your-aws-access-key' | base64
        echo -n 'your-aws-secret-key' | base64
     
    Replace <base64-encoded-access-key> and <base64-encoded-secret-key> with the base64-encoded values

    Apply Secrets

        kubectl apply -f aws-secret.yaml
    