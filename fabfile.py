from fabric import task
from invoke import Responder
from _credentials import github_username, github_password


def _get_github_auth_responders():
    username_responder = Responder(pattern="Username for 'https://github.com':",
                                   response='{}\n'.format(github_username))

    password_responder = Responder(pattern="Password for 'https://{}@github.com':".format(github_username),
                                   response='{}\n'.format(github_password))

    return [username_responder, password_responder]


@task()
def deploy(c):
    supervisor_conf_path = '~/etc/'  # supervisor配置文件的目录
    supervisor_program_name = 'blogproject'  # 应用名
    project_root_path = '~/apps/blog-django/'

    # 先停止应用
    with c.cd(supervisor_conf_path):
        cmd = 'supervisorctl stop {}'.format(supervisor_program_name)
        c.run(cmd)

    # 进入项目根目录,拉取最新代码
    with c.cd(project_root_path):
        cmd = 'git pull'
        responders = _get_github_auth_responders()
        c.run(cmd, watchers=responders)
        # c.run(cmd)

    # 迁移数据库, 收集静态文件
    with c.cd(project_root_path):
        c.run('python3 manage.py migrate')
        c.run('python3 manage.py collectstatic --noinput')

    # 重新启动应用
    with c.cd(supervisor_conf_path):
        cmd = 'supervisorctl start {}'.format(supervisor_program_name)
        c.run(cmd)






















