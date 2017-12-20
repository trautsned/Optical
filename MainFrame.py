#Boa:Frame:MainFrame

#Optical, Copyright (C) 2005  Emanuele Centurioni
#see Optical.py

import wx

from math import *
from ScatteringMatrix import *
from os import *
import os.path
from functions import *
##from pickle import *
import About
import EdtStructure
import InternalFlux
import ThicknDet
#nota: la finestra con i valori di CHI va a capo (non si legge)
import Tauc

def create(parent):
    return MainFrame(parent)

[wxID_MAINFRAME, wxID_MAINFRAMEBTNALPHA, wxID_MAINFRAMEBTNBLACK, 
 wxID_MAINFRAMEBTNCHI, wxID_MAINFRAMEBTNCLEAR, wxID_MAINFRAMEBTNCOMPUTE, 
 wxID_MAINFRAMEBTNEDITSTR, wxID_MAINFRAMEBTNEFLUX, 
 wxID_MAINFRAMEBTNEFLUXPROFILE, wxID_MAINFRAMEBTNPSIDELTA, 
 wxID_MAINFRAMEBTNQE, wxID_MAINFRAMEBTNTHICKNESS, wxID_MAINFRAMECHKA, 
 wxID_MAINFRAMECHKR, wxID_MAINFRAMECHKT, wxID_MAINFRAMESTATICTEXT1, 
 wxID_MAINFRAMESTATICTEXT2, wxID_MAINFRAMESTATICTEXT3, wxID_MAINFRAMESTXTCM1, 
 wxID_MAINFRAMESTXTEV, wxID_MAINFRAMETXTCM1, wxID_MAINFRAMETXTEV, 
 wxID_MAINFRAMETXTFI, wxID_MAINFRAMETXTRTA, wxID_MAINFRAMETXTWAVELENGTH, 
 wxID_MAINFRAMEWINDOW1, 
] = [wx.NewId() for _init_ctrls in range(26)]

[wxID_MAINFRAMEMNUFILECLOSEEXP, wxID_MAINFRAMEMNUFILECLOSESTRUCTURE, 
 wxID_MAINFRAMEMNUFILEEXIT, wxID_MAINFRAMEMNUFILELOADEXP, 
 wxID_MAINFRAMEMNUFILENEWSTRUCT, wxID_MAINFRAMEMNUFILEOPENSTRUCT, 
 wxID_MAINFRAMEMNUFILESAVESTRUCT, wxID_MAINFRAMEMNUFILESAVESTRUCTAS, 
] = [wx.NewId() for _init_coll_mnuFile_Items in range(8)]

[wxID_MAINFRAMEMNUHELPABOUT, wxID_MAINFRAMEMNUHELPHELP, 
] = [wx.NewId() for _init_coll_mnuHelp_Items in range(2)]

[wxID_MAINFRAMEMNUSETTINGSSETGRAPHSCALE] = [wx.NewId() for _init_coll_mnuSettings_Items in range(1)]

[wxID_MAINFRAMEMNUINDEXPLOTINDEX] = [wx.NewId() for _init_coll_mnuIndex_Items in range(1)]

