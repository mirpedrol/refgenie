from refgenconf import CFG_ENV_VARS

__all__ = ["RefgenieError", "MissingGenomeConfigError"]


class RefgenieError(Exception):
    """ Base refegnie exception type """
    pass


class MissingGenomeConfigError(RefgenieError):
    """ Exception for when a genome config filepath doesn't point to a file. """

    def __init__(self, conf_file=None):
        """
        Create the error message, using optionally an attempt filepath.

        :param str conf_file: path attempted to be used as genome config file
        """
        msg = "You must provide a config file either as an argument " \
              "or via an environment variable: " \
              "{}".format(CFG_ENV_VARS)
        if conf_file:
            msg = "Not a file {} -- {}.".format(conf_file, msg)
        super(MissingGenomeConfigError, self).__init__(msg)


class MissingGenomeFolderError(RefgenieError):
    def __init__(self, genome_folder):
        """
        Create the error message.

        :param str genome_folder: path attempted to be used as genome folder
        """
        msg = "The specified genome folder does not exist: {}".format(genome_folder)
        super(MissingGenomeFolderError, self).__init__(msg)

