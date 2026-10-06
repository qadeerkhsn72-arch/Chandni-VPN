from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
Window.clearcolor = (0.16,0.08,0.32,1)
class ChandniVPN(App):
    def build(self):
        root=BoxLayout(orientation='vertical',padding=25,spacing=15)
        root.add_widget(Label(text='🌙',font_size='70sp'))
        root.add_widget(Label(text='CHANDNI VPN',font_size='32sp',bold=True,color=(1,0.84,0,1)))
        root.add_widget(Label(text='By Abdul Qadeer\n03253416471',halign='center'))
        btn=Button(text='✨ CONNECT PREMIUM ✨',size_hint=(1,0.3),background_color=(1,0.84,0,1),background_normal='',bold=True)
        status=Label(text='SG 12ms | USA 24ms | UK 30ms\nDisconnected')
        def connect(i):
            btn.text='✅ CONNECTED SG-01'
            status.text='Connected! Protected\n100MBPS Premium'
            btn.background_color=(0,0.8,0.4,1)
        btn.bind(on_press=connect)
        root.add_widget(btn)
        root.add_widget(status)
        return root
ChandniVPN().run()