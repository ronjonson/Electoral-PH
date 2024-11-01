from pathlib import Path

from renderer import HTMLPage, HTMLText

save_dir = r'C:\Users\Neil\Documents\Projects\Electoral-PH\Electoral-PH\rendered\rendered_pages'

def main_page():
    main_page = HTMLPage(body=HTMLText("test"), name="welcome")
    page = main_page.render()
    save_path = Path(save_dir+'/'+'main.html')
    save_path.write_text(page,encoding='utf-8')


if __name__ == '__main__':
    main_page()