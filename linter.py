from SublimeLinter.lint import NodeLinter

class XO(NodeLinter):
	npm_name = 'xo'
	cmd = ('xo', '--stdin', '--reporter', 'compact', '--filename', '@')
	regex = (
		r'^.+?: line (?P<line>\d+), col (?P<col>\d+), '
		r'(?:(?P<error>Error)|(?P<warning>Warning)) - '
		r'(?P<message>.+)'
	)
	defaults = {
		'selector': 'source.js - meta.attribute-with-value',
		'disable_if_not_dependency': True
	}
