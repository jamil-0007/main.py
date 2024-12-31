from flet import *

def main(page:Page):
    page.add(
        #you must set safe area.
        SafeArea(
            content=Text("Hellow World", size=40, color="white")
        )
    )
    
    app(main)
