
# AWS Real-Time Data Pipeline with Kinesis, Lambda, S3, Glue, Athena & QuickSight

## 🚀 Project Overview

This project demonstrates a **real-time data pipeline** built on AWS using the following services:

- Amazon Kinesis Data Streams
- AWS Lambda
- Amazon S3
- AWS Glue
- Amazon Athena
- Amazon QuickSight

The pipeline captures user activity data, processes and stores it, and visualizes it in a live dashboard.

---

## 📌 Architecture Diagram



---

## 🛠️ Services Used

- **Amazon Kinesis** – For ingesting streaming data
- **AWS Lambda** – To process and send data to S3
- **Amazon S3** – Storage layer for processed data
- **AWS Glue** – Crawls and catalogs S3 data into a table
- **Amazon Athena** – Queries the cataloged data
- **Amazon QuickSight** – Visualizes the queried data in a live dashboard

---

## 📂 Project Structure

```
aws-kinesis-data-pipeline/
├── lambda/
│   └── stream_to_s3.py
├── README.md
└── architecture-diagram.png
```

---

## 📦 End-to-End Implementation Steps

### 1. **Create an S3 Bucket**

- Name: `user-activity-processed-data`
- Enable versioning (optional)

### 2. **Create a Kinesis Data Stream**

- Name: `user-activity-stream`
- Shard count: 1 (adjustable)

### 3. **Deploy AWS Lambda Function**

- Trigger: Kinesis stream
- Logic:
  - Reads records from Kinesis
  - Parses and pushes to S3 in JSON format
  - S3 Prefix: `user-events/yyyy-mm-dd/`

Example code: `lambda/stream_to_s3.py`

### 4. **Push Sample Data to Kinesis**

Use AWS CLI or Python script:

```bash
aws kinesis put-record   --stream-name user-activity-stream   --partition-key 1234   --data '{"event": "login", "user_id": "u1"}'
```

### 5. **Verify Data in S3**

Navigate to `user-activity-processed-data/user-events/yyyy-mm-dd/`

### 6. **Create AWS Glue Crawler**

- Data source: S3 (same prefix as Lambda output)
- Target: New database `user_activity`
- Table name: `user_activity_user_events`
- Run once to create schema

### 7. **Query Data with Athena**

Sample query:

```sql
SELECT event, COUNT(*) AS total_events
FROM user_activity_user_events
GROUP BY event;
```

- Athena reads live data from S3 prefix, even if Glue crawler ran once

### 8. **Configure QuickSight Dashboard**

- Enable access to Athena and S3 buckets (`user-activity-processed-data`, `athena-results`)
- Create dataset from Athena table
- Visualize results (bar charts, pie charts, etc.)

> **Note**: QuickSight pulls live data from the underlying S3 via Athena table

---

## 🧠 Key Takeaways

- Kinesis + Lambda enables real-time ingestion and processing
- S3 acts as a data lake for raw/processed events
- Glue crawlers help create schema and table in AWS Glue Data Catalog
- Athena queries S3 directly using the Glue schema
- QuickSight visualizes dynamic, live data in dashboards

---

## 🧹 Future Enhancements

- Add partitioning (`dt=yyyy-mm-dd`) in S3 for cost-efficient queries
- Automate Glue crawler or use `MSCK REPAIR TABLE` to manage partitions
- Use Kinesis Firehose for simplified delivery (optional)
- Schedule QuickSight refresh every 15 min (if needed)

---

## 📸 Screenshots

> 📁 Add screenshots of:

- S3 Data Landing
- Athena Query Results
- QuickSight Dashboard

---

## 🤝 Contributors

- **Sawan** – AWS Cloud Developer

---

## 📄 License

MIT License
