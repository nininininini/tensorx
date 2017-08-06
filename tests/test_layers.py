from unittest import TestCase
import tensorflow as tf
import numpy as np
from tensorx.layers import Input
from tensorx.layers import Activation as Act


class TestLayers(TestCase):
    # setup and close TensorFlow sessions before and after the tests (so we can use tensor.eval())
    def setUp(self):
        self.ss = tf.InteractiveSession()

    def tearDown(self):
        self.ss.close()

    def test_input(self):
        """ Test Input layer - creates a TensorFlow Placeholder

        this corresponds to an input layer with n_units in the input
        and a shape corresponding to [batch_size, n_units]
        """
        in_layer = Input(n_units=10)
        self.assertIsInstance(in_layer.y, tf.Tensor)


        ones = np.ones(shape=(2, 10))
        result = self.ss.run(in_layer.y, feed_dict={in_layer.y: ones})

        np.testing.assert_array_equal(ones, result)

        ones_wrong_shape = np.ones(shape=(2, 11))
        try:
            self.ss.run(in_layer.y, feed_dict={in_layer.y: ones_wrong_shape})
            self.fail("Should have raised an exception since shapes don't match")
        except ValueError:
            pass

    def test_index_input(self):
        """ Create a Sparse Input by providing
        a n_active parameter


        """
        dim = 10
        index = np.random.randint(0, 10)
        index = [[index]]

        input_layer = Input(n_units=dim, n_active=1)

        result = self.ss.run(input_layer.y, feed_dict={input_layer.y: index})
        s = np.shape(result)
        self.assertEqual(s[1], 1)

    def test_activation(self):
        pass
        # Act.Fn.sigmoid


        # fn = Act(None,sg)
