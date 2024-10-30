
# MEAN Stack Docker Swarm Deployment

This repository contains a MEAN stack application deployed on Docker Swarm with MongoDB replication. 
Follow the instructions below to build, deploy, and access the application.

## Prerequisites

- Docker Desktop or Docker Engine installed.
- Docker Swarm initialized.

## Project Structure

- `backEnd/`: Node.js backend application.
- `frontEnd/`: Angular frontend application.
- `docker-compose.yml`: Docker Compose file for configuring services.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository>
cd <repository-directory>/docker
```

### 2. Run the Deployment Script

Use the provided PowerShell or Bash script to build the images, initialize Docker Swarm, and deploy the stack.

#### Windows PowerShell

Run the PowerShell script:
```powershell
.\deploy.ps1
```

#### Linux/Mac

Run the Bash script:
```bash
./deploy.sh
```

### 3. Check Service Status

After deployment, the script will display the status of all services in the stack.

You can also check manually with:
```bash
docker stack services mean-stack
```

### 4. Access the Application

- **Frontend**: Open [http://localhost:4200](http://localhost:4200) in your browser.
- **Backend API**: The backend runs on port `8000`, accessible at `http://localhost:8000`.
- **MongoDB Replicas**: Accessible on ports `27017`, `27018`, and `27019`.

## Stopping and Removing the Stack

To remove the stack and leave Swarm mode, use:
```powershell
docker stack rm mean-stack
docker swarm leave --force
```

## Troubleshooting

- Ensure that Docker Swarm is initialized before deploying the stack.
- Verify that the required ports (4200, 8000, 27017-27019) are available.
- Run `docker service logs <service_name>` for specific logs.
