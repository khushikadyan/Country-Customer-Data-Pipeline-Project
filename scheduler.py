import schedule
import time
import os
from datetime import datetime
import pytz 
from fetch_countries import fetch_country_data


IST = pytz.timezone('Asia/Kolkata')


def fetch_job():
    """Main scheduled job with enhanced logging"""
    try:
      
        current_time = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S %Z')
        print(f"\n [{current_time}] Starting scheduled data fetch...")
        
        
        fetch_country_data()
        
    
        next_run = schedule.next_run().astimezone(IST).strftime('%Y-%m-%d %H:%M:%S %Z')
        print(f" [{current_time}] Job completed successfully!")
        print(f" Next run at: {next_run}")
        
    except Exception as e:
        error_time = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S %Z')
        print(f"\n [{error_time}] Job failed: {str(e)}")

schedule.clear()

schedule.every().day.at("00:00").do(fetch_job).tag('daily', 'midnight')
schedule.every().day.at("12:00").do(fetch_job).tag('daily', 'noon')

def print_schedule():
    """Print current schedule configuration"""
    print("\n" + "="*40)
    print(" COUNTRY DATA FETCH SCHEDULER")
    print(f" Configured Timezone: Asia/Kolkata (IST)")
    print(f" System Time: {datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("\nCurrent Schedule:")
    for job in schedule.get_jobs():
        next_run = job.next_run.astimezone(IST).strftime('%Y-%m-%d %H:%M:%S %Z')
        print(f"- {job.tags}: {next_run}")
    print("="*40 + "\n")
    print("Press Ctrl+C to stop the scheduler...")


if __name__ == "__main__":
    
    print_schedule()
    fetch_job()  
    

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped by user")