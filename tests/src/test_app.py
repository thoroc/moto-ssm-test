import sure  # noqa # pylint: disable=unused-import
from src.app import lambda_handler


def test_lambda_handler(mock_ssm_client):
    # Arrange
    event = {}
    context = "test"

    # Act
    results = lambda_handler(event, context)

    # Assert
    assert len(results).should.be.equal(2)
