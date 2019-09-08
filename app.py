import wx
import bot
import datamg

class BotFrame(wx.Frame):
    def __init__(self):
        self.data = datamg.DataApp("", "", "").readData()
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
        self.text_ctrl3 = wx.SpinCtrl(panel, value='5', min=5, max=320)
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
        username = self.text_ctrl.GetValue()
        password = self.text_ctrl2.GetValue()
        delay = self.text_ctrl3.GetValue()
        checkbox = self.checkbox.IsChecked()
        if checkbox is True:
            datamg.DataApp(username,password, delay).saveData()
        self.Hide()
        botleague = bot.AdminBot(username, password, delay)
        botleague.login()
        botleague.checkLeagueJoins()

if __name__ == "__main__":
    app = wx.App()
    frame = BotFrame()
    frame.SetMaxSize(wx.Size(400,400))
    frame.SetMinSize(wx.Size(400,400))
    app.MainLoop()
