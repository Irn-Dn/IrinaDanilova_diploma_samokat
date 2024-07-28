import sender_stand_request
import data


def test_get_order_by_track_200_response():
    create_order_response = sender_stand_request.post_new_order(data.order_body)
    tr = create_order_response.json()["track"]

    response = sender_stand_request.get_order_by_track(tr)
    # Проверка кода ответа
    assert response.status_code == 200





# Ирина Данилова, 19-я когорта — Финальный проект. Инженер по тестированию плюс