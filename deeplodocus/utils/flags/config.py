from deeplodocus.utils.flags.ext import DEEP_EXT_YAML
#
# DEEP CONFIG FLAGS
#

DEEP_CONFIG_DIVIDER = "/"

DEEP_CONFIG_PROJECT = "project"
DEEP_CONFIG_DATA = "data"
DEEP_CONFIG_TRANSFORM = "transform"
DEEP_CONFIG_OPTIMIZER = "optimizer"
DEEP_CONFIG_METRICS = "metrics"
DEEP_CONFIG_LOSS = "loss"
DEEP_CONFIG_HISTORY = "history"

DEEP_CONFIG_SECTIONS = [DEEP_CONFIG_PROJECT,
                        DEEP_CONFIG_DATA,
                        DEEP_CONFIG_TRANSFORM,
                        DEEP_CONFIG_OPTIMIZER,
                        DEEP_CONFIG_METRICS,
                        DEEP_CONFIG_LOSS,
                        DEEP_CONFIG_HISTORY]


DEEP_CONFIG = {"project": ["name",
                           "cv_library",
                           "write_logs",
                           "on_wake"],
               "data": [{"dataloader": ["batch_size",
                                        "num_workers"]},
                        {"dataset": [{"train": ["inputs",
                                                "labels",
                                                "additional_data"],
                                      "validation": ["inputs",
                                                     "labels",
                                                     "additional_data"],
                                      "test": ["inputs",
                                               "labels",
                                               "additional_data"]}]}]}

DEEP_CONFIG_FILES = {item: "%s.%s" % (item, DEEP_EXT_YAML) for item in DEEP_CONFIG_SECTIONS}