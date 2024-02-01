import logging
import json
from delete_backup import delete

def clean():

    logging.basicConfig(filename='/var/log/backup/logs-backup', filemode='w', format='%(asctime)s %(levelname)s %(message)s')
    try:
        with open('state.json', 'r') as file:
            state = json.load(file)
            logging.info("Opening state.json")
    except Exception as e:
        logging.error("Error while opening state.json\nException:" + str(e))
        return
    delete(min(state, key=lambda id: state[id]["time"]))

if __name__ == "__main__":
    clean()