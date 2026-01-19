from fastapi import FastAPI, HTTPException
from typing import List,Dict
from models import PaymentLog, FailureCategory
from analyzer import FailureAnalyzer


app = FastAPI(title="Payment Failure RCA system")

log_database : List[Dict] = []

@app.post("/logs")
def ingest_log(log:PaymentLog):
    category, rca_explanation = FailureAnalyzer.analyze(log.raw_error_code)
    
    enriched_log = log.dict()
    enriched_log.update({
        "analyzed_category":category,
        "rca_explanation":rca_explanation
    })
    
    log_database.append(enriched_log)
    return {"status":"ingested","analysis":rca_explanation,"category":category}

@app.get("/failure/summary")
def get_failure_summary():
    summary = {cat.value : 0 for cat in FailureCategory}
    
    for entry in log_database:
        cat = entry["analyzed_category"]
        summary[cat] += 1 
    return summary

@app.get("/failure/{transaction_id}")
def get_transaction_details(transaction_id:str):
    for entry in log_database:
        if entry["transaction_id"] == transaction_id:
            return entry
    raise HTTPException(status_code=404,detail="Transaction Not Found")
    
    