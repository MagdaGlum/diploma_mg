import function

# Марина Глинская, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import pytest
import requests

def test_order_info():
    order_resp = function.get_order_info()
    assert order_resp.status_code == 200


