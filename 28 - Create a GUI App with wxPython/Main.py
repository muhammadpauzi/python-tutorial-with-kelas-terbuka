import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')

        # panel = wx.Panel(self)
        # my_sizer = wx.BoxSizer(wx.VERTICAL)
        # self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        # my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 3)
        # my_btn = wx.Button(panel, label='Click Me!!', pos=(5, 30))
        # my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        # my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 3)
        # panel.SetSizer(my_sizer)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        panel_2 = wx.Panel(self)
        self.tree_list = wx.TreeCtrl(panel_2, style=wx.TR_HAS_BUTTONS)
        self.root = self.tree_list.AddRoot('Root')
        self.tree_list.AppendItem(self.root, 'Child 1')
        self.tree_list.Expand(self.root)
        
        panel_2.SetSizer(sizer_2)

        self.Show()

    def on_press(self, e):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything in text field")
        else:
            print(f'You typed: {value}')


if __name__ == '__main__':
    app = wx.App()
    window = MyFrame()
    app.MainLoop()