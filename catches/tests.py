from django.http import HttpRequest
from django.test import TestCase

from django.urls import resolve
from catches.views import top,catche_new,catche_edit,catche_detail

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


# あるURLにアクセスしたときに意図したビュー関数に紐づいているか確認

class CreateCatcheTest(TestCase):
    def test_should_resolve_catche_new(self):
        found = resolve("/catches/new/")
        self.assertEqual(catche_new, found.func)


class CatcheDetailTest(TestCase):
    def test_should_resolve_catche_detail(self):
        found = resolve("/catches/1/")
        self.assertEqual(catche_detail, found.func)


class EditCatcheTest(TestCase):
    def test_should_resolve_catche_edit(self):
        found = resolve("/catches/1/edit/")
        self.assertEqual(catche_edit, found.func)