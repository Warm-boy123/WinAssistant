from http import HTTPStatus
from dashscope import Application


def rag_call():
    response = Application.call(app_id='f875893cf93d48ca8a0bcaf752407f31',
                                prompt='说说指导书中lab1的内容',
                                api_key='sk-3PV3EtIzgP'
                                )

    if response.status_code != HTTPStatus.OK:
        # print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
        print(response.message)
    else:
        # print('request_id=%s\n output=%s\n usage=%s\n' % (response.request_id, response.output, response.usage))
        print(response.output.text)


if __name__ == '__main__':
    rag_call()
