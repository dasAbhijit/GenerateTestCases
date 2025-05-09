from pathlib import Path
from typing import Optional

import pandas as pd

from ..config.logging import get_logger

logger = get_logger(__name__)

class FileService:
    """Service for handling file operations."""
    
    @staticmethod
    def read_file(file_path: Path) -> str:
        """
        Read the contents of a file.
        
        Args:
            file_path: Path to the file to read.
            
        Returns:
            The contents of the file as a string.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            Exception: For other file reading errors.
        """
        logger.debug(f"Reading file: {file_path}")
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            logger.debug(f"Successfully read file: {file_path}")
            return content
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {str(e)}", exc_info=True)
            raise
    
    @staticmethod
    def save_to_csv(
        data: str,
        output_path: Path,
        remove_markers: bool = True
    ) -> Optional[Path]:
        """
        Save data to a CSV file.
        
        Args:
            data: The data to save.
            output_path: Path where to save the CSV file.
            remove_markers: Whether to remove code block markers from the data.
            
        Returns:
            The path to the saved file if successful, None otherwise.
            
        Raises:
            Exception: If there's an error processing or saving the data.
        """
        logger.info(f"Processing data and saving to CSV: {output_path}")
        try:
            if remove_markers:
                data = data.replace('```csv', '').replace('```', '')
                logger.debug("Removed code block markers from data")
            
            # Split the data into rows and then split each row into columns
            rows = [row.split(',') for row in data.split('\n') if row.strip()]
            logger.debug(f"Split data into {len(rows)} rows")
            
            # Convert the rows into a pandas DataFrame
            df = pd.DataFrame(rows[1:], columns=rows[0])
            logger.debug(
                f"Created DataFrame with {len(df)} rows and {len(df.columns)} columns"
            )
            
            # Save the DataFrame to a CSV file
            df.to_csv(output_path, index=False)
            logger.info(f"Successfully saved {len(df)} rows to {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error saving to CSV: {str(e)}", exc_info=True)
            return None 