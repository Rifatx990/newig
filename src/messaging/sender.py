# sender.py
class InstagramMessageSender:
    async def send_message_with_image(self, recipient: str, text: str, image_path: str):
        """Send text followed by image in correct order"""
        # Step 1: Navigate to DM
        await self.navigate_to_direct_messages()
        
        # Step 2: Find recipient
        await self.search_and_select_recipient(recipient)
        
        # Step 3: Send text message
        await self.type_and_send_text(text)
        
        # Step 4: Send image (strictly after text)
        await self.upload_and_send_image(image_path)
        
        # Step 5: Verify delivery
        return await self.verify_delivery()
    
    async def type_and_send_text(self, text: str):
        """Type and send text message"""
        # Locate message input box
        # Type text character by character (mimics human)
        # Press Enter or click send
        # Wait for send confirmation
        pass
    
    async def upload_and_send_image(self, image_path: str):
        """Upload and send image attachment"""
        # Click attachment button
        # Select file from system
        # Wait for upload completion
        # Add optional caption
        # Click send
        # Verify image sent
        pass
