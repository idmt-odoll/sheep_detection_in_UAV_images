import tensorflow as tf
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2_as_graph
import numpy as np

# script for estimating the model complexity for one forward pass of tensorflow models


def get_flops(concrete_func):
    frozen_func, graph_def = convert_variables_to_constants_v2_as_graph(concrete_func)

    with tf.Graph().as_default() as graph:
        tf.graph_util.import_graph_def(graph_def, name='')

        run_meta = tf.compat.v1.RunMetadata()
        opts = tf.compat.v1.profiler.ProfileOptionBuilder.float_operation()
        flops = tf.compat.v1.profiler.profile(graph=graph, run_meta=run_meta, cmd="op", options=opts)

        return flops.total_float_ops


if __name__ == "__main__":
    # PATH_TO_MODEL = path to the "saved_model" directory of the tensorflow model
    # must be changed to the wanted model

    PATH_TO_MODEL = "path/to/model"
    model = tf.saved_model.load(PATH_TO_MODEL)
    f = model.signatures["serving_default"]

    complexity = ""
    flops = get_flops(f)

    flops = str(flops)
    length_string = len(flops)
    for idx in range(1, length_string+1):
        complexity = flops[-idx] + complexity
        if idx > 1 and idx % 3 == 0:
            complexity = "." + complexity

    print("The estimated complexity of the model is {} FLOPS.".format(complexity))