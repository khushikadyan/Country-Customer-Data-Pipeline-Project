#  Country & Customer Data Pipeline Project

##  Overview
This project implements two automated data pipelines:
1. **Country Data Pipeline**: Fetches country information from REST Countries API and stores it as JSON files.
2. **Customer-Product Pipeline**: Simulates data transfer from database to Azure Data Lake Storage (ADLS) with conditional triggers.

---

##  Technical Components

### 1. Country Data Pipeline
- **Purpose**: Collect and store country data twice daily.
- **Data Source**: [REST Countries API](https://restcountries.com/v3.1/name/{name})
- **Countries Tracked**: India, US, UK, China, Russia
- **Output**: JSON files named after each country (`india.json`, `us.json`, etc.)

### 2. Customer-Product Pipeline
- **Main Pipeline**:
  - Simulates customer data extraction
  - Triggers ADLS transfer when record count > 500
- **Child Pipeline**:
  - Activates when customer count > 600
  - Simulates product data transfer to ADLS
 
---

##  Project Structure
Celebal_Project/
├── country_data/ # Auto-created folder for country JSONs
├── pipelines/
│ ├── fetch_countries.py # Country data fetcher
│ ├── customer_pipeline.py # Main customer pipeline
│ └── product_pipeline.py # Child product pipeline
├── scheduler.py # Central scheduler
├── pipeline.log # Automated logs
└── requirements.txt # Python dependencies

##  Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/country-customer-pipeline.git
   cd country-customer-pipeline
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure timezone (if needed):
   ```bash
   # In scheduler.py
   os.environ['TZ'] = 'Asia/Kolkata'  # Set your preferred timezone
   ```
---

## How It Works
# Country Data Pipeline
1. Scheduled to run at 12:00 AM and 12:00 PM IST daily.
2. For each country:
   - Calls REST API endpoint
   - Saves response as JSON
   - Updates existing files with new data

# Customer-Product Pipeline
1. Main Pipeline:
   - Generates random customer count (400–700)
   - Triggers customer data transfer when count > 500
   - Passes count to child pipeline

2. Child Pipeline:
   - Receives customer count parameter
   - Activates when count > 600
   - Simulates product data transfer

# Scheduling Mechanism
1. Uses Python schedule library
2. Timezone-aware (IST by default)
3. Self-healing with retry logic

# Future Enhancements
1. Add email/SMS alerts for failures
2. Implement database integration
3. Add data validation checks
4. Containerize with Docker

---

## Author
Khushi Kadyan
Btech CSE( data Science & AI)
