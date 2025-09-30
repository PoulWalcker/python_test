import pytest

POST_OUTPUT_REQUIRED_KEYS = ("userId", "id", "title", "body")


class TestPosts:
    """Basic CRUD operations for /post"""

    @pytest.mark.parametrize("post_id", [1, 10, 100])
    def test_status_code(self, session, base_url, post_id):
        resp = session.get(f"{base_url}/posts/{post_id}", timeout=10)
        assert resp.status_code == 200

    def test_get_wrong_path_404(self, session, base_url):
        resp = session.get(f"{base_url}/postsss/1", timeout=10)
        assert resp.status_code == 404

    @pytest.mark.parametrize("post_id", [1, 10, 100])
    def test_get_post_data(self, session, base_url, post_id):
        resp = session.get(f"{base_url}/posts/{post_id}", timeout=10)
        data = resp.json()

        assert all(k in data for k in POST_OUTPUT_REQUIRED_KEYS)
        assert data["id"] == post_id

        assert isinstance(data["userId"], int)
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)

    def test_get_posts_list(self, session, base_url):
        resp = session.get(f"{base_url}/posts", timeout=10)
        assert resp.status_code == 200

        data = resp.json()
        assert isinstance(data, list) and len(data) > 0

        sample = data[0]
        for k in POST_OUTPUT_REQUIRED_KEYS:
            assert k in sample

    @pytest.mark.parametrize(
        "payload",
        [
            {"title": "test_1", "body": "test_1_body", "userId": 1},
            {"title": "test_2", "body": "test_2_body", "userId": 2},
        ],
    )
    def test_create_post_data(self, session, base_url, payload):
        resp = session.post(f"{base_url}/posts", json=payload, timeout=10)
        assert resp.status_code == 201
        data = resp.json()
        for k, v in payload.items():
            assert data.get(k) == v
        assert "id" in data and isinstance(data["id"], int)

    def test_update_post_put_data(self, session, base_url):
        payload = {"id": 1, "title": "updated", "body": "content", "userId": 1}
        resp = session.put(f"{base_url}/posts/1", json=payload, timeout=10)

        assert resp.status_code == 200

        data = resp.json()
        for k, v in payload.items():
            assert data.get(k) == v

    def test_patch_post_data(self, session, base_url):
        resp = session.patch(
            f"{base_url}/posts/1", json={"title": "patched"}, timeout=10
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("title") == "patched"

    def test_delete_post(self, session, base_url):
        r = session.delete(f"{base_url}/posts/1", timeout=10)
        assert r.status_code == 200
        assert r.json() == {}
