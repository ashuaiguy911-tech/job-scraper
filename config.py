import os
from dotenv import load_dotenv
load_dotenv()

# =================================================================
# 1. CORE SYSTEM CONFIGURATION (Do Not Modify)
# =================================================================
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_TABLE_NAME: str = "jobs"
SUPABASE_CUSTOMIZED_RESUMES_TABLE_NAME = "customized_resumes"
SUPABASE_STORAGE_BUCKET="personalized_resumes"
SUPABASE_RESUME_STORAGE_BUCKET="resumes"
SUPABASE_BASE_RESUME_TABLE_NAME = "base_resume"
BASE_RESUME_PATH = "resume.json"
LLM_API_KEY = os.environ.get("LLM_API_KEY") or os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_FIRST_API_KEY")

# =================================================================
# 2. USER PREFERENCES (Editable)
# =================================================================
LLM_MODEL = "groq/llama-3.3-70b-versatile"

LINKEDIN_SEARCH_QUERIES = [
    "Business Development Manager",
    "Senior Sales Manager",
    "Sales Manager B2B",
    "Business Development Manager B2B",
    "Senior Business Development",
    "VP Sales",
    "Head of Sales",
    "Regional Sales Manager",
    "Enterprise Sales Manager",
    "B2B Sales Manager"
]

LINKEDIN_LOCATION = "India"
LINKEDIN_GEO_ID = 102713980
LINKEDIN_JOB_TYPE = "F"
LINKEDIN_JOB_POSTING_DATE = "r86400"
LINKEDIN_F_WT = 1

CAREERS_FUTURE_SEARCH_QUERIES = []
CAREERS_FUTURE_SEARCH_CATEGORIES = []
CAREERS_FUTURE_SEARCH_EMPLOYMENT_TYPES = ["Full Time"]

SCRAPING_SOURCES = ["linkedin"]
JOBS_TO_SCORE_PER_RUN = 20
JOBS_TO_CUSTOMIZE_PER_RUN = 1
MAX_JOBS_PER_SEARCH = {
    "linkedin": 10,
    "careers_future": 10,
}

# =================================================================
# 3. ADVANCED SYSTEM SETTINGS (Do Not Modify)
# =================================================================
LLM_MAX_RPM = 10
LLM_MAX_RETRIES = 3
LLM_RETRY_BASE_DELAY = 10
LLM_DAILY_REQUEST_BUDGET = 0
LLM_REQUEST_DELAY_SECONDS = 15
LINKEDIN_MAX_START = 5
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 15
JOB_EXPIRY_DAYS = 30
JOB_CHECK_DAYS = 3
JOB_DELETION_DAYS = 60
JOB_CHECK_LIMIT = 50
ACTIVE_CHECK_TIMEOUT = 20
ACTIVE_CHECK_MAX_RETRIES = 2
ACTIVE_CHECK_RETRY_DELAY = 10
