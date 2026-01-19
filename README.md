# 🔍 Payment Failure Analysis & RCA System

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-green)
![Type](https://img.shields.io/badge/Type-Production%20Support%20Engineering-orange)

> **A "Pure PSE" Observability Tool for Automated Root Cause Analysis.**

## 🚀 Overview
In high-volume payment ecosystems, merchants often report generic issues like *"Payments are failing."* Without proper tooling, engineers waste hours digging through raw logs to identify if the issue is a **Merchant Error**, **Bank Downtime**, or **Network Timeout**.

This project solves that problem by implementing **Structured Logging** and an **Automated RCA Engine**. It ingests raw payment logs, classifies them into actionable buckets using a standardized Knowledge Base, and provides real-time failure summaries.

**The "Differentiator":** This system handles real-world edge cases like missing correlation IDs, unknown error codes, and partial log data.

## 🏗️ Architecture
1.  **Ingestion:** Accepts structured JSON logs via REST API.
2.  **Normalization:** Auto-generates `correlation_id` if missing for traceability.
3.  **Analysis:** Maps raw banking error codes (e.g., `err_503`) to human-readable categories (e.g., `PSP_ERROR`).
4.  **Aggregation:** Provides a live dashboard of error distributions.

## 🛠️ Tech Stack
* **Core:** Python 3.12+
* **API Framework:** FastAPI
* **Data Validation:** Pydantic (Strict Schema Enforcement)
* **Server:** Uvicorn (ASGI)
* **Testing:** Custom Python Traffic Simulator

## 📂 Project Structure
```bash
payment-rca-system/
│
├── main.py              # API Entry point, Routes, and Logic
├── models.py            # Pydantic Schemas (Structured Logging Definitions)
├── analyzer.py          # The "Brain": Maps raw codes to RCA categories
├── simulate_traffic.py  # Script to flood the system with mock chaos data
└── README.md            # Documentation
