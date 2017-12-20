#Boa:Dialog:About

#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

import wx

def create(parent):
    return About(parent)

[wxID_ABOUT, wxID_ABOUTTXTABOUT, 
] = [wx.NewId() for _init_ctrls in range(2)]

class About(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ABOUT, name='About', parent=prnt,
              pos=wx.Point(256, 167), size=wx.Size(683, 445),
              style=wx.DEFAULT_DIALOG_STYLE, title='About')
        self.SetClientSize(wx.Size(683, 445))

        self.txtAbout = wx.TextCtrl(id=wxID_ABOUTTXTABOUT, name='txtAbout',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(680, 440),
              style=wx.TE_MULTILINE, value='textCtrl1')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.txtAbout.LoadFile("about.txt")

        
