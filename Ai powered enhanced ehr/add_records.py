import json
import os

file_path = 'data/FINAL_CLINICAL_NOTES.json'

new_records = [
    {
        "patient_id": 99001,
        "patient_name": "Vikram Malhotra",
        "age": 58,
        "gender": "Male",
        "provisional_diagnosis": "Malignant Brain Tumor",
        "symptoms": "Severe morning headaches, nausea, visual disturbances",
        "mri_findings": "Large enhancing mass in right parietal lobe with central necrosis and surrounding edema.",
        "clinical_note": "Vikram Malhotra, 58-year-old male, presents with severe morning headaches and visual disturbances. MRI reveals a large enhancing mass in the right parietal lobe with features suggestive of a high-grade glioma (Glioblastoma). Immediate neurosurgical and oncological consultation is required. Starting dexamethasone for edema management.",
        "icd10_code": "C71.3",
        "icd10_description": "Malignant neoplasm of parietal lobe"
    },
    {
        "patient_id": 99002,
        "patient_name": "Anjali Desai",
        "age": 34,
        "gender": "Female",
        "provisional_diagnosis": "Benign Brain Tumor",
        "symptoms": "Unilateral hearing loss, mild imbalance",
        "mri_findings": "Well-circumscribed mass in the left cerebellopontine angle, enhancing homogeneously.",
        "clinical_note": "Anjali Desai, 34-year-old female, presents with left-sided hearing loss and mild imbalance. MRI shows a well-circumscribed lesion in the left cerebellopontine angle, consistent with valid Vestibular Schwannoma (Acoustic Neuroma). The lesion appears benign. Management options including observation vs. radiosurgery discussed.",
        "icd10_code": "D33.3",
        "icd10_description": "Benign neoplasm of cranial nerves"
    },
    {
        "patient_id": 99003,
        "patient_name": "Rahul Verma",
        "age": 29,
        "gender": "Male",
        "provisional_diagnosis": "No Tumor",
        "symptoms": "Band-like tightness around head, stress related",
        "mri_findings": "Normal brain parenchyma. No intracranial mass or abnormal enhancement.",
        "clinical_note": "Rahul Verma, 29-year-old male, complains of chronic band-like headache exacerbated by work stress. Neurological exam is normal. MRI Brain is completely normal, ruling out intracranial pathology. Diagnosis is Tension-Type Headache. Reassured patient. Prescribed analgesics and stress management techniques.",
        "icd10_code": "G44.2",
        "icd10_description": "Tension-type headache"
    }
]

try:
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Append new records
    data.extend(new_records)
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
        
    print("Successfully added 3 new records.")
except Exception as e:
    print(f"Error: {e}")
