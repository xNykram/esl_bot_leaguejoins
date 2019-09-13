import wx
import bot
import datamg

class BotFrame(wx.Frame):
    def __init__(self):
        self.data = datamg.DataApp("", "", "").readData()
        self.delay = self.data[2]
        self.delay = str(self.delay)
        super().__init__(parent=None, title="ESL MP BOT")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL) 
        # Email
        textlabel = wx.StaticText(panel, -1, "E-mail:")
        my_sizer.Add(textlabel,0,wx.ALL | wx.CENTER, 2)   
        #  
        self.text_ctrl = wx.TextCtrl(panel, value=self.data[0])
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 2)
        # Password
        textlabel2 = wx.StaticText(panel, -1, "Hasło:")
        my_sizer.Add(textlabel2,0,wx.ALL | wx.CENTER, 2)
        #     
        self.text_ctrl2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER, value=self.data[1])
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.CENTER, 2)
        # Delay
        textlabel3 = wx.StaticText(panel, -1, "Częstotliwość odświeżania(sek.):")
        my_sizer.Add(textlabel3,0,wx.ALL | wx.CENTER, 2)
        #
        self.text_ctrl3 = wx.SpinCtrl(panel, value=self.delay, min=5, max=320)
        my_sizer.Add(self.text_ctrl3, 0 , wx.ALL| wx.CENTER, 2)
        # Remember me
        self.checkbox = wx.CheckBox(panel, label="Zapamiętaj mnie ")
        my_sizer.Add(self.checkbox,0,wx.ALL | wx.CENTER, 2)
        #btn
        main_btn = wx.Button(panel, label="Zatwierdź")
        main_btn.Bind(wx.EVT_BUTTON, self.on_press_btn)
        my_sizer.Add(main_btn, 0, wx.ALL | wx.CENTER, 2)
        panel.SetSizer(my_sizer)
        self.Show()
    def on_press_btn(self, event):
        #checkdata
        username = self.text_ctrl.GetValue()
        password = self.text_ctrl2.GetValue()
        delay = self.text_ctrl3.GetValue()
        checkbox = self.checkbox.IsChecked()
        if checkbox is True:
            datamg.DataApp(username,password, delay).saveData()
        if not len(username) or len(password) < 5:
            wx.MessageBox( "Proszę uzupełnić dwa pierwsze pola!", caption="Błąd!",
              style=wx.OK)
        else:
            self.Hide()
            botleague = bot.AdminBot(username, password, delay)
            botleague.login()
            botleague.checkLeagueJoins()
            botleague.closeBrowser()
            exit()

if __name__ == "__main__":
    app = wx.App()
    frame = BotFrame()
    frame.SetMaxSize(wx.Size(500,500))
    frame.SetIcon(wx.Icon("images/icon.ico"))
    frame.SetMinSize(wx.Size(300,300))
    app.MainLoop()
