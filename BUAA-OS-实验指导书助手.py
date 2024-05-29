import flet as ft
from http import HTTPStatus
from dashscope import Application
import os


def main(page: ft.page):
    page.title = "BUAA-OS-实验指导书"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    question = ft.TextField(label="请输入你的问题", autofocus=True)
    answer = ft.TextField(label="问题解答", disabled=False)
    output_str = ft.TextField(label="控制台输出")

    def btn_click(e):
        if not question.value:
            question.error_text = "输入为空"
            page.update()
        else:
            message = "你的身份是windows上的命令行使用向导，每次收到任务时，结合windows命令行指令，只回答要在命令行中使用的指令，不要有多余的回答（当需要打开程序时，依照程序路径将其打开）。接下来用windows命令行指令完成以下任务：\n"
            message = message + question.value
            print(message)
            response = Application.call(app_id='f875893cf93d48ca8a0bcaf752407f31',
                                        prompt=message,
                                        api_key='sk-3PV3EtIzgP'
                                        )

            print("正在回答。。。")

            if response.status_code != HTTPStatus.OK:
                # print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code,
                # response.message))
                answer.value = response.message
                page.update()
            else:
                # print('request_id=%s, output=%s, usage=%s\n' % (response.request_id, response.output, response.usage))
                answer.value = response.output.text
                page.update()
                cmd = response.output.text
                print(cmd)
                result = os.popen(cmd)
                a = result.read()
                print(a)
                output_str.value = a
                page.update()

            print("回答完毕。。。")

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        question,
                        ft.ElevatedButton("提交", on_click=btn_click),
                    ],
                    # alignment=ft.MainAxisAlignment.CENTER
                ),
                answer,
                output_str
            ],
            # alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
