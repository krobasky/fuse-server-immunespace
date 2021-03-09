import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add one "get_" function for each operationId in the ./openapi/api.yml file

import json
def get_config():
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)

# xxx kludged for now
def get_object(objectId):
    obj = {
        "id": "1",
        "resourceType":"eset",
        "value": {"6005":1.5, "622":0.74, "6120":0.33, "22934":1.2}
    }
    
    return obj


