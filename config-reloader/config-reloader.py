from yaml import safe_load, safe_dump
import os
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

modules = {}
path = os.getcwd()
# path = "/config"

configFiles = [file for file in os.listdir(path) if file.endswith(".yml") or file.endswith("yaml")]
logging.info(f"Detected files: {configFiles}")

for filename in configFiles:
    if filename == 'config.yml': continue
    with open(filename) as configMap:
        jsonConfig = configMap.read()
    
    logging.info("Loaded file: {filename}")
    
    modulesData = safe_load(jsonConfig)
    
    if 'modules' in modulesData:
        modules.update(modulesData["modules"])

if not modules:
    logging.warning("No modules detected")
else:
    logging.info(f"Modules loaded: {list(modules.keys())}")
    config = {"modules": modules}



    with open(os.path.join("config.yml"), "w") as cfg:
        cfg.write(safe_dump(config))

    logging.info(f"Created config file at {os.path.join(path, 'config.yml')}")