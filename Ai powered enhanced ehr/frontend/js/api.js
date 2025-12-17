/**
 * EHR GenAI - API Integration Layer
 * Handles all communication with FastAPI backend
 */

const API_BASE = 'http://localhost:8000';

// Check if API is running
async function checkHealth() {
    try {
        const response = await fetch(`${API_BASE}/health`, {
            method: 'GET',
            mode: 'cors'
        });
        if (!response.ok) throw new Error('API not responding');
        return await response.json();
    } catch (error) {
        console.error('Health check failed:', error);
        return { status: 'error', message: error.message };
    }
}

// Enhance medical image
async function enhanceImage(file) {
    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${API_BASE}/enhance-image`, {
            method: 'POST',
            body: formData,
            mode: 'cors'
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Image enhancement failed');
        }

        return await response.json();
    } catch (error) {
        console.error('Image enhancement error:', error);
        throw error;
    }
}

// Generate clinical note with ICD-10 coding
async function generateNote(patientData) {
    try {
        const response = await fetch(`${API_BASE}/generate-note`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(patientData),
            mode: 'cors'
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Note generation failed');
        }

        return await response.json();
    } catch (error) {
        console.error('Note generation error:', error);
        throw error;
    }
}

// Load sample patient records from JSON
async function loadPatientRecords() {
    try {
        const response = await fetch(`${API_BASE}/records`);
        if (!response.ok) throw new Error('Could not load records');
        return await response.json();
    } catch (error) {
        console.error('Failed to load patient records:', error);
        throw error;
    }
}

// Export functions
window.EHRApi = {
    checkHealth,
    enhanceImage,
    generateNote,
    loadPatientRecords,
    API_BASE
};
