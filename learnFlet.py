import os
import time

import flet as ft


def main(page: ft.Page):
    page.title = "oo评测工具"
    page.scroll = ft.ScrollMode.ADAPTIVE
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    zip_text = ft.Text("", size=20)  # 选择文件显示
    out_list = ft.Column()
    upload_button = ft.Ref[ft.ElevatedButton]()
    test_type = ft.Ref[ft.Dropdown]()
    times = ft.Ref[ft.Dropdown]()

    page.add(
            ft.Column([
                ft.Container(height=100),
                ft.Row([
                    ft.ElevatedButton(
                        "选择文件",
                        icon=ft.icons.FOLDER_OPEN,
                        on_click=lambda _: file_picker.pick_files(file_type=ft.FilePickerFileType.CUSTOM,
                                                                  allowed_extensions=["zip"]),
                    ),
                    ft.Container(ft.Row([zip_text], scroll=ft.ScrollMode.ADAPTIVE),
                                 height=40, border_radius=5,
                                 width=250, border=ft.border.all(1, ft.colors.BLACK)),
                    ft.Dropdown(ref=test_type,
                                height=40,
                                width=200,
                                content_padding=2,
                                alignment=ft.alignment.center,
                                label="测试方案",
                                value="中测(互测)",
                                options=[ft.dropdown.Option("弱测"),
                                         ft.dropdown.Option("中测(互测)"),
                                         ft.dropdown.Option("强测"),
                                         ft.dropdown.Option("特测")],
                                ),
                    ft.Dropdown(ref=times,
                                height=40,
                                width=80,
                                content_padding=2,
                                alignment=ft.alignment.center,
                                label="评测次数",
                                value="5",
                                options=[ft.dropdown.Option("5"),
                                         ft.dropdown.Option("10"),
                                         ft.dropdown.Option("20"),
                                         ft.dropdown.Option("50")]),
                    ft.ElevatedButton(
                        content=ft.Text("开始评测", weight=ft.FontWeight.W_600),
                        ref=upload_button,
                        disabled=True,
                    )
                ],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [out_list],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ])
    )
    """
    t = ft.Text(value="Hello world!", color="white")
    page.controls.append(t)
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )
    page.update()
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    first_name = ft.TextField()
    last_name = ft.TextField()
    first_name.disabled = False
    last_name.disabled = False
    page.add(first_name, last_name)

    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )

    # 创建引用
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        # 将问候语添加到greetings的controls列表中
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        # 清空输入框的值
        first_name.current.value = ""
        last_name.current.value = ""
        # 页面更新
        page.update()
        # 重新聚焦到first_name输入框
        first_name.current.focus()

    # 将控件添加到页面中
    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )
    """


ft.app(target=main)
