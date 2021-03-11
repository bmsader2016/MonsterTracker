# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:01:13 2021

@author: cha11201
"""

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class monster():    
    def __init__(self, name = "Name", hp = 0, ac = 0):
        self.name = str(name)
        self.hp = hp
        self.currenthp = hp
        self.ac = ac
    
    def damage(self, dmg):
        self.currenthp -= dmg
        if self.currenthp <= 0:
            self.currenthp = 0
            self.name += " *DEAD*"
    
    def heal(self, heal):
        self.currenthp += heal
        if self.currenthp > self.hp:
            self.currenthp = self.hp
            
    def info(self):
        print("Name: ",self.name)
        print("AC: ", self.ac)
        print("Max HP: ",self.hp)
        print("Current HP: ",self.currenthp)
        print()
        return self.name, self.ac, self.hp, self.currenthp
   
class MonsterWidget(Widget, monster):
    def __init__(self,monster, **kwargs):
        super(MonsterWidget,self).__init__(**kwargs)
        self.size = (800,100)
        self.size_hint_y = None
        self.name = monster.name
        self.hp = monster.hp
        
    def addMonster(self):
        MonName = Button(text = self.name, pos = (0,0), size = (800,100), size_hint = (None,None))
        self.add_widget(MonName)
        
class MonsterApp(App):
    def build(self):
        mon1 = MonsterWidget(monster = monster('dog',10,8))
        mon1.addMonster()
        return mon1
    
    
myapp = MonsterApp()
myapp.run()




#from kivy.lang import Builder
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.recycleview import RecycleView
#from kivy.properties import StringProperty
#from kivy.properties import NumericProperty


"""
Builder.load_string('''
<RV>:
    viewclass: 'Button'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1,None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
                    
''')

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        self.data = [{'name':str(i)} for i in range(20)]
        self.data.append(MonsterWidget())
"""        

        

        
