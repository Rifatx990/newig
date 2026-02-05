# retry_manager.py
class ExponentialBackoffRetry:
    def __init__(self, max_retries=3, base_delay=5):
        self.max_retries = max_retries
        self.base_delay = base_delay
    
    async def execute_with_retry(self, operation: callable, *args, **kwargs):
        """Execute operation with exponential backoff"""
        for attempt in range(self.max_retries):
            try:
                return await operation(*args, **kwargs)
            except RecoverableError as e:
                if attempt == self.max_retries - 1:
                    raise MaxRetriesExceededError()
                
                delay = self.base_delay * (2 ** attempt)
                await asyncio.sleep(delay)
                
                # Refresh session/proxy on retry
                await self.refresh_resources()
