from pyramid.config import Configurator

# Returns a router to act as a WSGI which is used to start a WSGI server, Waitress
# **settings refers to a set of key/value pairs in development and production.ini
# more information under "startup" in the pyramid narrative docs
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/startup.html#startup-chapter
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
