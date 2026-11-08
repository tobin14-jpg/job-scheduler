"""Tracks jobs by their current status."""

from collections import defaultdict
from typing import Dict, List

from models import Job


class TaskManager:
    def __init__(self) -> None:
        self._jobs: List[Job] = []
        self.jobs_by_status: Dict[str, List[Job]] = defaultdict(list)

    def add_job(self, job: Job) -> None:
        self._jobs.append(job)
        self.jobs_by_status[job.status].append(job)

    def get_all(self) -> Dict[str, List[Job]]:
        self.jobs_by_status.clear()
        for job in self._jobs:
            self.jobs_by_status[job.status].append(job)
        return self.jobs_by_status

    def get_jobs_by_status(self, status: str) -> List[Job]:
        return list(self.get_all().get(status, []))
