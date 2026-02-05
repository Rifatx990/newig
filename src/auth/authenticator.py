# authenticator.py
class InstagramAuthenticator:
    def __init__(self, username: str, password: str, proxy: dict):
        self.username = username
        self.password = password
        self.proxy = proxy
        self.session_manager = SessionManager()
    
    async def login(self) -> bool:
        """Handle login with session persistence"""
        if self.session_manager.has_valid_session():
            return await self.restore_session()
        
        # Fresh login with 2FA/challenge handling
        return await self.perform_fresh_login()
    
    async def perform_fresh_login(self):
        """Complete login flow with error handling"""
        try:
            # Navigate to login page
            # Fill credentials
            # Handle Instagram's security checks
            # Save encrypted cookies
            # Verify login success
            pass
        except CheckpointRequiredError:
            await self.handle_checkpoint()
        except LoginFailedError:
            await self.handle_login_failure()
