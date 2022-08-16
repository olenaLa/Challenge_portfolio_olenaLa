from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_header_xpath = "//h6"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//div[2][@role='button']"
    language_button_xpath = "//ul[2]/div[1]"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    players_count_xpath = "//main/div[2]/div[1]"
    dev_team_contact_link_xpath = "//main/div[3]/div[1]/div/div[3]/a" "//a[contains(@href, '://')]"
    report_link_xpath = "//div[4]/div/div/a/button"
    shortcuts_card_xpath = "//main/div[3]/div[2]/div/div"
    activity_card_xpath = "//div[3]/div/div/h2"
    search_input_xpath = "//*[contains(@class, 'MuiInputBase-input')]"

