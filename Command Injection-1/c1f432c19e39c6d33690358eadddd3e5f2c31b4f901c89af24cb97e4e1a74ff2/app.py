#!/usr/bin/env python3
import subprocess

from flask import Flask, request, render_template, redirect

from flag import FLAG

APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/ping', methods=['GET', 'POST'])     
def ping():
    if request.method == 'POST':       # ping 버튼 누르면 아래의 코드의 실행
        host = request.form.get('host')          #입력값이 host 변수에 담긴다.
        cmd = f'ping -c 3 "{host}"'      #cmd는 명령 프롬포트이며, cmd 변수 명령어 실행
        try:
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)        #bin과 쉘을 통해 리눅스 명령어를 사용함을 알림
            return render_template('ping_result.html', data=output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return render_template('ping_result.html', data='Timeout !')
        except subprocess.CalledProcessError:
            return render_template('ping_result.html', data=f'an error occurred while executing the command. -> {cmd}')

    return render_template('ping.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000)
