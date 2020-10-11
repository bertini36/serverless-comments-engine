def test_get_comments_ok(client):
    # Exists at data/comments.json
    res = client.get('comments/recoding-my-blog')

    assert res.status_code == 200
    assert len(res.json) > 0


def test_get_comments_ko(client):
    res = client.get('comments/invent')

    assert res.status_code == 200
    assert len(res.json) == 0


def test_add_comment_ok(client):
    data = {
        'name': 'Brook',
        'email': 'brook@op.com',
        'text': 'Yohoho'
    }
    res = client.get('comments/recoding-my-blog')
    num_comments_before = len(res.json)

    client.post('comments/recoding-my-blog', json=data)

    res = client.get('comments/recoding-my-blog')
    num_comments_after = len(res.json)
    assert res.status_code == 200
    assert num_comments_before + 1 == num_comments_after


def test_add_comment_ko(client):
    data = {'invent': 'invent'}

    res = client.post('comments/recoding-my-blog', json=data)

    assert res.status_code == 400
