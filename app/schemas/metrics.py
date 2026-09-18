from pydantic import BaseModel


class RuntimeMetricsResponse(BaseModel):
    requests_total: int
    errors_total: int
    slow_requests_total: int
    average_duration_ms: float
