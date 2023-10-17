from flask import Flask, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import logging

sentry_sdk.init(
    dsn="https://e1d80580a03ad4bfb85abab2322ccb46@o1190567.ingest.sentry.io/4505993437511680",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


@app.route('/test_type')
def test_type():
    user_id = request.args.get('user_id')
    user_id = float(user_id)


@app.route('/test')
def ll():
    raise IndexError


@app.route('/test_logging222')
def test_logging():
    logging.error("error to log")


if __name__ == '__main__':
    app.run()