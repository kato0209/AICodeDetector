if self.container: return # ignore in case we're not within an SVG div with the container attribute
if self.style: self.style.remove
self.style = ''

# if self.width: if self.width[-1] != '%': self.style += 'width:%spx;' % self.width else: self.style += 'width:%s;' % self.width if self.height: