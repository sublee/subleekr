import urlparse


class Site(object):
    """The site."""

    DEFAULT_ICON = "/favicon.ico"

    def __init__(self, name, url, description=None, icon=False):
        self.name, self.description = name, description
        self.url = url 
        if isinstance(icon, bool):
            self.use_icon = icon
        elif isinstance(icon, basestring):
            self.icon_url = icon
            self.use_icon = True
        else:
            raise ValueError("icon should be bool or basestring.")

    @property
    def icon(self):
        if self.use_icon:
            try:
                return urlparse.urljoin(self.url, self.icon_url)
            except AttributeError:
                return urlparse.urljoin(self.url, self.DEFAULT_ICON)

