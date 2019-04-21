# -*- coding: utf-8 -*-
###
### Core > Config
###
import colored
import os

from lib.core.Constants import *
from lib._version import __version__


# -- Banner/Help ----------------------------------------------------------------------------------
BANNER = colored.stylize("""
         ____.       __    ________              `Combina lo mejor de...
        |    | ____ |  | __\_____  \______           ...los Tools de Auditoría Etica`
        |    |/  _ \|  |/ /  _(__  <_  __ \ 
    /\__|    (  (_) )    <  /       \  | \/
    \________|\____/|__|_ \/______  /__|      v{version} | By. YottaiQ
                         \/       \/     
    
              ~ Network & Web Pentest Framework ~
   [ Administrar Toolbox | Automatizar Ataques | Tools de Hacking ]
   
""".format(version=__version__), colored.fg('light_green') + colored.attr('bold'))

USAGE = """
python3 jok3r.py <command> [<args>]

Supported commands:
   toolbox    Administrar toolbox
   info       Ver servicios/opciones/cheques
   db         Defina las misiones, seguimiento de los objetivos, vea resultados de los ataques.
   attack     Ejecutar ataques a objetivos.
   
"""

DB_INTRO = """
The local database stores the missions, targets info & attacks results.
This shell allows for easy access to this database. New missions can be added and
scopes can be defined by importing new targets.
"""

# -- Arguments parsing settings --------------------------------------------------------------------
ARGPARSE_MAX_HELP_POS    = 45
TARGET_FILTERS           = {'ip'      : FilterData.IP, 
                            'host'    : FilterData.HOST,
                            'port'    : FilterData.PORT, 
                            'service' : FilterData.SERVICE, 
                            'url'     : FilterData.URL,
                            'os'      : FilterData.OS}


# -- Basic settings -------------------------------------------------------------------------------
TOOL_BASEPATH            = os.path.dirname(os.path.realpath(__file__+os.sep +'..'+os.sep+'..'))
TOOLBOX_DIR              = TOOL_BASEPATH + os.sep + 'toolbox'
DEFAULT_OUTPUT_DIR       = 'output'
WEBSHELLS_DIR            = TOOL_BASEPATH + os.sep + 'webshells'
WORDLISTS_DIR            = TOOL_BASEPATH + os.sep + 'wordlists'
DB_FILE                  = TOOL_BASEPATH + os.sep + 'local.db'
DB_HIST_FILE             = TOOL_BASEPATH + os.sep + '.dbhistory'
SMART, SMART_I           = '[SMART] ', colored.stylize('[SMART] ', colored.fg('blue') + colored.attr('bold'))


# -- Settings files -------------------------------------------------------------------------------
SETTINGS_DIR             = TOOL_BASEPATH + os.sep + 'settings'
CONF_EXT                 = '.conf'
TOOLBOX_CONF_FILE        = 'toolbox'
INSTALL_STATUS_CONF_FILE = '_install_status'
PREFIX_SECTION_CHECK     = 'check_'
MULTI_CONF               = 'multi'
MULTI_TOOLBOX_SUBDIR     = 'multi'

TOOL_OPTIONS = {
    MANDATORY: [
        'name',
        'description',
        'target_service',
    ],
    OPTIONAL: [
        'install',
        'update',
        'check_command',
    ]
}

SERVICE_CHECKS_CONFIG_OPTIONS = {
    MANDATORY: [
        'default_port',
        'protocol',
        'categories',
    ],
    OPTIONAL: [
        'auth_types'
    ]
}

CHECK_OPTIONS = {
    MANDATORY: [
        'name',
        'category',
        'description',
        'tool',
        # command
    ],
    OPTIONAL: [
        'postrun',
    ]
}

# -- Services -------------------------------------------------------------------------------------
# Table conversion: nmap service names to Jok3r service names
# Used to avoid confusion if necessary
# In particular, unencrypted and encrypted versions of the same protocol are differentiated in Nmap
# (eg: smtp/smtps, http/https, etc.), but in Jok3r this distinction is done by context-specific options
SERVICES_NMAP_TO_JOKER = {
    'rmiregistry' : 'java-rmi',
    'http-alt'    : 'http',
    'https'       : 'http',
    'https-alt'   : 'http',
    'ssl/http'    : 'http',
    'oracle-tns'  : 'oracle', 
    'smtps'       : 'smtp',
}

