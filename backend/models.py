"""Defines the Job hierarchy and its concrete job types."""


class Job:
    """Parent/base class shared by all job types."""

    def __init__(self, job_id: int, description: str) -> None:
        self.job_id = job_id
        self.description = description
        self.status = "pending"

    def execute(self) -> None:
        """Must be overridden by subclasses."""
        raise NotImplementedError(
            "Each job must implement its own execution logic."
        )

    def mark_done(self) -> None:
        self.status = "completed"

    def mark_failed(self) -> None:
        self.status = "failed"

    def __repr__(self) -> str:
        return (
            f"<Job id={self.job_id} status={self.status} "
            f"description='{self.description}'>"
        )


class EmailJob(Job):
    """A job that sends an email."""

    def __init__(self, job_id: int, recipient: str) -> None:
        super().__init__(job_id, f"Send email to {recipient}")
        self.recipient = recipient

    def execute(self) -> None:
        print(f"Sending email to {self.recipient}...")
        self.mark_done()


class DataProcessingJob(Job):
    """A job that processes a dataset."""

    def __init__(self, job_id: int, dataset: str) -> None:
        super().__init__(job_id, f"Process dataset {dataset}")
        self.dataset = dataset

    def execute(self) -> None:
        print(f"Processing dataset {self.dataset}...")
        self.mark_done()
