import vk
import time
TOKEN = input('Введите токен:')
post_coment = input('id пользователя/сообщества где нужно оставить комент:')
postID = input('id поста:')
mess = input('Сообщение для спама в коментариях:')
session = vk.Session(access_token=TOKEN)
api = vk.API(session ,v='5.92', lang='ru')


while True:
    (api.wall.createComment(owner_id=post_coment,post_id=postID,message=mess))
    (api.wall.createComment(owner_id=post_coment,post_id=postID,message=mess))
    (api.wall.createComment(owner_id=post_coment,post_id=postID,message=mess))
    time.sleep(6.6)
   
