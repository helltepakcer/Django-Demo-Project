from django.test import TestCase
from .form import PageCreatorForm
from .models import PageCreator
from django.contrib.auth.models import AnonymousUser, User


class PageCreatorFormTest(TestCase):

    def test_page_creator_form_title_exist(self):
        form = PageCreatorForm()
        self.assertTrue(form['title'])

    def test_page_creator_form_title_max_len(self):
        two_hundred_simbols = ''
        for i in range(104):  # equal len = 202
            two_hundred_simbols = '{}{}'.format(two_hundred_simbols, str(i))
        data = {'title': two_hundred_simbols}
        request = self.client.post('/page-creator/', data=data)
        self.assertNotEqual(request.status_code, 302)

    def test_page_creator_form_title_default_len(self):
        two_hundred_simbols = ''
        for i in range(103):  # equal len = 199
            two_hundred_simbols = '{}{}'.format(two_hundred_simbols, str(i))
        data = {'title': two_hundred_simbols}
        request = self.client.post('/page-creator/', data=data)
        self.assertEqual(request.status_code, 302)

    def test_form_one_word_input(self):
        one_word = 'oneWord'
        data = {'title': one_word}
        request = self.client.post('/page-creator/', data=data)
        self.assertEqual(request.status_code, 302)

    def test_form_more_words_input(self):
        two_words = 'two words'
        data = {'title': two_words}
        request = self.client.post('/page-creator/', data=data)
        self.assertEqual(request.url, '/page-creator/input_error')


class PageCreatorPageTest(TestCase):

    # TODO Test for PageCreator page work
    # TODO 1)Make request 2)Check for status 200

    # TODO Test for result of PageCreator |
    # TODO 1)SetUp 2)Create new 3)Check for exist

    pass


