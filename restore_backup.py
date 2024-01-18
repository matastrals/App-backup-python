import tarfile
import logging
import json

def restore(id: str):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    try:
        with open('state.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            path = data[id]['path']
            logging.info("Opening state.json")
    except Exception as e:
        logging.error("Error while opening state.json\nException:" + str(e))
        return
    try:
        with tarfile.open(path + '/' + id + '.tar.gz', 'r') as file:
            file.extractall(path + '/' + id)
            logging.info("Restoring backup with id: " + id + " and path: " + data[id]['path'] + '/' + id + '.tar.gz')
    except Exception as e:
        logging.error("Error while extracting backup with id: " + id + " and path: " + data[id]['path'] + '/' + id + '.tar.gz\nException:' + str(e))
        return
        
if __name__ == "__main__":
    restore('2z4Qda13a')