from data_display import show_phonebook
import logger as log


def create_html():
    log.log_input_data('Phonebook preview in html-format reguested by user')
    style1 = 'style="font-size:42px;"'
    style2 = 'style="font-size:22px;"'
    style3 = 'style="font-size:28px;"'

    html = '<html>\n <head>    <p {}>{}</p></head>\n <body>\n'\
        .format(style1, 'Phonebook')
    count = 0
    for i in range(len(show_phonebook())):
        data = (show_phonebook())[i]
        if 'Surname:' in data:
            count += 1
            html += '<html>\n <head>    <p {}>{}</p></head>\n <body>\n'\
                .format(style3, f'Contact {count}')
        html += '    <p {}>{}</p>\n'\
            .format(style2, data)
    html += '   </body>\n</html'

    with open('index.html', 'w') as page:
        page.write(html)
    log.log_input_data('File .html unloaded')
    return html
