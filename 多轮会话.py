from http import HTTPStatus
from dashscope import Application


def call_with_session():
    while True:
        message = input('问题：')
        response = Application.call(app_id='f875893cf93d48ca8a0bcaf752407f31',
                                    prompt=message,
                                    api_key='sk-3PV3EtIzgP'
                                    )

        if response.status_code != HTTPStatus.OK:
            # print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code,
            # response.message))
            print(response.message)
        else:
            # print('request_id=%s, output=%s, usage=%s\n' % (response.request_id, response.output, response.usage))
            print(response.output.text)


if __name__ == '__main__':
    call_with_session()
