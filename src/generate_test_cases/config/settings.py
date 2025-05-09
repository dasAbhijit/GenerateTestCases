import os
from pathlib import Path
from typing import Dict, Any

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent.parent
SRC_DIR = BASE_DIR / "src"
RESOURCES_DIR = BASE_DIR / "resources"
OUTPUT_DIR = BASE_DIR / "output"
LOGS_DIR = BASE_DIR / "logs"

# Create necessary directories
for directory in [RESOURCES_DIR, OUTPUT_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# LLM Configuration
LLM_CONFIG: Dict[str, Any] = {
    "model_identifier": "gemini-2.0-flash",
    "temperature": 0.5,
}

# File paths
EXAMPLE_PATHS = {
    "brd": RESOURCES_DIR / "example" / "brd-ordertracking.md",
    "erd": RESOURCES_DIR / "example" / "erd-ordertracking.md",
    "tc": RESOURCES_DIR / "example" / "tc-ordertracking.csv",
}

TARGET_PATHS = {
    "brd": RESOURCES_DIR / "target" / "brd-ordercreation.md",
    "erd": RESOURCES_DIR / "target" / "erd-ordercreation.md",
}

# Logging Configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": str(LOGS_DIR / "app.log"),
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True
        },
    }
} 