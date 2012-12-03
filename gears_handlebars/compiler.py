import os
from gears.compilers import ExecCompiler


SOURCE = '\n'.join((
    "(function() {",
    "  var template  = Handlebars.template,",
    "      templates = Handlebars.templates = Handlebars.templates || {};",
    "  templates['%(path_without_suffix)s'] = template(%(processed_source)s);",
    "}).call(this);"))


class HandlebarsCompiler(ExecCompiler):

    result_mimetype = 'application/javascript'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'compiler.js')]

    def __init__(self, source=SOURCE):
        self.source = source

    def __call__(self, asset):
        super(HandlebarsCompiler, self).__call__(asset)
        data = asset.__dict__
        data.update(asset.attributes.__dict__)
        asset.processed_source = self.source % data