class MainFrame(wx.Frame):
    def _init_coll_mnuIndex_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MAINFRAMEMNUINDEXPLOTINDEX,
              kind=wx.ITEM_NORMAL, text=u'Plot Index')
        self.Bind(wx.EVT_MENU, self.OnMnuIndexPlotindexMenu,
              id=wxID_MAINFRAMEMNUINDEXPLOTINDEX)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.mnuFile, title=u'File')
        parent.Append(menu=self.mnuIndex, title=u'Index')
        parent.Append(menu=self.mnuSettings, title=u'Settings')
        parent.Append(menu=self.mnuHelp, title=u'Help')

    def _init_coll_mnuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MAINFRAMEMNUFILENEWSTRUCT,
              kind=wx.ITEM_NORMAL, text=u'New Multilayer')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILEOPENSTRUCT,
              kind=wx.ITEM_NORMAL, text=u'Open Multilayer')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILESAVESTRUCT,
              kind=wx.ITEM_NORMAL, text=u'Save Multilayer')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILESAVESTRUCTAS,
              kind=wx.ITEM_NORMAL, text=u'Save Multilayer As ...')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILECLOSESTRUCTURE,
              kind=wx.ITEM_NORMAL, text=u'Close Multilayer')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILELOADEXP,
              kind=wx.ITEM_NORMAL, text=u'Load Experimental Data')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILECLOSEEXP,
              kind=wx.ITEM_NORMAL, text=u'Close Experimental Data')
        parent.Append(help='', id=wxID_MAINFRAMEMNUFILEEXIT,
              kind=wx.ITEM_NORMAL, text=u'Exit')
        self.Bind(wx.EVT_MENU, self.OnMnuFileNewstructMenu,
              id=wxID_MAINFRAMEMNUFILENEWSTRUCT)
        self.Bind(wx.EVT_MENU, self.OnMnuFileOpenstructMenu,
              id=wxID_MAINFRAMEMNUFILEOPENSTRUCT)
        self.Bind(wx.EVT_MENU, self.OnMnuFileSavestructMenu,
              id=wxID_MAINFRAMEMNUFILESAVESTRUCT)
        self.Bind(wx.EVT_MENU, self.OnMnuFileSavestructasMenu,
              id=wxID_MAINFRAMEMNUFILESAVESTRUCTAS)
        self.Bind(wx.EVT_MENU, self.OnMnuFileClosestructureMenu,
              id=wxID_MAINFRAMEMNUFILECLOSESTRUCTURE)
        self.Bind(wx.EVT_MENU, self.OnMnuFileLoadexpMenu,
              id=wxID_MAINFRAMEMNUFILELOADEXP)
        self.Bind(wx.EVT_MENU, self.OnMnuFileCloseexpMenu,
              id=wxID_MAINFRAMEMNUFILECLOSEEXP)
        self.Bind(wx.EVT_MENU, self.OnMnuFileExitMenu,
              id=wxID_MAINFRAMEMNUFILEEXIT)

    def _init_coll_mnuSettings_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MAINFRAMEMNUSETTINGSSETGRAPHSCALE,
              kind=wx.ITEM_NORMAL, text=u'Set Graph Scale')
        self.Bind(wx.EVT_MENU, self.OnMnuSettingsSetgraphscaleMenu,
              id=wxID_MAINFRAMEMNUSETTINGSSETGRAPHSCALE)

    def _init_coll_mnuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MAINFRAMEMNUHELPHELP,
              kind=wx.ITEM_NORMAL, text=u'Help')
        parent.Append(help='', id=wxID_MAINFRAMEMNUHELPABOUT,
              kind=wx.ITEM_NORMAL, text=u'About')
        self.Bind(wx.EVT_MENU, self.OnMnuHelpHelpMenu,
              id=wxID_MAINFRAMEMNUHELPHELP)
        self.Bind(wx.EVT_MENU, self.OnMnuHelpAboutMenu,
              id=wxID_MAINFRAMEMNUHELPABOUT)

    def _init_utils(self):
        # generated method, don't edit
        self.mnuFile = wx.Menu(title=u'')

        self.mnuIndex = wx.Menu(title='')

        self.mnuSettings = wx.Menu(title='')

        self.mnuHelp = wx.Menu(title='')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_mnuFile_Items(self.mnuFile)
        self._init_coll_mnuIndex_Items(self.mnuIndex)
        self._init_coll_mnuSettings_Items(self.mnuSettings)
        self._init_coll_mnuHelp_Items(self.mnuHelp)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'MainFrame',
              parent=prnt, pos=wx.Point(216, 66), size=wx.Size(800, 600),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Optical')
        self._init_utils()
        self.SetClientSize(wx.Size(800, 600))
        self.SetMenuBar(self.menuBar1)
        self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.SetBackgroundColour(wx.Colour(220, 218, 213))
        self.Bind(wx.EVT_CLOSE, self.OnMainFrameClose)

        self.btnEditStr = wx.Button(id=wxID_MAINFRAMEBTNEDITSTR,
              label=u'Edit M', name=u'btnEditStr', parent=self, pos=wx.Point(16,
              192), size=wx.Size(85, 32), style=0)
        self.btnEditStr.Bind(wx.EVT_BUTTON, self.OnBtnEditStrButton,
              id=wxID_MAINFRAMEBTNEDITSTR)

        self.btnAlpha = wx.Button(id=wxID_MAINFRAMEBTNALPHA, label=u'Alpha',
              name=u'btnAlpha', parent=self, pos=wx.Point(16, 288),
              size=wx.Size(85, 32), style=0)
        self.btnAlpha.Bind(wx.EVT_BUTTON, self.OnBtnAlphaButton,
              id=wxID_MAINFRAMEBTNALPHA)

        self.btnEFluxProfile = wx.Button(id=wxID_MAINFRAMEBTNEFLUXPROFILE,
              label=u'Flux Prof', name=u'btnEFluxProfile', parent=self,
              pos=wx.Point(16, 384), size=wx.Size(85, 32), style=0)
        self.btnEFluxProfile.Bind(wx.EVT_BUTTON, self.OnBtnEFluxProfileButton,
              id=wxID_MAINFRAMEBTNEFLUXPROFILE)

        self.btnPsiDelta = wx.Button(id=wxID_MAINFRAMEBTNPSIDELTA,
              label=u'PsiDelta', name=u'btnPsiDelta', parent=self,
              pos=wx.Point(16, 488), size=wx.Size(85, 32), style=0)
        self.btnPsiDelta.Bind(wx.EVT_BUTTON, self.OnBtnPsiDeltaButton,
              id=wxID_MAINFRAMEBTNPSIDELTA)

        self.btnQE = wx.Button(id=wxID_MAINFRAMEBTNQE, label=u'QE',
              name=u'btnQE', parent=self, pos=wx.Point(16, 528),
              size=wx.Size(85, 32), style=0)
        self.btnQE.Bind(wx.EVT_BUTTON, self.OnBtnQEButton,
              id=wxID_MAINFRAMEBTNQE)

        self.btnThickness = wx.Button(id=wxID_MAINFRAMEBTNTHICKNESS,
              label=u'Thick det', name=u'btnThickness', parent=self,
              pos=wx.Point(136, 288), size=wx.Size(85, 32), style=0)
        self.btnThickness.Bind(wx.EVT_BUTTON, self.OnBtnThicknessButton,
              id=wxID_MAINFRAMEBTNTHICKNESS)

        self.btnChi = wx.Button(id=wxID_MAINFRAMEBTNCHI, label=u'Chi test',
              name=u'btnChi', parent=self, pos=wx.Point(136, 328),
              size=wx.Size(85, 32), style=0)
        self.btnChi.Bind(wx.EVT_BUTTON, self.OnBtnChiButton,
              id=wxID_MAINFRAMEBTNCHI)

        self.btnEFlux = wx.Button(id=wxID_MAINFRAMEBTNEFLUX, label=u'E Flux',
              name=u'btnEFlux', parent=self, pos=wx.Point(136, 384),
              size=wx.Size(85, 32), style=0)
        self.btnEFlux.Bind(wx.EVT_BUTTON, self.OnBtnEFluxButton,
              id=wxID_MAINFRAMEBTNEFLUX)

        self.btnCompute = wx.Button(id=wxID_MAINFRAMEBTNCOMPUTE,
              label=u'Compute', name=u'btnCompute', parent=self,
              pos=wx.Point(136, 448), size=wx.Size(85, 32), style=0)
        self.btnCompute.Bind(wx.EVT_BUTTON, self.OnBtnComputeButton,
              id=wxID_MAINFRAMEBTNCOMPUTE)

        self.btnClear = wx.Button(id=wxID_MAINFRAMEBTNCLEAR, label=u'Clear',
              name=u'btnClear', parent=self, pos=wx.Point(136, 488),
              size=wx.Size(85, 32), style=0)
        self.btnClear.Bind(wx.EVT_BUTTON, self.OnBtnClearButton,
              id=wxID_MAINFRAMEBTNCLEAR)

        self.window1 = wx.Window(id=wxID_MAINFRAMEWINDOW1, name='window1',
              parent=self, pos=wx.Point(232, 0), size=wx.Size(552, 480),
              style=0)
        self.window1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.window1.SetHelpText(u'prova')
        self.window1.Enable(True)
        self.window1.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.window1.Bind(wx.EVT_PAINT, self.OnWindow1Paint)
        self.window1.Bind(wx.EVT_LEFT_DOWN, self.OnWindow1LeftDown)

        self.chkA = wx.CheckBox(id=wxID_MAINFRAMECHKA, label=u'Show A',
              name=u'chkA', parent=self, pos=wx.Point(136, 8), size=wx.Size(91,
              21), style=0)
        self.chkA.SetValue(False)

        self.chkT = wx.CheckBox(id=wxID_MAINFRAMECHKT, label=u'Show T',
              name=u'chkT', parent=self, pos=wx.Point(136, 40), size=wx.Size(91,
              21), style=0)
        self.chkT.SetValue(True)

        self.chkR = wx.CheckBox(id=wxID_MAINFRAMECHKR, label=u'Show R',
              name=u'chkR', parent=self, pos=wx.Point(136, 80), size=wx.Size(91,
              21), style=0)
        self.chkR.SetValue(True)

        self.txtRTA = wx.TextCtrl(id=wxID_MAINFRAMETXTRTA, name=u'txtRTA',
              parent=self, pos=wx.Point(144, 232), size=wx.Size(80, 27),
              style=0, value=u'')

        self.txtWavelength = wx.TextCtrl(id=wxID_MAINFRAMETXTWAVELENGTH,
              name=u'txtWavelength', parent=self, pos=wx.Point(448, 512),
              size=wx.Size(80, 27), style=0, value=u'')

        self.txtFi = wx.TextCtrl(id=wxID_MAINFRAMETXTFI, name=u'txtFi',
              parent=self, pos=wx.Point(712, 512), size=wx.Size(80, 27),
              style=0, value=u'')

        self.staticText1 = wx.StaticText(id=wxID_MAINFRAMESTATICTEXT1,
              label=u'Wavelength (A)', name='staticText1', parent=self,
              pos=wx.Point(440, 488), size=wx.Size(113, 17), style=0)

        self.staticText2 = wx.StaticText(id=wxID_MAINFRAMESTATICTEXT2,
              label=u'(%)', name='staticText2', parent=self, pos=wx.Point(170,
              210), size=wx.Size(22, 17), style=0)

        self.staticText3 = wx.StaticText(id=wxID_MAINFRAMESTATICTEXT3,
              label=u'Angle (deg)', name='staticText3', parent=self,
              pos=wx.Point(715, 490), size=wx.Size(74, 17), style=0)

        self.btnBlack = wx.Button(id=wxID_MAINFRAMEBTNBLACK, label=u'Black',
              name=u'btnBlack', parent=self, pos=wx.Point(136, 528),
              size=wx.Size(85, 30), style=0)
        self.btnBlack.Bind(wx.EVT_BUTTON, self.OnBtnBlackButton,
              id=wxID_MAINFRAMEBTNBLACK)

        self.txteV = wx.TextCtrl(id=wxID_MAINFRAMETXTEV, name=u'txteV',
              parent=self, pos=wx.Point(328, 512), size=wx.Size(80, 25),
              style=0, value=u'')

        self.txtcm1 = wx.TextCtrl(id=wxID_MAINFRAMETXTCM1, name=u'txtcm1',
              parent=self, pos=wx.Point(560, 512), size=wx.Size(80, 25),
              style=0, value=u'')

        self.stxteV = wx.StaticText(id=wxID_MAINFRAMESTXTEV, label=u'eV',
              name=u'stxteV', parent=self, pos=wx.Point(360, 488),
              size=wx.Size(17, 17), style=0)

        self.stxtcm1 = wx.StaticText(id=wxID_MAINFRAMESTXTCM1, label=u'cm-1',
              name=u'stxtcm1', parent=self, pos=wx.Point(585, 488),
              size=wx.Size(33, 17), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

        #load settings from file settings.txt
        settings=LoadConf()

        #version of the software
        #self.Version=settings[settings.index("version")+1]
        self.Version="0.1.8"
        
        #set relative path to directory containig structures
        StructureDir=settings[settings.index("StructureDir")+1]
        #StructureDir=replace(StructureDir,"\\","/")#for win compatibility
        StructureDir=StructureDir.replace("\\","/")
        self.StructureDir=os.path.normpath(StructureDir)
        
        #set relative path to directory containig refraction indexes
        IndexDir=settings[settings.index("IndexDir")+1]        
        #IndexDir=replace(IndexDir,"\\","/")#for win compatibility
        IndexDir=IndexDir.replace("\\","/")
        self.IndexDir=os.path.normpath(IndexDir)

        #set absolute path to directory containig experimental data
        ExpDir=settings[settings.index("ExpDir")+1]        
        #ExpDir=replace(ExpDir,"\\","/")#for win compatibility
        ExpDir=ExpDir.replace("\\","/")
        self.ExpDir=os.path.normpath(ExpDir)

        #the current working directory
        self.CurDir=getcwd()
        
        #set accuracy of experimental data
        StDev=float(settings[settings.index("StDev")+1])
        self.StDev=StDev/100.0
        
        #Set number of points used in the plot
        PlotPoints=int(settings[settings.index("PlotPoints")+1])        
        self.PlotPoints=PlotPoints
        
        # Get the size of the drawing area in pixels.
        self.window1.wi, self.window1.he = self.window1.GetSizeTuple()

        # Create BufferBmp and set the same size as the drawing area.
        self.window1.BufferBmp = wx.EmptyBitmap(self.window1.wi, self.window1.he)

        # borders of the plot %
        xborder=float(settings[settings.index("xborder")+1])
        yborder=float(settings[settings.index("yborder")+1])        
        self.xborder = xborder
        self.yborder = yborder

        # define the scale of the plot
        xmin=int(settings[settings.index("xmin")+1])
        xmax=int(settings[settings.index("xmax")+1])
        self.window1.xmin, self.window1.xmax, self.window1.ymin, \
        self.window1.ymax = xmin, xmax, 0.0, 1.0
        
        #set default incidence angle
        Fi=settings[settings.index("Fi")+1]
        self.txtFi.SetValue(Fi)
        
        #set lower valid T value for absorption calculation
        lowT=float(settings[settings.index("lowT")+1])
        self.lowT=lowT/100.0

        # available wavelength range from index files
        self.IndexRange=[1, 100000000]
        
        #generic list used for data transfer between modules
        self.Dialog=[]
        
        #Experiment File name
        self.ExperimentFilename=""

        #experimental data
        self.Experiment=[]

        #list of colors to be used in plotting
        self.color=[wx.RED,wx.BLUE,wx.GREEN]
        self.ncolor=-1
        
        #used to handle cancel actions
        self.Cancel=False
        
        #Chi_test history
        self.ChiHist=[""]*10
        
        #other variables are defined in ClearStructure
        self.ClearStructure()

        #plot axis and thick
        self.PlotAxis()
        #self.UpdatePlot()
        
        #new functions under test (disabled)
        test=settings[settings.index("test")+1]=="True"
        self.btnQE.Show(test)
        self.btnBlack.Show(test)
        #self.txteV.Show(test)
        #self.txtcm1.Show(test)
        #self.stxteV.Show(test)
        #self.stxtcm1.Show(test)

    def ClearStructure(self):
        
        #Structure File name        
        self.StructureFilename=""
        
        self.StructureName="Untitled"

        #multilayer structure
        self.Structure=[]

        #store edit structure situation
        self.StoreEdtStr=[0]

        #store EFlux structure situation        
        self.StoreEFlux=[0,"0"]

        #store Thickness determination situation        
        self.StoreThickDet=[0,0,5,"R",1.0]

        #used to check if structure is saved
        self.StructureSaved=True

        #check and enable/disable buttons
        self.UpdateButtons()

    def XX(self,x):
        #convert x to be plotted basing on the scale of the plot
        a=self.window1.wi*(x-self.window1.xmin)/(self.window1.xmax-self.window1.xmin)
        a=a*(100-2*self.xborder)/100.0
        a=a+self.xborder*self.window1.wi/100.0
        return int(round(a))
        
    def YY(self,y):
        #convert y to be plotted basing on the scale of the plot
        a=self.window1.he-self.window1.he*(y-self.window1.ymin)/(self.window1.ymax-self.window1.ymin)
        a=a*(100-2*self.yborder)/100.0
        a=a+self.yborder*self.window1.he/100.0
        return int(round(a))

    def UpdatePlot(self):        
        dc = wx.ClientDC(self.window1)
        dc.BeginDrawing()
        dc.DrawBitmap(self.window1.BufferBmp, 0, 0, True)
        dc.EndDrawing()
        
    def PlotAxis(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self.window1.BufferBmp)
        dc.Clear()
        dc.BeginDrawing()
        dc.SetPen(wx.Pen(wx.BLACK, 1, wx.SOLID))
        
        xmin,xmax=self.window1.xmin,self.window1.xmax
        ymin,ymax=self.window1.ymin,self.window1.ymax
        
        dix = (xmax-xmin)/4.0
        i = 0
        while dix > 10:
            i = i + 1
            dix = dix / 10.0
        
        dix = int(dix)
        dix = dix * 10**i
            
        for x in range(xmin,xmax+1,dix):
            dc.DrawLine(self.XX(x),self.YY(0),self.XX(x),self.YY(1))
            dc.DrawText(str(x), self.XX(x),self.YY(0))
        
        offset=int(round((xmax-xmin)/(100.0-2*self.xborder)*self.xborder))
        
        for y in range(0, 101, 20):
            dc.DrawLine(self.XX(xmin),self.YY(y/100.0),self.XX(xmax),self.YY(y/100.0))
            dc.DrawText(str(y), self.XX(xmin-offset),self.YY(y/100.0))
        dc.EndDrawing()

    def CheckIfSaved(self):
        if self.StructureSaved==False:
            dlg = wx.SingleChoiceDialog(self, 
            "The current Multilayer has been modified.\nDo you want to save your changes ?", 
            'Question', ["Yes","No"])
            try:
                if dlg.ShowModal() == wx.ID_OK:
                    selected = dlg.GetStringSelection()
                    if selected == "Yes":
                        self.OnMnuFileSavestructMenu(None)
                    else:
                        self.Cancel=False
                else:
                    self.Cancel=True
            finally:
                dlg.Destroy()
        else:
            self.Cancel=False

    def PlotExperiment(self):
            lam,R,T=[],[],[]
            for i in range(len(self.Experiment)):
                lam.append(self.Experiment[i][0])
                R.append(self.Experiment[i][1])
                T.append(self.Experiment[i][2])

            color=wx.BLACK
            self.PlotData(lam,R,T,color,color,color)

    def ShowChi(self):
        text=""
        for i in range(len(self.ChiHist)):
            text=text+str(self.ChiHist[i])+"\n"
        caption="Chi Square Test       Assuming experimental accuracy = +- "+str(self.StDev*100)+"% of full scale"
        
        dlg = wx.MessageDialog(self, text,
        caption, wx.OK | wx.ICON_INFORMATION)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def UpdateButtons(self):
        self.SetTitle("Optical "+self.Version+"   Multilayer =.."+self.StructureFilename[-25:]+"    Experiment =.."+self.ExperimentFilename[-25:])
        if len(self.Structure)>1:
            self.btnEditStr.Enable(True)
            self.btnCompute.Enable(True)
            self.btnPsiDelta.Enable(True)
        else:
            self.btnEditStr.Enable(False)
            self.btnCompute.Enable(False)
            self.btnPsiDelta.Enable(False)
                    
        if len(self.Structure)>2:
            self.btnEFlux.Enable(True)
            self.btnEFluxProfile.Enable(True)
            if len(self.Experiment)!=0:
                self.btnThickness.Enable(True)
                self.btnChi.Enable(True)
                self.btnAlpha.Enable(True)
            else:
                self.btnThickness.Enable(False)
                self.btnChi.Enable(False)
                self.btnAlpha.Enable(False)
        else:
            self.btnEFlux.Enable(False)
            self.btnEFluxProfile.Enable(False)
            self.btnThickness.Enable(False)
            self.btnChi.Enable(False)
            self.btnAlpha.Enable(False)

    def PlotData(self,lam,R,T,RColor,TColor,AColor):
        dc = wx.MemoryDC()
        dc.SelectObject(self.window1.BufferBmp)
        dc.BeginDrawing()

        for i in range(len(lam)):
            if i>0:
                if self.chkT.GetValue():
                    dc.SetPen(wx.Pen(TColor, 3, wx.SOLID))
                    dc.DrawLine(self.XX(lamold),self.YY(Told),self.XX(lam[i]),self.YY(T[i]))
                if self.chkR.GetValue():
                    dc.SetPen(wx.Pen(RColor, 2, wx.SOLID))
                    dc.DrawLine(self.XX(lamold),self.YY(Rold),self.XX(lam[i]),self.YY(R[i]))
                if self.chkA.GetValue():
                    dc.SetPen(wx.Pen(AColor, 3, wx.SOLID))
                    dc.DrawLine(self.XX(lamold),self.YY(1-Rold-Told),self.XX(lam[i]),self.YY(1-R[i]-T[i]))
            lamold=lam[i]
            Told=T[i]
            Rold=R[i]
        dc.EndDrawing()

    def PlotSingleData(self,lam,T,TColor):
        dc = wx.MemoryDC()
        dc.SelectObject(self.window1.BufferBmp)
        dc.BeginDrawing()
        dc.SetPen(wx.Pen(TColor, 3, wx.SOLID))

        for i in range(len(lam)):
            if i>0:
                dc.DrawLine(self.XX(lamold),self.YY(Told),self.XX(lam[i]),self.YY(T[i]))
            lamold=lam[i]
            Told=T[i]
        dc.EndDrawing()

    def OnMnuFileNewstructMenu(self, event):
        self.CheckIfSaved()
        if self.Cancel==False:
            self.ClearStructure()
            self.StructureFilename="Untitled"
            TopLayer=["TopMedium", self.IndexDir+"/air.in3", "Not_selected", \
            "Not_selected", "100", "0", "0", [], [], "0", 0, "0"]
            BotLayer=["BottomMedium", self.IndexDir+"/air.in3", "Not_selected", \
            "Not_selected", "100", "0", "0", [], [], "0", 0, "0"]
            self.Structure.append(TopLayer)
            self.Structure.append(BotLayer)
            self.Structure=EMA(self.Structure)
            self.UpdateButtons()

    def OnMnuFileOpenstructMenu(self, event):
        self.CheckIfSaved()
        if self.Cancel==False:
            dlg = wx.FileDialog(self, "Open Multilayer", self.CurDir+"/"+self.StructureDir, path.split(self.StructureFilename)[1], "str files (*.str)|*.str|" "All files (*.*)|*.*", wx.OPEN)
            try:
                if dlg.ShowModal() == wx.ID_OK:
                    self.ClearStructure()
                    filename = dlg.GetPath()
                    self.Structure, self.StructureName=OpenStructure(filename)
                    self.Structure=EMA(self.Structure)
                    self.StructureFilename=filename
                    self.StructureSaved=True
                    self.UpdateButtons()

            except:
                dlg = wx.MessageDialog(self, "Problems",
                  'Caption', wx.OK | wx.ICON_INFORMATION)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
            dlg.Destroy()

    def OnMnuFileSavestructMenu(self, event):
        if self.StructureFilename <> "Untitled":
            SaveStructure(self.StructureFilename,self.StructureName,self.Structure)
            self.StructureSaved=True
        else:
            self.OnMnuFileSavestructasMenu(None)

    def OnMnuFileSavestructasMenu(self, event):
        if len(self.Structure) > 1:
            dlg = wx.FileDialog(self, "Save Multilayer As", self.CurDir+"/"+self.StructureDir, "", "str files (*.str)|*.str|" "All files (*.*)|*.*", wx.SAVE)
            try:
                if dlg.ShowModal() == wx.ID_OK:
                    filename = dlg.GetPath()
                    self.Cancel=False
                else:
                    self.Cancel=True
            finally:
                dlg.Destroy()
            
            if self.Cancel==False:
                if FileExists(filename):
                    dlg = wx.SingleChoiceDialog(self, "File already exists: do you want to overwrite ?", "Question", ["Yes","No"])
                    try:
                        if dlg.ShowModal() == wx.ID_OK:
                            selected = dlg.GetStringSelection()
                            if selected=="Yes":
                                self.Cancel=False
                            else:
                                self.Cancel=True
                        else:
                            self.Cancel=True
                    finally:
                        dlg.Destroy()
                if self.Cancel==False:
                    SaveStructure(filename,self.StructureName,self.Structure)
                    self.StructureFilename=filename
                    self.StructureSaved=True
                    self.UpdateButtons()

    def OnMnuFileClosestructureMenu(self, event):
        self.CheckIfSaved()
        if self.Cancel==False:
            self.ClearStructure()

    def OnMnuFileLoadexpMenu(self, event):
            wildcard = "(*.dat)|*.dat|" \
            "(*.wav)|*.wav|" "(*.csv)|*.csv|" "All files (*.*)|*.*"
            dlg = wx.FileDialog(self, "Open Experiment", self.ExpDir, "", wildcard,
                       wx.OPEN| wx.MULTIPLE)
            if dlg.ShowModal() == wx.ID_OK:
                Filename=dlg.GetPath()
                self.ExperimentFilename=Filename
                self.Experiment=LoadRT(Filename)
                self.PlotExperiment()
                self.UpdatePlot()
                self.UpdateButtons()
                self.ExpDir=path.split(Filename)[0]

    def OnMnuFileCloseexpMenu(self, event):
        self.Experiment=[]
        self.UpdatePlot()
        self.ExperimentFilename=""
        self.UpdateButtons()

    def OnMnuFileExitMenu(self, event):
        self.CheckIfSaved()
        if self.Cancel==False:
            self.Destroy()

    def OnMnuIndexPlotindexMenu(self, event):
            dlg = wx.FileDialog(self, "Open Index File", self.CurDir+"/"+self.IndexDir, "", "*.in3", wx.OPEN)
            try:
                if dlg.ShowModal() == wx.ID_OK:
                    Filename=dlg.GetPath()
                    ln,lk=ReadIn3(Filename)
                    lam,n=[],[]#plot n
                    for i in range(len(ln)):
                        lam.append(ln[i][0])
                        n.append(ln[i][1]/10.0)
                    
                    self.PlotSingleData(lam,n,wx.BLACK)
        
                    lam,k=[],[]#plot k
                    for i in range(len(lk)):
                        lam.append(lk[i][0])
                        k.append(lk[i][1]/10.0)
                    
                    self.PlotSingleData(lam,k,wx.RED)
                    
                    self.UpdatePlot()
            except:
                pass

    def OnMnuSettingsSetgraphscaleMenu(self, event):
        suggest=str(self.window1.xmin)+", "+str(self.window1.xmax)
        dlg = wx.TextEntryDialog(self, 'lambda min, lambda max (A)', 'Graph Scale', suggest)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                answer = dlg.GetValue()
                answer=answer.split(",")
                self.window1.xmin, self.window1.xmax=int(answer[0]), int(answer[1])
                self.PlotAxis()
                self.PlotExperiment()
                self.UpdatePlot()
        finally:
            dlg.Destroy()

    def OnMnuHelpHelpMenu(self, event):
        text="See the file 'help.txt' and 'manual.html'"
        dlg = wx.MessageDialog(self, text,
        "Help", wx.OK | wx.ICON_INFORMATION)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnMnuHelpAboutMenu(self, event):
        dlg=About.About(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnWindow1Paint(self, event):
        dc = wx.PaintDC(self.window1)
        dc.BeginDrawing()
        if self.window1.BufferBmp != None:
            dc.DrawBitmap(self.window1.BufferBmp, 0, 0, True)
        else:
            pass
        dc.EndDrawing()

    def OnWindow1LeftDown(self, event):
        #when clicking on the plot returns coordinates
        self.x, self.y = event.GetPositionTuple()
        a=self.x
        a=a-self.xborder*self.window1.wi/100.0
        a=a/(100-2*self.xborder)*100.0
        x=self.window1.xmin+a*(self.window1.xmax-self.window1.xmin)/self.window1.wi
        self.txtWavelength.SetValue(str(int(round(x))))
        #self.txteV.SetValue(str(12400/x))
        self.txteV.SetValue("%0.3e" %(12400/x))
        "%0.3e" %0.939993939
        self.txtcm1.SetValue("%0.3e" %(1E8/x))
        lams=int(x)
        
        a=self.y
        a=a-self.yborder*self.window1.he/100.0
        a=a/(100-2*self.yborder)*100.0                
        x=self.window1.ymin+a*(self.window1.ymax-self.window1.ymin)/self.window1.he
        x=int(round((1-x)*100))
        self.txtRTA.SetValue(str(x))

    def OnBtnQEButton(self, event):
        Jsc=ComputeQE()
        dlg = wx.MessageDialog(self, 'Jsc = '+str(Jsc)+'ma/cm2',
          'Caption', wx.OK | wx.ICON_INFORMATION)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

    def OnBtnEditStrButton(self, event):
        dlg=EdtStructure.EdtStructure(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
        self.UpdateButtons()


    def OnBtnAlphaButton(self, event):
        dlg = wx.TextEntryDialog(self, 'Layer', 'Select layer', '1')
        try:
            if dlg.ShowModal() == wx.ID_OK:
                layer = int(dlg.GetValue())
        finally:
            dlg.Destroy()

        #compute absorption coefficient
        self.IndexRange=CheckWaveRange(self.Structure)
        start=max(self.window1.xmin,self.IndexRange[0])
        end=min(self.window1.xmax,self.IndexRange[1])
        
        Fi=float(self.txtFi.GetValue())
        Fi=pi*Fi/180.0
        thick=float(self.Structure[layer][9])
        thick=thick*1E-8#convert from A to cm

        lam,Ti,a=[],[],[]
        for i in range(len(self.Experiment)):
            if start<= self.Experiment[i][0] <= end:
                l=self.Experiment[i][0]
                R=self.Experiment[i][1]
                T=self.Experiment[i][2]
                if T>self.lowT and T/(1-R)<1:
                    lam.append(l)
                    Ti.append(T/(1-R))
                    a.append((-1/thick)*log(T/(1-R)))#guess value for alpha

        structure=PrepareList(self.Structure,lam)
        a=Alpha(structure,lam,Ti,a,Fi,layer)
        self.Dialog=[lam,a]
        
        SaveAlpha(lam,a,self.ExperimentFilename)
        n=structure[1][1]
        SaveAlphaIn3(self.IndexDir+"/Alpha.in3",lam,n,a,self.ExperimentFilename)

        dlg=Tauc.Tauc(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

        #self.ExperimentFilename
        
#        SaveAlpha(lam,a,self.ExperimentFilename)
#        n=structure[1][1]
#        SaveAlphaIn3(self.IndexDir+"/Alpha.in3",lam,n,a,self.ExperimentFilename)

    def OnBtnEFluxProfileButton(self, event):
        #compute light energy flux profile for a single wavelength
        dlg = wx.TextEntryDialog(self, 'Please choose wavelength and number of points / layer', 'Energy flux depth profile calculation', '5000,10')
        try:
            if dlg.ShowModal() == wx.ID_OK:
                answer = dlg.GetValue()
                Fi=float(self.txtFi.GetValue())
                Fi=pi*Fi/180.0
                l,npoints=int(answer.split(",")[0]),int(answer.split(",")[1])
                lmin,lmax=CheckWaveRange(self.Structure)
                if lmin<=l<=lmax:
                    lam=[l]
                    structure=PrepareList(self.Structure,lam)
                    E=[]
                    CumThick=0.0
                    for j in range(len(self.Structure)-2):
                        thick=float(self.Structure[j+1][9])
                        for i in range(npoints-1):
                            x=i*1.0/(npoints-1)
                            A=ComputeFlux(structure,lam,Fi,j+1,x)
                            E.append([CumThick+x*thick,A[0]])
                        CumThick=CumThick+thick
                    A=ComputeFlux(structure,lam,Fi,j+1,1)
                    E.append([CumThick,A[0]])
                    SaveFluxProfile(E)
                else:
                    dlg = wx.MessageDialog(self, 'Wavelength is out of range !',
                      ' ', wx.OK | wx.ICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
        finally:
            dlg.Destroy()

    def OnBtnPsiDeltaButton(self, event):
        #the following line is not striclty necessary
        #it allows to change index file by hand
        #and to have changes taken into account
        #every time the compute button is pressed
        #added because a specific request
        self.Structure=EMA(self.Structure)
        
        self.IndexRange=CheckWaveRange(self.Structure)
        start=max(self.window1.xmin,self.IndexRange[0])
        end=min(self.window1.xmax,self.IndexRange[1])
        
        Fi=float(self.txtFi.GetValue())
        Fi=pi*Fi/180.0
        if Fi==0:
            dlg = wx.MessageDialog(self, 'Incidence angle is 0, Aborted !',
              'Warning', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
        else:
            
            lam=[]
            for i in range(self.PlotPoints):
                lam.append(int(round(start+i*(end-start)/(self.PlotPoints-1))))
             
            structure=PrepareList(self.Structure,lam)
            psi,delta,e1,e2,n,k=ComputeRo(structure,lam,Fi)
            
            color=wx.BLACK
            self.PlotData(lam,psi/100,delta/1000,color,wx.RED,color)
            self.UpdatePlot()
            
            SavePsiDelta(lam,psi,delta,e1,e2,n,k)

    def OnBtnThicknessButton(self, event):
    #fit on thickness

        dlg=ThicknDet.ThicknDet(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()

        if self.Dialog[0]!="C":
            layer=self.Dialog[1]
            dlambda=2**self.Dialog[2]
            layerLink=self.Dialog[3]
            Density=self.Dialog[4]

            self.IndexRange=CheckWaveRange(self.Structure)
            start=max(self.window1.xmin,self.IndexRange[0])
            end=min(self.window1.xmax,self.IndexRange[1])
            
            Fi=float(self.txtFi.GetValue())
            Fi=pi*Fi/180.0
    
            lam,Re,Te=[],[],[]
            for i in range(len(self.Experiment)):
                if start<= self.Experiment[i][0] <= end:
                    lam.append(self.Experiment[i][0])
                    Re.append(self.Experiment[i][1])
                    Te.append(self.Experiment[i][2])

            structure=PrepareList(self.Structure,lam)
            if layerLink!=0:
                TotalThick = structure[layer][0]*Density+structure[layerLink][0]

            while dlambda >= 1:
                structure[layer][0] = structure[layer][0]-1
                if layerLink!=0:
                    structure[layerLink][0]=int(round(TotalThick-structure[layer][0]*Density))
                R,T=ComputeRT(structure,lam,Fi)
                Chi_R,Chi_T,Chi_RT=Chi(R,T,Re,Te,self.StDev)
                if self.Dialog[0]=="R":
                    Chi1=Chi_R
                elif self.Dialog[0]=="T":
                    Chi1=Chi_T
                else:
                    Chi1=Chi_RT
                structure[layer][0] = structure[layer][0]+1
                if layerLink!=0:
                    structure[layerLink][0]=int(round(TotalThick-structure[layer][0]*Density))
                R,T=ComputeRT(structure,lam,Fi)
                Chi_R,Chi_T,Chi_RT=Chi(R,T,Re,Te,self.StDev)                
                #Chi_R,Chi_T,Chi_RT=Chi(R,T,self.Experiment[-len(lam):],self.StDev)
                if self.Dialog[0]=="R":
                    Chi2=Chi_R
                elif self.Dialog[0]=="T":
                    Chi2=Chi_T
                else:
                    Chi2=Chi_RT
                if Chi2-Chi1!=0:
                    sign =(Chi2 - Chi1)/abs(Chi2 - Chi1)
                else:
                    sign=0
                structure[layer][0]=structure[layer][0]-dlambda*sign
                dlambda=dlambda/2
    
            if layerLink!=0:
                structure[layerLink][0]=int(round(TotalThick-structure[layer][0]*Density))
            R,T=ComputeRT(structure,lam,Fi)
            Chi_R,Chi_T,Chi_RT=Chi(R,T,Re,Te,self.StDev)
            if self.Dialog[0]=="R":
                Chi1=Chi_R
            elif self.Dialog[0]=="T":
                Chi1=Chi_T
            else:
                Chi1=Chi_RT
            structure[layer][0]=structure[layer][0]-1
            if layerLink!=0:
                structure[layerLink][0]=int(round(TotalThick-structure[layer][0]*Density))
            R,T=ComputeRT(structure,lam,Fi)
            Chi_R,Chi_T,Chi_RT=Chi(R,T,Re,Te,self.StDev)
            if self.Dialog[0]=="R":
                Chi2=Chi_R
            elif self.Dialog[0]=="T":
                Chi2=Chi_T
            else:
                Chi2=Chi_RT
            if Chi1<Chi2:
                structure[layer][0]=structure[layer][0]+1

            if layerLink!=0:
                structure[layerLink][0]=int(round(TotalThick-structure[layer][0]*Density))
            R,T=ComputeRT(structure,lam,Fi)
            Chi_R,Chi_T,Chi_RT=Chi(R,T,Re,Te,self.StDev)
            self.Structure[layer][9]=str(int(structure[layer][0]))
            self.Structure[layerLink][9]=str(int(structure[layerLink][0]))
    
            self.ncolor=self.ncolor+1
            if self.ncolor>len(self.color)-1:
                self.ncolor=0
        
            color=self.color[self.ncolor]
            self.PlotData(lam,R,T,color,color,color)
            self.UpdatePlot()
            
            del self.ChiHist[0]
            self.ChiHist.append("Thickness = "+str(structure[layer][0])+"   Chi_R = "+str("%0.3e" %Chi_R)+"   Chi_T = "+str("%0.3e" %Chi_T)+"   Chi_RT = "+str("%0.3e" %Chi_RT))
            self.ShowChi()

    def OnBtnChiButton(self, event):
        self.IndexRange=CheckWaveRange(self.Structure)
        start=max(self.window1.xmin,self.IndexRange[0])
        end=min(self.window1.xmax,self.IndexRange[1])
        
        Fi=float(self.txtFi.GetValue())
        Fi=pi*Fi/180.0

        lam,Re,Te=[],[],[]
        for i in range(len(self.Experiment)):
            if start<= self.Experiment[i][0] <= end:
                lam.append(self.Experiment[i][0])
                Re.append(self.Experiment[i][1])
                Te.append(self.Experiment[i][2])

        structure=PrepareList(self.Structure,lam)
        R,T=ComputeRT(structure,lam,Fi)
        
        self.ncolor=self.ncolor+1
        if self.ncolor>len(self.color)-1:
            self.ncolor=0
    
        color=self.color[self.ncolor]
        self.PlotData(lam,R,T,color,color,color)
        self.UpdatePlot()
        
        Chi_R,Chi_T,Chi_RT=Chi(R,T,Re,Te,self.StDev)
        del self.ChiHist[0]
        self.ChiHist.append("Thickness = ?   Chi_R = "+str("%0.3e" %Chi_R)+"   Chi_T = "+str("%0.3e" %Chi_T)+"   Chi_RT = "+str("%0.3e" %Chi_RT))
        self.ShowChi()

    def OnBtnEFluxButton(self, event):
        self.IndexRange=CheckWaveRange(self.Structure)
        start=max(self.window1.xmin,self.IndexRange[0])
        end=min(self.window1.xmax,self.IndexRange[1])

        RT=[]
        
        Fi=float(self.txtFi.GetValue())
        Fi=pi*Fi/180.0

        lam=[]
        for i in range(self.PlotPoints):
            lam.append(int(round(start+i*(end-start)/(self.PlotPoints-1))))

        dlg=InternalFlux.InternalFlux(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()
        
        if self.Dialog[0]!="C":
            if self.Dialog[0]=="A":#Compute absorption
                j=self.Dialog[1]
                structure=PrepareList(self.Structure,lam)
                A=ComputeA(structure,lam,Fi,j)
                SaveA(lam,A)
            elif self.Dialog[0]=="E":#Compute Energy Flux
                j=self.Dialog[1]
                x=self.Dialog[2]
                structure=PrepareList(self.Structure,lam)
                A=ComputeFlux(structure,lam,Fi,j,x)
                SaveFlux(lam,A)
            self.PlotSingleData(lam,A,wx.BLACK)
            self.UpdatePlot()

    def OnBtnComputeButton(self, event):
        #the following line is not striclty necessary
        #it allows to change index file by hand
        #and to have changes taken into account
        #every time the compute button is pressed
        #added because a specific request
        self.Structure=EMA(self.Structure)

        self.IndexRange=CheckWaveRange(self.Structure)
        start=max(self.window1.xmin,self.IndexRange[0])
        end=min(self.window1.xmax,self.IndexRange[1])
        
        if end > start:

            Fi=float(self.txtFi.GetValue())
            Fi=pi*Fi/180.0
            
            lam=[]
            for i in range(self.PlotPoints):
                lam.append(int(round(start+i*(end-start)/(self.PlotPoints-1))))
             
            structure=PrepareList(self.Structure,lam)

    #        rough=0
    #        for i in range(len(structure)):
    #            rough=rough+structure[i][3]
    #        if rough <> 0 and Fi <> 0.0:
    #            dlg = wx.MessageDialog(self, 'Calculation with rough interfaces works only for normal incidence !!',
    #              'Warning', wx.OK | wx.ICON_INFORMATION)
    #            try:
    #                dlg.ShowModal()
    #            finally:
    #                dlg.Destroy()
            
            R,T=ComputeRT(structure,lam,Fi)
            
            self.ncolor=self.ncolor+1
            if self.ncolor>len(self.color)-1:
                self.ncolor=0
            
            color=self.color[self.ncolor]
            self.PlotData(lam,R,T,color,color,color)
            self.UpdatePlot()
            
            SaveRT(lam,T,R)
        else:
            dlg = wx.MessageDialog(self, 'No points to plot ! Check wavelength range.',
              'Warning', wx.OK | wx.ICON_INFORMATION)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()


    def OnBtnClearButton(self, event):
        self.PlotAxis()
        self.PlotExperiment()
        self.UpdatePlot()

    def OnMainFrameClose(self, event):
        self.OnMnuFileExitMenu(None)

    def OnBtnBlackButton(self, event):
        dlg = wx.TextEntryDialog(self, 'Temperature', 'Set Temperature', '400')
        try:
            if dlg.ShowModal() == wx.ID_OK:
                answer = dlg.GetValue()
                # Your code
        finally:
            dlg.Destroy()
        
        
        T=float(answer)+273.15
        BlackBody(T)

