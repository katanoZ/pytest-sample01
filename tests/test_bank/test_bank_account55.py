import pytest

from src.bank_account import BankAccount


@pytest.mark.raises
def test_withdraw_insufficient_balance():
    amount = BankAccount(500)
    with pytest.raises(ValueError, match="残高不足です"):
        amount.withdraw(501)


@pytest.mark.skip(reason="作り途中です")
def test_features_XXX():
    # 未実装のテスト
    pass
