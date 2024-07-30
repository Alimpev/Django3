from django import template

register = template.Library()


@register.filter()
def censor(value):
    text = value.split(' ')

    bad_words = ['first', 'second', 'idiot', 'idiots', 'country', 'countries']
    result = ""
    for word in text:

        if word[-1].isalpha():
            if word.lower() in bad_words:
                new_word = word[0] + '*' * (len(word) - 2) + word[-1]
                word = new_word
        else:
            sec_word = word[-1]
            word = word[0: -1]
            if word.lower() in bad_words:
                new_word = word[0] + '*' * (len(word) - 2) + word[-1]
                word = new_word + sec_word

        result = result + ' ' + word
    return result
