#Boa:Dialog:Tauc

#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

import wx

def create(parent):
    return Tauc(parent)

[wxID_TAUC, wxID_TAUCSASHWINDOW1, wxID_TAUCSTATICBOX1, wxID_TAUCSTATICBOX2, 
 wxID_TAUCSTATICTEXT1, wxID_TAUCSTATICTEXT2, wxID_TAUCTXTGAP, 
 wxID_TAUCTXTSLOPE, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Tauc(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_TAUC, name='Tauc', parent=prnt,
              pos=wx.Point(232, 134), size=wx.Size(752, 445),
              style=wx.DEFAULT_DIALOG_STYLE, title="Tauc's Plot")
        self.SetClientSize(wx.Size(752, 445))

        self.sashWindow1 = wx.SashWindow(id=wxID_TAUCSASHWINDOW1,
              name='sashWindow1', parent=self, pos=wx.Point(168, 16),
              size=wx.Size(552, 384), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashWindow1.Bind(wx.EVT_PAINT, self.OnSashWindow1Paint)
        self.sashWindow1.Bind(wx.EVT_LEFT_DOWN, self.OnSashWindow1LeftDown)

        self.txtGap = wx.TextCtrl(id=wxID_TAUCTXTGAP, name='txtGap',
              parent=self, pos=wx.Point(40, 272), size=wx.Size(80, 26), style=0,
              value='textCtrl1')

        self.staticBox1 = wx.StaticBox(id=wxID_TAUCSTATICBOX1,
              label='Energy Gap (eV)', name='staticBox1', parent=self,
              pos=wx.Point(16, 248), size=wx.Size(136, 56), style=0)

        self.staticText1 = wx.StaticText(id=wxID_TAUCSTATICTEXT1, label='eV',
              name='staticText1', parent=self, pos=wx.Point(420, 410),
              size=wx.Size(20, 20), style=0)

        self.staticText2 = wx.StaticText(id=wxID_TAUCSTATICTEXT2,
              label='sqrt(alpha*E)', name='staticText2', parent=self,
              pos=wx.Point(55, 176), size=wx.Size(95, 20), style=0)

        self.txtSlope = wx.TextCtrl(id=wxID_TAUCTXTSLOPE, name='txtSlope',
              parent=self, pos=wx.Point(40, 360), size=wx.Size(80, 26), style=0,
              value='textCtrl1')

        self.staticBox2 = wx.StaticBox(id=wxID_TAUCSTATICBOX2,
              label='B (sqrt [cm*eV])', name='staticBox2', parent=self,
              pos=wx.Point(16, 336), size=wx.Size(136, 56), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # define the scale of the plot
        self.sashWindow1.xmin, self.sashWindow1.xmax, self.sashWindow1.ymin, \
        self.sashWindow1.ymax = 1.0, 5.0, 0.0, 1200.0
        
        # Get the size of the drawing area in pixels.
        self.sashWindow1.wi, self.sashWindow1.he = self.sashWindow1.GetSizeTuple()

        # Create BufferBmp and set the same size as the drawing area.
        self.sashWindow1.BufferBmp = wx.EmptyBitmap(self.sashWindow1.wi, self.sashWindow1.he)

        # borders of the plot %
        self.xborder =10
        self.yborder = 10
        
        self.Emin=1
        self.Emax=5

        self.lam,self.a=parent.Dialog[0],parent.Dialog[1]
        
        self.PlotData()
        self.UpdatePlot()


    def OnSashWindow1Paint(self, event):
        dc = wx.PaintDC(self.sashWindow1)
        dc.BeginDrawing()
        if self.sashWindow1.BufferBmp != None:
            dc.DrawBitmap(self.sashWindow1.BufferBmp, 0, 0, True)
        else:
            pass
        dc.EndDrawing()
        
    def XX(self,x):
        #convert x to be plotted basing on the scale of the plot
        a=self.sashWindow1.wi*(x-self.sashWindow1.xmin)/(self.sashWindow1.xmax-self.sashWindow1.xmin)
        a=a*(100-2*self.xborder)/100.0
        a=a+self.xborder*self.sashWindow1.wi/100.0
        return int(round(a))
        
    def YY(self,y):
        #convert y to be plotted basing on the scale of the plot
        a=self.sashWindow1.he-self.sashWindow1.he*(y-self.sashWindow1.ymin)/(self.sashWindow1.ymax-self.sashWindow1.ymin)
        a=a*(100-2*self.yborder)/100.0
        a=a+self.yborder*self.sashWindow1.he/100.0
        return int(round(a))

    def UpdatePlot(self):        
        dc = wx.ClientDC(self.sashWindow1)
        dc.BeginDrawing()
        dc.DrawBitmap(self.sashWindow1.BufferBmp, 0, 0, True)
        dc.EndDrawing()

    def PlotData(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self.sashWindow1.BufferBmp)
        dc.Clear()
        dc.BeginDrawing()

        dc.SetPen(wx.Pen(wx.BLACK, 1, wx.SOLID))
        
        xmin,xmax=self.sashWindow1.xmin,self.sashWindow1.xmax
        ymin,ymax=self.sashWindow1.ymin,self.sashWindow1.ymax
        
            
        for x in [1,2,3,4,5]:
            dc.DrawLine(self.XX(x),self.YY(0),self.XX(x),self.YY(1200))
            dc.DrawText(str(x), self.XX(x),self.YY(0))
        
        offset=(xmax-xmin)/(100.0-2*self.xborder)*self.xborder
        
        for y in range(0, 1201, 200):
            dc.DrawLine(self.XX(xmin),self.YY(y),self.XX(xmax),self.YY(y))
            dc.DrawText(str(y), self.XX(xmin-offset),self.YY(y))

        dc.SetPen(wx.Pen(wx.RED, 1, wx.SOLID))

        if self.Emin<12400.0/max(self.lam):
            self.Emin=12400.0/max(self.lam)
        if self.Emax>12400.0/min(self.lam):
            self.Emax=12400.0/min(self.lam)

        dc.DrawLine(self.XX(self.Emin),self.YY(0),self.XX(self.Emin),self.YY(1200))
        dc.DrawLine(self.XX(self.Emax),self.YY(0),self.XX(self.Emax),self.YY(1200))
        

        S1,S2,S3,S4 = 0,0,0,0
        num=0
        for i in range (len(self.lam)):
            if self.Emin<=12400.0/self.lam[i]<=self.Emax:
                E=12400.0/self.lam[i]
                Y=(E*self.a[i])**(0.5)
                S1=S1+(E*Y)
                S2=S2+E
                S3=S3+Y
                S4=S4+(E*E)
                num=num+1

        A=(num*S1-(S2*S3))/(num*S4-(S2*S2))
        B=(S3*S4-(S2*S1))/(num*S4-(S2*S2))
        self.A=A
        self.B=B

        dc.DrawLine(self.XX(-B/A),self.YY(0),self.XX((1000-B)/A),self.YY(1000))

        self.txtGap.SetValue("%0.2f" %(-B/A))
        self.txtSlope.SetValue("%0.2f" %(A))
        
        dc.SetPen(wx.Pen(wx.BLACK, 3, wx.SOLID))
        for i in range(len(self.lam)):
            E=12400.0/self.lam[i]
            Y=(self.a[i]*E)**(0.5)
            dc.DrawCircle(self.XX(E),self.YY(Y),1)
        #dc.DrawLine(self.XX(2),self.YY(100),self.XX(4),self.YY(1000))

        dc.EndDrawing()

    def OnSashWindow1LeftDown(self, event):
        self.x, self.y = event.GetPositionTuple()
        a=self.x
        a=a-self.xborder*self.sashWindow1.wi/100.0
        a=a/(100-2*self.xborder)*100.0
        x=self.sashWindow1.xmin+a*(self.sashWindow1.xmax-self.sashWindow1.xmin)/self.sashWindow1.wi
        if x<=self.Emin:
            self.Emin=x
        elif x>=self.Emax:
            self.Emax=x
        else:
            if self.Emax-x<=x-self.Emin:
                self.Emax=x
            else:
                self.Emin=x

        self.PlotData()
        self.UpdatePlot()





