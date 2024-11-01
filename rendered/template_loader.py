import warnings
from typing import Any

import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_DIR = "templates"

# initialize jinja environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def template(template_name:str)-> jinja2.Template:
    if not template_name.endswith('.html'):
        warnings.warn(f"Template {template_name} does not have the correct file extension '.html'! adding '.html' to template name", stacklevel=2)
        template_name += ".html"

    return env.get_template(template_name)
