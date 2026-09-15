



class AIServiceError(Exception):
    pass

class AIServiceTimeoutError(AIServiceError):
    def __init__(self):
        self.message="AI provider request timed out."
        super().__init__(self.message)

class AIServiceRateLimitError(AIServiceError):
    def __init__(self):
        self.message="AI provider rate limit exceeded."
        super().__init__(self.message)

class AIServiceConnectionError(AIServiceError):
    def __init__(self):
        self.message="Unable to connect with AI provider."
        super().__init__(self.message)

class AIServiceProviderError(AIServiceError):
    def __init__(self):
        self.message="AI provider request failed."
        super().__init__(self.message)