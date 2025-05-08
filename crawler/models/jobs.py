from pydantic import BaseModel

class Job(BaseModel):
    """Model for Job List."""

    job_urls: list[str] = []