import tarfile
import logging
import json

def restore(id: str):
    logging.basicConfig(filename='/var/log/backup/logs-backup', filemode='w', format='%(asctime)s %(levelname)s %(message)s')
    
    data_json = {}
    with open("backup.json") as mon_fichier:
        data_json = json.load(mon_fichier)
    try:
        with open('state.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            path = data[id]['path']
            time = data[id]['time']
            logging.info("Opening state.json")
    except Exception as e:
        logging.error("Error while opening state.json\nException:" + str(e))
        return
    try:
        with tarfile.open(path + id + "_" + time + '.tar', 'r') as file:
            file.extractall(data_json["backup"]["files"]["path"])
            logging.info("Restoring backup with id: " + id + "_" + time + " and path: " + data[id]['path'] + '/' + id + '.tar.gz')
    except Exception as e:
        logging.error("Error while extracting backup with id: " + id + " and path: " + data[id]['path'] + id + time + '.tar\nException:' + str(e))
        return
        