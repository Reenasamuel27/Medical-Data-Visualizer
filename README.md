# Medical-Data-Visualizer
This project visualizes and analyzes medical examination data using **pandas**, **matplotlib**, and **seaborn**. The data includes body measurements, blood test results, and lifestyle choices for patients, helping identify patterns related to cardiovascular disease.

---

## 📁 Dataset

- **File**: `medical_examination.csv`
- **Rows**: Each represents a patient
- **Columns**: Include objective measurements, examination results, lifestyle choices, and a target variable (`cardio`) indicating the presence of heart disease.

### 🔍 Features:

| Feature | Description |
|--------|-------------|
| age | Age in days |
| height | Height in cm |
| weight | Weight in kg |
| gender | Gender code |
| ap_hi | Systolic blood pressure |
| ap_lo | Diastolic blood pressure |
| cholesterol | 1: normal, 2: above normal, 3: well above normal |
| gluc | 1: normal, 2: above normal, 3: well above normal |
| smoke | 0: no, 1: yes |
| alco | 0: no, 1: yes |
| active | 0: no, 1: yes |
| cardio | 0: no disease, 1: has disease |

---

## 🚀 Project Tasks

### 1. Data Preparation
- Added an `overweight` column based on BMI (`>25` → 1, else 0).
- Normalized `cholesterol` and `gluc` to make `0 = good` and `1 = bad`.

### 2. Categorical Plot
- Melted the data to long format.
- Created a bar chart showing counts of each health/lifestyle factor, separated by presence of heart disease.

### 3. Heatmap
- Cleaned data:
  - Removed outliers in height and weight.
  - Removed invalid blood pressure values.
- Calculated correlations.
- Plotted a heatmap to show relationships between medical features.

---

## 📊 Visualizations

### 🔹 Categorical Plot
Displays the distribution of features (`cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`) by disease status (`cardio`).

### 🔹 Heatmap
Shows the correlation matrix for all numeric features, highlighting strong and weak relationships.

---

## 🛠 How to Run

### ✅ Requirements
Make sure you have the following libraries installed:
```bash
pip install pandas seaborn matplotlib numpy
▶️ Run the Visualizer
You can test your code using main.py:

bash
Copy
Edit
python main.py
This will:

Generate and display the categorical plot

Generate and display the heatmap

🧪 Testing
Unit tests are located in test_module.py. They validate the correctness of data processing and visual output. These tests are run automatically via main.py.

✅ Submitting
Once you're done:

Push your project to GitHub.

Copy the repository link.

Submit it on the freeCodeCamp portal.

📚 Credits
Project inspired by the freeCodeCamp Data Analysis with Python course.

