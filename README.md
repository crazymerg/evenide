Запуск API

``` bash
cd $project_dir
docker-compose up -d 
```

Запуск тестов

``` bash
cd $project_dir
pipenv install
pipenv run pytest
```

Использование

``` python
import requests

awesome_ruby_api_url = 'https://example.com'
r = requests.get(f'{awesome_ruby_api_url}/check_is_even/{your_number}')

#returns True, if your number is even


License

Even number checker is open-source project, and distributed under the MIT license
