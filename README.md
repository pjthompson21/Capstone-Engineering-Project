# Agentic AI SOC-in-a-Box
Built a virtual Security Operations Center (SOC) lab that demonstrates an end-to-end detection and response pipeline. The system integrates attack simulation, telemetry ingestion, detection engineering, AI-assisted triage, and automated incident response using SOAR workflows.

The goal of the project is to replicate a modern SOC environment with agentic automation layered on top of traditional SIEM operations.

## Functional Capabilities

---

### 🔹Telemetry Pipeline

Designed and validated a reliable log ingestion pipeline where security events from a target environment are consistently collected, normalized, and made searchable for analysis and detection.

---

### 🔹Detection Engineering

Developed and tested 8–10 working detection rules covering authentication, privilege escalation, persistence, and file integrity monitoring. Each detection was validated against controlled attack scenarios to ensure reliability and repeatability.

---

### 🔹Reproducible Attack Simulation

Implemented three fully reproducible attack scenarios using scripted or runbook-based execution:

- Privilege escalation via sudo abuse  
- Persistence via cron job manipulation  
- File integrity violations (create/modify/delete events)

Each scenario generates predictable telemetry for detection and response validation.

---

### 🔹SOAR Automation (n8n Workflows)

Built automated SOAR workflows using n8n to:

- Ingest and parse security alerts  
- Enrich events with contextual metadata  
- Trigger AI-assisted triage workflows  
- Generate structured incident artifacts  
- Trigger response actions based on playbook selection

---

### 🔹Agentic AI Triage System

Implemented an AI-assisted triage layer that processes security alerts and produces structured, validated JSON outputs including:

- Event correlation and evidence extraction (event IDs, timestamps)  
- Classification of attack type and severity  
- Recommended response playbook selection  
- Guarded decision-making to prevent unsafe or unverified actions  

This enables consistent, evidence-driven incident handling aligned with SOC workflows.

---

## Submission Package

[VMs, Project Report, and Video Demo](https://auburn.box.com/s/o8qxyx7kyilt9bospoltq3zlz01tvfct)
