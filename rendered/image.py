from pathlib import Path

from template_loader import template

save_dir = r'C:\Users\Neil\Documents\Projects\Electoral-PH\Electoral-PH\rendered\rendered_pages'
file_name= 'pres_2004.html'

def 

def main_page():
    main_page = template('base.html')
    page = main_page.render()
    save_path = Path(save_dir+'/'+file_name)
    save_path.write_text(page,encoding='utf-8')


if __name__ == '__main__':
    main_page()