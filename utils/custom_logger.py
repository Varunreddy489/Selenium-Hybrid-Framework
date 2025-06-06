# import logging
#
#
# class LogGen:
#     @staticmethod
#     def log_gen():
#         logging.basicConfig(
#             filename=r"C:\Users\varun\OneDrive\Desktop\GE\WEB AUTOMATION\nopcommerce\logs\automation.log",
#             # Correct relative path
#             format="%(asctime)s: %(levelname)s: %(message)s",
#             datefmt="%Y-%m-%d %I:%M:%S %p")
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


import os
import logging


class LogGen:
    @staticmethod
    def log_gen():
        logger = logging.getLogger("automationLogger")

        # Avoid adding multiple handlers on repeated test runs
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            log_path = r"C:\Users\varun\OneDrive\Desktop\GE\WEB AUTOMATION\nopcommerce\logs"
            os.makedirs(log_path, exist_ok=True)  # Ensure the directory exists

            file_handler = logging.FileHandler(os.path.join(log_path, "automation.log"), mode='a')
            formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", "%Y-%m-%d %I:%M:%S %p")
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger
