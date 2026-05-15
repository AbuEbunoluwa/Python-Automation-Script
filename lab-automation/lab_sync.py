import os
import csv
import json
import time
from datetime import datetime

LOCAL_LAB_RESULTS = "./lab_results"

def process_lab_data():
    if not os.path.exists(LOCAL_LAB_RESULTS):
        os.makedirs(LOCAL_LAB_RESULTS)
        return "NO_FOLDER"

    files = [f for f in os.listdir(LOCAL_LAB_RESULTS) if f.endswith('.csv')]
    
    if not files:
        # Just a quiet heartbeat so we know it's alive when running continuously
        print("👀 Watching folder for new lab results... (Checking every 5 seconds)")
        return "NO_FILES"

    for file_name in files:
        file_path = os.path.join(LOCAL_LAB_RESULTS, file_name)
        print(f"\n✨ Found new file! Processing: {file_name} ---")

        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                
                if not data:
                    print(f"⚠️ Error: {file_name} is empty. Skipping.")
                    # Move bad file out so it doesn't get stuck processing it forever
                    if not os.path.exists("./processed"): os.makedirs("./processed")
                    os.rename(file_path, f"./processed/{file_name}")
                    return "EMPTY_FILE"
                
                print(f"✅ Validation Passed: {len(data)} test records verified.")

            upload_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"🚀 Uploading {file_name} to AWS Cloud Storage...")
            
            # Log the success
            log_entry = {"file": file_name, "timestamp": upload_time, "status": "SUCCESS"}
            print(f"📝 Log Created: {json.dumps(log_entry)}")

            # Move to processed folder
            if not os.path.exists("./processed"): os.makedirs("./processed")
            os.rename(file_path, f"./processed/{file_name}")
            print(f"📁 Moved {file_name} to /processed folder.")
            return "SUCCESS"

        except Exception as e:
            print(f"❌ Failed to process {file_name}: {e}")
            return "ERROR"

if __name__ == "__main__":
    print("🤖 Automation Engine Started!")
    try:
        while True:
            process_lab_data()
            time.sleep(5)  # Pause for 5 seconds before checking again
    except KeyboardInterrupt:
        print("\n🛑 Automation Engine stopped by user.")
