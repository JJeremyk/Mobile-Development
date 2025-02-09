# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
age = 7
name = ''
p1, p2, p3 = 0, 0, 0
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        lbl1 = Label(text = 'Enter your name:',halign = 'right')
        self.in_name = TextInput(multiline = False)
        lbl2 = Label(text = 'Enter your age:', halign = 'right')
        self.in_age = TextInput(text = '7', multiline =False)
        self.btn = Button(text = 'Start', size_hint = (0.3, 0.2), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        line2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing =8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
    
        instr = Label(text=txt_test1)
        #lbl1 = Label(text='Count your pulse')
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Input the result:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)
    
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        self.btn = Button(text='Start', size_hint=(0.3, 0.4), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        #outer.add_widget(lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.next = 'Continue'

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_sits)
        self.btn = Button(text = 'Continue', size_hint = (0.3, 0.2), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'pulse2'

class HeartCheck(App):
  def build(self):
      sm = ScreenManager()
      sm.add_widget(InstrScr(name='instr'))
      sm.add_widget(PulseScr(name='pulse1'))
      sm.add_widget(CheckSits(name='sits'))
      return sm
app = HeartCheck()
app.run()