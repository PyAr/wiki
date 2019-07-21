{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(400, 300),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileAyuda',
                   'label':u'Ayuda',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'btnEjecutar', 
    'position':(285, 16), 
    'label':'Ejecutar', 
    },

{'type':'TextArea', 
    'name':'txtResultados', 
    'position':(19, 43), 
    'size':(341, 175), 
    },

{'type':'TextField', 
    'name':'txtComando', 
    'position':(83, 17), 
    'size':(190, -1), 
    },

{'type':'StaticText', 
    'name':'Comando', 
    'position':(20, 20), 
    'text':'Comando', 
    },

] # end components
} # end background
] # end backgrounds
} }
