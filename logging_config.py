import os
import logging

LOGS_DIR = "client_logs"

# Ensure the base logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

def get_logger(client_id: str = None):
    """Creates a logger that logs to both file and console."""

    try:
        # If client_id is missing, use a default "general_logs"
        client_id = client_id if client_id else "general_logs"

        # Create a directory for this specific client
        client_log_dir = os.path.join(LOGS_DIR, client_id)
        os.makedirs(client_log_dir, exist_ok=True)

        # Log file path
        log_file = os.path.join(client_log_dir, f"{client_id}.log")

        # Get the logger
        logger = logging.getLogger(client_id)

        # Prevent duplicate handlers
        if not logger.handlers:
            # File Handler
            file_handler = logging.FileHandler(log_file)
            file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(file_formatter)

            # Console Handler (to print logs)
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
            console_handler.setFormatter(console_formatter)

            # Add handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            logger.setLevel(logging.INFO)
            logger.propagate = False  # Prevent duplicate logs

        return logger

    except Exception as e:
        # Fallback logger for logging issues
        fallback_logger = logging.getLogger("fallback_logger")
        if not fallback_logger.handlers:
            fallback_handler = logging.FileHandler("fallback_error.log")
            fallback_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            fallback_handler.setFormatter(fallback_formatter)
            fallback_logger.addHandler(fallback_handler)
            fallback_logger.setLevel(logging.ERROR)

        fallback_logger.error(f"Error in get_logger: {e}")
        return fallback_logger
