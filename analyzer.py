from models import FailureCategory

class FailureAnalyzer:
    ERROR_KNOWLEDGE_BASE = {
        "insufficient_funds":(FailureCategory.MERCHANT_ERROR,"Customer Card has low balance"),
        "invalid_api_key": (FailureCategory.MERCHANT_ERROR,"Merchant send wrong credentials"),
        "gateway_timeout": (FailureCategory.PSP_ERROR,"Upstream bank did not respond in time"),
        "bank_downtime": (FailureCategory.PSP_ERROR,"Bank is currently under maintainance"),
        "connection_reset":(FailureCategory.NETWORK_TIMEOUT,"Network Packet lost or reset"),
        "order_exist":(FailureCategory.DUPLICATE_REQUEST,"Transaction id already processed")
    }
    
    @staticmethod
    def analyze(raw_code:str):
        category, human_reason = FailureAnalyzer.ERROR_KNOWLEDGE_BASE.get(
            raw_code.lower(),
            (FailureCategory.UNKNOWN,"Error Code not recognised in knowledge base")
        )
        return category, human_reason