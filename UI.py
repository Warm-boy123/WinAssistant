import flet as ft


def main(page: ft.Page):
    page.title = "大模型操作助手"
    page.window_height = 455
    page.window_width = 335
    page.window_resizable = False  # window is not resizable
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    order = ft.TextField(label="输入命令", autofocus=True, width=330, multiline=True, min_lines=2, max_lines=2)
    answer = ft.TextField(label="将要执行的命令", width=330, read_only=True, multiline=True, min_lines=2, max_lines=2,
                          disabled=True)
    submit = ft.ElevatedButton("提交")
    refresh = ft.ElevatedButton("刷新")
    model = ft.Text(value="当前模式：")
    choose = ft.Dropdown(
        options=[
            ft.dropdown.Option("文字"),
            ft.dropdown.Option("语音"),
        ],
        width=150
    )
    choose.value = "文字"
    row1 = ft.Row(
        [model, choose],
        spacing=80,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
    row2 = ft.Row([submit, refresh], spacing=150)
    column = ft.Column(
        [
            row1,
            order,
            answer,
            row2
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30
    )
    page.add(column)
    page.window_center()
    page.window_to_front()


if __name__ == "__main__":
    ft.app(target=main)
