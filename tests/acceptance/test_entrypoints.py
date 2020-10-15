def test_add_comment_ok(client):
    data = {'name': 'John Doe', 'email': 'john@doe.com', 'text': 'Ouh mama'}

    res = client.post('comments/test-post', json=data)

    assert res.status_code == 200


def test_get_comments_ok(client):
    res = client.get('comments/test-post')

    assert res.status_code == 200
    assert len(res.json) == 1


def test_get_comments_ko(client):
    res = client.get('comments/invent')

    assert res.status_code == 200
    assert len(res.json) == 0


def test_add_comment_ko(client):
    data = {'invent': 'invent'}

    res = client.post('comments/invent', json=data)

    assert res.status_code == 400
