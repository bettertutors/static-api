from unittest import TestCase, main as unittest_main
from re import compile, match

from webtest import TestApp

from bettertutors_static_api import static_app


class TestStaticApi(TestCase):
    app = TestApp(static_app)
    starts_num_dot_num_dot_num = compile('\d{1,3}\.\d{1,3}\.\d{1,3}\w*')

    def test_setup_dots(self):
        """ Not a full semver check, just checking if it starts like num.num.num """
        status_resp = self.app.get('/api/status').json
        # Just an example test, could obviously import `__version__`, but want scaffold for API functional testing
        self.assertTrue(match(self.starts_num_dot_num_dot_num,
                              status_resp[filter(lambda k: k.endswith('_version'), status_resp.keys())[0]]),
                        "Not in semver format")


if __name__ == '__main__':
    unittest_main()
