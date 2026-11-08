"""Runs jobs concurrently using threads to simulate a scheduler."""

import random
import threading
import time
from datetime import datetime
from typing import List

from errors import JobExecutionError
from models import Job


class Executor:
    def __init__(self, jobs: List[Job]) -> None:
        self.jobs = jobs

    def _ts(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def run_job(self, job: Job) -> None:
        print(
            f"[{self._ts()}] Executing job "
            f"{job.job_id} ({job.description})..."
        )
        try:
            time.sleep(random.uniform(1, 3))
            if random.random() < 0.2:
                raise JobExecutionError(job.job_id)
            job.execute()
            print(f"[{self._ts()}] Completed job {job.job_id}.")
        except JobExecutionError as error:
            job.mark_failed()
            print(f"[{self._ts()}] Error in job {error.job_id}: {error}")

    def run(self) -> None:
        threads: List[threading.Thread] = []
        for job in self.jobs:
            thread = threading.Thread(target=self.run_job, args=(job,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
