#!/bin/bash

echo "🧪 Testing BookVibe Docker build for AMD64 platform..."

# Build the image for AMD64
echo "🏗️ Building Docker image..."
docker build --platform linux/amd64 -t bookvibe:test .

if [ $? -eq 0 ]; then
    echo "✅ Docker build successful!"
    
    # Test the container
    echo "🚀 Testing container startup..."
    docker run --rm -d --name bookvibe-test -p 8001:8000 bookvibe:test
    
    # Wait a moment for the app to start
    sleep 5
    
    # Test health endpoint
    echo "🏥 Testing health endpoint..."
    curl -f http://localhost:8001/health
    
    if [ $? -eq 0 ]; then
        echo "✅ Health check passed!"
        echo "🌍 Application is running at http://localhost:8001"
    else
        echo "❌ Health check failed!"
    fi
    
    # Stop and remove test container
    docker stop bookvibe-test
    docker rmi bookvibe:test
    
    echo "🧹 Cleanup completed"
else
    echo "❌ Docker build failed!"
    exit 1
fi 