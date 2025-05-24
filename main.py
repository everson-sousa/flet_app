# import flet as ft

# def main(page:ft.Page):
#  page.bgcolor='#8485dc'
#  page.theme_mode= 'dark'
#  page.title= 'Base Flet'
#  page.window_width= 450
#  page.window_heigth = 700

#  page.window.maximizable = False

#  #navegações
#  page.floating_action_button= ft.FloatingActionButton(icon=ft.Icons.ADD,bgcolor='black')
#  page.floating_action_button_location= ft.FloatingActionButtonLocation.CENTER_DOCKED
 
#  page.bottom_appbar = ft.BottomAppBar(

#   bgcolor='#eaeaf2',
#   shape=ft.NotchShape.CIRCULAR,
#         content=ft.Row(
#             controls=[
#                 ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.BLACK, icon_size=22),
#                 ft.IconButton(icon=ft.Icons.LOGIN, icon_color=ft.Colors.BLACK, icon_size=22),
#                 ft.Container(expand=True),
#                 ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.BLACK, icon_size=22),
#                 ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.BLACK, icon_size=22),
#             ]
#         ),
#     )
# #Container Principal 
# _main=ft.Container(
#  width=400,
#  height=600,
#  bgcolor='#8485dc'
# )

#  #stack principal
# stack_main=ft.Stack(
# controls=[
#    ...
#   ]
#  )
# page.add(stack_main)





# ft.app(target= main)
import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#8485dc'
    page.theme_mode = 'dark'
    page.title = 'Base Flet'
    page.window_width = 450
    page.window_height = 700  # Corrigido aqui também
    page.window.maximizable = False
    page.vertical_alignment='center'
    page.horizontal_alignment='center'

    # Navegação
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, bgcolor='black')
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor='#eaeaf2',
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.BLACK, icon_size=22),
                ft.IconButton(icon=ft.Icons.LOGIN, icon_color=ft.Colors.BLACK, icon_size=22),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.BLACK, icon_size=22),
                ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.BLACK, icon_size=22),
            ]
        ),
    )

    # Container principal
    _main = ft.Container(
        width=480,
        height=580,
        bgcolor='#eaeaf2',
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=3, color=ft.Colors.with_opacity(opacity=0.5,color='black'))
    )

    # Stack principal
    stack_main = ft.Stack(
        alignment=ft.alignment.center,
        controls=[
            _main
        ]
    )

    page.add(stack_main)


# Rodando o app
ft.app(target=main)
