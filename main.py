print("Как пользоваться прогой:");print("Вводите для вас непонятное слово, и получайте результат");print("Введите ""слова"", чтобы увидеть список слов")
words = {"LOL": "LOL - Lots Of Laughs (много смеха) - аббревиатура означающая смех.",
    "ROFL": "ROFL - Rolling On the Floor (кувыркаюсь на полу от смеха) - аббревиатура означающая смех.",
    "кринж": "кринж - испанский стыд (как я понял)"
}
while True:
    my_word = input(str("Введите слово которые вы не понимаете:"))
    print("")
    if my_word in words.keys():
        print(words[my_word])
        print("")
    if my_word == "слова":
        print(words.keys())
    if my_word not in words.keys() and my_word != "слова":
        print("такого слова нет!")
        print("")
