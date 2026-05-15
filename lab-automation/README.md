# Cloud-Native Lab Data Automation Engine

An automated, containerized data pipeline that simulates ingesting medical lab data, validating file integrity, and managing system logs. This project features a robust CI/CD pipeline that automatically builds and tests the execution environment inside an isolated Docker container on every code deployment.

## 🏗️ System Architecture

The automation workflow follows these professional DevOps stages:
1. **Trigger Stage:** Code changes are pushed to the `main` branch on GitHub.
2. **Build Stage:** GitHub Actions provisions a clean, hosted cloud runner.
3. **Containerization:** The cloud runner reads the project `Dockerfile` and builds an isolated Python environment.
4. **Test Stage (CI):** `pytest` runs inside the live Docker container to validate data handling logic, catching empty or corrupted files before deployment.

## 🚀 Technical Stack
* **Language:** Python 3.12
* **Testing Framework:** pytest 9.0
* **Containerization:** Docker
* **CI/CD Platform:** GitHub Actions

## 🛠️ How to Run Locally

### Prerequisites
Make sure you have Docker installed and running on your local machine or Windows Subsystem for Linux (WSL).

### 1. Clone the Project
```bash
git clone [https://github.com/AbuEbunoluwa/Python-Automation-Script.git](https://github.com/AbuEbunoluwa/Python-Automation-Script.git)
cd Python-Automation-Script/lab-automation
