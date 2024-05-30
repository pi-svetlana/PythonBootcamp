import yaml


def generate_ansible_playbook(todo_file):
    with open(todo_file, 'r') as f:
        todo_data = yaml.safe_load(f)

    playbook = [{
        'hosts': 'localhost',
        'connection': 'local',
        'become': True,
        'become_user': "{{ lookup('env', 'USER') }}",
        'tasks': []
    }]

    playbook[0]['tasks'].append({
        'name': 'Create directory',
        'file': {
            'path': '{{ playbook_dir }}/server',
            'state': 'directory'
        }
    })

    if 'install_packages' in todo_data.get('server', {}):
        playbook[0]['tasks'].append({
            'name': 'Install packages',
            'homebrew': {
                'name': todo_data['server']['install_packages'],
                'state': 'present'
            }
        })

    if 'exploit_files' in todo_data.get('server', {}):
        for file in todo_data['server']['exploit_files']:
            playbook[0]['tasks'].append({
                'name': f'Copy {file}',
                'copy': {
                    'src': file,
                    'dest': '{{ playbook_dir }}/server/' + file,
                }
            })

    bad_gays: list = todo_data.get('bad_guys')
    if bad_gays:
        bad_gays_arg = ''
        for bad_gay in bad_gays:
            bad_gays_arg += f',{bad_gay}'
        bad_gays_arg = bad_gays_arg.strip(',')

    playbook[0]['tasks'].append({
        'name': 'Run exploit.py',
        'command': 'python3 ' + '{{ playbook_dir }}/server/' + 'exploit.py',
    })

    playbook[0]['tasks'].append({
        'name': 'Run consumer.py',
        'command': 'python3 ' + '{{ playbook_dir }}/server/' + f'consumer.py -e {bad_gays_arg}',
    })

    with open('deploy.yml', 'w') as f:
        yaml.dump(playbook, f)


if __name__ == "__main__":
    generate_ansible_playbook('../materials/todo.yml')
