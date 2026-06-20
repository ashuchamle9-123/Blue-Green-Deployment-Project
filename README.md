# 🚀 Blue-Green Deployment & Zero Downtime Release Strategy




## 📌 Project Overview

This project demonstrates a **Blue-Green Deployment Strategy** to achieve **Zero Downtime Application Releases** using Docker, Nginx, and AWS EC2.

Blue-Green Deployment is a production-grade release strategy where two identical environments are maintained:

* 🔵 **Blue Environment** – Current Live Version
* 🟢 **Green Environment** – New Version

Traffic is switched between environments through Nginx without impacting end users, ensuring high availability and safe deployments.

---



## 🎯 Objectives

* Deploy two application versions simultaneously
* Implement Blue-Green deployment architecture
* Configure Nginx as a load balancer
* Achieve zero downtime releases
* Perform instant rollback during failures
* Simulate production deployment workflow

---



## 🏗️ Architecture

```text
User Request
      │
      ▼
 ┌─────────┐
 │  Nginx  │
 └────┬────┘
      │
 ┌────┴────┐
 │         │
 ▼         ▼

🔵 Blue    🟢 Green
Version    Version
```

---

## 🛠️ Technologies Used

* Docker
* Docker Compose
* Nginx
* Python Flask
* AWS EC2
* Git
* GitHub

---



## 📂 Project Structure

```text
Blue-Green-Deployment-Project
│
├── app
│   ├── app-blue
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── app-green
│       ├── app.py
│       ├── Dockerfile
│       └── requirements.txt
│
├── nginx
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md
```

---



## ⚙️ Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd Blue-Green-Deployment-Project
```

### Build Docker Images

```bash
docker build -t blue-app ./app/app-blue

docker build -t green-app ./app/app-green
```

### Run Containers

```bash
docker run -d --name blue -p 5001:5000 blue-app

docker run -d --name green -p 5002:5000 green-app
```

### Verify Running Containers

```bash
docker ps
```

---



## 🔵 Blue Environment

Access:

```text
http://EC2_PUBLIC_IP:5001
```

Output:

```text
BLUE ENVIRONMENT V1
```

---



## 🟢 Green Environment

Access:

```text
http://EC2_PUBLIC_IP:5002
```

Output:

```text
GREEN ENVIRONMENT V2
```

---



## 🔄 Traffic Switching

### Route Traffic to Blue

```nginx
proxy_pass http://localhost:5001;
```

### Route Traffic to Green

```nginx
proxy_pass http://localhost:5002;
```

Reload Nginx:

```bash
systemctl restart nginx
```

---



## ↩️ Rollback Strategy

If the Green deployment fails:

1. Update Nginx configuration
2. Redirect traffic back to Blue
3. Reload Nginx
4. Restore service instantly

This provides a safe and reliable rollback mechanism.

---



## 📸 Project Screenshots

### 1. Docker Images

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/16135fcb-a890-4c76-bbf7-92e68559eefd" />



### 2. Blue Environment Output

<img width="1920" height="1009" alt="BLUE ENVIRONMENT " src="https://github.com/user-attachments/assets/2fe37856-816b-44ec-8767-b25616d9b682" />



### 3. Green Environment Output

<img width="1920" height="1033" alt="GREEN ENVIRONMENT" src="https://github.com/user-attachments/assets/19551e3a-897f-4922-ab21-b3db9db002b5" />



### 4. Nginx Configuration

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/401b7500-c502-4019-a304-69d4752a1b80" />



### 5. Traffic Switch Demonstration

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/2097e2e7-2643-4342-80e4-bba83356ae15" />



### 6. Rollback Demonstration

<img width="1920" height="1030" alt="Green-Environment-Output png" src="https://github.com/user-attachments/assets/779c3693-05f7-4ea6-bf84-044a5dd1d2c2" />



---

## ✅ Expected Outcomes

* Zero Downtime Deployment
* Traffic Switching Capability
* Instant Rollback Mechanism
* High Availability Architecture
* Production Deployment Simulation

---

## 🎓 Learning Outcomes

This project provides hands-on experience with:

* Blue-Green Deployment Strategy
* Load Balancing Concepts
* Release Management
* High Availability Systems
* Containerized Deployments
* DevOps Best Practices

---

## 👨‍💻 Author

**Ashu Chamle**

DevOps Project Portfolio
