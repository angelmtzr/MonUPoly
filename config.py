#config files library
import configparser

config = configparser.ConfigParser()

settings = {
        }

try:
    #look for the settings file
    config.read("settings.ini");
    if len(config.sections()) <= 0:
        raise IOError

except IOError:
    #Creates the Settings File
    config["DISPLAY"] = {
        "Screen_width" : "800",
        "Screen_height" : "500",
        "Fullscreen" : "off"
        }
    #saves the settings file
    with open("settings.ini", 'w') as configfile:
        config.write(configfile);

#reads the config file
config.read("settings.ini")


#read & add the settings to the dictionary
settings.update({
    "Screen_width": int(config["DISPLAY"]["Screen_width"]),
    "Screen_height": int(config["DISPLAY"]["Screen_height"]),
    "Fullscreen" : config["DISPLAY"].getboolean("Fullscreen")
    })
