from flask import Flask, render_template

meu_web_app = Flask('meu_web_app')

GUILHERME = {
    'nome': 'Guilherme',
    'descricao': 'Desenvolvedor de Software.',
    'url': 'https://github.com/guilhermegouw',
    'nome_url': 'Github',
    'foto': 'https://avatars3.githubusercontent.com/u/47614296?v=4&s=128'
}


@meu_web_app.route('/')
def pagina_inicial():
    return render_template('home.html', perfil=GUILHERME)


if __name__ == '__main__':
    meu_web_app.run()
