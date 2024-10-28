from django.http import HttpRequest
from django.test import TestCase
from catches.views import top


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        # request = HttpRequest() # HttpRequestオブジェクトの作成
        # response = top(request)
        # Clientクラスを用いると、任意のエンドポイントに対してGETやPOSTといったHTTPリクエストを送信
        # した際の挙動を確認できる。
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        # request = HttpRequest()
        # response = top(request)
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")
