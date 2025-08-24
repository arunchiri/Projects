import os
from jinja2 import Environment, FileSystemLoader

def generate_code(template_path, output_path, context):
    """
    Generates code from a Jinja2 template.
    """
    template_dir, template_name = os.path.split(template_path)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)

    rendered_code = template.render(context)

    with open(output_path, 'w') as f:
        f.write(rendered_code)
