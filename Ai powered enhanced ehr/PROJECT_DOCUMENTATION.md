# AI-Powered Enhanced EHR Imaging & Documentation System
## Complete Project Documentation

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [System Architecture](#2-system-architecture)
3. [Technologies Used](#3-technologies-used)
4. [Project Structure](#4-project-structure)
5. [Installation Guide](#5-installation-guide)
6. [Configuration](#6-configuration)
7. [Running the Application](#7-running-the-application)
8. [API Documentation](#8-api-documentation)
9. [Frontend Guide](#9-frontend-guide)
10. [Module Details](#10-module-details)
11. [Data Files](#11-data-files)
12. [Troubleshooting](#12-troubleshooting)
13. [Future Enhancements](#13-future-enhancements)

---

## 1. Project Overview

### 1.1 Introduction

This project is an **AI-Powered Enhanced Electronic Health Records (EHR) System** that leverages Generative AI to improve medical workflows. It combines:

- **Medical Image Enhancement**: Improving the quality of MRI, X-ray, and CT scans using computer vision techniques
- **Automated Clinical Note Generation**: Using GPT-4o-mini to generate professional clinical notes from patient data
- **Automated ICD-10 Coding**: Automatically assigning standardized medical diagnosis codes

### 1.2 Problem Statement

Healthcare professionals spend significant time on:
- Interpreting low-quality medical images
- Writing repetitive clinical documentation
- Manually assigning diagnosis codes

This system aims to reduce administrative burden and improve diagnostic accuracy.

### 1.3 Key Features

| Feature | Description |
|---------|-------------|
| Image Enhancement | CLAHE + Sharpening for improved image clarity |
| Clinical Notes | AI-generated OPD-style notes in 4-6 sentences |
| ICD-10 Coding | Automatic code assignment (C71.9, D33.9, Z03.8, etc.) |
| REST API | FastAPI-based endpoints for integration |
| Web Dashboard | Modern dark-mode interface for all features |

### 1.4 Expected Outcomes

- ✅ Improved interpretation of medical images through AI-driven enhancement
- ✅ Significant reduction in documentation time
- ✅ Streamlined ICD-10 coding integrated into clinical workflows
- ✅ Greater focus on patient care by minimizing administrative efforts

---

## 2. System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │Dashboard │ │ Image    │ │ Clinical │ │ Patient  │           │
│  │          │ │ Enhance  │ │ Notes    │ │ Records  │           │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘           │
│       │            │            │            │                   │
│       └────────────┴────────────┴────────────┘                   │
│                         │                                        │
│                    HTTP Requests                                 │
│                         │                                        │
└─────────────────────────┼───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FASTAPI BACKEND                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                      api.py                              │    │
│  │  ┌──────────┐ ┌────────────────┐ ┌─────────────────┐   │    │
│  │  │ /health  │ │ /enhance-image │ │ /generate-note  │   │    │
│  │  └──────────┘ └───────┬────────┘ └────────┬────────┘   │    │
│  └───────────────────────┼────────────────────┼─────────────┘    │
│                          │                    │                  │
│  ┌───────────────────────┴────────────────────┴─────────────┐   │
│  │                      utils.py                             │   │
│  │  ┌──────────────────┐    ┌─────────────────────────┐    │   │
│  │  │ enhance_image()  │    │ generate_note()         │    │   │
│  │  │ - CLAHE          │    │ - OpenAI GPT-4o-mini    │    │   │
│  │  │ - Sharpening     │    │ - ICD-10 Assignment     │    │   │
│  │  └──────────────────┘    └─────────────────────────┘    │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                  │
│  ┌───────────────┐ ┌───────────────┐ ┌───────────────────────┐ │
│  │ mapping.csv   │ │ Clinical      │ │ MRI Images            │ │
│  │ (20K records) │ │ Notes JSON    │ │ (original + enhanced) │ │
│  └───────────────┘ └───────────────┘ └───────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Technologies Used

### 3.1 Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Core programming language |
| FastAPI | Latest | REST API framework |
| Uvicorn | Latest | ASGI server for FastAPI |
| OpenAI | Latest | GPT-4o-mini for note generation |
| OpenCV | Latest | Image processing (CLAHE, sharpening) |
| NumPy | Latest | Numerical operations |
| Pillow | Latest | Image handling |
| python-dotenv | Latest | Environment variable management |
| Pydantic | Latest | Data validation |

### 3.2 Frontend Technologies

| Technology | Purpose |
|------------|---------|
| HTML5 | Page structure |
| CSS3 | Styling with CSS variables |
| Vanilla JavaScript | Interactivity and API calls |
| Google Fonts (Inter) | Typography |

### 3.3 AI/ML Technologies

| Technology | Purpose |
|------------|---------|
| OpenAI GPT-4o-mini | Clinical note generation |
| CLAHE Algorithm | Contrast enhancement |
| Real-ESRGAN (notebooks) | Super-resolution training |

### 3.4 Development Tools

| Tool | Purpose |
|------|---------|
| Google Colab | Notebook execution |
| Jupyter Notebook | Data preprocessing |
| Kaggle Datasets | Training data source |

---

## 4. Project Structure

```
e:\Code and Use cases\Ai powered enhanced ehr\
│
├── api/                          # Backend API
│   ├── api.py                    # FastAPI endpoints
│   └── utils.py                  # Image enhancement & note generation
│
├── frontend/                     # Web Dashboard
│   ├── index.html                # Dashboard/Home page
│   ├── enhance.html              # Image enhancement page
│   ├── generate.html             # Clinical note generator
│   ├── records.html              # Patient records viewer
│   ├── css/
│   │   └── styles.css            # Complete design system (700+ lines)
│   └── js/
│       ├── api.js                # API integration layer
│       └── app.js                # Shared utilities
│
├── notebooks/                    # Jupyter Notebooks
│   ├── 01_data_prep.ipynb        # Data preprocessing & ICD-10 mapping
│   └── 02_enhancing_images.ipynb # Real-ESRGAN training pipeline
│
├── data/                         # Data files
│   ├── mapping.csv               # 20,000 EHR records with ICD-10
│   ├── original_images/          # 15 sample MRI images
│   ├── enhanced_images/          # 15 enhanced MRI images
│   ├── INPUT_FOR_AI.csv          # AI input data (CSV format)
│   ├── INPUT_FOR_AI.json         # AI input data (JSON format)
│   ├── FINAL_CLINICAL_NOTES.json # Generated clinical notes (15 samples)
│   └── FINAL_EVALUATION_REPORT.xlsx # ICD-10 accuracy metrics
│
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── .gitignore                    # Git ignore rules
├── README.md                     # Quick start guide
└── PROJECT_DOCUMENTATION.md      # This file
```

---

## 5. Installation Guide

### 5.1 Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **OpenAI API Key** (for clinical note generation)
- **Modern web browser** (Chrome, Firefox, Edge)

### 5.2 Step-by-Step Installation

#### Step 1: Clone/Download the Project

```bash
# If using Git
git clone <repository-url>
cd "Ai powered enhanced ehr"

# Or download and extract the ZIP file
```

#### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- fastapi
- uvicorn[standard]
- openai
- python-dotenv
- opencv-python-headless
- pillow
- numpy
- pydantic
- python-multipart

#### Step 4: Verify Installation

```bash
python -c "import fastapi, cv2, openai; print('All packages installed successfully!')"
```

---

## 6. Configuration

### 6.1 Environment Variables

Create a `.env` file in the `api/` directory:

```bash
cd api
cp ../.env.example .env
```

Edit the `.env` file:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

### 6.2 Getting an OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to **API Keys** section
4. Click **Create new secret key**
5. Copy the key and paste into `.env`

### 6.3 Configuration Options

| Variable | Required | Description |
|----------|----------|-------------|
| OPENAI_API_KEY | Optional* | Required for clinical note generation |

*Note: Image enhancement works without the API key.

---

## 7. Running the Application

### 7.1 Start the Backend API

```bash
cd api
python -m uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Will watch for changes in these directories: [...]
WARNING:  OPENAI_API_KEY not found! Clinical note generation will not work.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...]
INFO:     Application startup complete.
```

### 7.2 Open the Frontend

#### Option A: Direct File Access
1. Navigate to `frontend/` folder in File Explorer
2. Double-click `index.html`
3. The dashboard opens in your default browser

#### Option B: Python HTTP Server
```bash
cd frontend
python -m http.server 3000
```
Then open `http://localhost:3000` in your browser.

### 7.3 Verify Everything Works

1. **Check API**: Visit `http://localhost:8000/docs` for Swagger UI
2. **Check Frontend**: Look for green "Online" badge in sidebar
3. **Test Health**: `http://localhost:8000/health` should return `{"status":"ok"}`

---

## 8. API Documentation

### 8.1 Base URL

```
http://localhost:8000
```

### 8.2 Endpoints

#### GET /health
Check if the API is running.

**Response:**
```json
{
  "status": "ok"
}
```

---

#### POST /enhance-image
Enhance a medical image using CLAHE and sharpening.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (image file - PNG, JPG, etc.)

**Example (cURL):**
```bash
curl -X POST "http://localhost:8000/enhance-image" \
  -F "file=@brain_mri.png"
```

**Response:**
```json
{
  "enhanced_image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

**Usage:**
```javascript
// Convert base64 to image
const img = document.createElement('img');
img.src = `data:image/png;base64,${response.enhanced_image_base64}`;
```

---

#### POST /generate-note
Generate a clinical note with ICD-10 code.

**Request:**
- Content-Type: `application/json`
- Body:

```json
{
  "patient_id": "P001",
  "age": 45,
  "gender": "Male",
  "chief_complaint": "Persistent headache for 2 weeks",
  "history": "No prior neurological conditions",
  "observations": "MRI shows irregular enhancing lesion in right temporal lobe",
  "prelim_diagnosis": "Brain tumor suspected"
}
```

**Response (with API key):**
```json
{
  "patient_id": "P001",
  "note": "45-year-old male presents with persistent headache for 2 weeks...",
  "icd10": [
    {
      "code": "C71.9",
      "description": "Malignant neoplasm of brain, unspecified"
    }
  ]
}
```

**Response (without API key):**
```json
{
  "patient_id": "P001",
  "note": "ERROR: OpenAI API key not configured...",
  "icd10": [
    {
      "code": "ERROR",
      "description": "API key missing"
    }
  ]
}
```

### 8.3 Interactive API Docs

Visit `http://localhost:8000/docs` for Swagger UI with interactive testing.

---

## 9. Frontend Guide

### 9.1 Dashboard (index.html)

**Features:**
- System status overview
- API connection indicator
- Quick stats (Image AI, GPT-4o, ICD-10, Records)
- Quick action buttons
- Module descriptions

**URL:** `frontend/index.html`

---

### 9.2 Image Enhancement (enhance.html)

**Features:**
- Drag-and-drop image upload
- Side-by-side comparison (Original vs Enhanced)
- Download enhanced image button
- Technology explanation

**How to Use:**
1. Drop an MRI/X-ray image or click to browse
2. Wait for processing (spinner shown)
3. View enhanced result alongside original
4. Click "Download Enhanced" to save

**URL:** `frontend/enhance.html`

---

### 9.3 Clinical Notes (generate.html)

**Features:**
- Patient information form
- Quick-fill sample data buttons
- AI-generated clinical note display
- ICD-10 code badge
- Copy to clipboard

**Form Fields:**
| Field | Type | Required | Example |
|-------|------|----------|---------|
| Patient ID | Text | Yes | P001 |
| Age | Number | Yes | 45 |
| Gender | Select | Yes | Male/Female/Other |
| Chief Complaint | Text | Yes | Persistent headache |
| Medical History | Textarea | No | No prior conditions |
| MRI Observations | Textarea | Yes | Irregular lesion seen |
| Preliminary Diagnosis | Text | Yes | Brain tumor suspected |

**URL:** `frontend/generate.html`

---

### 9.4 Patient Records (records.html)

**Features:**
- Table of 15 sample clinical records
- Search by name, diagnosis, or ICD code
- Filter by diagnosis type
- Detail modal with full information
- Copy record to clipboard

**Data Source:** `data/FINAL_CLINICAL_NOTES.json`

**URL:** `frontend/records.html`

---

## 10. Module Details

### 10.1 Module 1: Data Collection & Preprocessing

**Notebook:** `notebooks/01_data_prep.ipynb`

**Tasks Completed:**
- Collected 20,000 EHR records from Kaggle
- Processed 21,672 MRI brain tumor images
- Created ICD-10 code mappings:
  - C71.9 = Malignant neoplasm of brain
  - D33.9 = Benign neoplasm of brain
  - Z03.8 = Observation for other suspected conditions

**Output Files:**
- `data/mapping.csv` (2.7 MB)

---

### 10.2 Module 2: Medical Imaging Enhancement

**Notebook:** `notebooks/02_enhancing_images.ipynb`

**Technologies:**
- Real-ESRGAN for super-resolution
- CLAHE for contrast enhancement
- Sharpening kernel for edge enhancement

**API Implementation:** `api/utils.py` → `enhance_image()`

```python
def enhance_image(image_bytes):
    # 1. Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    
    # 2. Apply Sharpening
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    enhanced = cv2.filter2D(enhanced, -1, kernel)
    
    return enhanced_bytes
```

**Metrics Collected:**
- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)

---

### 10.3 Module 3: Clinical Note Generation & ICD-10 Coding

**Notebook:** Referenced in `03_clinical_note_generation.ipynb` (in original milestone)

**API Implementation:** `api/utils.py` → `generate_note()`

**AI Model:** OpenAI GPT-4o-mini

**Prompt Template:**
```
You are a senior neurologist writing a short, crisp OPD clinical note.

Patient: [Name], [Age]-year-old [Gender]
Chief Complaint: [Symptoms]
MRI Brain: [Findings]
Provisional Diagnosis: [Diagnosis]

Write a concise, professional clinical note in 4–6 sentences only.
Then give ONLY ONE correct ICD-10 code.
```

**Output Format:**
```json
{
  "clinical_note": "...",
  "icd10_code": "C71.9",
  "icd10_description": "Malignant neoplasm of brain, unspecified"
}
```

---

### 10.4 Module 4: Integration & Deployment

**Components:**
- FastAPI REST API (`api/api.py`)
- CORS middleware for frontend access
- Frontend web dashboard (HTML/CSS/JS)

**API Endpoints:**
- `GET /health` - Health check
- `POST /enhance-image` - Image enhancement
- `POST /generate-note` - Note generation

---

## 11. Data Files

### 11.1 mapping.csv

**Location:** `data/mapping.csv`
**Size:** 2.7 MB
**Records:** 20,000

**Columns:**
| Column | Description |
|--------|-------------|
| Patient_ID | Unique patient identifier |
| Age | Patient age |
| Gender | Male/Female |
| Tumor_Size(cm) | Tumor size in centimeters |
| Tumor_Type | Benign/Malignant |
| Biopsy_Result | Positive/Negative |
| Treatment | Surgery/Chemotherapy/Radiation |
| Response_to_Treatment | Complete/Partial/None |
| Survival_Status | Survived/Deceased |
| ICD-10 | Diagnosis code |

---

### 11.2 FINAL_CLINICAL_NOTES.json

**Location:** `data/FINAL_CLINICAL_NOTES.json`
**Records:** 15 sample patients

**Schema:**
```json
{
  "patient_id": 10651,
  "patient_name": "Priya Sharma",
  "age": 60,
  "gender": "Female",
  "provisional_diagnosis": "Benign Brain Tumor",
  "symptoms": "Occasional dizziness",
  "mri_findings": "Smooth, homogeneous lesion...",
  "clinical_note": "Priya Sharma, a 60-year-old female...",
  "icd10_code": "D33.9",
  "icd10_description": "Benign neoplasm of brain, unspecified"
}
```

---

### 11.3 Sample Images

**Location:** `data/original_images/` and `data/enhanced_images/`
**Count:** 15 pairs (original + enhanced)
**Format:** PNG
**Source:** Brain Tumors MRI Dataset (Kaggle)

---

## 12. Troubleshooting

### 12.1 API Won't Start

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
pip install -r requirements.txt
```

---

**Error:** `OPENAI_API_KEY not found`

**Solution:**
This is a warning, not an error. The API will still start. Image enhancement works without the key.

---

### 12.2 Frontend Can't Connect to API

**Error:** API Status shows "Offline"

**Solutions:**
1. Ensure API is running on port 8000
2. Check for CORS errors in browser console
3. Try running frontend with Python HTTP server instead of file://

---

### 12.3 Image Enhancement Fails

**Error:** `Enhancement failed, returning original`

**Solutions:**
1. Ensure image is valid (PNG, JPG)
2. Check file size (not too large)
3. Verify OpenCV is installed correctly

---

### 12.4 Clinical Notes Return Error

**Error:** `ERROR: OpenAI API key not configured`

**Solution:**
1. Create `api/.env` file
2. Add `OPENAI_API_KEY=sk-your-key`
3. Restart the API server

---

## 13. Future Enhancements

### Short-term

- [ ] Add user authentication
- [ ] Support more image formats (DICOM)
- [ ] Export clinical notes as PDF
- [ ] Batch image processing

### Long-term

- [ ] Azure deployment guide
- [ ] Hospital EHR system integration (HL7/FHIR)
- [ ] Multi-language clinical notes
- [ ] Advanced AI models (GPT-4 Vision for image analysis)
- [ ] Real-time collaboration features

---

## Contributors

- **Afreen** - Data Preprocessing, Image Enhancement, Clinical Note Generation, API Development
- **Team B** - Enhancing EHRs with GenAI Project

---

## License

This project is for educational purposes as part of the "Enhancing EHRs with GenAI" curriculum.

---

## Contact & Support

For issues or questions, please refer to the troubleshooting section or contact the project maintainers.

---

*Last Updated: December 2024*
