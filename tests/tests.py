import os
import tempfile

import pytest

from flaskr import flaskr

@pytest.fixture
def client():
    db_fd, flaskr.apis.config['DATABASE'] = tempfile.mkstemp()
    flaskr.apis.config['TESTING'] = True
    client = flaskr.apis.test_client()

    with flaskr.apis.app_context():
        flaskr.init_db()

    yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])