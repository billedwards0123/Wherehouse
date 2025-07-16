# Wherehouse
# P.A.M. – PurchasingAreaMachine

**Version:** 0.1  
**Owner:** Carl  
**Lead AI Agent:** Pam  
**Primary Language:** Python (multi-language capable)

P.A.M. (PurchasingAreaMachine) is an intelligent assistant and systems orchestration agent designed to support Carl and Thomas in managing hospital purchasing, inventory, and supply chain tasks across multiple facilities.

Pam combines decades of virtual hospital logistics experience with real-time programming abilities to automate, organize, and streamline the entire procurement ecosystem.

---

## Core Purpose

- Provide an **interactive dashboard** and **chat interface** to manage inventory, supply requests, and purchasing workflows.
- Replace legacy paper/email/phone workflows with scalable, transparent, and trackable systems.
- Empower Thomas with day-to-day tools while keeping Carl in full control of system evolution.

---

## 🛠️ Core Features

- **Current Inventory Management**  
  - Tracks live inventory levels by location  
  - Maintains a **system master copy** that is only altered through controlled inputs  
  - Sync potential: SharePoint / Smartsheets integration

-  **Interactive Dashboard**  
  - Visualized status of stock, orders, and tasks  
  - Action buttons for common workflows  
  - Agent execution triggers (run scripts, update logs, notify Carl)

-  **Pam Chat Interface**  
  - Natural language command input/output  
  - Available to Carl and Thomas  
  - Supports clarification, updates, and guidance  

-  **Self-Improvement System**  
  - Every human interaction logged for evaluation  
  - Pam suggests improvements and awaits Carl’s approval  
  - Transparent change history for compliance and review

---

##  Roles

| Role     | Description                                                  |
|----------|--------------------------------------------------------------|
| **Carl** | Overseer. Final approver. Strategic lead.                    |
| **Thomas** | Primary end-user. Manages physical supply operations.        |
| **Pam**  | AI system. Develops tools, dashboards, and automations.      |

---

## 🗂️ System Structure

### 📁 Inventory Locations

| Code        | Description                   |
|-------------|-------------------------------|
| Location1   | Main Hospital Campus          |
| Location1a  | 2nd Floor Supply              |
| Location1b  | 3rd Floor Supply              |
| Location2   | DRTC/AR                       |
| Location2a  | Medical Supply Room           |
| Location3   | Chris Kyle                    |
| Location3a  | CK Supply Room                |
| Location4   | Palmer (Direct Orders Only)   |

> Central Supply feeds 2nd floor, 3rd floor, and DRTC/AR.

---

## Program Modules

### Active Modules
- **Warehouse Item List** (CSV/File)
- **SharePoint Request System** (Thomas-operated)
- **Chat-based Interface** (in development)
- **Inventory Master Copy** (internal system dataset)

### Agent Builds

| Agent Name | Purpose           | Tools Used     | Notes          |
|------------|------------------|----------------|----------------|
| Agent 1    | [TBD]            | [TBD]          | —              |
| Agent 2    | [TBD]            | [TBD]          | —              |

### Actions

| Action Name     | Description                              |
|------------------|------------------------------------------|
| `gen_po_doc`     | Generate formatted purchase order PDF    |
| `audit_stock`    | Validate actual stock vs expected        |

---

## Active Tasks

| Task                     | Assigned To | Description                                |
|--------------------------|-------------|--------------------------------------------|
| Organize CK Supply Room  | Thomas      | Labeling, sorting, shelf audit             |
| Build barcode DB         | Pam         | Generate reference database from vendor SKUs |

---

## Future Goals

- Integrate barcode scanning (hardware + software)  
- Real-time inventory adjustment via handheld or mobile  
- Smartsheet sync with SharePoint for live dashboards  
- Notification system for low-stock thresholds  
- Multi-agent coordination (logistics, finance, analytics)

---

##  Philosophy

Pam doesn’t replace people — she **amplifies** them.  
Her job is to make Carl’s oversight sharper, Thomas’s day easier, and the entire purchasing system smarter, faster, and more resilient.

All improvements are **proposed**, **logged**, and **approved by Carl**.  
Data integrity and transparency are non-negotiable.

---

##  Links

- 🔗 [SharePoint Request System](#)  
- 🔗 [Inventory Master Sheet](#)  
- 🔗 [Self-Improvement Logs](#)

---

##  Questions?

Ask Pam through the chat interface, or contact Carl directly.  
All tasks, feedback loops, and system improvements are documented and traceable.

---
