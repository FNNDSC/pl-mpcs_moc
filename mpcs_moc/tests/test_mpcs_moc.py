
from unittest import TestCase
from unittest import mock
from mpcs_moc.mpcs_moc import Mpcs_moc


class Mpcs_mocTests(TestCase):
    """
    Test Mpcs_moc.
    """
    def setUp(self):
        self.app = Mpcs_moc()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')
