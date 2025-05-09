from typing import Any, Dict

from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from ..config.logging import get_logger
from ..config.settings import LLM_CONFIG

logger = get_logger(__name__)

class LLMService:
    """Service for interacting with the Language Model."""
    
    def __init__(self):
        """Initialize the LLM service with configuration."""
        self.model_identifier = LLM_CONFIG["model_identifier"]
        self.temperature = LLM_CONFIG["temperature"]
        self._initialize_llm()
    
    def _initialize_llm(self) -> None:
        """Initialize the LLM client."""
        logger.info(
            f"Initializing LLM with model: {self.model_identifier}, "
            f"temperature: {self.temperature}"
        )
        self.llm = ChatGoogleGenerativeAI(
            model=self.model_identifier,
            temperature=self.temperature
        )
    
    def invoke(self, prompt: ChatPromptTemplate, **kwargs) -> str:
        """
        Invoke the LLM with the given prompt and parameters.
        
        Args:
            prompt: The prompt template to use.
            **kwargs: Additional parameters for the prompt.
            
        Returns:
            The text response from the LLM.
            
        Raises:
            Exception: If there's an error invoking the LLM.
        """
        logger.debug("Preparing to invoke LLM")
        try:
            messages = prompt.format_messages(**kwargs)
            content = [{"role": m.type, "content": m.content} for m in messages]
            logger.debug("Sending request to LLM")
            response = self.llm.invoke(input=content[0]['content'])
            logger.info("Successfully received response from LLM")
            return response.text()
        except Exception as e:
            logger.error(f"Error invoking LLM: {str(e)}", exc_info=True)
            raise 