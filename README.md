# E-Learning Platform — CI/CD Pipeline & AKS Deployment

A containerized e-learning platform with automated multi-stage CI/CD pipeline on Azure DevOps, deployed on Azure Kubernetes Service (AKS).

## Architecture

```
GitHub Push → Azure Pipelines → Docker Build → ACR Push → AKS Deploy
                     |
              (4 Stages)
           Build → Test → Staging → Production
```

## Tech Stack

| Layer | Technology |
|---|---|
| CI/CD | Azure DevOps, Azure Pipelines (YAML) |
| Containers | Docker, Docker Compose |
| Orchestration | Azure Kubernetes Service (AKS) |
| Registry | Azure Container Registry (ACR) |
| Database | Azure SQL |
| Monitoring | Azure Monitor, Log Analytics |
| Version Control | Git |

## Project Structure

```
elearning-cicd-aks/
├── azure-pipelines.yml        # Multi-stage CI/CD pipeline
├── docker-compose.yml         # Local development setup
├── frontend/
│   ├── Dockerfile
│   └── app.py                 # Frontend service
├── backend/
│   ├── Dockerfile
│   └── app.py                 # Backend API service
├── kubernetes/
│   ├── namespace.yaml
│   ├── frontend-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── services.yaml
│   └── hpa.yaml               # Horizontal Pod Autoscaler
└── scripts/
    └── smoke_test.py          # Post-deploy smoke tests
```

## Key Features

- **4-stage YAML pipeline**: Build → Test → Staging → Production
- **Zero-downtime deployments** via Kubernetes rolling updates
- **Branch-based triggers**: `develop` deploys to Staging, `main` deploys to Production
- **Azure Monitor** dashboards for CPU, memory, and pod health
- **Automated smoke tests** post-deployment using Python
- **~80% reduction** in manual deployment effort

## Setup & Deployment

### Prerequisites
- Azure CLI installed
- Azure DevOps account
- AKS cluster created
- ACR registry created

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/elearning-cicd-aks.git
cd elearning-cicd-aks
```

### 2. Run locally
```bash
docker-compose up --build
```

### 3. Configure Azure DevOps
- Create a new pipeline pointing to `azure-pipelines.yml`
- Add service connections: ACR and AKS
- Set pipeline variables: `ACR_NAME`, `AKS_CLUSTER`, `RESOURCE_GROUP`

### 4. Deploy to AKS manually (optional)
```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/
```

## Monitoring

Azure Monitor alerts configured for:
- CPU usage > 80%
- Memory usage > 75%
- Pod restart count > 3

## Author
Sushree Jyotirmayee Mallick — [LinkedIn](https://linkedin.com/in/sushreejyotirmayee)
