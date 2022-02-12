"""Perform integration tests for `orion.algo.pb2`."""
from orion.testing.algo import BaseAlgoTests


# Test suite for algorithms. You may reimplement some of the tests to adapt them to your algorithm
# Full documentation is available at https://orion.readthedocs.io/en/stable/code/testing/algo.html
# Look for algorithms tests in https://github.com/Epistimio/orion/blob/master/tests/unittests/algo
# for examples of customized tests.
class TestPB2(BaseAlgoTests):
    """Test suite for algorithm PB2"""

    algo_name = "pb2"
    config = {
        "seed": 1234,  # Because this is so random
        # Add other arguments for your algorithm to pass test_configuration
    }


# You may add other phases for test.
# See https://github.com/Epistimio/orion.algo.skopt/blob/master/tests/integration_test.py
# for an example where two phases are registered, one for the initial random step, and
# another for the optimization step with a Gaussian Process.
TestPB2.set_phases([("random", 0, "space.sample")])
