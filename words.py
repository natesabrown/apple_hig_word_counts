# https://www.twilio.com/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def getWordCountFor(system):
    # make sure valid system user is checking for
    # VALID_SYSTEMS = ["ios", "macos", "tvos", "watchos"]
    # if system not in VALID_SYSTEMS:
    #     systems_string = ", ".join(VALID_SYSTEMS)
    #     exception_text = f"Valid system was not given for word count: {system}.\nValid systems include: {systems_string}"
    #     raise Exception(exception_text)
    url = f"https://developer.apple.com/design/human-interface-guidelines/{system}/overview/"
    # handle exceptions
    if system == "augmented-reality":
        url = "https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/augmented-reality/"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    NAV_ID = "doc-nav"
    nav = soup.find(id = NAV_ID)
    links = nav.findAll("a")
    iosLinks = []
    for link in links:
        href = link.get("href")
        if system in href:
            iosLinks.append(link)
    sanitized_links = []
    # sanitize links, because apple included some redundancy
    for index in range(len(iosLinks)):
        if index == 0:
            sanitized_links.append(iosLinks[index])
        curEl = iosLinks[index]
        lastEl = iosLinks[index - 1]
        curLink = curEl.get("href")
        lastLink = lastEl.get("href")
        if lastLink in curLink:
            continue
        else:
            sanitized_links.append(curEl)
    iosLinks = sanitized_links
    # now we have ios links, we can check the content

    print("Loading text...")
    text_strings = []
    for link in tqdm(iosLinks):
        href = link.get("href")
        apple_href = f"https://developer.apple.com{href}"
        page_text = requests.get(apple_href).text
        soup = BeautifulSoup(page_text, 'html.parser')
        main_content = soup.find("div", class_="column large-9 small-12 hig-content")
        text = main_content.getText()
        text_strings.append(text)

    total_words = 0
    for string in text_strings:
        words = string.split()
        total_words += len(words)

    # result_str = f"Total Words: {total_words}"
    # print(result_str)
    return total_words

def getTechnologiesWordCount():
    tech_strings = [
        "accessibility",
        "airplay",
        "app-clips",
        "apple-pay",
        "augmented-reality",
        "business-chat",
        "carekit",
        "carplay",
        "game-center",
        "glyphs",
        "healthkit",
        "homekit",
        "icloud",
        "in-app-purchase",
        "inclusion",
        "live-photos",
        "mac-catalyst",
        "machine-learning",
        "maps",
        "researchkit",
        "right-to-left",
        "shareplay",
        "sign-in-with-apple",
        "siri",
        "social-media",
        "sf-symbols",
        "wallet",
        "widgets"
    ]
    count = 0
    for string in tech_strings:
        word_count = getWordCountFor(string)
        count += word_count
    return count

if __name__ == "__main__":
    # system_choice = input("What system to count the words for? ")
    # word_count = getWordCountFor(system_choice)
    word_count = getTechnologiesWordCount()
    print(f"Total words: {word_count}")