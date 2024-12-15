from unittest.mock import patch

from src.bank_account import BankAccount


def test_get_balance_in_currency():
    amount = BankAccount(1000)
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rate": 150}

        balance_JPY = amount.get_balance_in_currency("JPY")
        assert balance_JPY == 150000, "変換後の値が正しくありません"
