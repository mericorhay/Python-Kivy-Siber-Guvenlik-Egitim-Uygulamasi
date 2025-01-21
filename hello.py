from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


# Ana Sayfa
class AnaSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.buton = Button(text="Saldırgan Takımda Çalış", size_hint=(0.8, 0.15), pos_hint={"center_x": 0.5},
                            background_color=(0, 0, 0, 1))
        self.buton1 = Button(text="Savunma Takımında Çalış", size_hint=(0.8, 0.15), pos_hint={"center_x": 0.5},
                             background_color=(0, 0, 0, 1))

        self.buton.color = (1, 0, 0, 1)  # Kırmızı metin
        self.buton1.color = (0, 1, 0, 1)  # Yeşil metin
        self.buton.bold = self.buton1.bold = True

        self.buton.bind(on_press=lambda x: setattr(self.manager, "current", "saldirgan"))
        self.buton1.bind(on_press=lambda x: setattr(self.manager, "current", "savunma"))

        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)
        layout.add_widget(self.buton)
        layout.add_widget(self.buton1)
        self.add_widget(layout)


# Saldırgan Sayfası
class SaldirganSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="Saldırgan Takımında Çalışıyorsunuz!", size_hint=(0.8, 0.2), pos_hint={"center_x": 0.5})
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)
        layout.add_widget(label)

        # Eğitim butonları
        egitim_buton1 = Button(text="Bilgi Toplama", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton2 = Button(text="Web Güvenliği", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton3 = Button(text="Exploit ve Post-Exploitation", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton4 = Button(text="Sosyal Mühendislik", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton5 = Button(text="Ağ Saldırıları", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))

        egitim_buton1.color = (1, 1, 1, 1)
        egitim_buton2.color = (1, 1, 1, 1)
        egitim_buton3.color = (1, 1, 1, 1)
        egitim_buton4.color = (1, 1, 1, 1)
        egitim_buton5.color = (1, 1, 1, 1)

        egitim_buton1.bind(on_press=lambda x: setattr(self.manager, "current", "saldirgan_bilgi"))
        egitim_buton2.bind(on_press=lambda x: setattr(self.manager, "current", "saldirgan_web"))
        egitim_buton3.bind(on_press=lambda x: setattr(self.manager, "current", "saldirgan_exploit"))
        egitim_buton4.bind(on_press=lambda x: setattr(self.manager, "current", "saldirgan_sosyal"))
        egitim_buton5.bind(on_press=lambda x: setattr(self.manager, "current", "saldirgan_ag"))

        layout.add_widget(egitim_buton1)
        layout.add_widget(egitim_buton2)
        layout.add_widget(egitim_buton3)
        layout.add_widget(egitim_buton4)
        layout.add_widget(egitim_buton5)
        self.add_widget(layout)


# Savunma Sayfası
class SavunmaSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(text="Savunma Takımında Çalışıyorsunuz!", size_hint=(0.8, 0.2), pos_hint={"center_x": 0.5})
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)
        layout.add_widget(label)

        # Eğitim butonları
        egitim_buton1 = Button(text="Ağ Güvenliği", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton2 = Button(text="Sistem Güvenliği", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton3 = Button(text="Olay Müdahale", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton4 = Button(text="Firewall ve IDS Konfigürasyonu", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))
        egitim_buton5 = Button(text="İzleme ve Log Analizi", size_hint=(1, 0.1), background_color=(0, 0, 0, 1))

        egitim_buton1.color = (1, 1, 1, 1)
        egitim_buton2.color = (1, 1, 1, 1)
        egitim_buton3.color = (1, 1, 1, 1)
        egitim_buton4.color = (1, 1, 1, 1)
        egitim_buton5.color = (1, 1, 1, 1)

        egitim_buton1.bind(on_press=lambda x: setattr(self.manager, "current", "savunma_ag"))
        egitim_buton2.bind(on_press=lambda x: setattr(self.manager, "current", "savunma_sistem"))
        egitim_buton3.bind(on_press=lambda x: setattr(self.manager, "current", "savunma_olay"))
        egitim_buton4.bind(on_press=lambda x: setattr(self.manager, "current", "savunma_firewall"))
        egitim_buton5.bind(on_press=lambda x: setattr(self.manager, "current", "savunma_log"))

        layout.add_widget(egitim_buton1)
        layout.add_widget(egitim_buton2)
        layout.add_widget(egitim_buton3)
        layout.add_widget(egitim_buton4)
        layout.add_widget(egitim_buton5)
        self.add_widget(layout)


# Saldırgan Eğitim Sayfaları
class SaldirganBilgiSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll_view = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        label = Label(
            text="""Saldırganlar için Bilgi Toplama aşamasına hoş geldiniz.
Bu aşamada, hedef hakkında bilgi toplamak için çeşitli araçları kullanmayı öğreneceksiniz. 
OSINT, passive ve active reconnaissance gibi yöntemlerle hedeflerinizi belirleyeceksiniz.""",
            size_hint_y=None,
            text_size=(800, None),
            halign='center',
            valign='top'
        )
        label.bind(texture_size=label.setter('size'))

        layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)


class SaldirganWebSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll_view = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        label = Label(
            text="""Web Güvenliği aşamasına hoş geldiniz. 
Bu aşamada, web uygulamaları ve sunucularının güvenliğini test etmek için kullanılan araçları ve teknikleri öğreneceksiniz.
Sızma testlerinin temel kavramlarına ve saldırganların kullandığı yöntemlere göz atacağız.""",
            size_hint_y=None,
            text_size=(800, None),
            halign='center',
            valign='top'
        )
        label.bind(texture_size=label.setter('size'))

        layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)


class SaldirganSosyalSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll_view = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        label = Label(
            text="""Sosyal mühendislik, insanları manipüle ederek bilgi elde etmeyi amaçlayan bir saldırı türüdür. 
Bu aşamada, e-posta phishing, telefon dolandırıcılığı ve sosyal medya saldırıları gibi yöntemleri öğreneceksiniz.""",
            size_hint_y=None,
            text_size=(800, None),
            halign='center',
            valign='top'
        )
        label.bind(texture_size=label.setter('size'))

        layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)


class SaldirganAgSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll_view = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        label = Label(
            text="""Ağ saldırıları, hedef ağlara doğrudan saldırılar yapmayı içerir. 
Bu aşamada, ağdaki zayıflıkları keşfetme, ağ trafiği izleme ve veri hırsızlığı yöntemlerini öğreneceksiniz.""",
            size_hint_y=None,
            text_size=(800, None),
            halign='center',
            valign='top'
        )
        label.bind(texture_size=label.setter('size'))

        layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)


