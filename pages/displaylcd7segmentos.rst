.. title: Display LCD de 7 Segmentos


Crear un Widget de Canvas tipo Display LCD Digital de 7 Segmentos.

Toma los sys.argv, tiene punto, tiene guion de negativo, tiene import con wilcard *(ups!)*.

Util para importarlo dentro de otro programa para representar otras cosas.

**Screenshot:**

.. image:: /images/DisplayLCD7Segmentos/temp.jpg

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    try:
        from Tkinter import *  # Python2
    except ImportError:
        from tkinter import *  # Python3
    import time
    import math
    import sys

    def ledLit(pos, val):
        if val < 0:
            if pos == 1:
                return 1
            else:
                return 0
        else:
            lookup = (125,80,55,87,90,79,111,81,127,95)
            return (1<<pos) & lookup[val]

    class ResolveSegColor:
        def __init__(self, bg, fg):
            self.__bg, self.__fg = bg, fg
        def get(self, seg, val):
            if ledLit(seg, val):
                return self.__fg
            else:
                return self.__bg

    class Digit(Frame):
        def __init__(self, master, w, h, init = None):
            Frame.__init__(self, master)
            self.__bg, self.__fg = '#000000', '#0800FF'
            self.__lastVal = 0
            self.__dpon = 0
            self.__startx = self.__starty = 3
            self.setSize(h, w)
            self.__c = Canvas(self, width = w, height = h, bg=self.__bg, highlightthickness=0)
            self.__c.pack(side=TOP, fill=BOTH, expand=YES)
            self.__lines = []
            self.__dplines = []
            self.__makeLines()
            self.__rseg = ResolveSegColor(self.__bg, self.__fg)
            if init != None:
                self.draw(init)

        def getCanvas(self):
            return self.__c

        def setSize(self, h, w):
            self.__x = w - 6
            self.__y = h/2 - 4
            self.__w = min(self.__x, self.__y)/6
            if self.__w < 3:
                self.__w = 3
            self.__x = self.__x - self.__w - 1

        def resizeEvent(self, event):
            self.setSize(event.height, event.width)
            self.__c.config(height = event.height, width = event.width)
            for i in self.__lines:
                self.__c.delete(i)
            del self.__lines[:]
            self.__lines = []
            self.__makeLines()
            self.draw(self.__lastVal)

        def dpon(self):
            self.__dpon = 1
            for i in self.__dplines:
                self.__c.itemconfigure(i, fill = self.__fg)

        def dpoff(self):
            self.__dpon = 0
            for i in self.__dplines:
                self.__c.itemconfigure(i, fill = self.__bg)

        def refresh(self):
            self.draw(self.__lastVal)

        def draw(self, val, dp = None):
            self.__lastVal = val
            if dp != None or self.__dpon:
                dpc = self.__fg
            else:
                dpc = self.__bg
            for i in range(self.__w):
                ii = i*8
                self.__c.itemconfigure(self.__lines[ii],
                                       fill = self.__rseg.get(0, val))
                if not i % 2:
                    self.__c.itemconfigure(self.__lines[ii + 1],
                                           fill = self.__rseg.get(1, val))
                else:
                    self.__c.itemconfigure(self.__lines[ii + 1],
                                           fill = self.__rseg.get(1, val))
                self.__c.itemconfigure(self.__lines[ii + 2],
                                       fill = self.__rseg.get(2, val))
                self.__c.itemconfigure(self.__lines[ii + 3],
                                       fill = self.__rseg.get(3, val))
                self.__c.itemconfigure(self.__lines[ii + 4],
                                       fill = self.__rseg.get(4, val))
                self.__c.itemconfigure(self.__lines[ii + 5],
                                       fill = self.__rseg.get(5, val))
                self.__c.itemconfigure(self.__lines[ii + 6],
                                       fill = self.__rseg.get(6, val))
                self.__c.itemconfigure(self.__lines[ii + 7], fill = dpc)

        def clear(self):
            for i in self.__lines:
                self.__c.itemconfigure(i, fill = self.__bg)

        def __makeLines(self):
            start_x, start_y = self.__startx, self.__starty
            x, y = self.__x, self.__y
            for i in range(self.__w):
                self.__lines.append(self.__c.create_line(start_x+1+i, start_y+i,
                                                         start_x+x-2-i, start_y+i,
                                                         fill = self.__bg))
                if not i % 2:
                    self.__lines.append(self.__c.create_line(start_x+2+(i/2),
                                                             start_y+y-(i/2)+1,
                                                             start_x+x-3-(i/2),
                                                             start_y+y-(i/2)+1,
                                                             fill = self.__bg))
                else:
                    self.__lines.append(self.__c.create_line(start_x+2+(i/2)+1,
                                                             start_y+y+(i/2)+2,
                                                             start_x+x-3-((i/2)+1),
                                                             start_y+y+(i/2)+2,
                                                             fill = self.__bg))
                self.__lines.append(self.__c.create_line(start_x+1+i,
                                                         start_y+2*y-i+2,
                                                         start_x+x-2-i,
                                                         start_y+2*y-i+2,
                                                         fill = self.__bg))
                self.__lines.append(self.__c.create_line(start_x+i, start_y+2+i,
                                                         start_x+i, start_y+y-i,
                                                         fill = self.__bg))
                self.__lines.append(self.__c.create_line(start_x+x-i-1,
                                                         start_y+2+i,
                                                         start_x+x-i-1,
                                                         start_y+y-i,
                                                         fill = self.__bg))
                self.__lines.append(self.__c.create_line(start_x+i, start_y+2+i+y,
                                                         start_x+i, start_y+2*y-i,
                                                         fill = self.__bg))
                self.__lines.append(self.__c.create_line(start_x+x-i-1,
                                                         start_y+2+i+y,
                                                         start_x+x-1-i,
                                                         start_y+2*y-i,
                                                         fill = self.__bg))

                l = self.__c.create_line(start_x + x + 4,
                                         start_y +2*y - i,
                                         start_x + x + 4 + self.__w,
                                         start_y +2*y - i,
                                         fill = self.__bg)
                self.__lines.append(l)
                self.__dplines.append(l)

    class Display(Frame):
        def __init__(self, master, w, h, ndigits, orient = LEFT):
            Frame.__init__(self, master)
            self.__ndigits, self.__orient= ndigits, orient
            self.setSize(h, w)
            self.digits = []
            for i in range(ndigits):
                d = Digit(self, self.__w, self.__h)
                d.pack(side = orient, fill=BOTH, expand=YES)
                self.digits.append(d)

        def int(self, val):
            if val < 0:
                negv = 1
                maxval = math.pow(10, self.__ndigits -1) -1
            else:
                negv = 0
                maxval = math.pow(10, self.__ndigits) - 1
            val = abs(val)
            if val > maxval:
                raise 'Error del rango'
            map(Digit.dpoff, self.digits)
            for i in range(1, self.__ndigits + 1):
                d = val%10
                self.digits[-i].draw(d)
                val = val/10
            if negv:
                self.digits[0].draw(-1)

        def str(self, s):
            if '.' in s:
                l = len(s) - 1
            else:
                l = len(s)
            if l > self.__ndigits:
                raise 'Error del rango'
            map(Digit.dpoff, self.digits)
            p = 0
            for i in s:
                if i == '-':
                    self.digits[p].draw(-1)
                    p = p + 1
                elif i == '.':
                    self.digits[p-1].dpon()
                else:
                    if i == ' ':
                        self.digits[p].clear()
                    else:
                        self.digits[p].draw(ord(i) - 0x30)
                    p = p + 1

        def float(self, val, format):
            self.str(format % (val))

        def clear(self):
            map(Digit.clear, self.digits)

        def setSize(self, h, w):
            if self.__orient == LEFT or self.__orient == RIGHT:
                self.__w = w/self.__ndigits
                self.__h = h
            elif self.__orient == TOP or self.__orient == BOTTOM:
                self.__h = h/self.__ndigits
                self.__w = w

        def resizeEvent(self, event):
            self.setSize(event.height, event.width)
            for d in self.digits:
                event.height, event.width = self.__h, self.__w
                d.resizeEvent(event)
            self.refresh()

        def refresh(self):
            map(Digit.refresh, self.digits)

    def updater(d, v):
        d.int(v)
        d.after(100, updater, d, v + 1)

    if __name__ == '__main__':
        root = Tk()
        root.title('Tienes 60 Segundos para salvar al Mundo')
        root.config(cursor='watch')
        root.focus()
        print (' ... G O !!!')
        ndigits = 3
        orient = LEFT
        if len(sys.argv) > 1:
            ndigits = int(sys.argv[1])
        if len(sys.argv) > 2:
            orient = TOP
        d = Display(root, 400, 100, ndigits, orient)
        d.bind('<Configure>', d.resizeEvent)
        d.bind('<Expose>', d.refresh())
        d.pack(fill=BOTH, expand=YES)
        updater(d, 0)
        root.mainloop()

