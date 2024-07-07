meme_dict = {
            "КРИНЖ - что-то странное, стыдное",
            "ЛОЛ - очень смешно"
            }
            

word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Такого слова нет!')
   