# Savunma Eğitim Sayfaları
class SavunmaAgSayfa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll_view = ScrollView(size_hint=(1, 1))

        layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=10, spacing=10)
        layout.bind(minimum_height=layout.setter('height'))

        label = Label(
            text="""Ağ güvenliği, ağ trafiğini izleme, saldırıları tespit etme ve engelleme üzerine odaklanır. 
Bu aşamada, ağ güvenliği araçları ve teknikleri ile ilgili bilgi sahibi olacaksınız.""",
            size_hint_y=None,
            text_size=(800, None),
            halign='center',
            valign='top'
        )
        label.bind(texture_size=label.setter('size'))

        layout.add_widget(label)
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)


# Uygulama
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AnaSayfa(name="anasayfa"))
        sm.add_widget(SaldirganSayfa(name="saldirgan"))
        sm.add_widget(SavunmaSayfa(name="savunma"))
        sm.add_widget(SaldirganBilgiSayfa(name="saldirgan_bilgi"))
        sm.add_widget(SaldirganWebSayfa(name="saldirgan_web"))
        sm.add_widget(SaldirganSosyalSayfa(name="saldirgan_sosyal"))
        sm.add_widget(SaldirganAgSayfa(name="saldirgan_ag"))
        sm.add_widget(SavunmaAgSayfa(name="savunma_ag"))
        return sm

    def on_start(self):
        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 27:
            if self.root.current != "anasayfa":
                self.root.current = "anasayfa"
                return True
        return False


MyApp().run()
