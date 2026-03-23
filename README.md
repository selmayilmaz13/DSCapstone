# Job Automation Insights

**Live App Link:** [PASTE_YOUR_STREAMLIT_APP_URL_HERE](#)

## Project Overview

**Job Automation Insights** is an interactive Streamlit application that evaluates the automation risk of various occupations. It provides users with multiple perspectives on how susceptible a given job is to automation by comparing different estimation methods and offering a 10-year projected employment outlook.

## What the App Shows

When you enter a job title (e.g., "Data Scientist"), the application returns:
- **Model Automation Probability**: A machine learning prediction based on occupation-level features.
- **LLM-Only Automation Estimate**: A standalone, text-based estimate generated using a large language model.
- **Rule-Based Risk Index**: A structured baseline score derived from manually selected O*NET job traits.
- **US Employment Outlook (2024–2034)**: Projected employment changes and growth numbers over the next ten years.
- **Career Takeaway**: A synthesized summary comparing all signals to help users understand long-term job viability.

## How It Works

1. **User Input**: The user inputs a job title.
2. **AWS API Integration**: The app sends the job title to an AWS API Gateway which maps the title to standard occupational categories and fetches LLM predictions and rule-based baseline scores.
3. **Local ML Model**: The app loads a pre-trained Random Forest model (`automation_rf_model.pkl`) to predict the automation risk probability utilizing features stored locally (`job_features.csv`).
4. **Data Synthesis**: The app visualizes these estimates side-by-side, rendering metric cards, risk badges, and relevant skill breakdowns.

## Data Sources

- **O\*NET Database**: Used for occupation-level features, skills, and rule-based baseline traits.
- **US Bureau of Labor Statistics (BLS)**: Projected occupational employment data and trends for 2024–2034.

## Repository Structure

```text
DSCapstone/
├── Code/
│   ├── app.py                  # Main Streamlit application
│   ├── aws_lambda.py           # AWS Lambda backend function 
│   ├── model_training.py       # ML model training and evaluation script
│   ├── feature_engineering.py  # Data preprocessing and feature creation
│   └── ...                     # Additional utility and pipeline scripts
├── Datasets/
│   ├── automation_rf_model.pkl # Pickled, trained Random Forest model
│   ├── job_features.csv        # Preprocessed local job features
│   └── ...                     # Raw data and generated datasets
├── .env                        # Local environment variables (do not commit)
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Main Files

- `Code/app.py`: The frontend UI built with Streamlit that ties the local model and remote API calls together.
- `Code/model_training.py`: The pipeline used to train the Random Forest model on the automation datasets.
- `Datasets/automation_rf_model.pkl`: The saved model artifact consumed by the Streamlit application.
- `Datasets/job_features.csv`: The local dataset of processed occupational features needed for the model's inference.

## Local Setup

To quickly run this application on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/DSCapstone.git
   cd DSCapstone
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your API credentials:
   ```env
   API_BASE_URL=your_api_gateway_url
   API_KEY=your_api_key
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run Code/app.py
   ```

## Deployment

This app is designed to be easily deployed on **Streamlit Community Cloud**. 
1. Push your code to a public or private GitHub repository.
2. Log into Streamlit Cloud and establish a new app pointing to `Code/app.py`.
3. In the Streamlit Cloud dashboard under **Advanced Settings** -> **Secrets**, securely add your API credentials so the script can access them via `st.secrets`:
   ```toml
   API_BASE_URL = "your_api_gateway_url"
   API_KEY = "your_api_key"
   ```

## Interpretation Notes

- **Model vs. LLM**: The ML model relies entirely on structured tabular features from historic and occupational datasets, whereas the LLM estimates rely on vast, generalized textual knowledge and reasoning.
- **Rule-Based Baseline**: This score serves as an intuitive anchor, as it only factors in a few human-verified components that directly imply automation vulnerability.
- **Mixed Signals**: In cases where the systems disagree, the application text synthesizes a nuanced takeaway, acknowledging that complex jobs may be augmented rather than fully automated.

## Future Improvements

- Add more granular skill-level automation breakdowns.
- Incorporate real-time job posting trends to track immediate employer demand.
- Fine-tune a custom LLM strictly on recent academic automation research to improve the LLM-only estimates.
- Support international employment projections beyond the US BLS data.