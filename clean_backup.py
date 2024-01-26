import logging
import json
from delete_backup import delete

def clean():
    try:
        with open('state.json', 'r') as file:
            state = json.load(file)
            logging.info("Opening state.json")
        delete(min(state, key=lambda id: state[id]["time"]))
    except Exception as e:
        logging.error("Error while opening state.json\nException:" + str(e))
        return

if __name__ == "__main__":
    clean()