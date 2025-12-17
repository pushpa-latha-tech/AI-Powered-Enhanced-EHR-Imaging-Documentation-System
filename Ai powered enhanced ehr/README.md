# Enhancing EHRs with GenAI

AI-powered Electronic Health Records enhancement system that combines medical image processing, clinical note generation, and ICD-10 code assignment using GPT-4.

## Features

- **Data Preprocessing**: EHR and MRI image preprocessing with ICD-10 mapping
- **Image Enhancement**: Real-ESRGAN based MRI image enhancement (CLAHE + sharpening)
- **Clinical Note Generation**: AI-generated OPD-style clinical notes using GPT-4o-mini
- **ICD-10 Coding**: Automatic ICD-10 code assignment with safety evaluation
- **FastAPI Backend**: RESTful API for image enhancement and note generation
- **Modern Web Dashboard**: Dark-mode medical dashboard for easy access to all features

## Project Structure

```
├── api/
│   ├── api.py              # FastAPI server endpoints
│   └── utils.py            # Image enhancement & note generation utilities
├── frontend/
│   ├── index.html          # Dashboard
│   ├── enhance.html        # Image enhancement page
│   ├── generate.html       # Clinical note generator
│   ├── records.html        # Patient records viewer
│   ├── css/styles.css      # Design system
│   └── js/                 # JavaScript modules
├── notebooks/
│   ├── 01_data_prep.ipynb          # Data preprocessing & ICD-10 mapping
│   └── 02_enhancing_images.ipynb   # Real-ESRGAN image enhancement pipeline
├── data/
│   ├── mapping.csv                 # ICD-10 code mappings (20,000 records)
│   ├── original_images/            # Original MRI images
│   ├── enhanced_images/            # Enhanced MRI images
│   ├── INPUT_FOR_AI.csv/json       # AI input data
│   ├── FINAL_CLINICAL_NOTES.json   # Generated clinical notes
│   └── FINAL_EVALUATION_REPORT.xlsx # ICD-10 accuracy evaluation
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env
   ```

3. **Run the API server**:
   ```bash
   cd api
   uvicorn api:app --reload
   ```

4. **Open the Frontend**:
   ```bash
   # Option A: Simply open in browser
   # Navigate to frontend/index.html in your file explorer and double-click

   # Option B: Use Python's built-in server
   cd frontend
   python -m http.server 3000
   # Then open http://localhost:3000 in your browser
   ```

## API Endpoints

### Health Check
```
GET /health
```

### Enhance Image
```
POST /enhance-image
Content-Type: multipart/form-data
Body: file (MRI image)
Response: { "enhanced_image_base64": "..." }
```

### Generate Clinical Note
```
POST /generate-note
Content-Type: application/json
Body: {
  "patient_id": "P001",
  "age": 45,
  "gender": "Male",
  "chief_complaint": "Persistent headache",
  "history": "No prior history",
  "observations": "MRI shows abnormality",
  "prelim_diagnosis": "Brain tumor suspected"
}
Response: { "patient_id": "...", "note": "...", "icd10": [...] }
```

## Datasets

- **EHR Dataset**: 20,000 rows of cancer/tumor data ([Kaggle](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset))
- **Brain Tumors MRI Dataset**: ~21,672 JPEG images ([Kaggle](https://www.kaggle.com/datasets/mohammadhossein77/brain-tumors-dataset))

## Technologies

- Python, FastAPI, OpenAI GPT-4o-mini
- OpenCV, PIL, NumPy
- Real-ESRGAN, PyTorch
- Pandas, NLTK

## Contributors

- **Afreen** - Data Preprocessing, Image Enhancement, Clinical Note Generation, API Development
- **Team B** - Enhancing EHRs with GenAI Project
