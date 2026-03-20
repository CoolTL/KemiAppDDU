from nicegui import ui

ui.add_head_html('''
<style> .q-btn { width: 60px; } </style>
''')

ui.button.default_props('no-caps')

with ui.column():
    with ui.row().classes('w-full'):
        ui.button('H')
        ui.space()
        ui.button('He')
    with ui.row().classes('w-full'):
        ui.button('Li')
        ui.button('Be')
        ui.space()
        ui.button('B')
        ui.button('C')
        ui.button('N')
        ui.button('O')
        ui.button('F')
        ui.button('Ne')
    with ui.row().classes('w-full'):
        ui.button('Na')
        ui.button('Mg')
        ui.space()
        ui.button('Al')
        ui.button('Si')
        ui.button('P')
        ui.button('S')
        ui.button('Cl')
        ui.button('Ar')
    with ui.row().classes('w-full'):
        ui.button('K')
        ui.button('Ca')
        ui.button('Sc')
        ui.button('Ti')
        ui.button('V')
        ui.button('Cr')
        ui.button('Mn')
        ui.button('Fe')
        ui.button('Co')
        ui.button('Ni')
        ui.button('Cu')
        ui.button('Zn')
        ui.button('Ga')
        ui.button('Ge')
        ui.button('As')
        ui.button('Se')
        ui.button('Br')
        ui.button('Kr')

ui.run()
