<p align="center">
  <img src="assets/depi-logo.png" alt="DEPI Logo" width="200">
</p>

# Transport Analysis Data Pipeline

Analyze large public transport datasets to gain insights, using cloud data warehouses like **Snowflake**, **Redshift**, or **BigQuery**.

---

## Tech Stack & Tools

### 📁 Tools & Technologies

Navigate the stack by layer. Each tool serves a specific role in the pipeline.

```
Transport-Analysis-Data-pipeline/
├── PostgreSQL/                    # Database
├── Apache Airflow/                 # Orchestration & workflow scheduling
├── AWS (S3, Lake Formation)/       # Data lake
├── Google Cloud (Storage, BigLake)/ # Data lake
├── Azure (Data Lake Storage)/      # Data lake
├── Snowflake/                      # Data warehouse
├── Amazon Redshift/                # Data warehouse
├── Google BigQuery/                # Data warehouse
├── DBT/                            # Data modeling & transformation
└── Power BI/                       # Dashboarding & visualization
```

*Data lake: use AWS, Google Cloud, or Azure depending on your environment. Warehousing: use Snowflake, BigQuery, or Redshift.*

### By Layer

| Layer           | Tool(s)                                                                 |
|-----------------|-------------------------------------------------------------------------|
| **Database**    | PostgreSQL                                                              |
| **Orchestration** | Apache Airflow                                                        |
| **Data Lake**   | AWS (S3, Lake Formation), Google Cloud (Cloud Storage, BigLake), Azure (Data Lake Storage) |
| **Warehousing** | Snowflake, BigQuery, or Amazon Redshift                                |
| **Modeling**    | DBT (Data Build Tool)                                                  |
| **Dashboarding**| Power BI                                                               |

---

## Project Milestones

### Milestone 1: Data Collection, Exploration & Preprocessing
- Ingest transport CSV datasets.
- Explore trends and data properties.

### Milestone 2: Model / System Development & Evaluation
- Build analytical tables and queries in the data warehouse.

### Milestone 3: Deployment (Real-Time or Batch)
- Load data into Snowflake, BigQuery, or Redshift with batch processes.

### Milestone 4: MLOps / Monitoring / Automation
- Automate query refresh schedules.

### Milestone 5: Final Documentation, Demo & Presentation
- Deliver documentation, demo, and presentation materials.

---

## Repository Structure

*(To be updated as the project evolves.)*
