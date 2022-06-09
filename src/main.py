import argparse
import collections

from utils.parse_config import ConfigParser
from utils.parse_params import modify_params, get_lib
import data_loaders.data_loaders as data_loaders_
import models.models as models_
import optimizers.optimizers as optimizers_

import sklearn.model_selection as model_selection_


def load_data_optimizer(config):
    # Load X, y
    data_loader = config.init_obj(
        'data_loader', data_loaders_, **{'training': True, 'label_name': config['label_name']})
    model = config.init_obj('model', models_).created_model()
    cross_val = config.init_obj('cross_validation', model_selection_)
    mnt, scoring = config['score'].split()

    search_method_params = {
        'estimator': model,
        'scoring': scoring,
        'cv': cross_val
    }
    search_method_params, search_type = modify_params(
        search_method_params, config)
    search_method = config.init_obj(
        'search_method', get_lib(search_type), **search_method_params)

    Optimizer = config.import_module('optimizer', optimizers_)
    optim = Optimizer(model=model,
                      data_loader=data_loader,
                      search_method=search_method,
                      scoring=scoring,
                      mnt=mnt,
                      config=config)

    return optim

def main(config):
    """Main App

    Args:
        config (Config): Class object for configurations
    """
    optim = load_data_optimizer(config)

    # Optimize and train model
    if config['train_model']:
        optim.optimize()
    else:
        assert (config['model_dir'] != '') & (config['test_model']
                                              ), 'Without training, maintain config.model_dir with the path to load model.pkl.'


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