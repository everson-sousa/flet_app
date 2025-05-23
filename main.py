from flet import *

def main(page: Page):
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    first_page_contents = Container(
    content=Column(
        controls=[
            Row(
                alignment="spaceBetween",
                controls=[
                    Container(
                        content=Icon(Icons.MENU, color="WHITE")
                    ),
                    Row(
                        controls=[
                            Icon(Icons.SEARCH, color="WHITE"),
                            Icon(Icons.NOTIFICATION_ADD_OUTLINED, color="WHITE")
                        ]
                    )
                ]        
            ),
            Text(
                value='Olá, Gertrudes!', color="WHITE",
            )
        ],            
    ),
)

    page_1= Container()
    page_2 = Row(
        controls=[
            Container(
                width=450,        
                height=700, 
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50,
                    left=20, 
                    right=20,
                    bottom=5
                    ),
                    content=Column(
                        controls=[
                            first_page_contents
                        ]
                    )
)
        ]
    )
    container= Container(
        width=450,        
        height=700,
        bgcolor= BG,
        border_radius=35,
        content=Stack(
            controls=[
               page_1,
               page_2 
            ]
        )
    )
    page.add(container)

app(target=main, view=WEB_BROWSER)