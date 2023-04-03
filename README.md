## UI autotests demoqa.com

<!-- technologies -->

### Stack and tools
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

### What do tests check
![This is an image](images/screenshot/test_cases.png)

### Test features:

1. Тест test_submitting_form_successfully - данный тест параметризирован на запуск браузера на разных разрешений экрана (1920x1080 и 1280x720)
2. Тесты test_validation_field_email и test_send_empty_form - это примеры тестов созданных с использованием Page Module

### Демонстрация тестов для работы с файлами
![This is an image](images/screenshot/files_test_cases.png)
Первый тест создает архив из 3 файлов с расширением: pdf, csv, xlsx. 
Остальные три читают файлы внутри архива и проверяют содержимое файлов:
![This is an image](images/screenshot/tests-files.png)
![This is an image](images/screenshot/test-files-dir.png)

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/kudaev-demo-qa/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину при помощи Selenoid.
![This is an image](images/screenshot/jenkins.png)

Также мы можем посмотреть выполнение тестов в консоли перейдя во вкладку "Вывод консоли" у определенного билда
![This is an image](images/screenshot/jenkins_console.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](images/screenshot/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshot/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshot/allure_suites.png)

##### Видео прохождение теста
![This is an image](images/screenshot/tests_ui.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2021/dashboards)

##### Вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики и тестовые кейсы.
![This is an image](images/screenshot/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshot/allure_testops_suites.png)

Во вкладке Launches мы можем видить тестовые прогоны:
![This is an image](images/screenshot/tests_runs.png)



<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах, а также ссылка на allure report.

![This is an image](images/screenshot/tg_report.png)