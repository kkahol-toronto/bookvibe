# BookVibe Deployment Guide

## 🐳 Local Docker Deployment

### Prerequisites
- Docker and Docker Compose installed
- Environment variables configured in `.env` file

### Quick Start
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application at http://localhost:8000
# Note: The library.db file is included in the image with initial sample data
```

### Manual Docker Commands
```bash
# Build the image for AMD64 platform (required for Azure)
docker build --platform linux/amd64 -t bookvibe .

# Run the container
docker run -p 8000:8000 --env-file .env bookvibe

# Run in detached mode
docker run -d -p 8000:8000 --env-file .env --name bookvibe-app bookvibe
```

## ☁️ Azure Deployment

### Prerequisites
- Azure CLI installed and logged in
- Azure Container Registry (ACR) created
- Environment variables set:
  - `AZURE_CONTAINER_REGISTRY`
  - `AZURE_CONTAINER_REGISTRY_USERNAME`
  - `AZURE_CONTAINER_REGISTRY_PASSWORD`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_KEY`
  - `AZURE_OPENAI_DEPLOYMENT`

### Automated Deployment
```bash
# Run the deployment script
./deploy-azure.sh
```

### Manual Azure Deployment Steps

1. **Login to Azure Container Registry**
   ```bash
   az acr login --name $AZURE_CONTAINER_REGISTRY
   ```

2. **Build and Push Docker Image**
   ```bash
   docker build --platform linux/amd64 -t bookvibe .
   docker tag bookvibe $AZURE_CONTAINER_REGISTRY.azurecr.io/bookvibe:latest
   docker push $AZURE_CONTAINER_REGISTRY.azurecr.io/bookvibe:latest
   ```

3. **Create Resource Group**
   ```bash
   az group create --name bookvibe-rg --location eastus
   ```

4. **Create App Service Plan**
   ```bash
   az appservice plan create \
     --name bookvibe-plan \
     --resource-group bookvibe-rg \
     --location eastus \
     --sku B1 \
     --is-linux
   ```

5. **Create Web App**
   ```bash
   az webapp create \
     --name bookvibe \
     --resource-group bookvibe-rg \
     --plan bookvibe-plan \
     --deployment-local-git
   ```

6. **Configure Container Deployment**
   ```bash
   az webapp config container set \
     --name bookvibe \
     --resource-group bookvibe-rg \
     --docker-custom-image-name $AZURE_CONTAINER_REGISTRY.azurecr.io/bookvibe:latest \
     --docker-registry-server-url https://$AZURE_CONTAINER_REGISTRY.azurecr.io \
     --docker-registry-server-user $AZURE_CONTAINER_REGISTRY_USERNAME \
     --docker-registry-server-password $AZURE_CONTAINER_REGISTRY_PASSWORD
   ```

7. **Set Environment Variables**
   ```bash
   az webapp config appsettings set \
     --name bookvibe \
     --resource-group bookvibe-rg \
     --settings \
       AZURE_OPENAI_ENDPOINT="$AZURE_OPENAI_ENDPOINT" \
       AZURE_OPENAI_KEY="$AZURE_OPENAI_KEY" \
       AZURE_OPENAI_DEPLOYMENT="$AZURE_OPENAI_DEPLOYMENT" \
       WEBSITES_PORT=8000
   ```

## 🔄 Continuous Deployment with GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/azure-app-service.yml`) that automatically deploys to Azure when code is pushed to the main branch.

### Required GitHub Secrets
- `AZURE_CONTAINER_REGISTRY`
- `AZURE_CONTAINER_REGISTRY_USERNAME`
- `AZURE_CONTAINER_REGISTRY_PASSWORD`

## 📊 Monitoring and Logs

### View Application Logs
```bash
# Azure CLI
az webapp log tail --name bookvibe --resource-group bookvibe-rg

# Docker
docker logs bookvibe-app
```

### Health Check
The application includes a health check endpoint at `/health` that returns:
```json
{
  "status": "healthy",
  "service": "BookVibe"
}
```

## 🔧 Environment Variables

### Required for Azure OpenAI
- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint
- `AZURE_OPENAI_KEY`: Your Azure OpenAI API key
- `AZURE_OPENAI_DEPLOYMENT`: Your Azure OpenAI deployment name

### Azure Container Registry
- `AZURE_CONTAINER_REGISTRY`: Your ACR registry name
- `AZURE_CONTAINER_REGISTRY_USERNAME`: ACR username
- `AZURE_CONTAINER_REGISTRY_PASSWORD`: ACR password

## 🚀 Scaling and Performance

### App Service Plan Tiers
- **B1 (Basic)**: Recommended for development and testing
- **S1 (Standard)**: Better for production workloads
- **P1V2 (Premium)**: For high-performance requirements

### Database Considerations
The current implementation uses SQLite with the database file included in the Docker image. This provides:
- Initial data persistence across deployments
- Simple setup for development and testing
- No external database dependencies

For production with multiple instances:
- Consider using Azure SQL Database or PostgreSQL
- Implement proper connection pooling
- Set up automated backups
- Use Azure File Storage for shared database access

## 🔒 Security Best Practices

1. **Environment Variables**: Never commit sensitive data to version control
2. **Container Security**: Use non-root user in Docker container
3. **Network Security**: Configure Azure Network Security Groups
4. **HTTPS**: Enable HTTPS for production deployments
5. **Secrets Management**: Use Azure Key Vault for sensitive configuration

## 🐛 Troubleshooting

### Common Issues

1. **Container won't start**
   - Check logs: `docker logs <container-name>`
   - Verify environment variables are set
   - Ensure port 8000 is exposed

2. **Azure deployment fails**
   - Verify ACR credentials
   - Check resource group permissions
   - Ensure App Service Plan supports containers
   - Ensure Docker image is built for AMD64 platform (required for Azure)

3. **OpenAI API errors**
   - Verify Azure OpenAI endpoint and key
   - Check deployment name
   - Ensure proper API version

### Support
For issues related to:
- **Azure Services**: Check Azure documentation and support
- **Docker**: Refer to Docker documentation
- **Application**: Check application logs and GitHub issues 