import requests 
import random 
import uuid
import time


API_URL = "http://127.0.0.1:8000/logs"

ERROR_SCENARIOS = [
    "insufficient_funds",
    "invalid_api_key",
    "gateway_timeout",
    "bank_downtime",
    "connection_reset",
    "order_exists",
    "junk_error_999",
    "legacy_system_fail"
]

def generate_traffic(total_requests=50):
    print("---Starting Simulation : Sending {total_requests} Logs --- ")
    for i in range(total_requests):
        random_error = random.choice(ERROR_SCENARIOS)
        corr_id = f"corr_{uuid.uuid4().hex[:8]}" if random.random() > 0.2 else None
        payload= {
            "transaction_id":f"tx_{uuid.uuid4().hex[0:10]}",
            "merchant_id" : f"merchant_{random.randint(1,5)}",
            "amount" : round(random.uniform(10.00,999.99),2),
            "raw_error_code" : random_error,
            "correlation_id" : corr_id
        }
        
        try:
            response = requests.post(API_URL,json=payload)
            
            if response.status_code == 200 :
                data = response.json()
                print(f'[{i+1}/{total_requests}] Sent "{random_error}" \t-> Classified as : {data['category']}') 
            else :
                print(f"[{i+1}/{total_requests}] request failed : {response.text} ")
                
        except requests.exceptions.ConnectionError:
            print("Error : could not connect. Is your fastapi server running ")
            break
        
        time.sleep(0.05)
        
    print("\n--- Simulation Complete---")

if __name__ == "__main__":
    generate_traffic()