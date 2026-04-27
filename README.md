# 🏦 LoanOracle — ML-Based Loan Prediction & Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**An intelligent loan eligibility screening and advisory system powered by Machine Learning, OCR-based document verification, and Explainable AI.**

*B.Tech Final Year Project — KCG College of Technology, Chennai (Anna University) | April 2026*

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Modules](#-modules)
- [How It Works](#-how-it-works)
- [ML Model Performance](#-ml-model-performance)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Team](#-team)
- [Publication](#-publication)
- [License](#-license)

---

## 📖 Overview

Traditional loan approval processes rely on manual verification, rigid rule-based systems, and subjective officer judgment — leading to slow processing, inconsistent decisions, and poor transparency for applicants.

**LoanOracle** addresses these issues by building an AI-driven loan evaluation platform that:

- Replaces binary approve/reject decisions with **probability-based eligibility scores**
- Uses **OCR** to automatically verify uploaded financial documents
- Applies **Explainable AI (XAI)** to justify every decision with feature-level reasoning
- Provides **personalized advisory recommendations** to help applicants improve their profiles
- Supports **human-in-the-loop** decision making, keeping loan officers in control

> 📄 This project was accepted for presentation at the **NCRPAIDST 2K26 Conference** and is published in the **IEEE Xplore** conference proceedings.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **Role-Based Auth** | Separate portals for Admin/Loan Officers and Customers |
| 📋 **Loan Application** | Structured digital form with real-time client-side validation |
| 📄 **OCR Verification** | Automated extraction and cross-checking of uploaded documents |
| 🤖 **ML Prediction** | Random Forest ensemble model generating loan approval probability |
| 💡 **Explainable AI** | Feature-level explanations for every prediction |
| 📊 **Risk Classification** | Applicants categorized as Low / Moderate / High risk |
| 💬 **LLM Advisory** | Gemini API-powered personalized improvement suggestions |
| 🛡️ **PAN + OTP Auth** | PAN format validation and mobile OTP verification |
| 📈 **Admin Dashboard** | Centralized view with approve/reject controls and audit trail |
| 🗃️ **Audit Logging** | All decisions stored with timestamps for compliance |

---

## 🏛️ System Architecture

LoanOracle uses a **five-layer architecture**:

```
┌──────────────────────────────────────────────┐
│           PRESENTATION LAYER                 │
│   (HTML/CSS/JS + Django Templates)           │
│   Applicant Portal  |  Admin/Officer Portal  │
└─────────────────────┬────────────────────────┘
                      │
┌─────────────────────▼────────────────────────┐
│         SECURITY & AUTHENTICATION LAYER      │
│   PAN Validation | OTP Auth | Role-Based ACL │
└─────────────────────┬────────────────────────┘
                      │
┌─────────────────────▼────────────────────────┐
│       APPLICATION & BUSINESS LOGIC LAYER     │
│   Data Validation | OCR Processing           │
│   Preprocessing | Feature Engineering        │
└─────────────────────┬────────────────────────┘
                      │
┌─────────────────────▼────────────────────────┐
│        INTELLIGENCE & ANALYTICS LAYER        │
│   Random Forest ML Model | XAI Module        │
│   Anomaly Detection | Gemini LLM Advisory    │
└─────────────────────┬────────────────────────┘
                      │
┌─────────────────────▼────────────────────────┐
│           DATA MANAGEMENT LAYER              │
│   MySQL/PostgreSQL | Django ORM | Audit Logs │
└──────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

**Backend**
- Python 3.10+
- Django / Flask
- Scikit-learn (Random Forest, Voting Classifier)
- Tesseract OCR + OpenCV
- Google Gemini API (LLM advisory)

**Frontend**
- HTML5, CSS3, JavaScript
- Bootstrap 5

**Database**
- MySQL / PostgreSQL
- Django ORM

**Tools & Libraries**
- Pandas, NumPy (data processing)
- Joblib / Pickle (model serialization)
- Django REST Framework

---

## 📦 Modules

### 1. Applicant Management Module
Handles user registration, login, profile management, and application history tracking.

### 2. Loan Application Module
Collects structured financial details: income, employment type, existing liabilities, loan amount, and tenure.

### 3. Document Upload & OCR Verification Module
- Accepts salary slips, bank statements, and income certificates
- Uses Tesseract OCR with OpenCV preprocessing
- Cross-verifies extracted data with user inputs
- Flags mismatches for officer review

### 4. Preprocessing & Feature Engineering Module
Derives financial indicators used by the ML model:
- Debt-to-Income (DTI) Ratio
- EMI Burden Ratio
- Repayment Capacity
- Credit Utilization Ratio
- Net Disposable Income

### 5. Machine Learning Prediction Module
- Trained Random Forest / Voting Classifier ensemble
- Outputs probability score `P(y) ∈ [0, 1]`
- Decision logic:
  - `P ≥ 0.75` → High confidence → Auto-process
  - `0.50 ≤ P < 0.75` → Medium confidence → Admin review
  - `P < 0.50` → Low confidence → Rejected / High risk

### 6. Explainable AI (XAI) Module
Identifies key positive and negative features driving each prediction, displayed to both the applicant and the loan officer.

### 7. Loan Officer Review Module
Admin dashboard for reviewing applications, ML scores, OCR results, and XAI explanations — with approve/reject controls.

### 8. Database Management Module
Stores all application records, prediction outputs, XAI logs, and officer decisions with full audit trail support.

---

## ⚙️ How It Works

```
Applicant Registers & Logs In
        │
        ▼
Enters Financial Details + Uploads Documents
        │
        ▼
PAN Validation + OTP Authentication
        │
        ▼
OCR Extracts Document Data → Cross-Verification + Anomaly Detection
        │
        ▼
Preprocessing → Feature Engineering (DTI, EMI Burden, etc.)
        │
        ▼
ML Model Generates Eligibility Probability Score
        │
        ▼
XAI Module Explains Decision Factors
        │
        ▼
Gemini LLM Generates Advisory Recommendations
        │
        ▼
Result Displayed to Applicant
        │
        ▼
Loan Officer Reviews → Final Decision (Approve / Reject / Review)
        │
        ▼
Decision Stored in Database with Audit Log
```

---

## 📊 ML Model Performance

The system uses a **Voting Classifier ensemble** (Random Forest + supporting classifiers) trained on historical loan data.

| Metric | Score |
|---|---|
| **Accuracy** | > 92% |
| **True Positives (Eligible)** | 97 |
| **True Negatives (Not Eligible)** | 85 |
| **Precision** | High |
| **Recall** | High |

> Minor accuracy variations occur with incomplete or inconsistent input data — highlighting the importance of data quality in financial ML systems.

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- pip
- MySQL or PostgreSQL
- Tesseract OCR installed on your system ([installation guide](https://github.com/tesseract-ocr/tesseract))
- Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/loanoracle.git
cd loanoracle
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=loanoracle_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
GEMINI_API_KEY=your_gemini_api_key
TESSERACT_CMD=/usr/bin/tesseract   # Update path as needed
```

### 5. Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Load / Train the ML Model

Place your pre-trained model file (`.pkl`) in the `models/` directory, or run:

```bash
python train_model.py
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🖥️ Usage

### As a Customer
1. Navigate to the **Customer Portal** and register/login
2. Complete PAN validation and OTP verification
3. Fill in the loan application form with your financial details
4. Upload required documents (salary slip, bank statement, ID proof)
5. Submit and view your **eligibility result**, XAI explanation, and advisory recommendations
6. Track your application status (Pending / Accepted / Rejected)

### As an Admin / Loan Officer
1. Log in via the **Admin Portal**
2. View all submitted loan applications on the dashboard
3. Review applicant details, ML scores, OCR verification status, and XAI insights
4. Approve ✔ or Reject ✖ applications

---

## 📁 Project Structure

```
loanoracle/
├── manage.py
├── requirements.txt
├── .env
│
├── user_management/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/                    # Main application
│   ├── models.py             # CustomUser, LoanApplication, Profile
│   ├── views.py              # All view logic
│   ├── urls.py               # URL routing
│   ├── forms.py              # Registration & login forms
│   └── admin.py
│
├── ml/                       # ML components
│   ├── train_model.py        # Model training script
│   ├── predict.py            # Prediction logic
│   └── model.pkl             # Trained model file
│
├── ocr/                      # OCR verification module
│   └── extractor.py
│
├── templates/                # HTML templates
│   ├── login.html
│   ├── dashboard.html
│   ├── loan_form.html
│   ├── result.html
│   └── admin_dashboard.html
│
├── static/                   # CSS, JS, images
│
└── media/                    # Uploaded documents
```

---

## 👥 Team

| Name | Roll Number | Email |
|---|---|---|
| **Ahamed Anas H** | 311022205004 | ahanas2004@gmail.com |
| **Eswaran S** | 311022205011 | exhwar13@gmail.com |
| **Gunaseelan K** | 311022205301 | gunaseelan9384@gmail.com |

**Guide:** Mrs. Suwathi P, Assistant Professor, Dept. of IT, KCG College of Technology

**HOD:** Dr. S. Muthuselvan, Professor & Head, Dept. of IT, KCG College of Technology

---

## 📰 Publication

This project was presented at the **NCRPAIDST 2K26 National Conference** on April 18, 2026.

- **Conference:** NCRPAIDST 2K26
- **Publication:** IEEE Xplore Conference Proceedings
- **Paper Title:** *LoanOracle: Machine Learning-Based Loan Prediction & Management System*
- **Authors:** Ahamed Anas H, Eswaran S, Gunaseelan K, Mrs. Suwathi P, Dr. Adline Freeda R

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by the LoanOracle Team | KCG College of Technology, Chennai | 2026

</div>


---\n*Last updated: 2026-04-27*
