"""Logging configuration for the application."""
import logging
import os
from datetime import datetime

def setup_logger(name: str) -> logging.Logger:
    """
    Set up and configure a logger with both file and console handlers.
    
    Args:
        name (str): Name of the logger
        
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_handler = logging.FileHandler(f'logs/{name}_{current_time}.log')
    console_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    # Uncomment to enable file logging
    logger.addHandler(file_handler)

    return logger 