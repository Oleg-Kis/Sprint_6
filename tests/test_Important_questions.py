import pytest
from pages.main_page import MainPage
import data

class TestImportantQuestions:
    @pytest.mark.parametrize('question_number, answer_text', data.Questions.block_questions)
    def test_text_all_question(self, driver, question_number, answer_text):
        main_page = MainPage(driver)
        main_page.click_on_question(question_number)

        assert main_page.check_answer(answer_text)
