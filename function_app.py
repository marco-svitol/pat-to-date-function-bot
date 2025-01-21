from botlogging import logger
from be_requests import RequestClient
import azure.functions as func
import configs
import time
import os

app = func.FunctionApp()

@app.timer_trigger(schedule="30 3 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def pattodatebotfunction(myTimer: func.TimerRequest) -> None:
    common_main()
    if myTimer.past_due:
        logger.info('The timer is past due!')

    logger.info('Python timer trigger function executed.')

def common_main():
    logger.info("Starting function execution")
    # Send requests to APIs
    request_client = RequestClient()
    
    profile = request_client.send_request(configs.BE_PROFILE_PATH)
    applicants = profile[0]['searchvalues']['applicants']
    
    logger.info(f"Processing {len(applicants)} applicants")
    
    logger.debug(f"Applicants: {applicants}")

    # Iterate through applicants and send requests
    for index, applicant in enumerate(applicants):
        applicant_id = applicant['id']
        search_path = configs.BE_SEARCH_PATH.replace('@', applicant_id)
        
        start_time = time.time()  # Start time of the request
        
        result = request_client.send_request(search_path)
        
        end_time = time.time()  # End time of the request
        duration = end_time - start_time  # Duration of the request in seconds
        
        logger.info(f"Processing applicant {index+1}/{len(applicants)}")
        logger.info(f"Request for applicant {applicant['name']} (ID: {applicant_id}) took {duration:.2f} seconds")
        
        result_size_kb = len(str(result)) / 1024  # Size of the result in kilobytes
        logger.info(f"Result size for applicant {applicant['name']} (ID: {applicant_id}): {result_size_kb:.2f} KB")
        
        
        if index != len(applicants) - 1:
            logger.info(f"Waiting {configs.BE_WAIT_BETWEEN_REQUESTS_SECS} seconds for the next request...")
            time.sleep(configs.BE_WAIT_BETWEEN_REQUESTS_SECS)

if __name__ == "__main__":
    if os.getenv("ENV") != "production":
        common_main()