<p align="center">
  <img src="assets/depi-logo.png" alt="DEPI Logo" width="200">
</p>

# Transport Analysis Data Pipeline

Analyze large public transport datasets to gain insights, using **BigQuery** as the data warehouse, **Google Cloud Storage (GCS)** as the data lake, **DBT** for modeling, and **Apache Airflow** for orchestration.

---

## Tech Stack & Tools

### 🧰 The Toolkit

I am building end-to-end data solutions using this modern tech stack:

<p align="center">

| Infrastructure | Orchestration | Warehousing | Transformation | Dashboarding |
|:--------------:|:-------------:|:-----------:|:--------------:|:------------:|
| <img src="https://img.shields.io/badge/GCS-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="GCS"><br><img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"> | <img src="https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white" alt="Airflow"> | <img src="https://img.shields.io/badge/BigQuery-4285F4?style=flat-square&logo=googlebigquery&logoColor=white" alt="BigQuery"> | <img src="https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white" alt="dbt"> | <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black" alt="Power BI"> |

</p>

### 📁 Tools & Technologies

Navigate the stack by layer. Each tool serves a specific role in the pipeline.

```
Transport-Analysis-Data-pipeline/
├── PostgreSQL/                    # Database
├── Apache Airflow/ ✅              # Orchestration & workflow scheduling
├── Google Cloud Storage (GCS)/ ✅  # Data lake
├── Google BigQuery/ ✅             # Data warehouse
├── DBT/ ✅                         # Data modeling & transformation
└── Power BI/                       # Dashboarding & visualization
```

**Selected Stack:** Apache Airflow (Orchestration) → Google Cloud Storage (Data Lake) → Google BigQuery (Data Warehouse) → DBT (Modeling) → Power BI (Visualization)

### By Layer

| Layer           | Tool(s)                                                                 |
|-----------------|-------------------------------------------------------------------------|
| **Database**    | PostgreSQL                                                              |
| **Orchestration** | Apache Airflow ✅                                                      |
| **Data Lake**   | Google Cloud Storage (GCS) ✅                                           |
| **Warehousing** | Google BigQuery ✅                                                      |
| **Modeling**    | DBT (Data Build Tool) ✅                                                |
| **Dashboarding**| Power BI                                                               |

---

## Project Milestones

### Milestone 1: Data Collection, Exploration & Preprocessing
- Ingest transport CSV datasets.
- Explore trends and data properties.

### Milestone 2: Model / System Development & Evaluation
- Build analytical tables and queries in the data warehouse.

### Milestone 3: Deployment (Real-Time or Batch)
- Load data into BigQuery with batch processes using Airflow orchestration.

### Milestone 4: MLOps / Monitoring / Automation
- Automate query refresh schedules.

### Milestone 5: Final Documentation, Demo & Presentation
- Deliver documentation, demo, and presentation materials.

---

## Repository Structure

*(To be updated as the project evolves.)*
