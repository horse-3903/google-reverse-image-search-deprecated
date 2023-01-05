from playwright.sync_api import sync_playwright, Page, Playwright
from os.path import isfile
from time import sleep

def search_with_url(page:Page,url:str) -> None:
    page.get_by_role("button", name="Search by image").click()
    url_input = page.get_by_placeholder("Paste image link")
    url_input.hover()
    url_input.type(url)
    page.get_by_role("button",name="Search",exact=True).first.click()
    page.goto(page.get_by_role("link", name="Find image source").get_attribute("href"))
    pick_img_size(page=page,lens=True)
    return results_to_json(page=page, lens=False)

def search_with_file(page:Page,file_path:str):
    if not isfile(file_path):
        raise FileNotFoundError
    page.get_by_role("button", name="Search by image").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("upload a file").click()
    file_chooser = fc_info.value
    file_chooser.set_files(file_path)
    page.goto(page.get_by_role("link", name="Find image source").get_attribute("href"))
    pick_img_size(page=page,lens=True)
    return
    return results_to_json(page=page, lens=False)

def search_with_query(page:Page,query:str):
    query_input = page.get_by_role("combobox",name="Search")
    query_input.hover()
    query_input.type(query)
    query_input.press("Enter")
    return pick_img_size(page=page,lens=False)

def results_to_json(page:Page, lens:bool, num:int = 5) -> dict:
    if lens:
        pass
    else:
        loc = page.get_by_text("Image results").locator("../div")
        suc = 0
        idx = 0
        links:list = []

        while suc < num:
            div = loc.nth(idx)
            div.click()
            if page.get_by_role("region").get_by_role("link").get_by_role("img").get_attribute("src").find("data") != 0:
                links.append({
                    "link":page.get_by_role("region").get_by_role("link").get_by_role("img").get_attribute("src"),
                    "name":page.get_by_role("region").get_by_role("link").get_by_role("img").get_attribute("alt"),
                    "dimension":[int(i.replace(",","")) for i in page.get_by_role("region").get_by_role("link").locator("span").text_content().split(" × ")]
                })
                idx += 1
                suc += 1
            else:
                idx += 1
        return {
            "title":page.locator("input[role='combobox'][aria-label='Search']").get_attribute("value"),
            "data":links
        }

def pick_img_size (page:Page, lens:bool):
    if lens:
        page.get_by_role("button", name="Tools").click()
        page.get_by_role("button", name="Search by image").filter(has_text="Search by image").click()
        page.get_by_role("menuitemradio").filter(has_text="More sizes").click()
        try:
            if page.wait_for_selector("text='Looks like there aren’t any matches for your search'").is_visible():
                page.go_back()
                page.go_back() # go back to lens
                visual_matches = page.get_by_text("Visual matches").locator("//../../div").nth(1).locator("div").nth(1)
                col_num:int = int(visual_matches.get_attribute("style")[27:])

                # results_to_json(page=page, lens=False)
                # last resort
                # page.get_by_role("button", name="Tools").click()
                # page.get_by_role("button", name="Search by image").filter(has_text="Search by image").click()
                # page.get_by_role("menuitemradio").filter(has_text="Visually similar").click()
        except:
            print("failed")
            sleep(100)
            pass

    # if :
    # else:
    return
    page.get_by_role("button", name="Tools").click()
    page.get_by_text("Size").click()
    page.get_by_role("link", name="Large").filter(has_text="Large").click()

def main(p:Playwright) -> None:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com.my/imghp")
    
    # print(search_with_query(page=page,query="astronomy"))
    # print(search_with_url(page=page, url="https://picsum.photos/100"))
    print(search_with_file(page=page,file_path="C:/Users/chong/Downloads/rezerorealize-cropped.jpeg"))
    
    context.close()
    browser.close()

with sync_playwright() as p:
    main(p)