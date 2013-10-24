from fabric.api import local
import json
import os
import glob
from pprint import pprint
from sprout import * 

__all__ = ['get_artifacts', 'deploy']


def _clean(tmpdir):
    """ Remove any existing files from a previous run of sprout. """
    _ensure_exists(tmpdir)
    _remove_files(tmpdir)
        

def _ensure_exists(tmpdir):
    try:
        os.makedirs(tmpdir)
    except OSError:
        if not os.path.isdir(tmpdir):
            raise
        
def _remove_files(tmpdir):
    files = glob.glob(os.path.join(tmpdir, '*'))
    for f in files:
        print('removing %s' % f)
        os.remove(f)


def get_artifacts(config_file):
    cfg = config.load_config(config_file)
    _clean(cfg.settings['local_temp_dir'])

    for artifact in cfg.artifacts:
        # get that artifact and put it in the local store
        code, o, e = artifact.download(cfg.settings['nexus_hostname'], cfg.settings['local_temp_dir'])
        print('Download Results:' + str(code))
        output = (str(o) + '\n' + str(e)).strip()
        print(output)



def deploy(config_file):
    c = config.load_config(config_file)


