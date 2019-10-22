Запуск API

``` bash
cd $project_dir/app
docker build -t app .
docker run -p 8080:8080 app
```

Запуск тестов

``` bash
cd $project_dir/tests
pipenv shell
pipenv update
pytest
```

Использование

``` python
import requests

awesome_ruby_api_url = 'https://example.com'
r = requests.get(f'{awesome_ruby_api_url}/check_is_even/{your_number}')

#returns True, if your number is even
