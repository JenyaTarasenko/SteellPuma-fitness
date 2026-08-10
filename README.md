static/       ← НЕ удаляем
staticfiles/  ← удаляем и заново пересобираем

активировать виртуальное окружение 
 Steel-Panda git:(main) ✗ source venv/bin/activate
cd myshop/

удалить статику 
rm -rf staticfiles 


поменять настроика в settings.py 

--------------------------------Deployment---------------------------------------

поменять настроика в settings.py 

сборка статики 
python manage.py collectstatic

шде гит 
git rev-parse --show-toplevel

сделать коммит



