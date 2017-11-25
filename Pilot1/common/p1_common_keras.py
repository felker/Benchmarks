from __future__ import absolute_import

from keras import optimizers
from keras import initializers

def get_function(name):
    mapping = {}

    mapped = mapping.get(name)
    if not mapped:
        raise Exception('No keras function found for "{}"'.format(name))

    return mapped


#def build_optimizer(type, lr, kerasDefaults):
def build_optimizer(kerasParams):
    type = kerasParams['optimizer']
    if type == 'sgd':
        return optimizers.SGD(lr=kerasParams['learning_rate'], 
                              decay=kerasParams['decay'],
                              momentum=kerasParams['momentum'],
                              nesterov=kerasParams['nesterov'],
                              clipnorm=kerasParams['clipnorm'],
                              clipvalue=kerasParams['clipvalue'])

    elif type == 'rmsprop':
        return optimizers.RMSprop(lr=kerasParams['learning_rate'], 
                                  rho=kerasParams['rho'],
                                  epsilon=kerasParams['epsilon'],
                                  decay=kerasParams['decay'],
                                  clipnorm=kerasParams['clipnorm'],
                                  clipvalue=kerasParams['clipvalue'])

    elif type == 'adagrad':
        return optimizers.Adagrad(lr=kerasParams['learning_rate'],
                                  epsilon=kerasParams['epsilon'],
                                  decay=kerasParams['decay'],
                                  clipnorm=kerasParams['clipnorm'],
                                  clipvalue=kerasParams['clipvalue'])

    elif type == 'adadelta':
        return optimizers.Adadelta(lr=kerasParams['learning_rate'], 
                                   rho=kerasParams['rho'],
                                   epsilon=kerasParams['epsilon'],
                                   decay=kerasParams['decay'],
                                   clipnorm=kerasParams['clipnorm'],
                                   clipvalue=kerasParams['clipvalue'])

    elif type == 'adam':
        return optimizers.Adam(lr=kerasParams['learning_rate'], 
                               beta_1=kerasParams['beta_1'],
                               beta_2=kerasParams['beta_2'],
                               epsilon=kerasParams['epsilon'],
                               decay=kerasParams['decay'],
                               clipnorm=kerasParams['clipnorm'],
                               clipvalue=kerasParams['clipvalue'])

    elif type == 'adamax':
        return optimizers.Adamax(lr=kerasParams['learning_rate'], 
                                 beta_1=kerasParams['beta_1'],
                                 beta_2=kerasParams['beta_2'],
                                 epsilon=kerasParams['epsilon'],
                                 decay=kerasParams['decay'],
                                 clipnorm=kerasParams['clipnorm'],
                                 clipvalue=kerasParams['clipvalue'])
    elif type == 'nadam':
        return optimizers.Nadam(lr=kerasParams['learning_rate'], 
                                beta_1=kerasParams['beta_1'],
                                beta_2=kerasParams['beta_2'],
                                epsilon=kerasParams['epsilon'],
                                schedule_decay=kerasParams['decay_schedule_lr'],
                                clipnorm=kerasParams['clipnorm'],
                                clipvalue=kerasParams['clipvalue'])


def build_initializer(type, kerasParams, seed=None, constant=0.): 
    if type == 'constant':
        return initializers.Constant(value=constant)
    elif type == 'uniform':
        return initializers.RandomUniform(minval=kerasParams['minval_uniform'],
                                  maxval=kerasParams['maxval_uniform'],
                                  seed=seed)
    elif type == 'normal':
        return initializers.RandomNormal(mean=kerasParams['mean_normal'],
                                  stddev=kerasParams['stddev_normal'],
                                  seed=seed)
    elif type == 'glorot_normal':
        return initializers.glorot_normal(seed=seed)
    elif type == 'glorot_uniform':
        return initializers.glorot_uniform(seed=seed)
    elif type == 'lecun_uniform':
        return initializers.lecun_uniform(seed=seed)
    elif type == 'lecun_normal':
        return initializers.lecun_normal(seed=seed)
    elif type == 'he_normal':
        return initializers.he_normal(seed=seed)
