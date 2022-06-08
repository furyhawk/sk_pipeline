import argparse
import collections

from utils.parse_config import ConfigParser
import data_loaders.data_loaders as data_loaders_

def main(config):
    """Main App

    Args:
        config (Config): Class object for configurations
    """
    # print(repr(config))
    # Load X, y
    data_loader = config.init_obj(
        'data_loader', data_loaders_, **{'training': True, 'label_name': config['label_name']})


if __name__ == '__main__':

    args = argparse.ArgumentParser(description='Sklearn Template')
    args.add_argument('-c', '--config', default=None, type=str,
                      help='config file path (default: None)')

    # custom cli options to modify configuration from default values given in json file.
    CustomArgs = collections.namedtuple('CustomArgs', 'flags type target')
    options = [
        CustomArgs(['-cv', '--cross_validation'], type=int,
                   target='cross_validation;args;n_repeats'),
    ]
    config = ConfigParser.from_args(args, options)
    main(config)