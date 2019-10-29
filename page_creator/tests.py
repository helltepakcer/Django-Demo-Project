from django.test import TestCase
from .form import PageCreatorForm


class PageCreatorFormTest(TestCase):

    def test_page_creator_form_title_exist(self):
        form = PageCreatorForm()
        self.assertTrue(form['title'])

    def test_page_creator_form_title_len(self):
        form = PageCreatorForm()
        self.assertTrue()
        pass

