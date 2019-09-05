
Boton Grafico TK
================

Crear un boton grafico personalizado, con 3 estados posibles *(Activado, con el Roedor Encima, Normal)*, usando TK.

`temp.jpg </images/BotonGraficoTK/temp.jpg>`_

*En la foto de pantalla se muestra el Ejemplo con el Raton Encima (Mouse Over)*

* **Requisitos:** Es necesario saber usar encoding en Base64, que NO es cubierto por esta Receta, disculpe.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # Esto es okbutton.py
    import Tkinter

    class OkButton(Tkinter.Button):
        def __init__(self, master, data = 0, *args, **kwargs):
                if data:
                    self.onImage = Tkinter.PhotoImage(data = kwargs['onImage'])
                    self.offImage = Tkinter.PhotoImage(data = kwargs["offImage"])
                    self.activeImage = Tkinter.PhotoImage(data = kwargs["activeImage"])
                else:
                    self.onImage = Tkinter.PhotoImage(file = kwargs['onImage'])
                    self.offImage = Tkinter.PhotoImage(file = kwargs["offImage"])
                    self.activeImage = Tkinter.PhotoImage(file = kwargs["activeImage"])
                del kwargs['activeImage'], kwargs["onImage"], kwargs["offImage"]
                Tkinter.Widget.__init__(self, master, 'button', kwargs, args)
                self.bind("<Enter>", self.mouseOver)
                self.bind("<Leave>", self.mouseLeave)
                self.bind("<Button-1>", self.mouseClick)
                self.bind("<ButtonRelease-1>", self.mouseLeave)
                self.mouseLeave(None)
        def mouseOver(self, Event):
            self["image"] = self.onImage
        def mouseLeave(self, Event):
            self["image"] = self.offImage
        def mouseClick(self, Event):
            self["image"] = self.activeImage

    oexitOff = '''\
    R0lGODlhXgAiAOf/AAABAAYAAAQABgUCBw0ACBMACRQACxUBDBMCEgkGDBAEDBkCFBYEDhsDEBIH
    DxwFERgHERwGEhsHFx8HGBUMEhoLEyEKGh8MFRcPFB4OGyINGycMHR0QFyMOHCQPHR0SHCUQHh4U
    HiMTHysRISAVIC0SIiQVICkUIi4TIyYWIioVIy4UJCIYIi8UJScXIzEWJi4YJioaJjQYKSsbKDIZ
    LSwcKTEbKi4eKjkdLjAgLDIhLjkfNDwgMDwiNzYlMj4jODwlNEAkNTgnND8lOjopNj8oN0MnN0Io
    PUUoOUEqOT4tOkQtO0csQUYvPkguQ0suP0QwQ0ovRUkxQEswRk4xQkozQkY1QlIxSEw0Q04zSEg2
    Q001RE42RVA1SlM1Rko4RVU3SFE5SFQ4Tkw7SFU5T1o4UFc7UVc8UVo8TlY+TVJATWA+VlNES1pC
    UWJAWGNBWWRCWmBEWllHVWZEXGJGXFdLV2ZHWWlGXmpHYGVJX1pNWWFMVWtIYWBNW2hLYW1KYmBR
    WG9MZF5SXnFOZmZTYXJPaG5RaGJWYnZSa2pXZXNVbG1YYXhUbXlVbm1aaGtcY25baXtXcHxYcXha
    cXBda31Zcn9bdIZbdoFddn1fdohdeIRfeXNmcopfeoxgfI5ifollfntrcpBkgItmgHpteZJmgo1o
    gpRohJZqhpFshZdrh5ltiZVviZhuj4N2god3f55xjZhzjZxylKBzj5t1j6F0kIx8hIt9ip13kaN2
    kox+i6J3maV4lKZ5laR5m6J8lqZ7nZODi6t9mql+oKp/oZeHj62CpLCCn5uKkq+EprWDp7GGqLmG
    q7SJq7uIrZ+Sn7aLrbeMrqWUnL+MsbmOsLuQsqiYn8GPs6SaoKmZoMSRtaycpMaTt8eUuKmgpsiV
    ucOXucmWu8qXvMuYvc2av86bwLalrdCcwdGdwrSqsNOfxNSgxdWhxtaiyNekydilyrqwt9qmy9un
    zMC2vMq5wcS7wdfN09rQ1tzS2OHX3ufd4+rg5u7k6vvw9/7//P///yH+EUNyZWF0ZWQgd2l0aCBH
    SU1QACH5BAEKAP8ALAAAAABeACIAAAj+AAEIHEiQYAACBRIqXMiwocOHECM6JBCgoMWLFyVq3Mix
    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
    QjuGMFpRCTS4ACoBAQA7
    '''
    oexitOn = '''\
    R0lGODlhXgAiAOf/AAABAAYAAAcAAAkBAA0ACBAAARUAARYAAxQACxkADB0ADRoBDRwAFB4ADyIA
    ER8BECEAFSUAEiQAFiQAFygAGCUBFywAGSsAHS0AGiIEFyYEGSoDGi4CICgHGzAFIzIHJCwMHzUJ
    JzsIKTYKJzwJKhYA/zAQIhsA/z4LLB8A/yIA/0ANLT0PKEcMMUEPL0kQMwQQ/0AUMTkYKk0TNkcV
    NDwaLUwUO0QYNFAWOS4N/08XPlcVPFAYP0kcOVkXPkoeOjMR/1gZRFkaREwgPFobRTYT/0QkO04h
    PlkZflgfRlEciEUoOV4fSVEkQEsT/0soO2YfTWEiTGQfYmghT04X/04rPk4c2mMkTmUjWWojUGwl
    UkMg/2smWFEzRFMg/3ApVm8qXGImsVQ2R1Yj/3EsXlgk/3AnnWUk/30uX1o8TV8r53wwZGcn/30x
    ZX4yZmE9UF4/UYAzZ20v0WEv/3QvzYI1amBCU4o1bYU4bG4w/3Q0yGRFV4w3b3Az/2ZHWI45cWxH
    W5A7c3w0/2xJYoY22ZI9dYw/c25LY3BLXmdOXn43/2xNXpQ/d3BNZZRBfZdBeZZDf5pCh51Cgos7
    /5pEfJI/x41AzYM//59EhKFEf41C6o5C/51KhqRIiKVJinRba5hD8JFE/6ZKi55H2KdMjJhF/5xG
    83lfb6hLq55I56lOjp9J9qtQkKtQoqVK8q1Skq1Nx7RRlLJRmrZSlqZP77BRvrdTl6tP6rVUnLlW
    mb1UsoVre7FU4bxYm8NXnr5anbtV2bdW37hZxsNapr1aw8JbrItwgcZcqMJeoYxygsJcv8ddqb1c
    18heqsJd08VdzsVfwspgrMxgp8peys1irs9ksJJ7hctkyNBmss9lxJd8jNJotNlmttRnwddnu9Np
    tdpnt9tpuNxquZeDkd1rup6KmaCMm6KOnaaPmKWQn6iToqqVpLKdrbWgsLumtcCvt8mxu8iywtPE
    0tfFzdbI1drI0dzL0+LQ2OjX3+vZ4e7c5PDe5/nq+P3r8/78/////yH+EUNyZWF0ZWQgd2l0aCBH
    SU1QACH5BAEKAP8ALAAAAABeACIAAAj+AAEIHEiQoIABBxIqXMiwocOHECM2LDBAQMGLGDFK3Mix
    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
    '''
    oexitActive = '''\
    R0lGODlhXgAiAOffAEpLSU1LT09LSlVKS05MT1BMSlRLUFlKUlRMUVpLUl5KU1tMU11LWFpNWVxN
    VF5MWV1OVV9NWmBOW0lMtVJKtl9QV2FPXGJPXWRPWFNLt2BRWFpKsmNQXmhPX1tLs2ZRWmlQYFxM
    tGVSYGpRYV1NtWZTYWtSYmRVXF5OtmdUYmRWXVdRtl9Pt2hVY1lRt21UZGlWZG5VZWpXZW9WZmhZ
    YWFTtGtYZnBXZ2laYWJUtWxZZ25WgnFYaGpbYnJWfmNVtm1aaHJZaXNYdGlVsmRWt3ZYb3hYanNa
    amxdZGpWs3lZa2tYonRba2tXtHpabG5fZnZdbW1ZtnxcbnNblHtddGtjaG9at3tbinFiaXRas3Jj
    anVbtH1fdn9fcXdcqHNka3ZctX5gd3pennRlbH9heHtfn3VmbXhet4BieXFoboBfm4Fjen5fs3do
    b39ftIJke3hpcIBgtYNlfHRrcX9jpHlqcYFhtoRmfXVscollfnprcoplf4hkm4tmgIZloYlnhYdj
    s4Fls4xngYhktIJmtI1ogoplqXlwdolltY5pg4pmtoxnq4VotpBqhHtyeIpppY1orJFrhYFxeYlp
    snxzeY5prZJshpRri5JrkYpqs49qrpNth5NrnphsiJRuiJNrqpltiZJumZVviZpuipZvlYF4fptv
    i5lum5NvpppvnJ1wjJRwp5hwo4N6gJtxk55xjZ5wmJlxpIR7gZxxn59yjp9xmZ1yoKBzj550lp5z
    oaF0kKFzm4d+hJ91l6J1kaJ0nIh/haF2mKN1naR3k6J3mYqBh6N4moyDiY2Eio6Fi4+GjJCHjZGI
    jpWMkpaNk5iPlZySmJ2TmZ6UmqWboaacoqKfo6OgpKqhp6yjqa2kqqmnq6qorK6ssK+tsbWytv//
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////yH+EUNyZWF0ZWQgd2l0aCBH
    SU1QACH5BAEKAP8ALAAAAABeACIAAAj+AAEIHEiQYIECAxIqXMiwocOHECM6PFiwokWLEjNq3MjR
    4cWPAyMaSJDAgMmTKFOqXMmyZUqSJQ08BFlRZIUnc9Jo2cmzp8+fQIMK9ZkGTxosPSDI9EgTAEQD
    C3pIgnbtmrWrWLNq3cq1q1et17Bdq/bsUI+STD8+XTCGGbVu3uLKnUu3rt27ePN64zZt2RilaWs+
    HFkF2bRs2rYpXsy4sePHkCNL3qYt27RjY06gZYgRYoIepZpFk0a6tOnTqFOrXs36dDRnxRzhSBBY
    4NMKeoAhU8a7t+/fwIMLH048eLJjvOZUWLqw4GCTGtqUakW9uvXr2LNr3859eylKZpb+B26Y0gGN
    MXDS19FTp7379/Djy59PXz779OnbfEGi2WTDkAydBBMDGJQAgwwy6ACEDgw26OCDEEYo4YQRLoig
    DC2k8IEEDMTEnEK2LSRgAgxEYAEHIKRgggkvtOjiizDGKOOMNNYIw4opgMDBBRF06CFnTilkEkkl
    XgCCCTHcwMMRRjChxJNQRinllFQKsYMPRVCpJZVMGHEEDzfEYAIIPProH4gIJTQkiRZ0YMINRzhB
    RRdhkIHGnWvkqeeefPap5xITBBpoBlf4qecUE4SwJxohTIACGWF0QYUTR9xgQgcWmMncQWqOlMAD
    FowQgxFShLGGHHns0YcgrBbi6qv+rorBAgpqwGprIYKgMGgNLAjqxa2vijGBB7DWMEEGf/SxRx5y
    rBGGFEbEMIIFD5B0ZpoCMhDqDU5wscYehTRiiSWeeCKKKKCkq+4mOQiKibrwqttEoH6o24kVgfIR
    r7p0JKpuEhNQcEm54zZSyB5rcOHEDdN2eJKII2k7wg1QkCFHIZZ0AooqHL/i8cceu+KCoJyAbPIr
    oQT6yMkAo3Cyx4Y46jG+FJDiMceqgNJJJIXIQQYUDGcaU0IFrBlBBzE4QUYeiWwyiiq03KILLr5U
    bXXV7QYKydVcV73FBC507UsqgZ4i9iJg+0IzLFbjossttKgyyiaJ5EGGEzF0EIH+tQYcNCQDF5hw
    BBdyJOIJ1LpU3UswjDfOOBiCAuL45I2PzAbljG8wASGYQwI2zbVM3kvVusTtSSJycHGECRc43DcA
    Qx59gxRrFLKJKrdUHQwxw/Q+TCpW5DBMJYJu4fvxyA9DwQSMJN+7sWw477mgtjhPTDBV36LKJoWs
    IcUNesck0EgKWCB4GHlEMgotvuw+DDHGxG9M1ogIWoP8+Ocf//KK6B9/u2zwH/EEFQJb6I931/MF
    LUYRiTyEYXUWUEBJxkeiC7zACWsQxOESRwz45W9eggrYL/znv5HFgYSNCoQAJ8CCXDSKAqnwXwd9
    oQtVeEIQa3DCC1o3QYGQiAP+MZDCGxIBile0bxj+C0QIJ7AKEvovCxP4gf9+EShWrJAFxghG1gyo
    v2Fg7xWgSMQbpBADDnSIIJ8CIhXk0Ij1HXGKIbSDE/23ikDFQn+QCwEJiYdFYxDjBwHbRRext8BG
    yIEKZayWQR6gRja6MRhI9B++WDhHEs4LhvgbRKA0sUdKxo8YvXKBB+XnRQWOwpCI5MADClAQBgBR
    iEQ0IiRJSIxPfGKUlcRfMHQ1gSGcYQskCJQbnMhH/P1ieVvIXynBKEYymtEiFsSgBlXBQVzm8pp+
    PMMSPZCJORYTf6gI1CfkN8Ma3jCHO7xIAc6XvkciEJvwjB8qJpGJGMaTlu+ZIyQDHbg6Vl6EALOr
    3e1y1z7eOe+gCE2oQhfauwT6Qnvc894NCECTAgSBcIZDnOIwx9GOevSjIA3G6GhoOtRxIQj+bIoI
    lta0p0VtamKLqUxnSlOaug1ucqOb3UTQlIIEIAYXy9jGOvayohr1qEg9Ks50xjM5xCAAPb1IA24Q
    hj6Mq1zn2pdWt8rVrnb1XARrRB/CcIMGNCUgADs=
    '''


* **Ejemplo:** *(es el de la foto)*.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # License: GPLv3
    #import this
    try:
        from Tkinter import *  # Python2
    except ImportError:
        from tkinter import *  # Python3
    ################################################################
    from okbutton import *  # This is the file, from the example ^_^
    ################################################################
    root = Tk()
    root.title('Boton')
    root.focus()
    root.resizable(0, 0)
    botoncito = OkButton(root, 1, onImage = oexitOn, offImage = oexitOff, activeImage = oexitActive, bd = 0, relief='flat', cursor='hand2', command = root.destroy)
    botoncito.pack()
    root.mainloop()


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

