import json



def get_posts_all():
    """    возвращает посты
    """
    with open("data/posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)
        return posts


def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя. Функция должна вызывать ошибку
    `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.
    """
    posts = get_posts_all()
    posts_of_user = []
    for post in posts:
        if user_name.lower() in post["poster_name"].lower():
            posts_of_user.append(post)
        return posts_of_user

    raise ValueError  ("такого пользователя нет")


def get_comments_by_post_id(post_id):
    """
    возвращает комментарии определенного поста. Функция должна вызывать ошибку
    `ValueError` если такого поста нет и пустой список, если у поста нет комментов.
    """
    with open("comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    comments_by_post_id = []
    for comment in comments:
        if post_id == comment["post_id"]:
            comments_by_post_id.append(comment)
        return comments_by_post_id

    raise ValueError("такого поста нет")


def search_for_posts(query):
    """
    возвращает список постов по ключевому слову
    """
    posts = get_posts_all()
    posts_with_word = []
    for post in posts:
        if query in posts["content"]:
            posts_with_word.append(post)
            return posts_with_word

def get_post_by_pk(pk):
    """
    возвращает один пост по его идентификатору
    """
    posts = get_posts_all()

    for post in posts:
        if pk == post["pk"]:
            return post


#Напишите к каждой функции юнит тесты, расположите тесты в отдельной папке `/tests`.
print(get_posts_by_user("pop"))