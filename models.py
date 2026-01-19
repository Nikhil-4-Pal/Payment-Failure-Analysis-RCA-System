from pydantic import BaseModel, Field
from typing import Optional, Dict
from enum import Enum
from datetime import datetime


class FailureCategory(str, Enum):
    MERCHANT_ERROR = "MERCHANT_ERROR"
    PSP_ERROR = "PSP_ERROR"
    NETWORK_TIMEOUT = "NETWORK_TIMEOUT"
    DUPLICATE_REQUEST = "DUPLICATE_REQUIEST"
    UNKNOWN = "UNKNOWN"
    
class PaymentLog(BaseModel):
    transaction_id : str
    correlation_id : Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    merchant_id : str
    amount : float
    raw_error_code : str
    raw_error_message : Optional[str] = None
    