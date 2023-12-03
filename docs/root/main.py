from radiant.framework.server import RadiantAPI, RadiantServer, render
from browser import html
from browser.template import Template


########################################################################
class StaticApp(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        self.body <= self.under_construction()

        # Template("menu").render()

    # ----------------------------------------------------------------------

    def under_construction(self):
        """"""

        # <h1>Sitio en Construcción</h1>
            # <p>Estamos trabajando para lanzar nuestro nuevo sitio web. ¡Vuelve pronto!</p>

        return render('placeholder.html')

    # ----------------------------------------------------------------------

    def main(self):
        """"""
        context = {
            'title': 'TITULO',
            'titles': ["Rendered",
                       "Radiant",
                       "Framework",
                       "Layout",
                       ],
        }

        return render('main.html', context)


if __name__ == '__main__':
    RadiantServer('StaticApp',
                  port='5001',
                  template='layout.html',
                  static_app='docs',
                  )
