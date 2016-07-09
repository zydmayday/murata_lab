from django import template

register = template.Library()

def render_icon_url(url):
	'''
	NOT GOOD!
	need to use another formal way to handle url
	'''
	return '/' + '/'.join(url.split('/')[1:])

register.filter('render_icon_url', render_icon_url)