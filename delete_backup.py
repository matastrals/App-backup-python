import os
import logging
import json

def delete(id:str):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    try:
        with open('state.json', 'r') as file:
            state = json.load(file)
            logging.info("Opening state.json")
        if id in state:
            path = state[id]['path']
            time = state[id]['time']
            logging.info("Deleting backup in state.json with id: " + id + " and path: " + path + '/' + id + '.tar.gz')
            del state[id]
        else:
            logging.error("Backup with id: " + id + " not found in state.json")
            return
    except Exception as e:
        logging.error("Error while opening state.json\nException:" + str(e))
        return
    try:
        with open('state.json', 'w') as file:
            json.dump(state, file)
        backup_file = path + f'{id}_{time}.tar'
        if os.path.exists(backup_file):
            os.remove(backup_file)
            logging.info("Deleting backup with id: " + id + " and path: " + path + '/' + id + '.tar')
        else:
            logging.error("Backup with id: " + id + " not found in " + path + '/' + id + '.tar')
            return
    except Exception as e:
        logging.error("Error while deleting backup with id: " + id + " and path: " + path + '/' + id + '.tar.gz\nException:' + str(e))
        return


if __name__ == "__main__":
    delete('dzqdzq')