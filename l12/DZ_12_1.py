import os


def delete_html_tags(html_file, result_file=None):

    if (result_file is None or not os.path.exists(result_file)
            or not os.path.isfile(result_file)):
        print('Not found result file')
        return

    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.readlines()

    cleaned_html_lst = []
    for line in html:
        if line.count('<') > 1 or line.count('>') > 1:
            lst = line.split('>')
            lst = lst[1].split('<')
            if len(lst[0]) >= 1:
                line = lst[0]
                cleaned_html_lst.append(line)
    cleaned_html = '\n'.join(cleaned_html_lst)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_html)


delete_html_tags('draft.html', result_file='cleaned.txt')