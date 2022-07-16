import sys

from jinja2 import Environment, FileSystemLoader


def main(args):
    if len(args) > 1:
        plan = args[1]
    else:
        plan = 'kver'
    if len(args) > 2:
        runtime = args[2]
    else:
        runtime = 'shell'
    templates_paths = ['config/runtime']
    jinja2_env = Environment(loader=FileSystemLoader(templates_paths))
    template = jinja2_env.get_template(f'{plan}.jinja2')
    params = {
        'kver': {
            'message': "Hello.",
        },
        'runtime': runtime,
    }
    print(template.render(params))


if __name__ == '__main__':
    main(sys.argv)
