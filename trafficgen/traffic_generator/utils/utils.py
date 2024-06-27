import argparse
import os

import yaml

TRAFFICGEN_ROOT = os.path.dirname(os.path.dirname(__file__))


def load_config(path):
    """ load config file"""
    path = os.path.join(TRAFFICGEN_ROOT, "configs", f'{path}.yaml')
    with open(path, 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg


def get_parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', type=str, default='demo')
    parser.add_argument('--gif', action="store_true")
    parser.add_argument(
        '--save_metadrive',
        action="store_true",
        help="Whether to save generated scenarios to MetaDrive-compatible file."
    )
    args = parser.parse_args()
    return args
