import re
from playwright.sync_api import Page, expect
from testcontainers.compose import DockerCompose

def test_has_title(page: Page):


    compose = DockerCompose("./", compose_file_name="docker-compose.yml",
                        pull=True)
    with compose:
        stdout, stderr = compose.get_logs()

    compose.start()
    compose.wait_for("http://localhost:5000")

    page.goto("http://localhost:5000")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Hello, World!"))
