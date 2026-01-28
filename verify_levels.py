from playwright.sync_api import sync_playwright

def verify_levels():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file://" + "/app/index.html")

        # 1. Check Level Options in Setup
        # We need to click "Opslaan & Start" on parent screen first or "Mama & Papa" to see Setup?
        # Actually setup-container is hidden by default? No, Parent Screen is shown first usually if no config.
        # But wait, looking at code:
        # loadSettings() -> if configName exists -> updatePersonalizedLabels.
        # The HTML starts with parent-screen visible?
        # <div id="parent-screen" ... display: flex ...>
        # <div id="setup-container" ... display: none ...>

        # So we need to click "Opslaan & Start" to go to Setup.
        print("Navigating to Setup Screen...")
        page.locator("#parent-save-btn").click()

        setup = page.locator("#setup-container")
        setup.wait_for(state="visible")

        print("Checking Level Options...")
        level_buttons = page.locator("#level-options .option-btn")
        count = level_buttons.count()

        if count != 3:
            print(f"FAILURE: Expected 3 level buttons, found {count}")
            exit(1)

        texts = level_buttons.all_text_contents()
        expected = ["Level 1 (0-10)", "Level 2 (1-20)", "Level 3 (tot 100)"]

        for i, text in enumerate(texts):
            if expected[i] not in text:
                 print(f"FAILURE: Button {i} text mismatch. Expected '{expected[i]}', got '{text}'")
                 exit(1)

        print("Level buttons verified successfully.")

        # 2. Check Badge Descriptions in Parent Screen
        # Go back to parent screen
        page.locator("#to-parent-btn").click()
        page.locator("#parent-screen").wait_for(state="visible")

        print("Checking Badge Descriptions...")
        # Check specific badge descriptions updated
        bee = page.locator(".badge-card.session:has-text('Bij') .desc").text_content()
        if "Level 1 Voltooid" not in bee:
             print(f"FAILURE: Bee badge description wrong: '{bee}'")
             exit(1)

        bear = page.locator(".badge-card.session:has-text('Beer') .desc").text_content()
        if "Level 2 Bereikt" not in bear:
             print(f"FAILURE: Bear badge description wrong: '{bear}'")
             exit(1)

        fox = page.locator(".badge-card.session:has-text('Vos') .desc").text_content()
        if "Level 3 Bereikt" not in fox:
             print(f"FAILURE: Fox badge description wrong: '{fox}'")
             exit(1)

        print("Badge descriptions verified successfully.")

        browser.close()

if __name__ == "__main__":
    verify_levels()
