import pytest
from modules.api.clients.github import GitHub

@pytest.fixture
def github_api():
    return GitHub()

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('shykhaliievanarhiz')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    print(r)
    assert r['total_count'] == 26
    assert 'become-qa-auto' in r ['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('narhizshykhaliieva_repo_non_exist')
    assert r['total_count'] == 0    

@pytest.mark.api
def test_one_symbol_repo_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0    