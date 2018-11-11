import logging
from cmreslogging.handlers import CMRESHandler


def function_that_does_somehing():
    log.info("This is an info statement that will be logged into elasticsearch") 


def main():
    handler = CMRESHandler(hosts=[
        {'host': 'localhost', 'port': 9200}],
        auth_type=CMRESHandler.AuthType.NO_AUTH
        )
    global log
    log = logging.getLogger('PythonTest')
    log.setLevel(logging.INFO)
    log.addHandler(handler)

    function_that_does_somehing()
    return 0


if __name__ == "__main__":
    main()
