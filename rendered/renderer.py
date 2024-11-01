from abc import ABC, abstractmethod
from typing import Any, Dict,List

from template_loader import template


class BaseRenderer(ABC):
    def __init__(self, content: Dict[str, Any], name: str = None, id:str=None, config:dict=None,**kwargs):

        self.content = content
        self.kwargs = kwargs

        if name is not None:
            self.content['name'] = name
        
        if config is not None:
            self.content['config'] = config

        if id is not None:
            self.content['id'] = id

        if type is not None:
            self.type = type
        

    @property
    def name(self) -> str:
        return self.content.get('name', None)
    
    @property
    def id(self) -> str:
        return self.content.get('id', None)

    @abstractmethod
    def render(self) -> Any:
        pass

class HTMLSVG(BaseRenderer):
    """Renders the SVG Image"""
    def __init__(self, body: Any, name: str, **kwargs):
        if name is None:
            name = "Image"
        super().__init__(content={"body":body}, name=name, *kwargs)

    def render(self, **kwargs) -> str:
        nav_items = [self.content['name']]
        return template("svg.html").render(**self.content, **kwargs)

class HTMLText(BaseRenderer):
    """Just Text"""
    def __init__(self, text:List[str]=None, **kwargs):
        if not isinstance(text,list):
            text = [text]
        super().__init__(content={'text':text}, **kwargs)

    def render(self):
        return template("text.html").render(**self.content, **self.kwargs)

class HTMLDiv(BaseRenderer):
    def __init__(self, div_class, content, **kwargs):
        self.div_class = div_class
        content = [content] if isinstance(content,list) else content
        super().__init__(content=content,**kwargs)

    def render(self):
        return template("div").render(content=self.content, **self.kwargs)

class HTMLPage(BaseRenderer):
    """Renders the base report"""
    def __init__(self, body: Any, name: str, **kwargs):
        if name is None:
            name = "Election Result"
        super().__init__(content={"body":body}, name=name, *kwargs)

    def render(self, **kwargs) -> str:
        nav_items = [self.content['name']]
        return template("base.html").render(**self.content, nav_items=nav_items, **kwargs)