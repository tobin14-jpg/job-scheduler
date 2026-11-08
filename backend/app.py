"""Build sample jobs, execute them, and print a summary."""

from typing import List

from executor import Executor
from models import DataProcessingJob, EmailJob, Job
from task_manager import TaskManager


def build_jobs() -> List[Job]:
    return [
        EmailJob(1, "user@example.com"),
        DataProcessingJob(2, "dataset_A"),
        EmailJob(3, "admin@example.com"),
        DataProcessingJob(4, "dataset_B"),
    ]


if __name__ == "__main__":
    jobs = build_jobs()
    manager = TaskManager()
    for job in jobs:
        manager.add_job(job)

    Executor(jobs).run()

    print("\n=== SUMMARY ===")
    print(f"Pending: {len(manager.get_jobs_by_status('pending'))}")
    print(f"Completed: {len(manager.get_jobs_by_status('completed'))}")
    print(f"Failed: {len(manager.get_jobs_by_status('failed'))}")
