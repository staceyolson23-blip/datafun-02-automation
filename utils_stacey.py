"""
File: utils_stacey.py

Purpose: Reusable header/tagline module for analytics projects.

Description:
A short, first-week module to demonstrate key skills:
- declare basic variables (bool, int, str, list)
- compose a reusable f-string "tagline" (a formatted-string header block)
- expose a function named get_tagline() that can be imported into other modules
- run this file as a script via main() using the if __name__ == '__main__' pattern

Author: Stacey Olson
"""
import statistics
import loguru
import pyttsx3
#####################################
# Configure Simple Logger (better than print statements)
#####################################
logger = loguru.logger
logger.add(
    "project.log",
    level="INFO",
    rotation="100 KB",
    backtrace=False,
    diagnose=False,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}",
)
logger.info("Logger loaded.")
#####################################
# Declare Global Variables
#####################################

# ----------------------------------
# Define Boolean variables (True/False)
# ----------------------------------
is_accepting_clients: bool = True
offers_remote_workshops: bool = True

is_hiring: bool = False

current_year: int = 2025
year_started: int = 2020

number_of_employees: int = 25

author: str = "Stacey Olson"
organization: str = "Analytics for Teachers"
motto: str = "Because they are busy enough."

location: str = "Santa Rosa, CA"

services: list[str] = [
    "Student Data Analysis",
    "Curriculum Insights",
    "Classroom Dashboards",
    "Survey Analytics",
    "Professional Development Reports"
]

satisfaction_scores: list[float] = [4.8, 4.6, 4.9, 5.0, 4.7]

office_locations: list[str] = ["Santa Rosa", "Windsor", "Petaluma"]

years_active: int = current_year - year_started
min_score: float = min(satisfaction_scores)
max_scores: float = max(satisfaction_scores)
count_of_services: int = len(services)
count_of_scores: int = len(satisfaction_scores)
count_of_locations: int = len(office_locations)

mean_score: float = statistics.mean(satisfaction_scores)
stdev_score: float = statistics.stdev(satisfaction_scores)

byline: str = f"""
***********************************************
{organization} - Project Header
***********************************************
Author:                     {author}
Motto:                      {motto}
Location:                   {location}
Years Active:               {years_active}
Number of Employees:        {number_of_employees}
Accepting New Clients?:     {is_accepting_clients}
Remote Workshops?:          {offers_remote_workshops}
Services:                   {services}
Office Locations:           {office_locations}
Client Satisfaction Scores: {satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_scores}
Mean Satisfaction Score:    {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
***********************************************
"""

def get_byline() -> str:
    return byline

def get_tagline() -> str:
    """Alias so other projects can import a consistent name."""
    return get_byline()

def read_byline_aloud() -> None:
    """
    Use text-to-speech to read the byline aloud.
    """
    engine = pyttsx3.init()
    if engine is not None:
        engine.say(str(get_byline()))
        engine.runAndWait()

#####################################
# Define Function main() function for this module.
#####################################

def main() -> None:
    """
    Use this main() function to test this module when
    running it as a script.
    """

    loguru.logger.info("STARTING main()..")
    loguru.logger.info("Byline:\n" + get_byline())

    try:
        # TODO: Uncomment next line if you want audio feedback (use CTRL+C to stop)
        # read_byline_aloud()
        pass
    except KeyboardInterrupt:
        logger.info("Speech interrupted by user (Ctrl+C).")
    except Exception as ex:
        logger.warning(f"Text-to-speech skipped: {ex}")

    loguru.logger.info("This module is organized like all Python modules.")
    loguru.logger.info("We write professional Python from the start.")
    loguru.logger.info("END main()...")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == "__main__":
    main()
