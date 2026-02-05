# timezone_scheduler.py
class AsiaDhakaScheduler:
    def __init__(self):
        self.timezone = pytz.timezone('Asia/Dhaka')
        self.scheduler = BackgroundScheduler(timezone=self.timezone)
    
    def schedule_message(self, job_id: str, execute_at: datetime, func: callable):
        """Schedule job with precise Asia/Dhaka timing"""
        # Convert to timezone-aware datetime
        bd_time = self.timezone.localize(execute_at)
        
        # Schedule with misfire_grace_time for precision
        self.scheduler.add_job(
            func,
            'date',
            run_date=bd_time,
            id=job_id,
            misfire_grace_time=30,  # 30 seconds grace period
            coalesce=True,
            max_instances=1
        )
    
    def get_next_run_time(self, job_id: str) -> datetime:
        """Get next execution time in Asia/Dhaka"""
        job = self.scheduler.get_job(job_id)
        return job.next_run_time.astimezone(self.timezone)
