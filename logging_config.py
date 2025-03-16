import os
import logging

LOGS_DIR = "client_logs"

# Ensure the base logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

def get_logger(client_id: str = None):
    """Dynamically creates a logger for a specific client, handling missing client_id cases."""

    try:
        # If client_id is missing, use a default "unknown_client"
        client_id = client_id if client_id else "general_clients"

        # Create a directory for this specific client
        client_log_dir = os.path.join(LOGS_DIR, client_id)
        os.makedirs(client_log_dir, exist_ok=True)

        # Log file for this client
        log_file = os.path.join(client_log_dir, f"{client_id}.log")

        # Configure logger for this client
        logger = logging.getLogger(client_id)

        # Avoid duplicate handlers (important for performance)
        if not logger.handlers:
            handler = logging.FileHandler(log_file)
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

        return logger

    except Exception as e:
        # Create a fallback logger for critical logging issues
        fallback_logger = logging.getLogger("fallback_logger")
        if not fallback_logger.handlers:
            handler = logging.FileHandler("fallback_error.log")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            fallback_logger.addHandler(handler)
            fallback_logger.setLevel(logging.ERROR)
        
        fallback_logger.error(f"Error in get_logger: {e}")

        return fallback_logger  # Return a fallback logger instead of None
