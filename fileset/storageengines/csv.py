from fileset.config import get_config_factory


def create(raw_config):
    pass


get_config_factory().reg_src('csv', create)
