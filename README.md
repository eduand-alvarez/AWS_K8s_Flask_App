# Kubernetes-EKS-flask-demo-app


# Description
This repository is meant to serve as walkthrough and template for kubernetes (k8s) flask app deployments on the AWS cloud. The solution leverages AWS' Elastic K8s Service (EKS) to manage clusters on the public cloud. The code here provides both the infrastructure as code (IaC) components and a simple application script to handle the flask API. 

# Contents

## app Folder
This folder contains the code for the application image. 
- Dockerfile contains the instructions for building an image
- app.py contains the flask app
- requirements.txt has all of the dependancies for the application

## Kubernetes
This folder contains the kubernetes and EKS configurations. 
- cluster.yml EKS cluster configuration script
- models-deployment.yml K8s deployment script
- models-service.yml K8s service script

 
