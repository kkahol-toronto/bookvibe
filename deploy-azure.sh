#!/bin/bash

# Azure Container Registry and App Service Deployment Script for BookVibe
# Make sure you have Azure CLI installed and logged in

set -e

# Configuration
ACR_NAME="${AZURE_CONTAINER_REGISTRY}"
ACR_USERNAME="${AZURE_CONTAINER_REGISTRY_USERNAME}"
ACR_PASSWORD="${AZURE_CONTAINER_REGISTRY_PASSWORD}"
RESOURCE_GROUP="bookvibe-rg"
LOCATION="eastus"
APP_SERVICE_PLAN="bookvibe-plan"
APP_SERVICE_NAME="bookvibe"
IMAGE_NAME="bookvibe:latest"

# Handle ACR name with or without .azurecr.io suffix
if [[ "$ACR_NAME" == *".azurecr.io" ]]; then
    FULL_IMAGE_NAME="${ACR_NAME}/${IMAGE_NAME}"
    ACR_LOGIN_NAME="${ACR_NAME}"
else
    FULL_IMAGE_NAME="${ACR_NAME}.azurecr.io/${IMAGE_NAME}"
    ACR_LOGIN_NAME="${ACR_NAME}.azurecr.io"
fi

echo "🚀 Starting BookVibe deployment to Azure..."

# Check if required environment variables are set
if [ -z "$ACR_NAME" ] || [ -z "$ACR_USERNAME" ] || [ -z "$ACR_PASSWORD" ]; then
    echo "❌ Error: Required environment variables not set:"
    echo "   AZURE_CONTAINER_REGISTRY: $ACR_NAME"
    echo "   AZURE_CONTAINER_REGISTRY_USERNAME: $ACR_USERNAME"
    echo "   AZURE_CONTAINER_REGISTRY_PASSWORD: $ACR_PASSWORD"
    exit 1
fi

# Login to Azure Container Registry
echo "🔐 Logging into Azure Container Registry..."
echo $ACR_PASSWORD | docker login $ACR_LOGIN_NAME -u $ACR_USERNAME --password-stdin

# Build Docker image for AMD64 platform
echo "🏗️ Building Docker image for AMD64 platform..."
docker build --platform linux/amd64 -t $IMAGE_NAME .

# Tag image for ACR
echo "🏷️ Tagging image for Azure Container Registry..."
docker tag $IMAGE_NAME $FULL_IMAGE_NAME

# Push image to ACR
echo "📤 Pushing image to Azure Container Registry..."
docker push $FULL_IMAGE_NAME

# Create resource group if it doesn't exist
echo "📦 Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION --output none

# Create App Service Plan (Basic tier)
echo "📋 Creating App Service Plan..."
az appservice plan create \
    --name $APP_SERVICE_PLAN \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION \
    --sku B1 \
    --is-linux \
    --output none

# Create Web App
echo "🌐 Creating Web App..."
az webapp create \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP \
    --plan $APP_SERVICE_PLAN \
    --deployment-local-git \
    --output none

# Configure Web App for container deployment
echo "⚙️ Configuring Web App for container deployment..."
az webapp config container set \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP \
    --docker-custom-image-name $FULL_IMAGE_NAME \
    --docker-registry-server-url https://$ACR_LOGIN_NAME \
    --docker-registry-server-user $ACR_USERNAME \
    --docker-registry-server-password $ACR_PASSWORD \
    --output none

# Set environment variables
echo "🔧 Setting environment variables..."
az webapp config appsettings set \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP \
    --settings \
        AZURE_OPENAI_ENDPOINT="${AZURE_OPENAI_ENDPOINT}" \
        AZURE_OPENAI_KEY="${AZURE_OPENAI_KEY}" \
        AZURE_OPENAI_DEPLOYMENT="${AZURE_OPENAI_DEPLOYMENT}" \
        WEBSITES_PORT=8000 \
    --output none

# Enable continuous deployment
echo "🔄 Enabling continuous deployment..."
az webapp deployment container config \
    --enable-cd true \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP \
    --output none

# Get the app URL
APP_URL=$(az webapp show --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP --query defaultHostName --output tsv)

echo "✅ Deployment completed successfully!"
echo "🌍 Your BookVibe application is now available at:"
echo "   https://$APP_URL"
echo ""
echo "📊 To monitor your application:"
echo "   az webapp log tail --name $APP_SERVICE_NAME --resource-group $RESOURCE_GROUP"
echo ""
echo "🔧 To update the application, simply push new code and rebuild the image:"
echo "   docker build -t $IMAGE_NAME ."
echo "   docker tag $IMAGE_NAME $FULL_IMAGE_NAME"
echo "   docker push $FULL_IMAGE_NAME" 