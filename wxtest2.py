import wx 
import wx.grid
import wx.lib.buttons as buttons

class HelloFrame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure parents init is called 
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # CALCULATIONS
    
        # inputs
        self.input = ""
        self.term_1 = ""
        self.term_2 = ""
        self.result = None 

        # Display
        self.displayed = ""

        # operators
        self.operator = int

        # text test
        self.st = wx.StaticText(pnl, label = str(self.displayed))
        font = self.st.GetFont()
        font.PointSize += 70
        self.st.SetFont(font)

        # try use while loops to size and position buttons
        coords_x = [0, 100, 200]
        coords_y = [120,240,360]
        counter = 1

        # Put buttons on there
        for y in coords_y:

            for x in coords_x:
                
                bt = buttons.GenButton(pnl, label=str(counter), pos = wx.Point(x,y), size = (100,120))
                bt.Bind(wx.EVT_BUTTON, self.OnKeyDown)
                counter += 1 
        
        bt_0 = buttons.GenButton(pnl, label = "0", pos = (100, 480), size = (100,120))
        bt_0.Bind(wx.EVT_BUTTON, self.OnKeyDown)

        # Operator buttons 
        operators = ["+", "-", "÷", "x"]

        i = 120

        for o in operators:

            op_bts = buttons.GenButton(pnl, label=o, pos = wx.Point(300,i), size = (100,96))
            op_bts.Bind(wx.EVT_BUTTON, self.OnOperatorDown)
            i += 96
        
        eq_bt = buttons.GenButton(pnl, label="=", pos = wx.Point(300,504), size = (100,96))
        eq_bt.Bind(wx.EVT_BUTTON, self.OnEqualsDown)
        

        # create a menu bar 
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

        # Set size 
        self.SetSize(400,650)
        

    def makeMenuBar(self):

        # Make file menu with Hello and Exit items 
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", 
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)
    
    def OnKeyDown(self, event):

        if self.result != None:
            self.input = ""
            self.result = None
        
        # Register Button Press
        button = event.GetEventObject()
        label = button.GetLabel()
        
        # Fiddle with types
        self.input_str = str(self.input)
        self.input_str += label
        self.input = self.input_str
        
        # Finally set the StaticText
        self.displayed = self.input
        self.st.SetLabel(self.displayed)

    def OnOperatorDown(self, event):
        # Register button press 
        button = event.GetEventObject()
        opLabel = button.GetLabel()
        # Store input 1 
        self.term_1 = int(self.input)
        self.input = ""

        # Set operator value to something depending on label 
        if opLabel == "+":
            self.operator = 1
        elif opLabel == "-":
            self.operator = 2
        elif opLabel == "÷":
            self.operator = 3
        else:
            self.operator = 4
    
    def OnEqualsDown(self,event):
        # Register button press 
        self.term_2 = int(self.input)

        # Do math 
        if self.operator == 1:
            self.result = self.term_1 + self.term_2
        elif self.operator == 2:
            self.result = self.term_1 - self.term_2
        elif self.operator == 3:
            self.result = int(self.term_1/self.term_2)
        else:
            self.result = self.term_1 * self.term_2

        self.input = str(self.result)        
        self.displayed = str(self.result)
        self.st.SetLabel(self.displayed)
        


        
if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2', style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
    frm.Show()
    app.MainLoop()