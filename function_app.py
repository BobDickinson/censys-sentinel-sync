# Azure Functions deps
import logging
import os
import uuid
from datetime import datetime, timedelta
import azure.functions as func
from azure.core.exceptions import ResourceNotFoundError

# Azure Monitor Data Collector deps (built-in)
import json
import requests
import datetime
import hashlib
import hmac
import base64

# Censys ASM deps
from censys.asm import Logbook

app = func.FunctionApp()

@app.function_name(name="CensysLogbookSync")
@app.schedule(schedule="0 0 * * * *", arg_name="mytimer", run_on_startup=False) 
def censys_logbook_sync(mytimer: func.TimerRequest) -> None:

    logging.info('Not implemented yet')

@app.function_name(name="CensysRisksSync")
@app.schedule(schedule="0 0 * * * *", arg_name="mytimer", run_on_startup=False) 
def censys_risks_sync(mytimer: func.TimerRequest) -> None:

    logging.info("Not implemented yet")
