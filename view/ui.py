from nicegui import ui

with ui.column():
    with ui.row().classes('w-full'):
        ui.button('H')
        ui.space()
        ui.button('He')
    with ui.row().classes('w-full'):
        ui.button('Li')
        ui.button('Le')
        ui.button('Te')

ui.run()
