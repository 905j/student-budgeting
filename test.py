import unittest
from unittest.mock import patch
from chatgpt-api import get_budget_advice
import json

class TestChatGPTAPI(unittest.TestCase):

    @patch('openai.ChatCompletion.create')
    def test_budget_totals_to_monthly_earnings(self, mock_create):
        # Mock response content
        mock_response = {
            "savings": 500,
            "need1": 200,
            "need2": 100,
            "want1": 50,
            "feedback": "You don't need Netflix lmao"
        }
        mock_create.return_value.choices[0].message = {'content': json.dumps(mock_response)}
        # student_info for this instance
        student_info = {
            "name": "Tiffanie Giselle Jalal",
            "savings_amount": 1000,
            "monthly_earnings": 850,
            "needs": ["need1", "need2"],
            "wants": ["want1"]
        }

        result = get_budget_advice(student_info)
        budget = json.loads(result)
        # Making sure all the values in the response equal the student's monthly earning
        total = budget['savings'] + budget['need1'] + budget['need2'] + budget.get('want1', 0)
        self.assertEqual(total, student_info['monthly_earnings'])


