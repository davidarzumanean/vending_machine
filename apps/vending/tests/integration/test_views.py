from decimal import Decimal
from unittest.mock import ANY

import pytest
from rest_framework import status


@pytest.mark.django_db
class TestListVendingMachineSlots:
    def test_list_products_returns_expected_response(self, client):
        response = client.get("/products/")

        expected_response = [{"id":"80c7003e-0d40-443a-a2ea-794873de0961","name":"Kilikia","price":"2.00","stock":"777","logo":"https://www.ccifrance-armenie.com/fileadmin/_processed_/9/c/csm_kilikia_804f7f0295.jpg","color":"#214F33"},{"id":"883200a0-ada7-4885-8db8-5250c4a33add","name":"Estrella","price":"1.80","stock":"800","logo":"https://seeklogo.com/images/E/estrella-damm-logo-08E04711FC-seeklogo.com.png","color":"#C40420"},{"id":"72cbce21-5bba-4566-91e5-6f1c03762f93","name":"Estrella Galicia","price":"1.90","stock":"500","logo":"https://unisportconsulting.com/beerpalma/wp-content/uploads/2018/04/ESTRELLA-GALICIA-1.jpg","color":"#000000"},{"id":"447ebea8-7e0b-4663-8870-39063f9d5c6c","name":"Dargett","price":"2.50","stock":"400","logo":"https://cdn.dribbble.com/users/1053232/screenshots/2776494/dargett_logo.jpg","color":"#000000"},{"id":"2cad3b30-b533-47c3-acd8-5ae1d7a4b099","name":"Corona","price":"1.90","stock":"1000","logo":"https://getvectorlogo.com/wp-content/uploads/2018/12/corona-extra-vector-logo.png","color":"#ffffff"},{"id":"ca22351b-401d-4d86-8400-9063e3515cc8","name":"1906","price":"2.50","stock":"613","logo":"https://dinichance.ch/images/deals/602fb994caad9.png","color":"#EFE3B2"}]

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_response
