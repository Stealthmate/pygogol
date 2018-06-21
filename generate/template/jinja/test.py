fc = ""
with open("./Resource.py") as f:
    fc = f.read()

from jinja2 import Template

t = Template(fc)
print(t.render(
    resourceName="test",
    resourceUrl="/test/a/bc/",
    resourceMethod="POST",
    pathParams=["a"], 
    queryParams=["q1", "a2"], 
    bodyParam = "file"))