from pydantic import BaseModel

class Job(BaseModel):
    """Model for Job List."""

    job_no: int
    job_url: str