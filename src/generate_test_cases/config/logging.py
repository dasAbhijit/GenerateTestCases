import logging.config
from pathlib import Path
from typing import Optional

from .settings import LOGGING_CONFIG, LOGS_DIR

def setup_logging(
    log_file: Optional[Path] = None,
    log_level: str = "DEBUG",
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) -> None:
    """
    Set up logging configuration for the application.
    
    Args:
        log_file: Optional path to the log file. If None, uses default from settings.
        log_level: The logging level to use.
        log_format: The format string for log messages.
    """
    # Ensure logs directory exists
    LOGS_DIR.mkdir(exist_ok=True)
    
    # Update logging config with provided parameters
    config = LOGGING_CONFIG.copy()
    
    if log_file:
        config["handlers"]["file"]["filename"] = str(log_file)
    
    config["handlers"]["console"]["level"] = log_level
    config["handlers"]["file"]["level"] = log_level
    config["formatters"]["standard"]["format"] = log_format
    
    # Apply the configuration
    logging.config.dictConfig(config)

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: The name for the logger.
        
    Returns:
        A configured logger instance.
    """
    return logging.getLogger(name) 