import threading
import time
from shopping_app import app as shopping_app_module
from shopping_app.test_selenium_auth import run_test


def start_server():
    # Run Flask app in a thread
    shopping_app_module.app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)


if __name__ == '__main__':
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    # wait for server to start
    time.sleep(1.5)
    print('Server started at http://127.0.0.1:5000')
    print('A browser window will open so you can sign in manually. After signing in, press Enter here to let the test continue (or wait for auto-detect).')
    try:
        input('Press Enter to start the test runner (or Ctrl+C to exit and sign in manually in your own browser)...')
    except Exception:
        pass
    try:
        # run the selenium test in manual mode (it will open a browser and wait up to 10 minutes for manual sign-in)
        run_test()
    finally:
        print('Test finished; exiting.')
