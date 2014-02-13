import unittest

from app import app
from app.db_calls import init_db
from app.image_models import add_image
from app.image_models import get_all_images

from flask.ext.testing import TestCase


class AppBaseTestCase(TestCase):

    def create_app(self):
        '''
           Creates a sqlite db in memory when testing.
        '''
        app.config['TESTING'] = True
        app.config['DATABASE'] = ':memory:'
        return app


class APITestCase(AppBaseTestCase):

    def test_api(self):
        pass

    def test_image_db_calls(self):
        name = 'test_name'
        src = 'test_src'
        add_image(name, src)
        images = get_all_images()
        assert src in images

        # just checking if db.execute cleans values that it inserts
        src = "'123');DELETE from images where id in (1, 2, 3);"
        add_image(name, src)
        images = get_all_images()
        assert src in images

    def test_images_api_call(self):
        response = self.client.get('/images/')
        print response

        response = self.client.post('/images/', data='{"name":"Balanced","src":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAAQCAMAAADDNnYVAAAAmVBMVEVXWFpfYGJpaWtycnR7e32EhIaNjY+Wlpefn6CipA+mqB2oqKmxsbKztUS6uru8vV/AwW3Dw8TExXvFxnvJyojMzMzR0qPV1dXW1rHa2r7e3t7e38zj49nmpRLmqR/mrSzmrS3msTnnyonnzpfn1rLn27/n38zn49rn5+fox8Xo0tDqk43qnZjqqKTriIHrk43tU0ntXlTuPzMyENYEAAACeklEQVR42q2VC5PTIBDHIUCghquiRhQ9H3enx/k4td//w7nLApvUpDPO+J+W7oNkfyQLFQ+/T4+56d3Tw9UbMq0mmSn29BH8UO0Z7DmvlCDkFmlPJlvBKiGkmVIJsyy71pdy4tfpdPqeq14eDocrMrVoknBTjplqB7DDGssLUOS0JGywXKE2omo4YpilV65N4J1AP3PVc8B60hCYq5aaixd3sQZMO04LlRZYSQlW3MWiy8QjYD3kqteA9axjDQ6EtSYKjbSYPaxAa1g6ZoFlC8DkrRTCU3hwpOpqMFXhyiL/+PY1d7198YpfmG6PyFHrYFH4pB2s+o58S6OmjhV7LukxV47MamWCxHkib4qxjjDrWCIO5+N3GysixYBLpTRpbgUt/ZD2saigvoQltdYKn2lvnRGHYQuL6qaJopTG9y9TLagxfYYleSMyFrXoLtZ5x3usSOMWVpJInQSMLe0MLrwWRMy8wurSayx9GYu55rYHqLo5w2Jq2haxYSWFIxXErvw/WCqE4G3t8lmw4gbWwGnXsPIse0TTdSzeif7fXqKmFmyPgWXPsdBlyY6VfcdyfBSndKnlJ5zYsO5vbu63saiLk1hIpr+wzDLvOxauhg8IOgBnpdI+1iRAQVSqD9fXn3gOH6dW0TZ3WC2gHNdVdSdRUROKJMQZq7QXH6eDdYbOcdqJvBUxCaYUZdNUrLtr0N0aa9WT/UAqzTtQXU5b7pwRV9uxcpRkcRsw1s6fj8kN6zNifdnBGlPmY5QQwhorSRz5WB0ZKx+75STfcB9r8Ohl0u37j7d5Ke+qfMR7g9EyEewAY5evoaoJnGXEdytORmvtZoJkeXZr8g/c6MVVA/xargAAAABJRU5ErkJggg=="}')
        print response.data

        response = self.client.get('/images/')
        print response


if __name__ == '__main__':
    unittest.main()
