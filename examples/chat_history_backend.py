import os

os.environ["HISTORY_BACKEND"] = "postgres"
os.environ["REDIS_HOST"] = "redis://localhost:6379"

from codeinterpreter import CodeInterpreterSession  # noqa: E402


def main():
    session_id = None
    kernel_id = None
    port = None

    session = CodeInterpreterSession()
    session.start()

    print("Session ID:", session.session_id)
    session_id = session.session_id
    kernel_id = session.kernel_id
    port = session.port

    response = session.generate_response_sync(
        "Plot the bitcoin chart of 2023 YTD"
    )
    response.show()

    del session

    assert session_id is not None
    session = CodeInterpreterSession.from_id(session_id, kernel_id, port)

    response = session.generate_response_sync("Now for the last 5 years")
    response.show()

    session.stop()


if __name__ == "__main__":
    main()
